import os
import secrets
from datetime import datetime, timezone

from flask import Flask, send_from_directory, jsonify, request, g
from werkzeug.security import check_password_hash

from server.database import init_db, get_db, close_db
from server.auth_utils import create_token, require_auth

# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

app = Flask(__name__, static_folder=None)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-me')

STATIC_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.teardown_appcontext(close_db)

with app.app_context():
    init_db()

# ---------------------------------------------------------------------------
# Static files
# ---------------------------------------------------------------------------

@app.route('/')
def index():
    return send_from_directory(STATIC_ROOT, 'index.html')


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
           (id, title, description, priority, category, column_name, position, created_by, created_at, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (card_id, title,
         data.get('description', ''),
         data.get('priority', 'moyenne'),
         data.get('category', ''),
         data.get('column_name', 'propose'),
         data.get('position', 0),
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

    allowed = ('title', 'description', 'priority', 'category', 'column_name', 'position')
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

    db.execute('DELETE FROM kanban_cards WHERE id = ?', (card_id,))
    db.commit()
    return jsonify(ok=True)
