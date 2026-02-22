#!/usr/bin/env bash
set -euo pipefail

echo "=== Vibe Lab — Deploiement ==="

# Verifier .env
if [ ! -f .env ]; then
  echo "ERREUR: Fichier .env manquant."
  echo "  cp .env.example .env && nano .env"
  exit 1
fi

# Verifier reseau Docker
if ! docker network inspect ecosystem-network >/dev/null 2>&1; then
  echo "ERREUR: Le reseau Docker 'ecosystem-network' n'existe pas."
  echo "  docker network create ecosystem-network"
  exit 1
fi

# Mettre a jour le code
echo "Mise a jour du code (git pull)..."
git pull

# Build et demarrage
echo "Construction de l'image..."
docker compose build

echo "Demarrage du conteneur..."
docker compose up -d

echo ""
echo "=== Deploiement termine ==="
echo "Site : https://vibelab.bercy.matge.com"
echo ""
echo "Gestion des utilisateurs :"
echo "  docker exec vibelab python -m server.manage listusers"
echo "  docker exec vibelab python -m server.manage adduser <email> <password>"
echo "  docker exec vibelab python -m server.manage deluser <email>"
echo "  docker exec vibelab python -m server.manage changepassword <email> <password>"
