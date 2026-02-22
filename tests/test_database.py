"""Tests du schéma de base de données et des migrations."""
import sqlite3

from server.database import get_db


def test_init_db_creates_tables(db):
    """Vérifie que les tables users, kanban_cards et screenshots existent."""
    tables = {row[0] for row in db.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()}
    assert 'users' in tables
    assert 'kanban_cards' in tables
    assert 'screenshots' in tables


def test_kanban_columns_exist(db):
    """Vérifie que toutes les colonnes attendues existent dans kanban_cards."""
    cols = {row[1] for row in db.execute('PRAGMA table_info(kanban_cards)').fetchall()}
    # Colonnes de base
    for c in ('id', 'title', 'description', 'priority', 'category',
              'column_name', 'position', 'created_by', 'created_at', 'updated_at'):
        assert c in cols, f'Colonne manquante: {c}'
    # Colonnes migration 1 (repo/prod)
    assert 'repo_url' in cols
    assert 'prod_url' in cols
    # Colonnes migration 2 (fiche projet)
    for c in ('stack', 'loc', 'test_coverage', 'file_count', 'notes',
              'target_audience', 'potential_users', 'sponsor',
              'dev_duration', 'dev_duration_real', 'commit_count'):
        assert c in cols, f'Colonne manquante: {c}'
    # Colonnes migration 3 (scoring)
    for c in ('entry_sponsor', 'entry_besoin', 'entry_donnees',
              'entry_hors_bercyhub', 'entry_pas_existant', 'entry_prototypable',
              'score_impact', 'score_urgence', 'score_donnees',
              'score_visibilite', 'score_complexite', 'score_reutilisabilite',
              'score_total', 'entry_criteria_met', 'evaluated_at', 'evaluation_notes'):
        assert c in cols, f'Colonne manquante: {c}'


def test_migrations_idempotent(app, db):
    """Relancer init_db ne doit pas lever d'erreur."""
    from server.database import init_db
    # Re-run should not fail
    init_db()
    # Tables still exist
    tables = {row[0] for row in db.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()}
    assert 'kanban_cards' in tables


def test_seed_cards_created(db):
    """Vérifie que les 4 cartes seed sont créées."""
    count = db.execute('SELECT COUNT(*) FROM kanban_cards').fetchone()[0]
    assert count == 4


def test_seed_cards_not_duplicated(app, db):
    """Relancer init_db ne duplique pas les cartes seed."""
    from server.database import init_db
    init_db()
    count = db.execute('SELECT COUNT(*) FROM kanban_cards').fetchone()[0]
    assert count == 4


def test_default_user_created(db):
    """Un utilisateur par défaut est créé via les variables d'environnement."""
    user = db.execute('SELECT email FROM users LIMIT 1').fetchone()
    assert user is not None
    assert user['email'] == 'test@vibelab.fr'
