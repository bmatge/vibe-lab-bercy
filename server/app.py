import io
import json as json_module
import os
import re
import secrets
import urllib.error
import urllib.request
from datetime import datetime, timezone

import markdown
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
def add_security_headers(response):
    # Anti-cache sur les pages HTML
    if response.content_type and 'text/html' in response.content_type:
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    # Headers de sécurité
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response


# ---------------------------------------------------------------------------
# Pages (Jinja2 templates)
# ---------------------------------------------------------------------------

@app.route('/')
def page_accueil():
    return render_template('accueil.html', current_page='accueil')



@app.route('/proposition')
def page_proposition():
    return render_template('proposition.html', current_page='proposition')


@app.route('/kanban')
def page_kanban():
    return render_template('kanban.html', current_page='kanban')


@app.route('/documents')
def page_documents():
    return render_template('documents.html', current_page='documents')


@app.route('/backlog')
def page_backlog():
    return render_template('backlog.html', current_page='backlog')


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
# Markdown viewer + DOCX export
# ---------------------------------------------------------------------------

# Map of slug → human title for the doc viewer
DOC_TITLES = {
    'dossier-complet-vibe-lab': 'Dossier complet Vibe Lab',
    'rapport-vibe-coding-snum': 'Rapport SNUM',
    'rapport-vibe-coding-miweb': 'Rapport MIWEB',
    'rapport-vibe-coding-communication': 'Rapport SIRCOM',
    'rapport-vibe-lab-sg': 'Rapport SG',
    'manifeste-vibe-lab': 'Manifeste',
    'gouvernance-vibe-lab': 'Gouvernance',
    'plan-communication-vibe-lab': 'Plan de communication',
    'presentation-vibe-lab': 'Présentation synthétique',
    'vibe-lab-pitch': 'Pitch deck',
    'excelexit-vibe-lab': 'ExcelExit',
    'grille-evaluation-vibe-lab': "Grille d'évaluation",
    'matrice-risques-vibe-lab': 'Matrice de risques',
}


@app.route('/docs/view/<slug>')
def view_doc(slug):
    safe = re.sub(r'[^a-z0-9_-]', '', slug)
    md_path = os.path.join(STATIC_ROOT, 'docs', f'{safe}.md')
    if not os.path.isfile(md_path):
        return 'Document non trouvé', 404
    with open(md_path, encoding='utf-8') as f:
        md_text = f.read()
    md = markdown.Markdown(extensions=['tables', 'toc', 'fenced_code'],
                           extension_configs={'toc': {'toc_depth': '1-3'}})
    html = md.convert(md_text)
    toc_html = md.toc
    title = DOC_TITLES.get(safe, safe)
    return render_template('doc_view.html', content_html=html, toc_html=toc_html,
                           title=title, slug=safe, current_page='documents')


@app.route('/docs/export/<slug>.docx')
def export_docx(slug):
    safe = re.sub(r'[^a-z0-9_-]', '', slug)
    md_path = os.path.join(STATIC_ROOT, 'docs', f'{safe}.md')
    if not os.path.isfile(md_path):
        return 'Document non trouvé', 404
    with open(md_path, encoding='utf-8') as f:
        md_text = f.read()
    from server.md_to_docx import md_to_docx
    buf = md_to_docx(md_text, DOC_TITLES.get(safe, safe))
    return (
        buf.getvalue(),
        200,
        {
            'Content-Type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'Content-Disposition': f'attachment; filename="{safe}.docx"',
        },
    )


# ---------------------------------------------------------------------------
# Screenshots files (noms aléatoires → pas besoin d'auth)
# ---------------------------------------------------------------------------

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 Mo

IMAGE_MAGIC = {
    b'\x89PNG\r\n\x1a\n': 'png',
    b'\xff\xd8\xff': 'jpg',
    b'GIF87a': 'gif',
    b'GIF89a': 'gif',
}


