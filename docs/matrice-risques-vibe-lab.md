# Matrice des risques — Vibe Lab

**Vibe Lab — MIWEB / SNUM**
Ministère de l'Économie et des Finances — Février 2026

---

> Tout dispositif comporte des risques. Les identifier honnêtement et prévoir leur atténuation est la meilleure garantie de crédibilité. Voici les **8 risques principaux** du Vibe Lab et les réponses apportées.

## 1. Vue d'ensemble

La matrice ci-dessous évalue chaque risque selon sa **probabilité d'occurrence** (faible / modérée / élevée) et son **impact potentiel** (faible / modéré / critique). Le **niveau de risque résiduel** tient compte des mesures d'atténuation déjà en place ou prévues.

| Risque | Proba. | Impact | Mesure d'atténuation | Résiduel |
| --- | --- | --- | --- | --- |
| **Dépendance aux IA commerciales** | Modérée | Modéré | Code open source indépendant du modèle. Albert (souverain) intégré en backup. Aucun vendor lock-in : les prompts sont portables. | **Faible** |
| **Confusion de périmètre avec BercyHub** | Élevée | Critique | Règle de démarcation absolue documentée. Point trimestriel BercyHub. Chaque projet tagé « données publiques » ou « agrégé » dans le backlog. | **Faible** |
| **Non-adoption par les métiers** | Modérée | Critique | Co-construction obligatoire (pas de projet sans sponsor). Tests utilisateurs dès la semaine 1. Abandon à 4 semaines sans usage. | **Modéré** |
| **Perte de compétence (départ de l'agent)** | Modérée | Modéré | Code publié sur GitHub, documenté, testé. Architecture standard (React, Node, Docker). Reprise possible par tout développeur. | **Faible** |
| **Dérive vers du développement classique** | Modérée | Modéré | Cap à 5 projets actifs. Cycle maximum de 8 semaines. Comité mensuel qui arbitre entrées/sorties. | **Faible** |
| **Qualité de code insuffisante** | Faible | Modéré | CI/CD, tests automatisés, typage strict, conformité DSFR systématique. 1 800+ tests déjà en place sur les 8 projets existants. | **Faible** |
| **Fuite de données via l'IA** | Faible | Faible | Les prompts contiennent des spécifications techniques, pas de données. Le code produit est public. Aucune donnée sensible dans la chaîne. | **Faible** |
| **Effet « gadget » / perte de crédibilité** | Modérée | Critique | KPI mesurables (coûts évités, utilisateurs actifs). Bilan trimestriel chiffré. Transparence totale sur les abandons. | **Modéré** |

## 2. Analyse

### 2.1 Les deux risques à surveiller

**Non-adoption par les métiers** — C'est le risque numéro un de tout lab d'innovation. La mitigation repose sur un principe simple : **pas de projet sans sponsor, pas de prototype sans test utilisateur**. Si malgré cela l'outil n'est pas utilisé, on l'abandonne et on en tire les leçons. Le coût d'un échec est de quelques jours de travail — pas de quelques dizaines de milliers d'euros.

**Effet « gadget » / perte de crédibilité** — Le Lab doit prouver sa valeur par les chiffres, pas par les discours. Le **tableau de bord de pilotage** (KPI), les **bilans trimestriels transparents** et la capacité à dire « ce projet a échoué, voilà pourquoi » sont les meilleures protections. Un Lab qui ne cache pas ses échecs est plus crédible qu'un Lab qui prétend ne jamais se tromper.

### 2.2 Les risques maîtrisés par construction

> **Sécurité et confidentialité : risque résiduel faible.** Le périmètre du Lab (données publiques, code open source, aucun SI sensible) élimine structurellement les risques de fuite. Ce n'est pas une posture — c'est une architecture. Même en cas d'incident sur un outil d'IA, les seules données exposées seraient des spécifications techniques déjà publiques.

### 2.3 Synthèse

| Catégorie | Nombre | Risque résiduel |
| --- | --- | --- |
| Risques à résiduel **faible** | 6 sur 8 | Maîtrisés par l'architecture et les règles de gouvernance |
| Risques à résiduel **modéré** | 2 sur 8 | Atténués par la gouvernance, à surveiller via KPI |
| Risques à résiduel **critique** | 0 sur 8 | Aucun |

## 3. Ancrage dans la gouvernance

Les mesures d'atténuation de cette matrice ne sont pas théoriques : elles sont directement inscrites dans les documents opérationnels du Vibe Lab.

- La **règle de démarcation avec BercyHub** (risque R2) est formalisée dans la fiche de gouvernance et fait l'objet d'un point trimestriel structuré.
- Le **scoring objectif de la grille d'évaluation** (risque R5 — dépendance à un seul agent) permet à n'importe quel repreneur de comprendre les priorités.
- Les **cinq règles cardinales de gouvernance** — pas de projet sans sponsor, périmètre données publiques, maximum 5 projets actifs, abandon à 4 semaines, transparence totale — constituent le premier rempart contre la majorité des risques identifiés.
- Le projet **ExcelExit**, premier du backlog élargi avec un score de 47/50, illustre l'application concrète de ces garde-fous : les fichiers de niveau 4 (données sensibles) sont explicitement exclus et signalés à BercyHub.

## 4. Documents associés

Cette matrice s'articule avec les documents suivants :

1. **Fiche de gouvernance** — cycle de vie, instances, rôles, règles cardinales
2. **Grille d'évaluation** — critères d'entrée et scoring de priorisation
3. **Note de cadrage ExcelExit** — premier projet du backlog élargi
4. **Manifeste** — valeurs et positionnement du Lab
5. **Plan de communication** — 12 semaines pour générer la demande
