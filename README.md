# Vibe Lab — Ministères Économiques et Financiers

Laboratoire de prototypage augmenté par l'IA.

## Accès

Site : [vibelab.bercy.matge.com](https://vibelab.bercy.matge.com)

## Mode démo

Par défaut, le site fonctionne en **mode démo** (sans Supabase) :
- Email : n'importe quel email valide
- Mot de passe : `vibe2025`
- Les données du Kanban sont stockées en localStorage

## Configuration Supabase (production)

1. Créer un projet gratuit sur [supabase.com](https://supabase.com)
2. Exécuter le SQL ci-dessous dans l'éditeur SQL de Supabase
3. Modifier `js/config.js` avec votre URL et clé anon
4. Activer l'authentification Email/Password dans Authentication > Providers

### SQL de création

```sql
CREATE TABLE kanban_cards (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  priority VARCHAR(20) NOT NULL DEFAULT 'moyenne',
  category VARCHAR(50),
  column_name VARCHAR(50) NOT NULL DEFAULT 'backlog',
  position INT DEFAULT 0,
  created_by UUID REFERENCES auth.users(id),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE kanban_cards ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Authenticated read" ON kanban_cards
  FOR SELECT USING (auth.role() = 'authenticated');
CREATE POLICY "Authenticated insert" ON kanban_cards
  FOR INSERT WITH CHECK (auth.role() = 'authenticated');
CREATE POLICY "Authenticated update" ON kanban_cards
  FOR UPDATE USING (auth.role() = 'authenticated');
CREATE POLICY "Authenticated delete" ON kanban_cards
  FOR DELETE USING (auth.role() = 'authenticated');
```

### Créer des utilisateurs

Dans Supabase > Authentication > Users > Invite user, ajouter les adresses email des agents habilités.

## Déploiement GitHub Pages

Le site se déploie automatiquement via GitHub Pages. Le fichier `CNAME` configure le domaine personnalisé.

## Stack technique

- **Frontend** : HTML / CSS / JS vanilla + [DSFR v1.12](https://www.systeme-de-design.gouv.fr/)
- **Auth + BDD** : [Supabase](https://supabase.com) (free tier)
- **Drag & drop** : [SortableJS](https://sortablejs.github.io/Sortable/)
- **Hébergement** : GitHub Pages

## Licence

[Licence Ouverte / Open Licence Etalab 2.0](https://github.com/etalab/licence-ouverte/blob/master/LO.md)