def _validate_image_magic(data):
    """Vérifie que les magic bytes correspondent à un format image autorisé."""
    for magic, fmt in IMAGE_MAGIC.items():
        if data[:len(magic)] == magic:
            return fmt
    # WEBP: starts with RIFF....WEBP
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'webp'
    return None


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
    # Rate limiting
    ip = request.remote_addr or 'unknown'
    now_ts = datetime.now(timezone.utc).timestamp()
    attempts = _login_attempts.get(ip, [])
    attempts = [t for t in attempts if now_ts - t < LOGIN_WINDOW_SECONDS]
    if len(attempts) >= LOGIN_MAX_ATTEMPTS:
        return jsonify(error='Trop de tentatives, reessayez dans une minute'), 429
    _login_attempts[ip] = attempts

    data = request.get_json(silent=True) or {}
    email = (data.get('email') or '').strip()
    password = data.get('password') or ''

    if not email or not password:
        return jsonify(error='Email et mot de passe requis'), 400

    db = get_db()
    user = db.execute('SELECT id, email, password FROM users WHERE email = ?', (email,)).fetchone()

    if not user or not check_password_hash(user['password'], password):
        _login_attempts[ip] = attempts + [now_ts]
        return jsonify(error='Identifiants incorrects'), 401

    # Reset attempts on success
    _login_attempts.pop(ip, None)
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


VALID_PRIORITIES = ('haute', 'moyenne', 'basse')
VALID_COLUMNS = ('propose', 'roadmap', 'developpement', 'test', 'candidat', 'deploye')
MAX_FIELD_LENGTHS = {
    'title': 255, 'description': 5000, 'notes': 10000,
    'category': 255, 'stack': 1000, 'sponsor': 255,
    'target_audience': 500, 'potential_users': 255,
    'dev_duration': 100, 'dev_duration_real': 100,
    'repo_url': 500, 'prod_url': 500, 'evaluation_notes': 5000,
}


def _validate_card_data(data):
    """Valide les champs d'une carte. Retourne (None) si OK ou (error_msg, 400)."""
    for field, max_len in MAX_FIELD_LENGTHS.items():
        if field in data and isinstance(data[field], str) and len(data[field]) > max_len:
            return jsonify(error=f'{field} trop long (max {max_len} caracteres)'), 400
    if 'priority' in data and data['priority'] not in VALID_PRIORITIES:
        return jsonify(error=f'Priorite invalide'), 400
    if 'column_name' in data and data['column_name'] not in VALID_COLUMNS:
        return jsonify(error=f'Colonne invalide'), 400
    if 'position' in data:
        try:
            if int(data['position']) < 0:
                return jsonify(error='Position invalide'), 400
        except (ValueError, TypeError):
            return jsonify(error='Position invalide'), 400
    if 'loc' in data and data['loc'] is not None:
        try:
            if int(data['loc']) < 0:
                return jsonify(error='LOC invalide'), 400
        except (ValueError, TypeError):
            return jsonify(error='LOC invalide'), 400
    if 'test_coverage' in data and data['test_coverage'] is not None:
        try:
            v = float(data['test_coverage'])
            if v < 0 or v > 100:
                return jsonify(error='Couverture de tests invalide (0-100)'), 400
        except (ValueError, TypeError):
            return jsonify(error='Couverture de tests invalide'), 400
    if 'score_total' in data and data['score_total'] is not None:
        try:
            v = int(data['score_total'])
            if v < 0 or v > 50:
                return jsonify(error='Score invalide (0-50)'), 400
        except (ValueError, TypeError):
            return jsonify(error='Score invalide'), 400
    return None


