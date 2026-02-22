import os
import tempfile
import secrets

import pytest

# Force test config before importing app
os.environ['SECRET_KEY'] = 'test-secret-key-for-pytest'
os.environ.setdefault('DEFAULT_USER_EMAIL', 'test@vibelab.fr')
os.environ.setdefault('DEFAULT_USER_PASSWORD', 'testpass123')

from server.app import app as flask_app
from server.database import get_db, init_db
from server.auth_utils import create_token


@pytest.fixture()
def app(tmp_path):
    """App Flask configurée pour les tests avec une DB temporaire."""
    os.environ['DATA_DIR'] = str(tmp_path)
    flask_app.config['TESTING'] = True

    with flask_app.app_context():
        init_db()
        yield flask_app


@pytest.fixture()
def client(app):
    """Client de test Flask."""
    return app.test_client()


@pytest.fixture()
def db(app):
    """Connexion à la base SQLite de test."""
    with app.app_context():
        yield get_db()


@pytest.fixture()
def auth_token(db):
    """Token JWT valide pour les requêtes authentifiées."""
    user = db.execute('SELECT id, email FROM users LIMIT 1').fetchone()
    return create_token(user['id'], user['email'])


@pytest.fixture()
def auth_headers(auth_token):
    """Headers avec Authorization Bearer."""
    return {'Authorization': f'Bearer {auth_token}', 'Content-Type': 'application/json'}


@pytest.fixture()
def sample_card(client, auth_headers):
    """Carte kanban pré-insérée pour les tests CRUD."""
    resp = client.post('/api/kanban/cards', json={
        'title': 'Projet Test',
        'description': 'Description du projet test',
        'priority': 'haute',
        'category': 'Outils',
        'column_name': 'propose',
    }, headers=auth_headers)
    return resp.get_json()['card']
