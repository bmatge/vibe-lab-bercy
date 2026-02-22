# ExcelExit — Transformer les fichiers Excel du ministere en applications collaboratives Grist

**Note de cadrage projet** | Vibe Lab — MIWEB / SNUM
Ministere de l'Economie et des Finances — Fevrier 2026

> Chaque direction du ministere a ses dizaines de fichiers Excel critiques. Sans versioning, sans partage, sans interface, sans audit trail. Quand la personne qui les maintient s'en va, c'est la crise silencieuse.
>
> ExcelExit propose une migration systematique vers Grist (grist.numerique.gouv.fr) — infrastructure interministerielle deja en place — avec des interfaces web DSFR generees par le Vibe Lab. **La valeur repose dans les donnees et les formules. L'interface est un bonus jetable.**

---

## 1. Le probleme

Dans chaque direction, chaque bureau, chaque service, des fichiers Excel assurent des fonctions critiques : suivi d'activite, planification, reporting, calculs metier, tableaux de bord, listes de contacts, historiques. Certains ont 10 ou 15 ans. Certains contiennent des macros VBA que plus personne ne comprend. Certains sont le seul endroit ou une information critique existe.

Et ils partagent tous les memes problemes :

| Probleme | Consequence |
| --- | --- |
| Pas de partage simultane | Un seul utilisateur a la fois, ou des copies divergentes |
| Pas de versioning | Qui a modifie quoi, quand ? Impossible a savoir |
| Pas d'interface | Le fichier est son propre UI — illisible pour un non-initie |
| Pas d'API | Aucune interoperabilite avec d'autres outils ou systemes |
| Pas de securite | Sur le bureau, dans un mail, sur une cle USB |
| Pas de perennite | Le depart du mainteneur = la perte du savoir |

Pourquoi personne n'a resolu ce probleme ? Parce que migrer un fichier Excel vers une application web coute classiquement entre **10 000 et 50 000 EUR** en prestation. Pour un seul fichier. Quand il y en a des centaines, le calcul s'arrete la. On vit avec le risque.

> Le shadow IT Excel est le plus grand systeme d'information non reference du ministere.

---

## 2. La solution : Grist + Vibe Lab

### 2.1 Grist : l'infrastructure existe deja

Grist est un tableur collaboratif open source (licence Apache 2.0) qui combine la familiarite d'un tableur avec la puissance d'une base de donnees relationnelle :

| Caracteristique | Detail |
| --- | --- |
| **Collaboratif** | Co-edition en temps reel, comme Google Sheets, mais souverain |
| **Structure** | Vrais types de donnees, relations entre tables, integrite referentielle |
| **Programmable** | Formules Python (pas VBA), lisibles et maintenables |
| **Accessible par API** | API REST native — chaque document Grist est une base de donnees interrogeable |
| **Securise** | Gestion des droits par document, table, colonne. Audit trail integre |
| **Souverain** | Heberge par la DINUM, open source, donnees en France |
| **Familier** | Interface tableur — la courbe d'apprentissage est quasi nulle pour un utilisateur Excel |

> **grist.numerique.gouv.fr** est une instance interministerielle Grist operee par la DINUM, disponible pour tous les ministeres. Aucune infrastructure a deployer, aucun marche a passer, aucun cout d'hebergement.

### 2.2 Le role du Vibe Lab

Grist resout le probleme de la donnee. Le Vibe Lab resout le probleme de l'**adoption**, de la **migration** et de l'**experience utilisateur**.

1. **Analyse et diagnostic automatise des fichiers Excel** — L'IA analyse chaque fichier : structure des donnees, formules, macros VBA, mise en forme conditionnelle (qui est souvent de la logique metier deguisee), relations implicites entre onglets. Elle produit un diagnostic de complexite et un plan de migration.

2. **Migration assistee vers Grist** — L'IA genere le schema Grist : tables, colonnes, types, relations. Elle traduit les formules Excel en formules Python. Elle restructure les donnees (denormalisation des onglets, nettoyage des formats). Le resultat est un document Grist propre, structure, documente.

3. **Creation de widgets et interfaces DSFR** — Par-dessus les donnees Grist, le Vibe Lab produit des interfaces web DSFR : tableaux de bord, formulaires de saisie, vues filtrees, exports formates. Ces interfaces rendent le processus convivial et professionnel. Mais elles sont un bonus, pas un fondement.

---

## 3. Ou est la valeur

Cette architecture a deux couches est la cle de la perennite :

| Couche | Contenu | Hebergement | Durabilite |
| --- | --- | --- | --- |
| **Donnees** | Tables, colonnes, types, relations, historique | Grist (grist.numerique.gouv.fr) | Perenne — infra DINUM |
| **Logique** | Formules Python, calculs, validations, regles metier | Grist (integre au document) | Perenne — partie du document |
| **Interface** | Widgets DSFR, tableaux de bord, formulaires, vues | Mini-apps web Vibe Lab | Jetable — reconstruit en heures |

