import json as json_module
import os
import secrets
import urllib.error
import urllib.request
from datetime import datetime, timezone

from flask import Flask, send_from_directory, render_template, jsonify, request, g
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

from server.database import init_db, get_db, close_db
from server.auth_utils import create_token, require_auth

# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

app = Flask(__name__, static_folder=None,
            template_folder=os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                'templates'))
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-me')

STATIC_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.teardown_appcontext(close_db)

with app.app_context():
    init_db()

# ---------------------------------------------------------------------------
# Anti-cache sur les pages HTML (dev + déploiement rapide)
# ---------------------------------------------------------------------------

@app.after_request
def add_no_cache(response):
    if response.content_type and 'text/html' in response.content_type:
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response


# ---------------------------------------------------------------------------
# Pages (Jinja2 templates)
# ---------------------------------------------------------------------------

@app.route('/')
def page_accueil():
    return render_template('accueil.html', current_page='accueil')


@app.route('/constat')
def page_constat():
    return render_template('constat.html', current_page='constat')


@app.route('/proposition')
def page_proposition():
    return render_template('proposition.html', current_page='proposition')


@app.route('/methode')
def page_methode():
    return render_template('methode.html', current_page='methode')


@app.route('/kanban')
def page_kanban():
    return render_template('kanban.html', current_page='kanban')


@app.route('/documents')
def page_documents():
    return render_template('documents.html', current_page='documents')


@app.route('/projet/<card_id>')
def page_projet(card_id):
    return render_template('projet.html', current_page='kanban', card_id=card_id)


# ---------------------------------------------------------------------------
# Static files
# ---------------------------------------------------------------------------

@app.route('/css/<path:filename>')
def css_files(filename):
    return send_from_directory(os.path.join(STATIC_ROOT, 'css'), filename)


@app.route('/js/<path:filename>')
def js_files(filename):
    return send_from_directory(os.path.join(STATIC_ROOT, 'js'), filename)


@app.route('/docs/<path:filename>')
def docs_files(filename):
    return send_from_directory(os.path.join(STATIC_ROOT, 'docs'), filename)


# ---------------------------------------------------------------------------
# Screenshots files (noms aléatoires → pas besoin d'auth)
# ---------------------------------------------------------------------------

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 Mo


