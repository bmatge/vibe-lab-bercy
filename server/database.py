import os
import sqlite3
import secrets
from datetime import datetime, timezone

from flask import g
from werkzeug.security import generate_password_hash

DB_NAME = 'vibelab.db'

SEED_CARDS = [
    {
        'title': 'ExcelExit \u2014 Migration des Excel critiques',
        'description': 'Transformer les fichiers Excel du minist\u00e8re en applications collaboratives Grist avec interfaces web DSFR.',
        'priority': 'haute',
        'category': 'Infrastructure',
        'column_name': 'developpement',
        'position': 0,
    },
    {
        'title': "Outil de scoring \u2014 Grille d'\u00e9valuation interactive",
        'description': "D\u00e9velopper une interface web pour la grille d'\u00e9valuation des projets candidats (scoring /50).",
        'priority': 'moyenne',
        'category': 'Outils',
        'column_name': 'roadmap',
        'position': 0,
    },
    {
        'title': 'Dashboard de suivi \u2014 KPIs du Lab',
        'description': 'Tableau de bord interne pour suivre les KPIs : nombre de prototypes, temps moyen, co\u00fbt, satisfaction.',
        'priority': 'basse',
        'category': 'Pilotage',
        'column_name': 'propose',
        'position': 0,
    },
    {
        'title': 'Site vitrine Vibe Lab',
        'description': 'Mini-site de pr\u00e9sentation de la d\u00e9marche avec acc\u00e8s aux documents et Kanban de suivi.',
        'priority': 'haute',
        'category': 'Communication',
        'column_name': 'test',
        'position': 0,
    },
]


def _db_path():
    data_dir = os.environ.get('DATA_DIR', os.path.join(os.path.dirname(__file__), '..', 'data'))
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, DB_NAME)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(_db_path())
        g.db.row_factory = sqlite3.Row
        g.db.execute('PRAGMA journal_mode=WAL')
        g.db.execute('PRAGMA foreign_keys=ON')
    return g.db


def close_db(exc=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(_db_path())
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA journal_mode=WAL')
    db.execute('PRAGMA foreign_keys=ON')

    db.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id          TEXT PRIMARY KEY,
            email       TEXT NOT NULL UNIQUE COLLATE NOCASE,
            password    TEXT NOT NULL,
            created_at  TEXT NOT NULL,
            updated_at  TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS kanban_cards (
            id          TEXT PRIMARY KEY,
            title       TEXT NOT NULL,
            description TEXT DEFAULT '',
            priority    TEXT NOT NULL DEFAULT 'moyenne'
                        CHECK (priority IN ('haute', 'moyenne', 'basse')),
            category    TEXT DEFAULT '',
            column_name TEXT NOT NULL DEFAULT 'propose'
                        CHECK (column_name IN ('propose', 'roadmap', 'developpement', 'test', 'candidat', 'deploye')),
            position    INTEGER NOT NULL DEFAULT 0,
            created_by  TEXT REFERENCES users(id),
            created_at  TEXT NOT NULL,
            updated_at  TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_cards_column
            ON kanban_cards(column_name, position);
    ''')

    _seed_default_user(db)
    _seed_kanban_cards(db)
    db.close()


def _now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')


def _new_id():
    return secrets.token_hex(16)


def _seed_default_user(db):
    count = db.execute('SELECT COUNT(*) FROM users').fetchone()[0]
    if count > 0:
        return
    email = os.environ.get('DEFAULT_USER_EMAIL')
    password = os.environ.get('DEFAULT_USER_PASSWORD')
    if not email or not password:
        return
    now = _now()
    db.execute(
        'INSERT INTO users (id, email, password, created_at, updated_at) VALUES (?, ?, ?, ?, ?)',
        (_new_id(), email, generate_password_hash(password), now, now),
    )
    db.commit()


def _seed_kanban_cards(db):
    count = db.execute('SELECT COUNT(*) FROM kanban_cards').fetchone()[0]
    if count > 0:
        return
    user = db.execute('SELECT id FROM users LIMIT 1').fetchone()
    created_by = user['id'] if user else None
    now = _now()
    for card in SEED_CARDS:
        db.execute(
            '''INSERT INTO kanban_cards
               (id, title, description, priority, category, column_name, position, created_by, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (_new_id(), card['title'], card['description'], card['priority'],
             card['category'], card['column_name'], card['position'], created_by, now, now),
        )
    db.commit()