> **Principe fondamental d'ExcelExit :**
>
> La valeur repose dans les donnees et les formules Grist — pas dans l'interface.
>
> Si demain une interface web n'est plus maintenue ou plus a jour, ce n'est pas grave. Les donnees restent dans Grist : structurees, partageables, co-editables, accessibles par API, perennes. L'interface peut etre reconstruite en quelques heures par le Vibe Lab — ou abandonnee si elle n'est plus necessaire.

C'est l'exact inverse du modele Excel : dans un fichier Excel, les donnees, la logique et l'interface sont fusionnees dans un seul objet opaque. Si l'interface est cassee, tout est casse. Dans le modele ExcelExit, **chaque couche est independante et remplacable**.

---

## 4. Avant / Apres : exemples concrets

### Tableau de suivi d'activite d'un bureau

| Avant — Fichier Excel | Apres — Grist + interface |
| --- | --- |
| 12 onglets, 1 par mois, meme structure | 1 table Grist avec colonne « mois », une seule formule |
| Formules copiees a la main a chaque nouvel onglet | Co-edition simultanee par toute l'equipe |
| 1 seul utilisateur a la fois (fichier verrouille) | Synthese calculee automatiquement (vue + formule Python) |
| Synthese annuelle faite a la main | Interface DSFR : tableau de bord avec filtres par mois, export PDF |
| Graphiques mal formates, non imprimables | Accessible depuis n'importe quel navigateur |

### Fichier de reporting avec macros VBA

| Avant — Fichier Excel | Apres — Grist + interface |
| --- | --- |
| Macro VBA de 500 lignes pour generer un rapport | Donnees dans Grist, logique en Python (lisible, documentee) |
| Ne fonctionne que sur la machine de Jean-Pierre | Interface web de reporting generee par le Vibe Lab |
| Incompatible avec les mises a jour d'Office | Fonctionne sur tout navigateur, tout OS |
| Personne ne sait comment ca marche | La logique est visible et comprehensible par un non-developpeur |
| Donnees et presentation melangees | Si l'interface meurt, les donnees et calculs restent intacts |

### Annuaire / referentiel metier

| Avant — Fichier Excel | Apres — Grist + interface |
| --- | --- |
| Fichier Excel partage sur un lecteur reseau | Base relationnelle Grist avec tables liees |
| Donnees dupliquees entre onglets (pas de relations) | Recherche full-text, filtres par colonne |
| Recherche par Ctrl+F uniquement | API REST : alimentation automatique depuis / vers d'autres outils |
| Aucune API — impossible d'integrer ailleurs | Interface web avec fiche detaillee par enregistrement |

---

## 5. Modele de passage a l'echelle

> Chaque migration alimente un pipeline reutilisable. Le premier fichier Excel prend 3 jours. Le dixieme prend 1 jour. Le centieme prend 2 heures. L'outillage s'ameliore, les patterns se repetent, l'IA apprend les structures typiques du ministere.

### 5.1 Categorisation des fichiers

Tous les fichiers Excel ne se valent pas. La premiere etape est un diagnostic automatise qui categorise chaque fichier selon sa complexite :

| Niveau | Description | Effort | Part estimee |
| --- | --- | --- | --- |
| **Niveau 1** | Tableau simple : 1-3 onglets, formules basiques (SOMME, SI, NB.SI), pas de macro | 2-4 heures | ~60 % |
| **Niveau 2** | Tableur structure : 4-10 onglets, formules avancees (RECHERCHEV, INDEX, tableaux croises), mises en forme conditionnelles | 1-2 jours | ~25 % |
| **Niveau 3** | Application Excel : macros VBA, formulaires, interactions entre classeurs, logique metier complexe | 3-5 jours | ~12 % |
| **Niveau 4** | Usine a gaz : VBA massif, connexions ODBC, dependances externes, donnees sensibles | Hors scope | ~3 % |

> Le **niveau 4** est hors perimetre du Vibe Lab. Ces fichiers sont en realite des applications metier deguisees qui relevent d'un projet SI classique ou de BercyHub.

### 5.2 Effet de reseau

Le modele de scaling repose sur deux mecanismes :

- **L'outillage s'ameliore a chaque migration** — Chaque fichier migre enrichit la bibliotheque de patterns : structures de donnees typiques, formules recurrentes, widgets reutilisables. Apres 20 migrations, le diagnostic est quasi instantane et la generation du schema Grist est automatisee a 80 %.

- **La demande se genere d'elle-meme** — Quand un bureau voit que le bureau d'a cote a remplace son Excel infernal par une mini-app web collaborative et esthetique, il demande la meme chose. Pas besoin de vendre le projet — il se vend tout seul par l'exemple.

---

## 6. Scoring sur la grille Vibe Lab

Application de la grille d'evaluation du Vibe Lab au projet ExcelExit :

