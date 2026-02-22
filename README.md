# Vibe Lab — Ministères Économiques et Financiers

Laboratoire de prototypage augmenté par l'IA au service des agents du ministère.

**Site** : [vibelab.bercy.matge.com](https://vibelab.bercy.matge.com)

---

## Le Vibe Lab en bref

Le Vibe Lab permet à un agent métier d'exprimer un besoin en langage naturel et d'obtenir un prototype fonctionnel en quelques jours — sans compétence technique préalable, sans marché public, sans dette technique.

Le prototype sert ensuite de cahier des charges vivant, testé par les utilisateurs, documenté et prêt à industrialiser par les équipes SI.

| | |
|---|---|
| **2 à 3 jours** par prototype | **20x** plus rapide qu'un cycle classique |
| **~800 €/mois** hors ETP | **0** dépendance externe |

## À qui ça s'adresse

- **Agents métier** — proposer un projet, suivre son avancement sur le Kanban
- **Comité d'évaluation** — scorer les projets candidats via la grille /50, prioriser le backlog mensuel
- **Équipe Lab** — piloter le portefeuille de prototypes, documenter la démarche

## Ce que fait l'application

### Kanban de suivi des projets

Tableau en 6 colonnes (Proposé → Roadmap → En cours → Test → Candidat → Déployé) avec drag-and-drop, priorités, catégories et export CSV.

### Backlog et grille d'évaluation

Interface en 3 onglets pour le comité mensuel :
- **Backlog** — tableau trié par score, statut des critères d'entrée
- **Évaluer** — 6 critères d'entrée (oui/non) + 6 notes pondérées (impact ×3, urgence ×2, données ×2, visibilité ×1, complexité ×1, réutilisabilité ×1) = score /50
- **Saisir** — formulaire de soumission d'un nouveau projet

### Fiche projet détaillée

Page par projet avec métriques techniques (stack, LOC, couverture de tests, commits), métadonnées (sponsor, public cible, durée estimée/réelle), galerie de screenshots et intégration GitHub.

### Bibliothèque de documents

13 documents Markdown (dossier complet, rapports par direction, manifeste, gouvernance, grille d'évaluation…) consultables en ligne avec table des matières et export DOCX en un clic.

## Stack technique

| Couche | Technologies |
|---|---|
| **Backend** | Flask 3.1, SQLite (WAL), PyJWT, python-docx |
| **Frontend** | Vanilla JS, [DSFR v1.12](https://www.systeme-de-design.gouv.fr/), Jinja2 |
| **Auth** | JWT (HS256, 4h), rate limiting, hash bcrypt |
| **Tests** | pytest (55 tests : unitaires, intégration, sécurité) |
| **Déploiement** | Docker, Traefik, Let's Encrypt |

## Installation

### Développement local

```bash
# Cloner et installer les dépendances
git clone https://github.com/bmatge/vibe-lab-bercy.git
cd vibe-lab-bercy
pip install -r server/requirements.txt

# Configurer l'environnement
cp .env.example .env
# Éditer .env : SECRET_KEY, DEFAULT_USER_EMAIL, DEFAULT_USER_PASSWORD

# Lancer
flask --app server.app run --host 0.0.0.0 --port 5000
```

### Docker (production)

```bash
cp .env.example .env
# Éditer .env

docker compose build
docker compose up -d
# → http://localhost:5000
```

### Variables d'environnement

| Variable | Description | Requis |
|---|---|---|
| `SECRET_KEY` | Clé de signature JWT | oui |
| `DEFAULT_USER_EMAIL` | Email du premier utilisateur | oui |
| `DEFAULT_USER_PASSWORD` | Mot de passe du premier utilisateur | oui |
| `DATA_DIR` | Répertoire de la base SQLite (défaut : `./data`) | non |
| `GITHUB_TOKEN` | Token GitHub pour les appels API | non |

### Gestion des utilisateurs

```bash
docker exec vibelab python -m server.manage adduser email@domaine.fr motdepasse
docker exec vibelab python -m server.manage listusers
docker exec vibelab python -m server.manage changepassword email@domaine.fr nouveaumotdepasse
docker exec vibelab python -m server.manage deluser email@domaine.fr
```

## Tests

```bash
pytest tests/ -v
```

55 tests couvrant : schéma et migrations, authentification JWT, conversion DOCX, API CRUD cartes, API backlog/évaluation, viewer de documents, et sécurité (validation d'entrées, traversée de chemin, magic bytes, rate limiting, headers).

## Arborescence

```
vibe-lab-bercy/
├── server/
│   ├── app.py              # Application Flask principale
│   ├── database.py         # Schéma SQLite et migrations
│   ├── auth_utils.py       # JWT : création, décodage, décorateur
│   ├── md_to_docx.py       # Conversion Markdown → DOCX
│   └── manage.py           # CLI de gestion des utilisateurs
├── templates/              # Templates Jinja2 (DSFR)
├── js/                     # Modules JS vanilla (auth, kanban, backlog, projet)
├── css/custom.css          # Styles personnalisés
├── docs/                   # 13 documents Markdown
├── tests/                  # Suite pytest
├── data/                   # Base SQLite + screenshots (gitignored)
├── Dockerfile
├── docker-compose.yml
└── deploy.sh
```

## Licence

[Licence Ouverte / Open Licence Etalab 2.0](https://github.com/etalab/licence-ouverte/blob/master/LO.md)