# Rate limiting basique pour login
_login_attempts = {}  # {ip: [(timestamp, ...), ...]}
LOGIN_MAX_ATTEMPTS = 5
LOGIN_WINDOW_SECONDS = 60


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

    err = _validate_card_data(data)
    if err:
        return err

    priority = data.get('priority', 'moyenne')
    if priority not in VALID_PRIORITIES:
        priority = 'moyenne'
    column_name = data.get('column_name', 'propose')
    if column_name not in VALID_COLUMNS:
        column_name = 'propose'

    db = get_db()
    card_id = secrets.token_hex(16)
    now = _now()
    db.execute(
        '''INSERT INTO kanban_cards
           (id, title, description, priority, category, column_name, position,
            repo_url, prod_url, created_by, created_at, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (card_id, title,
         data.get('description', '')[:5000],
         priority,
         data.get('category', '')[:255],
         column_name,
         max(0, int(data.get('position', 0) or 0)),
         data.get('repo_url', '')[:500],
         data.get('prod_url', '')[:500],
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

    err = _validate_card_data(data)
    if err:
        return err

    allowed = ('title', 'description', 'priority', 'category', 'column_name', 'position',
               'repo_url', 'prod_url', 'stack', 'loc', 'test_coverage', 'file_count',
               'notes', 'target_audience', 'potential_users', 'sponsor', 'dev_duration',
               'dev_duration_real', 'commit_count', 'score_total')
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
# Backlog API
# ---------------------------------------------------------------------------

@app.route('/api/backlog/cards')
@require_auth
def list_backlog_cards():
    db = get_db()
    rows = db.execute('''
        SELECT * FROM kanban_cards
        WHERE column_name IN ('propose', 'roadmap')
           OR score_total IS NOT NULL
        ORDER BY
            CASE WHEN score_total IS NOT NULL THEN 0 ELSE 1 END,
            score_total DESC,
            created_at DESC
    ''').fetchall()
    return jsonify(cards=[dict(r) for r in rows])


@app.route('/api/kanban/cards/<card_id>/evaluate', methods=['PUT'])
@require_auth
def evaluate_card(card_id):
    data = request.get_json(silent=True) or {}
    db = get_db()

    existing = db.execute('SELECT * FROM kanban_cards WHERE id = ?', (card_id,)).fetchone()
    if not existing:
        return jsonify(error='Carte non trouvee'), 404

    entry_fields = ['entry_sponsor', 'entry_besoin', 'entry_donnees',
                    'entry_hors_bercyhub', 'entry_pas_existant', 'entry_prototypable']
    score_fields = ['score_impact', 'score_urgence', 'score_donnees',
                    'score_visibilite', 'score_complexite', 'score_reutilisabilite']
    weights = {'score_impact': 3, 'score_urgence': 2, 'score_donnees': 2,
               'score_visibilite': 1, 'score_complexite': 1, 'score_reutilisabilite': 1}

    updates = {}

    # Critères d'entrée
    for f in entry_fields:
        if f in data:
            updates[f] = 1 if data[f] else 0

    # Notes de scoring (1-5)
    for f in score_fields:
        if f in data and data[f] is not None:
            val = int(data[f])
            if val < 1 or val > 5:
                return jsonify(error=f'{f} doit etre entre 1 et 5'), 400
            updates[f] = val

    # Calculer entry_criteria_met
    merged_entry = {f: updates.get(f, existing[f]) for f in entry_fields}
    all_filled = all(merged_entry[f] is not None for f in entry_fields)
    all_met = all(merged_entry[f] == 1 for f in entry_fields if merged_entry[f] is not None)
    updates['entry_criteria_met'] = 1 if (all_filled and all_met) else 0

    # Calculer score_total
    merged_scores = {f: updates.get(f, existing[f]) for f in score_fields}
    if all(merged_scores[f] is not None for f in score_fields):
        updates['score_total'] = sum(merged_scores[f] * weights[f] for f in score_fields)
    elif any(merged_scores[f] is not None for f in score_fields):
        updates['score_total'] = sum((merged_scores[f] or 0) * weights[f] for f in score_fields)

    if 'evaluation_notes' in data:
        updates['evaluation_notes'] = data['evaluation_notes']
    updates['evaluated_at'] = _now()
    updates['updated_at'] = _now()

    set_clause = ', '.join(f'{k} = ?' for k in updates)
    values = list(updates.values()) + [card_id]
    db.execute(f'UPDATE kanban_cards SET {set_clause} WHERE id = ?', values)
    db.commit()

    card = db.execute('SELECT * FROM kanban_cards WHERE id = ?', (card_id,)).fetchone()
    return jsonify(card=dict(card))


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

    detected = _validate_image_magic(file_data)
    if not detected:
        return jsonify(error='Contenu du fichier invalide'), 400

    screenshot_id = secrets.token_hex(16)
    safe_filename = f'{screenshot_id}.{detected}'
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

_GITHUB_PATH_RE = re.compile(r'^[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+(/[a-z]+)?$')


@app.route('/api/github-proxy/<path:repo_path>')
@require_auth
def github_proxy(repo_path):
    if not _GITHUB_PATH_RE.match(repo_path):
        return jsonify(error='Chemin GitHub invalide'), 400

    url = 'https://api.github.com/repos/' + repo_path
    qs = request.query_string.decode()
    if qs:
        url += '?' + qs

    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'VibeLab-Bercy/1.0'
    }
    gh_token = os.environ.get('GITHUB_TOKEN')
    if gh_token:
        headers['Authorization'] = 'token ' + gh_token

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json_module.loads(response.read().decode())
            return jsonify(data)
    except urllib.error.HTTPError as e:
        return jsonify(error='Erreur GitHub API'), e.code
    except Exception:
        return jsonify(error='Erreur de connexion GitHub'), 502


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