| Critere | Note | Pondere | Justification |
| --- | --- | --- | --- |
| Impact utilisateur | 5/5 | x3 = 15 | Potentiellement chaque agent du ministere. Des centaines de fichiers concernes. |
| Urgence metier | 4/5 | x2 = 8 | Risque permanent de perte de donnees et de savoir. Chaque depart en retraite aggrave le probleme. |
| Disponibilite donnees | 5/5 | x2 = 10 | Les donnees sont dans les fichiers Excel eux-memes — fournies par le metier, pas a chercher. |
| Visibilite | 5/5 | x1 = 5 | Projet universel. Chaque ministere a le meme probleme. Effet vitrine garanti. |
| Complexite (inversee) | 4/5 | x1 = 4 | Niveaux 1-2 sont simples. Le mecanisme est repetitif et automatise progressivement. |
| Reutilisabilite | 5/5 | x1 = 5 | Chaque composant (diagnostic, generation de schema, widgets) est reutilisable pour toute migration. |

> **Score total : 47/50 — Entree prioritaire dans le backlog.**
> C'est le score le plus eleve de tous les projets evalues.

---

## 7. Positionnement

### 7.1 Par rapport a BercyHub

> **Zero chevauchement.**
>
> ExcelExit migre des fichiers Excel de suivi, de planification, de reporting — pas des donnees de SI metier. Les donnees atterrissent dans Grist, heberge par la DINUM, accessible par navigateur.
>
> Si un fichier s'avere contenir des donnees sensibles (niveau 4), il est exclu du perimetre ExcelExit et signale a BercyHub. La regle de demarcation s'applique comme pour tout projet du Lab.

### 7.2 Par rapport a la DSI

> **La DSI est une alliee naturelle.**
>
> La DSI reve de reduire le shadow IT Excel. ExcelExit lui offre un chemin de migration concret, a cout marginal, vers une infrastructure souveraine deja disponible. Chaque fichier migre est un fichier de moins qui echappe au radar.

### 7.3 Par rapport a la DINUM

> **ExcelExit valorise l'infrastructure Grist interministerielle.**
>
> grist.numerique.gouv.fr est un outil mis a disposition par la DINUM. Chaque migration ExcelExit est un cas d'usage supplementaire qui demontre la pertinence de cet investissement. Le ministere de l'Economie peut devenir le premier ministere a utiliser Grist a l'echelle.

---

## 8. Plan de deploiement

| Semaine | Activite | Livrable |
| --- | --- | --- |
| **S1-S2** | Identification de 5 fichiers Excel pilotes dans 2-3 directions differentes. Criteres : fichier utilise quotidiennement, douleur visible, sponsor motive. | Liste des 5 fichiers, diagnostic de complexite |
| **S3-S4** | Migration des 5 fichiers vers Grist. Creation des interfaces web DSFR. Tests avec les utilisateurs. | 5 documents Grist fonctionnels + 5 mini-apps DSFR |
| **S5-S6** | Retours utilisateurs, iterations, documentation. Mesure de l'adoption (connexions, frequence d'usage). | Bilan pilote chiffre, temoignages utilisateurs |
| **S7-S8** | Industrialisation de l'outillage : script de diagnostic automatise, generateur de schema, bibliotheque de widgets. | Pipeline de migration semi-automatise |
| **S9+** | Montee en charge : traitement par lots, ouverture aux demandes de toutes les directions, communication interne. | 10-20 fichiers migres/mois |

**Chiffres cles :**

- **0 EUR infrastructure** — Grist DINUM deja disponible
- **5 fichiers pilotes** en 6 semaines
- **10-20 fichiers/mois** en vitesse de croisiere a partir de S9

---

## 9. Ce qu'ExcelExit ne fait pas

- Ne migre pas les fichiers contenant des **donnees personnelles ou sensibles** (niveau 4)
- Ne remplace pas les **SI metier** (Chorus, SI-RH, etc.)
- Ne force personne — la migration est **proposee, pas imposee**
- Ne supprime pas les fichiers Excel sources (ils restent en **backup**)
- Ne promet pas une interface eternelle — **si l'interface meurt, les donnees vivent**

---

## 10. En resume

Le ministere de l'Economie a des centaines de fichiers Excel dont le maintien repose sur la memoire d'un agent. Chaque depart en retraite, chaque mutation, chaque reorganisation est un risque de perte silencieuse.

ExcelExit transforme ce risque en opportunite. Pas en remplacant Excel par un systeme lourd, mais en portant les donnees vers une plateforme ouverte, collaborative et souveraine — avec, en prime, des interfaces qui rendent le quotidien des agents plus agreable.

**Et si l'interface disparait un jour, les donnees restent. C'est toute la difference.**

> **ExcelExit, c'est :**
>
> - Un **probleme universel** (chaque bureau a ses Excel critiques)
> - Une **infrastructure deja en place** (grist.numerique.gouv.fr)
> - Un **cout marginal** (0 EUR d'infra, quelques heures par fichier)
> - Une **valeur perenne** (donnees + formules dans Grist, interface jetable)
> - Un **effet de reseau** (la demande se genere d'elle-meme)
> - **Zero chevauchement** BercyHub
> - **Score de 47/50** sur la grille d'evaluation Vibe Lab
