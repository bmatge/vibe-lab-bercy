"""Tests d'intégration API — Backlog et évaluation."""


def test_list_backlog_cards(client, auth_headers):
    """GET /api/backlog/cards → retourne des cartes propose/roadmap."""
    resp = client.get('/api/backlog/cards', headers=auth_headers)
    assert resp.status_code == 200
    cards = resp.get_json()['cards']
    assert isinstance(cards, list)
    # Les cartes seed incluent au moins une en 'propose' ou 'roadmap'
    assert len(cards) >= 1


def test_evaluate_card_full(client, auth_headers, sample_card):
    """Évaluation complète → score_total correct."""
    card_id = sample_card['id']
    resp = client.put(f'/api/kanban/cards/{card_id}/evaluate', json={
        'entry_sponsor': 1,
        'entry_besoin': 1,
        'entry_donnees': 1,
        'entry_hors_bercyhub': 1,
        'entry_pas_existant': 1,
        'entry_prototypable': 1,
        'score_impact': 5,       # ×3 = 15
        'score_urgence': 4,      # ×2 = 8
        'score_donnees': 3,      # ×2 = 6
        'score_visibilite': 4,   # ×1 = 4
        'score_complexite': 2,   # ×1 = 2
        'score_reutilisabilite': 3,  # ×1 = 3
        'evaluation_notes': 'Projet prometteur',
    }, headers=auth_headers)
    assert resp.status_code == 200
    card = resp.get_json()['card']
    # 15 + 8 + 6 + 4 + 2 + 3 = 38
    assert card['score_total'] == 38
    assert card['entry_criteria_met'] == 1
    assert card['evaluation_notes'] == 'Projet prometteur'


def test_evaluate_card_partial(client, auth_headers, sample_card):
    """Scores partiels → total partiel calculé."""
    card_id = sample_card['id']
    resp = client.put(f'/api/kanban/cards/{card_id}/evaluate', json={
        'score_impact': 3,   # ×3 = 9
        'score_urgence': 2,  # ×2 = 4
    }, headers=auth_headers)
    assert resp.status_code == 200
    card = resp.get_json()['card']
    # Partial: (3×3) + (2×2) + rest = 0 = 13
    assert card['score_total'] == 13


def test_evaluate_card_score_range(client, auth_headers, sample_card):
    """Score hors 1-5 → 400."""
    card_id = sample_card['id']
    resp = client.put(f'/api/kanban/cards/{card_id}/evaluate', json={
        'score_impact': 6,
    }, headers=auth_headers)
    assert resp.status_code == 400

    resp = client.put(f'/api/kanban/cards/{card_id}/evaluate', json={
        'score_impact': 0,
    }, headers=auth_headers)
    assert resp.status_code == 400


def test_evaluate_card_entry_criteria(client, auth_headers, sample_card):
    """entry_criteria_met calculé correctement."""
    card_id = sample_card['id']
    # Tous les critères = 1
    resp = client.put(f'/api/kanban/cards/{card_id}/evaluate', json={
        'entry_sponsor': 1,
        'entry_besoin': 1,
        'entry_donnees': 1,
        'entry_hors_bercyhub': 1,
        'entry_pas_existant': 1,
        'entry_prototypable': 1,
    }, headers=auth_headers)
    card = resp.get_json()['card']
    assert card['entry_criteria_met'] == 1

    # Un critère = 0 → entry_criteria_met = 0
    resp = client.put(f'/api/kanban/cards/{card_id}/evaluate', json={
        'entry_sponsor': 0,
    }, headers=auth_headers)
    card = resp.get_json()['card']
    assert card['entry_criteria_met'] == 0


def test_evaluate_card_not_found(client, auth_headers):
    """Évaluation carte inexistante → 404."""
    resp = client.put('/api/kanban/cards/inexistant-id/evaluate', json={
        'score_impact': 3,
    }, headers=auth_headers)
    assert resp.status_code == 404
