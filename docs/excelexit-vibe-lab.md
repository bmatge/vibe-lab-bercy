Vibe Lab — MIWEB / SNUM
Ministère de l’Économie et des Finances — Février 2026

# 1. Le problème

Dans chaque direction, chaque bureau, chaque service, des fichiers Excel assurent des fonctions critiques : suivi d’activité, planification, reporting, calculs métier, tableaux de bord, listes de contacts, historiques. Certains ont 10 ou 15 ans. Certains contiennent des macros VBA que plus personne ne comprend. Certains sont le seul endroit où une information critique existe.
Et ils partagent tous les mêmes problèmes :

Pourquoi personne n’a résolu ce problème ? Parce que migrer un fichier Excel vers une application web coûte classiquement entre 10 000 et 50 000 € en prestation. Pour un seul fichier. Quand il y en a des centaines, le calcul s’arrête là. On vit avec le risque.
# 2. La solution : Grist + Vibe Lab
## 2.1 Grist : l’infrastructure existe déjà

Grist est un tableur collaboratif open source (licence Apache 2.0) qui combine la familiarité d’un tableur avec la puissance d’une base de données relationnelle :

## 2.2 Le rôle du Vibe Lab
Grist résout le problème de la donnée. Le Vibe Lab résout le problème de l’adoption, de la migration et de l’expérience utilisateur.

# 3. Où est la valeur

Cette architecture à deux couches est la clé de la pérennité :

C’est l’exact inverse du modèle Excel : dans un fichier Excel, les données, la logique et l’interface sont fusionnées dans un seul objet opaque. Si l’interface est cassée, tout est cassé. Dans le modèle ExcelExit, chaque couche est indépendante et remplaçable.
# 4. Avant / Après : exemples concrets
▶ Tableau de suivi d’activité d’un bureau

▶ Fichier de reporting avec macros VBA

▶ Annuaire / référentiel métier

# 5. Modèle de passage à l’échelle

## 5.1 Catégorisation des fichiers
Tous les fichiers Excel ne se valent pas. La première étape est un diagnostic automatisé qui catégorise chaque fichier selon sa complexité :

## 5.2 Effet de réseau
Le modèle de scaling repose sur deux mécanismes :

# 6. Scoring sur la grille Vibe Lab
Application de la grille d’évaluation du Vibe Lab au projet ExcelExit :

# 7. Positionnement
## 7.1 Par rapport à BercyHub

## 7.2 Par rapport à la DSI

## 7.3 Par rapport à la DINUM

# 8. Plan de déploiement

# 9. Ce qu’ExcelExit ne fait pas
# 10. En résumé

Le ministère de l’Économie a des centaines de fichiers Excel dont le maintien repose sur la mémoire d’un agent. Chaque départ en retraite, chaque mutation, chaque réorganisation est un risque de perte silencieuse.

ExcelExit transforme ce risque en opportunité. Pas en remplaçant Excel par un système lourd, mais en portant les données vers une plateforme ouverte, collaborative et souveraine — avec, en prime, des interfaces qui rendent le quotidien des agents plus agréable.

Et si l’interface disparaît un jour, les données restent. C’est toute la différence.

| NOTE DE CADRAGE PROJET
ExcelExit
Transformer les fichiers Excel du ministère
en applications collaboratives Grist |
| --- |

| Chaque direction du ministère a ses dizaines de fichiers Excel critiques. Sans versioning, sans partage, sans interface, sans audit trail. Quand la personne qui les maintient s’en va, c’est la crise silencieuse.

ExcelExit propose une migration systématique vers Grist (grist.numerique.gouv.fr) — infrastructure interministérielle déjà en place — avec des interfaces web DSFR générées par le Vibe Lab. La valeur repose dans les données et les formules. L’interface est un bonus jetable. |
| --- |

| Le shadow IT Excel est le plus grand système d’information non référencé du ministère. |
| --- |

| Problème | Conséquence |
| --- | --- |
| Pas de partage simultané | Un seul utilisateur à la fois, ou des copies divergentes |
| Pas de versioning | Qui a modifié quoi, quand ? Impossible à savoir |
| Pas d’interface | Le fichier est son propre UI — illisible pour un non-initié |
| Pas d’API | Aucune interopérabilité avec d’autres outils ou systèmes |
| Pas de sécurité | Sur le bureau, dans un mail, sur une clé USB |
| Pas de pérennité | Le départ du mainteneur = la perte du savoir |

| grist.numerique.gouv.fr est une instance interministérielle Grist opérée par la DINUM, disponible pour tous les ministères. Aucune infrastructure à déployer, aucun marché à passer, aucun coût d’hébergement. |
| --- |

| Caractéristique | Détail |
| --- | --- |
| Collaboratif | Co-édition en temps réel, comme Google Sheets, mais souverain |
| Structuré | Vrais types de données, relations entre tables, intégrité référentielle |
| Programmable | Formules Python (pas VBA), lisibles et maintenables |
| Accessible par API | API REST native — chaque document Grist est une base de données interrogeable |
| Sécurisé | Gestion des droits par document, table, colonne. Audit trail intégré |
| Souverain | Hébergé par la DINUM, open source, données en France |
| Familiar | Interface tableur — la courbe d’apprentissage est quasi nulle pour un utilisateur Excel |