def _screenshots_dir():
    data_dir = os.environ.get('DATA_DIR', os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data'))
    d = os.path.join(data_dir, 'screenshots')
    os.makedirs(d, exist_ok=True)
    return d


@app.route('/data/screenshots/<path:filename>')
def screenshot_files(filename):
    return send_from_directory(_screenshots_dir(), filename)


# ---------------------------------------------------------------------------
# Auth API
# ---------------------------------------------------------------------------

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    email = (data.get('email') or '').strip()
    password = data.get('password') or ''

    if not email or not password:
        return jsonify(error='Email et mot de passe requis'), 400

    db = get_db()
    user = db.execute('SELECT id, email, password FROM users WHERE email = ?', (email,)).fetchone()

    if not user or not check_password_hash(user['password'], password):
        return jsonify(error='Identifiants incorrects'), 401

    token = create_token(user['id'], user['email'])
    return jsonify(token=token, user={'id': user['id'], 'email': user['email']})


@app.route('/api/auth/me')
@require_auth
def me():
    return jsonify(g.current_user)


# ---------------------------------------------------------------------------
# Kanban API
# ---------------------------------------------------------------------------

def _now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')


@app.route('/api/kanban/cards')
@require_auth
def list_cards():
    db = get_db()
    rows = db.execute('SELECT * FROM kanban_cards ORDER BY column_name, position').fetchall()
    return jsonify(cards=[dict(r) for r in rows])


@app.route('/api/kanban/cards/<card_id>')
@require_auth
def get_card(card_id):
    db = get_db()
    card = db.execute('SELECT * FROM kanban_cards WHERE id = ?', (card_id,)).fetchone()
    if not card:
        return jsonify(error='Carte non trouvee'), 404
    screenshots = db.execute(
        'SELECT id, filename, original_name, created_at FROM screenshots WHERE card_id = ? ORDER BY created_at',
        (card_id,)
    ).fetchall()
    result = dict(card)
    result['screenshots'] = [dict(s) for s in screenshots]
    return jsonify(card=result)


@app.route('/api/kanban/cards', methods=['POST'])
@require_auth
def create_card():
    data = request.get_json(silent=True) or {}
    title = (data.get('title') or '').strip()
    if not title:
        return jsonify(error='Titre requis'), 400

    db = get_db()
    card_id = secrets.token_hex(16)
    now = _now()
    db.execute(
        '''INSERT INTO kanban_cards
           (id, title, description, priority, category, column_name, position,
            repo_url, prod_url, created_by, created_at, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (card_id, title,
         data.get('description', ''),
         data.get('priority', 'moyenne'),
         data.get('category', ''),
         data.get('column_name', 'propose'),
         data.get('position', 0),
         data.get('repo_url', ''),
         data.get('prod_url', ''),
         g.current_user['id'], now, now),
    )
    db.commit()
    card = db.execute('SELECT * FROM kanban_cards WHERE id = ?', (card_id,)).fetchone()
    return jsonify(card=dict(card)), 201


@app.route('/api/kanban/cards/<card_id>', methods=['PUT'])
@require_auth
def update_card(card_id):
    data = request.get_json(silent=True) or {}
    db = get_db()

    existing = db.execute('SELECT * FROM kanban_cards WHERE id = ?', (card_id,)).fetchone()
    if not existing:
        return jsonify(error='Carte non trouvee'), 404

    allowed = ('title', 'description', 'priority', 'category', 'column_name', 'position',
               'repo_url', 'prod_url', 'stack', 'loc', 'test_coverage', 'file_count',
               'notes', 'target_audience', 'potential_users', 'sponsor', 'dev_duration',
               'dev_duration_real', 'commit_count')
    updates = {k: data[k] for k in allowed if k in data}
    if not updates:
        return jsonify(card=dict(existing))

    updates['updated_at'] = _now()
    set_clause = ', '.join(f'{k} = ?' for k in updates)
    values = list(updates.values()) + [card_id]
    db.execute(f'UPDATE kanban_cards SET {set_clause} WHERE id = ?', values)
    db.commit()

    card = db.execute('SELECT * FROM kanban_cards WHERE id = ?', (card_id,)).fetchone()
    return jsonify(card=dict(card))


@app.route('/api/kanban/cards/<card_id>', methods=['DELETE'])
@require_auth
def delete_card(card_id):
    db = get_db()
    existing = db.execute('SELECT id FROM kanban_cards WHERE id = ?', (card_id,)).fetchone()
    if not existing:
        return jsonify(error='Carte non trouvee'), 404

    # Nettoyer les fichiers screenshots du disque
    screenshots = db.execute('SELECT filename FROM screenshots WHERE card_id = ?', (card_id,)).fetchall()
    for s in screenshots:
        filepath = os.path.join(_screenshots_dir(), s['filename'])
        if os.path.exists(filepath):
            os.remove(filepath)

    db.execute('DELETE FROM kanban_cards WHERE id = ?', (card_id,))
    db.commit()
    return jsonify(ok=True)


# ---------------------------------------------------------------------------
# Screenshots API
# ---------------------------------------------------------------------------

@app.route('/api/kanban/cards/<card_id>/screenshots', methods=['POST'])
@require_auth
def upload_screenshot(card_id):
    db = get_db()
    card = db.execute('SELECT id FROM kanban_cards WHERE id = ?', (card_id,)).fetchone()
    if not card:
        return jsonify(error='Carte non trouvee'), 404

    if 'file' not in request.files:
        return jsonify(error='Aucun fichier'), 400

    file = request.files['file']
    if not file.filename:
        return jsonify(error='Nom de fichier vide'), 400

    ext = file.filename.rsplit('.', 1)[-1].lower() if '.' in file.filename else ''
    if ext not in ALLOWED_EXTENSIONS:
        return jsonify(error='Format non autorise (png, jpg, gif, webp)'), 400

    file_data = file.read()
    if len(file_data) > MAX_FILE_SIZE:
        return jsonify(error='Fichier trop volumineux (max 5 Mo)'), 400

    screenshot_id = secrets.token_hex(16)
    safe_filename = f'{screenshot_id}.{ext}'
    filepath = os.path.join(_screenshots_dir(), safe_filename)

    with open(filepath, 'wb') as f:
        f.write(file_data)

    now = _now()
    db.execute(
        'INSERT INTO screenshots (id, card_id, filename, original_name, created_at) VALUES (?, ?, ?, ?, ?)',
        (screenshot_id, card_id, safe_filename, secure_filename(file.filename), now)
    )
    db.commit()

    return jsonify(screenshot={
        'id': screenshot_id, 'filename': safe_filename,
        'original_name': file.filename, 'created_at': now
    }), 201


# ---------------------------------------------------------------------------
# GitHub proxy (avoid CORS from browser)
# ---------------------------------------------------------------------------

@app.route('/api/github-proxy/<path:repo_path>')
@require_auth
def github_proxy(repo_path):
    url = 'https://api.github.com/repos/' + repo_path
    req = urllib.request.Request(url, headers={
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'VibeLab-Bercy/1.0'
    })
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json_module.loads(response.read().decode())
            return jsonify(data)
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else '{}'
        return jsonify(error='GitHub API: ' + str(e.code)), e.code
    except Exception as e:
        return jsonify(error=str(e)), 502


@app.route('/api/kanban/cards/<card_id>/screenshots/<screenshot_id>', methods=['DELETE'])
@require_auth
def delete_screenshot(card_id, screenshot_id):
    db = get_db()
    row = db.execute(
        'SELECT filename FROM screenshots WHERE id = ? AND card_id = ?',
        (screenshot_id, card_id)
    ).fetchone()
    if not row:
        return jsonify(error='Screenshot non trouve'), 404

    filepath = os.path.join(_screenshots_dir(), row['filename'])
    if os.path.exists(filepath):
        os.remove(filepath)

    db.execute('DELETE FROM screenshots WHERE id = ?', (screenshot_id,))
    db.commit()
    return jsonify(ok=True)
