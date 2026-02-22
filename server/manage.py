#!/usr/bin/env python3
"""CLI de gestion des utilisateurs — Vibe Lab."""
import os
import sys
import sqlite3

from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.environ.get('DATA_DIR', '/app/data'), 'vibelab.db')


def _get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db


def _new_id():
    import secrets
    return secrets.token_hex(16)


def _now():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')


def adduser(email, password):
    db = _get_db()
    try:
        now = _now()
        db.execute(
            'INSERT INTO users (id, email, password, created_at, updated_at) VALUES (?, ?, ?, ?, ?)',
            (_new_id(), email, generate_password_hash(password), now, now),
        )
        db.commit()
        print(f'Utilisateur {email} cree.')
    except sqlite3.IntegrityError:
        print(f'Erreur: {email} existe deja.', file=sys.stderr)
        sys.exit(1)
    finally:
        db.close()


def listusers():
    db = _get_db()
    rows = db.execute('SELECT id, email, created_at FROM users ORDER BY created_at').fetchall()
    db.close()
    if not rows:
        print('Aucun utilisateur.')
        return
    for r in rows:
        print(f"  {r['email']}  (id: {r['id'][:8]}...  cree: {r['created_at']})")


def deluser(email):
    db = _get_db()
    result = db.execute('DELETE FROM users WHERE email = ?', (email,))
    db.commit()
    db.close()
    if result.rowcount:
        print(f'Utilisateur {email} supprime.')
    else:
        print(f'Utilisateur {email} non trouve.', file=sys.stderr)
        sys.exit(1)


def changepassword(email, new_password):
    db = _get_db()
    result = db.execute(
        'UPDATE users SET password = ?, updated_at = ? WHERE email = ?',
        (generate_password_hash(new_password), _now(), email),
    )
    db.commit()
    db.close()
    if result.rowcount:
        print(f'Mot de passe modifie pour {email}.')
    else:
        print(f'Utilisateur {email} non trouve.', file=sys.stderr)
        sys.exit(1)


USAGE = """Usage: python -m server.manage <commande> [args]

Commandes:
  adduser <email> <password>       Creer un utilisateur
  listusers                        Lister les utilisateurs
  deluser <email>                  Supprimer un utilisateur
  changepassword <email> <pwd>     Changer le mot de passe
"""

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        sys.exit(1)

    cmd = args[0]

    if cmd == 'adduser' and len(args) == 3:
        adduser(args[1], args[2])
    elif cmd == 'listusers':
        listusers()
    elif cmd == 'deluser' and len(args) == 2:
        deluser(args[1])
    elif cmd == 'changepassword' and len(args) == 3:
        changepassword(args[1], args[2])
    else:
        print(USAGE)
        sys.exit(1)