| 1. Analyse et diagnostic automatisé des fichiers Excel
L’IA analyse chaque fichier : structure des données, formules, macros VBA, mise en forme conditionnelle (qui est souvent de la logique métier déguisée), relations implicites entre onglets. Elle produit un diagnostic de complexité et un plan de migration. |
| --- |

| 2. Migration assistée vers Grist
L’IA génère le schéma Grist : tables, colonnes, types, relations. Elle traduit les formules Excel en formules Python. Elle restructure les données (dénormalisation des onglets, nettoyage des formats). Le résultat est un document Grist propre, structuré, documenté. |
| --- |

| 3. Création de widgets et interfaces DSFR
Par-dessus les données Grist, le Vibe Lab produit des interfaces web DSFR : tableaux de bord, formulaires de saisie, vues filtrées, exports formatés. Ces interfaces rendent le processus convivial et professionnel. Mais elles sont un bonus, pas un fondement. |
| --- |

| Principe fondamental d’ExcelExit :

La valeur repose dans les données et les formules Grist — pas dans l’interface.

Si demain une interface web n’est plus maintenue ou plus à jour, ce n’est pas grave. Les données restent dans Grist : structurées, partageables, co-éditables, accessibles par API, pérennes. L’interface peut être reconstruite en quelques heures par le Vibe Lab — ou abandonnée si elle n’est plus nécessaire. |
| --- |

| Couche | Contenu | Hébergement | Durabilité |
| --- | --- | --- | --- |
| Données | Tables, colonnes, types, relations, historique | Grist (grist.numerique.gouv.fr) | Pérenne — infra DINUM |
| Logique | Formules Python, calculs, validations, règles métier | Grist (intégré au document) | Pérenne — partie du document |
| Interface | Widgets DSFR, tableaux de bord, formulaires, vues | Mini-apps web Vibe Lab | Jetable — reconstruit en heures |

| Avant — Fichier Excel
→ 12 onglets, 1 par mois, même structure
→ Formules copiées à la main à chaque nouvel onglet
→ 1 seul utilisateur à la fois (fichier verrouillé)
→ Synthèse annuelle faite à la main
→ Graphiques mal formatés, non imprimables | Après — Grist + interface
→ 1 table Grist avec colonne « mois », une seule formule
→ Co-édition simultanée par toute l’équipe
→ Synthèse calculée automatiquement (vue + formule Python)
→ Interface DSFR : tableau de bord avec filtres par mois, export PDF
→ Accessible depuis n’importe quel navigateur |
| --- | --- |

| Avant — Fichier Excel
→ Macro VBA de 500 lignes pour générer un rapport
→ Ne fonctionne que sur la machine de Jean-Pierre
→ Incompatible avec les mises à jour d’Office
→ Personne ne sait comment ça marche
→ Données et présentation mélangées | Après — Grist + interface
→ Données dans Grist, logique en Python (lisible, documentée)
→ Interface web de reporting générée par le Vibe Lab
→ Fonctionne sur tout navigateur, tout OS
→ La logique est visible et compréhensible par un non-développeur
→ Si l’interface meurt, les données et calculs restent intacts |
| --- | --- |

| Avant — Fichier Excel
→ Fichier Excel partagé sur un lecteur réseau
→ Données dupliquées entre onglets (pas de relations)
→ Recherche par Ctrl+F uniquement
→ Aucune API — impossible d’intégrer ailleurs | Après — Grist + interface
→ Base relationnelle Grist avec tables liées
→ Recherche full-text, filtres par colonne
→ API REST : alimentation automatique depuis / vers d’autres outils
→ Interface web avec fiche détaillée par enregistrement |
| --- | --- |

| Chaque migration alimente un pipeline réutilisable. Le premier fichier Excel prend 3 jours. Le dixième prend 1 jour. Le centième prend 2 heures. L’outillage s’améliore, les patterns se répètent, l’IA apprend les structures typiques du ministère. |
| --- |

| Niveau | Description | Effort | Part estimée |
| --- | --- | --- | --- |
| Niveau 1 | Tableau simple : 1-3 onglets, formules basiques (SOMME, SI, NB.SI), pas de macro | 2-4 heures | ~60 % |
| Niveau 2 | Tableur structuré : 4-10 onglets, formules avancées (RECHERCHEV, INDEX, tableaux croisés), mises en forme conditionnelles | 1-2 jours | ~25 % |
| Niveau 3 | Application Excel : macros VBA, formulaires, interactions entre classeurs, logique métier complexe | 3-5 jours | ~12 % |
| Niveau 4 | Usine à gaz : VBA massif, connexions ODBC, dépendances externes, données sensibles | Hors scope | ~3 % |

