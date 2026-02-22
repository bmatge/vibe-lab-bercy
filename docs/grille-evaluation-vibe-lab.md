Vibe Lab — MIWEB / SNUM
Ministère de l’Économie et des Finances — Février 2026

# 1. Critères d’entrée
Un projet entre dans le backlog du Vibe Lab si et seulement si tous les critères ci-dessous sont remplis. Un seul critère non satisfait suffit à refuser l’entrée.

# 2. Scoring de priorisation
Quand plusieurs projets candidats remplissent les critères d’entrée, le scoring ci-dessous permet de prioriser. Chaque critère est noté de 1 (faible) à 5 (fort). Le score total détermine l’ordre d’entrée dans le backlog.

# 3. Critères de décision en fin de cycle
Après la phase de test et d’itération, chaque projet fait l’objet d’une décision au comité mensuel. Trois issues possibles :

# 4. Exemple : scoring d’Écosystème (G3)
Application rétrospective de la grille au projet Écosystème, déjà livré et en production.

# 5. Exemple : scoring d’ExcelExit — 47/50
Le projet ExcelExit — migration des fichiers Excel critiques vers Grist avec interfaces DSFR — a été évalué selon la même grille :
Impact utilisateur : 5/5 (chaque bureau a ses Excel critiques, problème universel). Alignement stratégique : 5/5 (transformation numérique, complémentarité BercyHub). Faisabilité technique : 5/5 (Grist déjà en place, DINUM, gratuit). Effet vitrine : 5/5 (résultat visible immédiatement, génère sa propre demande). Réutilisabilité : 5/5 (patron applicable à tout Excel du ministère). Urgence métier : 4/5 (pas de deadline réglementaire, mais dépendances réelles aux fichiers).
Score total : 47/50 — Entrée prioritaire dans le backlog (score le plus élevé de tous les projets évalués).
# 6. Documents associés
Cette grille s’inscrit dans un ensemble cohérent de documents : la Fiche de gouvernance (cycle de vie, instances, rôles, règles cardinales), la Matrice des risques (8 risques identifiés, mesures d’atténuation), la note de cadrage ExcelExit (premier projet du backlog élargi, score 47/50), le Manifeste (valeurs et positionnement du Lab), et le Plan de communication (12 semaines pour générer la demande entrante).

| GRILLE D’ÉVALUATION
Projets Vibe Lab
Critères d’entrée, scoring, décision
de pérennisation ou d’abandon |
| --- |

| Cette grille formalise les critères objectifs qui déterminent si un projet entre dans le Lab, comment il est évalué pendant son cycle de vie, et sur quels critères il est pérennisé ou abandonné. |
| --- |

|  | Critère | Définition |
| --- | --- | --- |
| ✅ | Sponsor métier identifié | Une personne nommée, côté métier, qui porte le besoin et fournira les testeurs |
| ✅ | Besoin exprimé clairement | Le problème à résoudre et les utilisateurs cibles sont définis |
| ✅ | Données publiques ou agrégées | Aucune donnée personnelle, fiscale, classifiée ou protégée |
| ✅ | Hors périmètre BercyHub | Pas de connexion à un SI métier, pas d’homologation requise |
| ✅ | Pas de solution existante | Aucun outil en place ne répond au besoin (ou l’outil existant est obsolète/inutilisable) |
| ✅ | Prototypable en 2 semaines | Le scope est suffisamment ciblé pour produire un premier résultat testable en 10 jours ouvrés |

| Critère | Pondération | Question clé |
| --- | --- | --- |
| Impact utilisateur | x3 | Combien d’agents/usagers concernés ? Gain de temps estimé ? |
| Urgence métier | x2 | Le besoin est-il lié à une échéance (obligation légale, campagne, événement) ? |
| Disponibilité des données | x2 | Les données sont-elles immédiatement accessibles via API ou export ? |
| Visibilité / effet de démonstration | x1 | Le projet a-t-il une valeur de vitrine pour le Lab ou le ministère ? |
| Complexité technique | x1 | Inversé : plus c’est simple, plus le score est élevé (quick wins d’abord) |
| Réutilisabilité | x1 | Les composants produits sont-ils réutilisables pour d’autres projets ? |

| Score maximum : 50 points (5 × 3 + 5 × 2 + 5 × 2 + 5 × 1 + 5 × 1 + 5 × 1)
Seuil d’entrée recommandé : ≥ 25 points
En cas d’égalité : le projet ayant le meilleur score « Impact utilisateur » passe en premier |
| --- |

| ✅  PÉRENNISER
Tous les critères suivants sont remplis :
→  Usage régulier mesuré (connexions, actions, retours positifs)
→  Sponsor métier qui s’engage sur le suivi et la maintenance fonctionnelle
→  Documentation complète (README, guide d’installation, architecture)
→  Tests automatisés et CI/CD en place
→  Conformité DSFR et accessibilité RGAA vérifiées |
| --- |

| ➡️  TRANSFÉRER À BERCYHUB
Le concept est validé ET le besoin justifie une évolution vers :
→  Des données sensibles ou personnelles (ex : connecter le chatbot RH au SIRH)
→  Un SI métier (ex : intégrer un tableau de bord dans Chorus)
→  Une homologation de sécurité (ex : outil accessible depuis l’extérieur du ministère)

Le Lab transmet : le prototype, les retours utilisateurs, les spécifications validées par l’usage. |
| --- |

| ❌  ABANDONNER
Au moins un des critères suivants est rempli :
→  Pas d’usage mesurable après 4 semaines de mise à disposition
→  Le besoin a changé ou n’existe plus
→  Le sponsor métier s’est désengagé
→  Le périmètre a dérivé vers le sensible (transfert BercyHub impossible ou non souhaité)

Un abandon n’est pas un échec : c’est une décision éclairée prise en quelques semaines au lieu d’un constat d’échec après 18 mois et 200 K€. |
| --- |

| Critère | Note | Pondéré | Justification |
| --- | --- | --- | --- |
| Impact utilisateur | 5/5 | x3 = 15 | Toutes les équipes web du ministère, DIRCOM, DSI |
| Urgence métier | 4/5 | x2 = 8 | Obligation DSFR, RGAA, conformité croissante |
| Disponibilité données | 5/5 | x2 = 10 | Scan de sites publics, API ouvertes |
| Visibilité | 5/5 | x1 = 5 | Projet vitrine, réutilisable en interministériel |
| Complexité (inversée) | 2/5 | x1 = 2 | Projet ambitieux (238K LOC, 18 critères) |
| Réutilisabilité | 4/5 | x1 = 4 | Architecture générique, extensible à d’autres périmètres |

| Score total : 44/50 — Entrée prioritaire dans le backlog

Décision effective : pérennisé. En production depuis décembre 2025, utilisé par la DIRCOM et le SNUM, publié sur GitHub. |
| --- |

| Cette grille n’est pas un outil bureaucratique — c’est un outil de transparence. Elle permet à chaque direction de comprendre pourquoi un projet est accepté, refusé, priorisé ou abandonné. Et elle protège le Lab contre l’arbitraire. |
| --- |
