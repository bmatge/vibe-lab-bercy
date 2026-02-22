"""Tests d'authentification (login, JWT, /me)."""
import time
from datetime import datetime, timedelta, timezone

import jwt


def test_login_success(client):
    """Credentials valides retournent un token."""
    resp = client.post('/api/auth/login', json={
        'email': 'test@vibelab.fr',
        'password': 'testpass123',
    })
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'token' in data
    assert data['user']['email'] == 'test@vibelab.fr'


def test_login_wrong_password(client):
    """Mot de passe incorrect → 401."""
    resp = client.post('/api/auth/login', json={
        'email': 'test@vibelab.fr',
        'password': 'mauvais',
    })
    assert resp.status_code == 401


def test_login_missing_fields(client):
    """Email ou mot de passe manquant → 400."""
    resp = client.post('/api/auth/login', json={'email': 'test@vibelab.fr'})
    assert resp.status_code == 400
    resp = client.post('/api/auth/login', json={'password': 'testpass123'})
    assert resp.status_code == 400


def test_login_unknown_email(client):
    """Email inconnu → 401."""
    resp = client.post('/api/auth/login', json={
        'email': 'inconnu@vibelab.fr',
        'password': 'testpass123',
    })
    assert resp.status_code == 401


def test_me_with_valid_token(client, auth_headers):
    """/me retourne les informations utilisateur."""
    resp = client.get('/api/auth/me', headers=auth_headers)
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['email'] == 'test@vibelab.fr'


def test_me_without_token(client):
    """/me sans token → 401."""
    resp = client.get('/api/auth/me')
    assert resp.status_code == 401


def test_me_with_invalid_token(client):
    """/me avec token invalide → 401."""
    resp = client.get('/api/auth/me', headers={
        'Authorization': 'Bearer invalid-token-xyz'
    })
    assert resp.status_code == 401


def test_me_with_expired_token(client):
    """/me avec token expiré → 401."""
    import os
    payload = {
        'sub': 'fake-user-id',
        'email': 'test@vibelab.fr',
        'exp': datetime.now(timezone.utc) - timedelta(hours=1),
    }
    expired_token = jwt.encode(payload, os.environ['SECRET_KEY'], algorithm='HS256')
    resp = client.get('/api/auth/me', headers={
        'Authorization': f'Bearer {expired_token}'
    })
    assert resp.status_code == 401
