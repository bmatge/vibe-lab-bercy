"""Tests d'intégration API — CRUD cartes kanban."""
import json


def test_create_card(client, auth_headers):
    """POST /api/kanban/cards → 201 avec les champs corrects."""
    resp = client.post('/api/kanban/cards', json={
        'title': 'Nouveau Projet',
        'description': 'Une description',
        'priority': 'haute',
        'category': 'Outils',
    }, headers=auth_headers)
    assert resp.status_code == 201
    card = resp.get_json()['card']
    assert card['title'] == 'Nouveau Projet'
    assert card['priority'] == 'haute'
    assert card['column_name'] == 'propose'


def test_create_card_no_title(client, auth_headers):
    """POST sans titre → 400."""
    resp = client.post('/api/kanban/cards', json={
        'description': 'Pas de titre',
    }, headers=auth_headers)
    assert resp.status_code == 400


def test_create_card_no_auth(client):
    """POST sans authentification → 401."""
    resp = client.post('/api/kanban/cards', json={
        'title': 'Test',
    }, content_type='application/json')
    assert resp.status_code == 401


def test_list_cards(client, auth_headers):
    """GET /api/kanban/cards → liste complète."""
    resp = client.get('/api/kanban/cards', headers=auth_headers)
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'cards' in data
    assert isinstance(data['cards'], list)
    # Au moins les 4 cartes seed
    assert len(data['cards']) >= 4


def test_get_card(client, auth_headers, sample_card):
    """GET /api/kanban/cards/<id> → détail avec screenshots."""
    card_id = sample_card['id']
    resp = client.get(f'/api/kanban/cards/{card_id}', headers=auth_headers)
    assert resp.status_code == 200
    card = resp.get_json()['card']
    assert card['id'] == card_id
    assert 'screenshots' in card


def test_get_card_not_found(client, auth_headers):
    """GET carte inexistante → 404."""
    resp = client.get('/api/kanban/cards/inexistant-id', headers=auth_headers)
    assert resp.status_code == 404


def test_update_card(client, auth_headers, sample_card):
    """PUT → champs mis à jour."""
    card_id = sample_card['id']
    resp = client.put(f'/api/kanban/cards/{card_id}', json={
        'title': 'Titre Modifie',
        'priority': 'basse',
    }, headers=auth_headers)
    assert resp.status_code == 200
    card = resp.get_json()['card']
    assert card['title'] == 'Titre Modifie'
    assert card['priority'] == 'basse'


def test_update_card_priority_validation(client, auth_headers, sample_card):
    """Priorité invalide → 400."""
    card_id = sample_card['id']
    resp = client.put(f'/api/kanban/cards/{card_id}', json={
        'priority': 'invalide',
    }, headers=auth_headers)
    assert resp.status_code == 400


def test_update_card_column_validation(client, auth_headers, sample_card):
    """column_name invalide → 400."""
    card_id = sample_card['id']
    resp = client.put(f'/api/kanban/cards/{card_id}', json={
        'column_name': 'colonne_inconnue',
    }, headers=auth_headers)
    assert resp.status_code == 400


def test_delete_card(client, auth_headers, sample_card):
    """DELETE → 200, carte supprimée."""
    card_id = sample_card['id']
    resp = client.delete(f'/api/kanban/cards/{card_id}', headers=auth_headers)
    assert resp.status_code == 200
    # Vérifier la suppression
    resp = client.get(f'/api/kanban/cards/{card_id}', headers=auth_headers)
    assert resp.status_code == 404


def test_delete_card_not_found(client, auth_headers):
    """DELETE carte inexistante → 404."""
    resp = client.delete('/api/kanban/cards/inexistant-id', headers=auth_headers)
    assert resp.status_code == 404
