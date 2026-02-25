"""Tests de sécurité — vérifie les protections mises en place."""
import io


def test_field_length_validation(client, auth_headers):
    """Titre trop long → 400."""
    resp = client.post('/api/kanban/cards', json={
        'title': 'A' * 300,  # max 255
    }, headers=auth_headers)
    assert resp.status_code == 400
    assert 'trop long' in resp.get_json()['error']


def test_description_length_validation(client, auth_headers):
    """Description trop longue → 400."""
    resp = client.post('/api/kanban/cards', json={
        'title': 'Test',
        'description': 'A' * 6000,  # max 5000
    }, headers=auth_headers)
    assert resp.status_code == 400


def test_path_traversal_docs(client):
    """../etc/passwd → 404 (slug nettoyé)."""
    resp = client.get('/docs/view/../../../etc/passwd')
    assert resp.status_code in (404, 308)


def test_github_proxy_path_validation(client, auth_headers):
    """Chemin GitHub invalide → 400."""
    # Tentative d'accès à un chemin arbitraire
    resp = client.get('/api/github-proxy/../../etc/passwd', headers=auth_headers)
    assert resp.status_code in (400, 404)

    resp = client.get('/api/github-proxy/owner/repo/../../etc', headers=auth_headers)
    assert resp.status_code == 400


def test_github_proxy_valid_paths(client, auth_headers):
    """Chemins GitHub valides → pas de 400 (mais peut être 502 si pas de réseau)."""
    # owner/repo format
    resp = client.get('/api/github-proxy/octocat/hello-world', headers=auth_headers)
    # Devrait être 200 ou 502 (pas de réseau en test), mais pas 400
    assert resp.status_code != 400

    # owner/repo/languages format
    resp = client.get('/api/github-proxy/octocat/hello-world/languages', headers=auth_headers)
    assert resp.status_code != 400


def test_scoring_bypass_via_update(client, auth_headers, sample_card):
    """score_total est modifiable via PUT, mais score_impact et entry_criteria_met restent protégés."""
    card_id = sample_card['id']
    resp = client.put(f'/api/kanban/cards/{card_id}', json={
        'title': 'Titre normal',
        'score_impact': 5,
        'score_total': 35,
        'entry_criteria_met': 1,
    }, headers=auth_headers)
    assert resp.status_code == 200
    card = resp.get_json()['card']
    # score_total est modifiable directement (édition fiche projet)
    assert card['score_total'] == 35
    # Les champs de scoring détaillé restent protégés (via /evaluate)
    assert card['score_impact'] is None
    assert card['entry_criteria_met'] is None


def test_security_headers(client):
    """Les headers de sécurité sont présents."""
    resp = client.get('/')
    assert resp.headers.get('X-Content-Type-Options') == 'nosniff'
    assert resp.headers.get('X-Frame-Options') == 'DENY'
    assert resp.headers.get('Referrer-Policy') == 'strict-origin-when-cross-origin'


def test_html_no_cache_headers(client):
    """Les pages HTML ont les headers anti-cache."""
    resp = client.get('/')
    assert 'no-cache' in resp.headers.get('Cache-Control', '')


def test_upload_invalid_magic_bytes(client, auth_headers, sample_card):
    """Upload d'un fichier avec extension .png mais contenu texte → rejeté."""
    card_id = sample_card['id']
    data = {
        'file': (io.BytesIO(b'This is not a PNG file'), 'fake.png'),
    }
    resp = client.post(
        f'/api/kanban/cards/{card_id}/screenshots',
        data=data,
        headers={'Authorization': auth_headers['Authorization']},
        content_type='multipart/form-data',
    )
    assert resp.status_code == 400
    assert 'invalide' in resp.get_json()['error']


def test_upload_valid_png(client, auth_headers, sample_card):
    """Upload d'un vrai fichier PNG → accepté."""
    card_id = sample_card['id']
    # Minimum PNG: magic bytes + minimal IHDR
    png_bytes = b'\x89PNG\r\n\x1a\n' + b'\x00' * 100
    data = {
        'file': (io.BytesIO(png_bytes), 'test.png'),
    }
    resp = client.post(
        f'/api/kanban/cards/{card_id}/screenshots',
        data=data,
        headers={'Authorization': auth_headers['Authorization']},
        content_type='multipart/form-data',
    )
    assert resp.status_code == 201


def test_rate_limiting_login(client):
    """Après 5 tentatives échouées → 429."""
    # Reset rate limiting state
    from server.app import _login_attempts
    _login_attempts.clear()

    for i in range(5):
        client.post('/api/auth/login', json={
            'email': 'test@vibelab.fr',
            'password': 'mauvais',
        })
    # 6e tentative → 429
    resp = client.post('/api/auth/login', json={
        'email': 'test@vibelab.fr',
        'password': 'mauvais',
    })
    assert resp.status_code == 429
    assert 'Trop de tentatives' in resp.get_json()['error']

    # Nettoyer
    _login_attempts.clear()