| Le niveau 4 est hors périmètre du Vibe Lab. Ces fichiers sont en réalité des applications métier déguisées qui relèvent d’un projet SI classique ou de BercyHub. |
| --- |

| L’outillage s’améliore à chaque migration
Chaque fichier migré enrichit la bibliothèque de patterns : structures de données typiques, formules récurrentes, widgets réutilisables. Après 20 migrations, le diagnostic est quasi instantané et la génération du schéma Grist est automatisée à 80 %. |
| --- |

| La demande se génère d’elle-même
Quand un bureau voit que le bureau d’à côté a remplacé son Excel infernal par une mini-app web collaborative et esthétique, il demande la même chose. Pas besoin de vendre le projet — il se vend tout seul par l’exemple. |
| --- |

| Critère | Note | Pondéré | Justification |
| --- | --- | --- | --- |
| Impact utilisateur | 5/5 | x3 = 15 | Potentiellement chaque agent du ministère. Des centaines de fichiers concernés. |
| Urgence métier | 4/5 | x2 = 8 | Risque permanent de perte de données et de savoir. Chaque départ en retraite aggrave le problème. |
| Disponibilité données | 5/5 | x2 = 10 | Les données sont dans les fichiers Excel eux-mêmes — fournies par le métier, pas à chercher. |
| Visibilité | 5/5 | x1 = 5 | Projet universel. Chaque ministère a le même problème. Effet vitrine garanti. |
| Complexité (inversée) | 4/5 | x1 = 4 | Niveaux 1-2 sont simples. Le mécanisme est répétitif et automatisé progressivement. |
| Réutilisabilité | 5/5 | x1 = 5 | Chaque composant (diagnostic, génération de schéma, widgets) est réutilisable pour toute migration. |

| Score total : 47/50 — Entrée prioritaire dans le backlog
C’est le score le plus élevé de tous les projets évalués. |
| --- |

| Zéro chevauchement.

ExcelExit migre des fichiers Excel de suivi, de planification, de reporting — pas des données de SI métier. Les données atterrissent dans Grist, hébergé par la DINUM, accessible par navigateur.

Si un fichier s’avère contenir des données sensibles (niveau 4), il est exclu du périmètre ExcelExit et signalé à BercyHub. La règle de démarcation s’applique comme pour tout projet du Lab. |
| --- |

| La DSI est une alliée naturelle.

La DSI rêve de réduire le shadow IT Excel. ExcelExit lui offre un chemin de migration concret, à coût marginal, vers une infrastructure souveraine déjà disponible. Chaque fichier migré est un fichier de moins qui échappe au radar. |
| --- |

| ExcelExit valorise l’infrastructure Grist interministérielle.

grist.numerique.gouv.fr est un outil mis à disposition par la DINUM. Chaque migration ExcelExit est un cas d’usage supplémentaire qui démontre la pertinence de cet investissement. Le ministère de l’Économie peut devenir le premier ministère à utiliser Grist à l’échelle. |
| --- |

| Semaine | Activité | Livrable |
| --- | --- | --- |
| S1-S2 | Identification de 5 fichiers Excel pilotes dans 2-3 directions différentes. Critères : fichier utilisé quotidiennement, douleur visible, sponsor motivé. | Liste des 5 fichiers, diagnostic de complexité |
| S3-S4 | Migration des 5 fichiers vers Grist. Création des interfaces web DSFR. Tests avec les utilisateurs. | 5 documents Grist fonctionnels + 5 mini-apps DSFR |
| S5-S6 | Retours utilisateurs, itérations, documentation. Mesure de l’adoption (connexions, fréquence d’usage). | Bilan pilote chiffré, témoignages utilisateurs |
| S7-S8 | Industrialisation de l’outillage : script de diagnostic automatisé, générateur de schéma, bibliothèque de widgets. | Pipeline de migration semi-automatisé |
| S9+ | Montée en charge : traitement par lots, ouverture aux demandes de toutes les directions, communication interne. | 10-20 fichiers migrés/mois |

| 0 €
infrastructure
Grist DINUM déjà disponible | 5
fichiers pilotes
en 6 semaines | 10-20/mois
vitesse de croisière
à partir de S9 |
| --- | --- | --- |

| →  Ne migre pas les fichiers contenant des données personnelles ou sensibles (niveau 4)
→  Ne remplace pas les SI métier (Chorus, SI-RH, etc.)
→  Ne force personne — la migration est proposée, pas imposée
→  Ne supprime pas les fichiers Excel sources (ils restent en backup)
→  Ne promet pas une interface éternelle — si l’interface meurt, les données vivent |
| --- |

| ExcelExit, c’est :

→  Un problème universel (chaque bureau a ses Excel critiques)
→  Une infrastructure déjà en place (grist.numerique.gouv.fr)
→  Un coût marginal (0 € d’infra, quelques heures par fichier)
→  Une valeur pérenne (données + formules dans Grist, interface jetable)
→  Un effet de réseau (la demande se génère d’elle-même)
→  Zéro chevauchement BercyHub
→  Score de 47/50 sur la grille d’évaluation Vibe Lab |
| --- |
