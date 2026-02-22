# Rapport d'opportunite : le vibe coding au service du ministere

**Retour d'experience sur 6 mois de prototypage assiste par IA -- Proposition de creation d'un Lab**

Bertrand Matge -- Responsable MIWEB (Mission Ingenierie du Web)
Service du numérique (SNUM) -- Fevrier 2026

---

## 1. Synthese executive

> En 6 mois, **1 agent** equipe d'IA generative a produit **8 outils numeriques** de qualite professionnelle representant **~376 000 lignes de code** -- soit l'equivalent de **~663 K Euros** en prestation, pour un cout reel inferieur a **80 K Euros**.
>
> Ce rapport propose la creation d'un **Lab Vibe Coding** : 1 a 3 agents dedies + ~1 000 Euros/mois de licences.

Entre septembre 2025 et fevrier 2026, une demarche experimentale de "vibe coding" -- developpement logiciel assiste par IA generative -- a ete menee au sein de la MIWEB. Un seul agent, equipe de **Claude (Anthropic)** et **GitHub Copilot**, a produit 8 outils numeriques fonctionnels couvrant un spectre large : monitoring web, intelligence editoriale, dataviz, enquetes publiques, organigrammes, comparateurs de donnees ouvertes et outillage contributeur.

Ce rapport detaille les realisations, analyse la qualite du code produit, et propose la creation d'une mission dediee "Lab Vibe Coding" : **1 a 3 agents** a temps plein, un investissement en licences plafonne a **~1 000 Euros/mois**, et un acces a l'infrastructure de deploiement existante.

| | | |
| --- | --- | --- |
| **8** produits numeriques fonctionnels, testes, documentes | **~376 000** lignes de code qualite professionnelle | **663 K Euros** cout presta. equiv. -- 1 105 jours-homme |
| **~80 K Euros** cout reel estime -- 130 j/h, 1 agent + IA | **88 %** d'economie vs. prestation classique | **6 mois** duree totale -- initiative personnelle |

---

## 2. Contexte et methodologie

### 2.1 Le vibe coding : un tandem humain-IA

Le vibe coding est une approche de developpement dans laquelle un professionnel collabore avec un modele d'IA generative pour produire du code. L'humain definit l'**intention**, l'**architecture** et les **contraintes metier**. L'IA genere, itere et corrige le code en temps reel. Ce tandem multiplie la productivite d'un profil tech/produit par un facteur estime entre **5 et 10**.

### 2.2 Conditions de l'experimentation

- **Periode** : septembre 2025 -- fevrier 2026 (6 mois)
- **Ressource** : 1 agent public (profil tech/produit, responsable MIWEB)
- **Outils IA** : Claude (Anthropic) + GitHub Copilot
- **Cadre** : initiative personnelle, sans budget dedie ni equipe projet
- **Contrainte** : respect systematique du DSFR, des standards RGAA et des preconisations ANSSI

### 2.3 Methodologie d'evaluation des couts

Pour chaque projet, l'analyse a ete realisee directement sur les depots GitHub : lignes de code, fichiers, technologies, presence de tests, patterns architecturaux, conformite aux standards. L'estimation du cout prestataire est basee sur un **TJM de 600 Euros** (developpeur junior/intermediaire en marche public), integrant specification, developpement, tests, integration et mise en production. Ces estimations sont conservatrices ; les couts reels de pilotage et contractualisation les majorent significativement.

---

## 3. Inventaire des realisations

### 3.1 Ecosysteme (G3) -- Monitoring et gouvernance web

Plateforme de monitoring de l'ensemble des sites web ministeriels. Inventaire centralise, 18 scanners automatises (SSL, accessibilite, performance, RGPD, DSFR), systeme d'alertes multi-niveaux, gestion des certificats SSL, KPI consolides, assistant IA integre, serveur MCP, administration complete avec RBAC.

| | | |
| --- | --- | --- |
| **~238 000 LOC** | **Stack** | **Qualite** |
| 520 j/h -- 312 000 Euros | TypeScript 5.7, React 19, Express.js, PostgreSQL, Redis/BullMQ, Vite, DSFR, D3.js, Playwright, Docker/Traefik | Monorepo pnpm, 25 modules, 63 migrations SQL, 456 fichiers de tests, architecture en couches, EventBus, TypeScript strict, CI/CD GitHub Actions, deploiement Docker conforme ANSSI |

### 3.2 Portail Eco Browser -- Intelligence editoriale

Outil d'exploration du portail economie.gouv.fr. Navigation dans le contenu Drupal, analytics multi-sources (Eulerian, Cloudflare, Google Search Console), clustering semantique (HDBSCAN/UMAP), recherche RAG avec embeddings, trajectoires de trafic, diagnostics SEO, assistant IA Albert.

| | | |
| --- | --- | --- |
| **~88 500 LOC** | **Stack** | **Qualite** |
| 270 j/h -- 162 000 Euros | React 18 + TypeScript (Vite), FastAPI + SQLAlchemy, Elasticsearch, Transformers/scikit-learn, DSFR, Docker Compose | Architecture modulaire FastAPI, 28 services metier, 1 290 tests backend (pytest) + 22 suites frontend (Vitest), typage strict Pydantic, CI/CD avec Ruff + Trivy |

### 3.3 ChartsBuilder (gouv-widgets) -- Dataviz DSFR

Bibliotheque de 24 web components DSFR pour la dataviz gouvernementale. 5 connecteurs API (OpenDataSoft, data.gouv.fr, Grist, INSEE, REST generique), 8 applications (builder visuel, builder IA, playground, dashboard). Zero JavaScript requis cote integrateur. Publie sur npm.

| | | |
| --- | --- | --- |
| **~41 500 LOC** | **Stack** | **Qualite** |
| 200 j/h -- 120 000 Euros | TypeScript 5.3, Lit 3.1, DSFR Chart 2.0, Vite, Tauri, D3-Geo, npm workspaces | Monorepo npm, composants Lit encapsules, pattern adapter/registry, accessibilite RGAA/WCAG AA native, build ESM + UMD (~50 KB gzippe), 83 specs de tests |

### 3.4 Theme LimeSurvey DSFR + Plugins

Theme DSFR complet pour LimeSurvey avec plugin ConversationIA (Albert), plugin DSFRMail pour les emails ministeriels, et type de question avance (ranking). Documentation exhaustive (60 Ko+).

| | | |
| --- | --- | --- |
| **23 fichiers custom + assets DSFR** | **Stack** | **Qualite** |
| 45 j/h -- 27 000 Euros | PHP/Yii (LimeSurvey), Twig, JavaScript, CSS/SCSS, DSFR, Gulp, Docker | Plugins structures (config.xml), 1000+ icones, 22 familles de polices, Prettier + ESLint + Stylelint, plan d'accessibilite dedie |

### 3.5 Organigrammes service public

Generateur automatique d'organigrammes a partir de l'API Annuaire du service public. Recherche par organisme, construction BFS de l'arbre hierarchique, deux modes de rendu (HTML/CSS et D3 interactif), filtrage par categorie, export multi-format (JSON, CSV, PNG, SVG, PDF A4/A3). Realise a la demande du studio graphique ministeriel pour automatiser la production d'organigrammes.

| | | |
| --- | --- | --- |
| **~500 LOC** | **Stack** | **Qualite** |
| 10 j/h -- 6 000 Euros | JavaScript vanilla, HTML5, CSS3, DSFR, D3-org-chart, API Annuaire service-public.gouv.fr | Zero framework, zero build, page statique deployee sur GitHub Pages, CI/CD integre |

### 3.6 Comparateurs de donnees ouvertes

Deux demonstrateurs de services grand public bases sur les open data du ministere :

- **Prix Controle Technique** : carte interactive choroplethe, filtres multi-criteres, observatoire statistique
- **Tarifs Bancaires** : wizard multi-etapes, comparaison cote a cote, export CSV

Les deux branches sur l'API data.economie.gouv.fr.

| | | |
| --- | --- | --- |
| **~5 500 LOC** | **Stack** | **Qualite** |
| 45 j/h -- 27 000 Euros | React 18, Leaflet, Zustand, Fuse.js, Vanilla JS, Node.js natif, DSFR, Docker/Nginx/Traefik | Architecture React moderne, optimisation performance, zero dependance framework (Tarifs), cles API cote serveur, headers securite, HTML semantique accessible |

### 3.7 LeFouineur -- Extension navigateur

Extension navigateur (Manifest V3) d'alerte et d'analyse qualite pour les contributeurs web. Script de contenu analysant les pages visitees, interface popup, systeme de messagerie inter-composants. 90 Ko, zero dependance externe.

| | | |
| --- | --- | --- |
| **~2 000 LOC** | **Stack** | **Qualite** |
| 15 j/h -- 9 000 Euros | JavaScript vanilla, HTML5, CSS3, Manifest V3, SVG | Architecture modulaire (content script / popup / config), branding professionnel (logo SVG, icones multi-resolution) |

---

## 4. Synthese comparative des couts

| Projet | LOC | J/H | Cout presta. | Stack principale |
| --- | --- | --- | --- | --- |
| Ecosysteme (G3) | ~238 000 | 520 | 312 000 Euros | TypeScript, React 19, Express, PostgreSQL, Redis, Docker |
| Portail Eco Browser | ~88 500 | 270 | 162 000 Euros | React 18, FastAPI, Elasticsearch, ML/NLP |
| ChartsBuilder (gouv-widgets) | ~41 500 | 200 | 120 000 Euros | TypeScript, Lit 3, DSFR Chart, Tauri |
| Theme LimeSurvey DSFR | -- | 45 | 27 000 Euros | PHP/Yii, Twig, DSFR, Docker |
| Organigrammes service public | -- | 10 | 6 000 Euros | JS vanilla, D3, API Annuaire, DSFR |
| Prix Controle Technique | ~3 300 | 25 | 15 000 Euros | React 18, Leaflet, Zustand, DSFR |
| Tarifs Bancaires | ~2 100 | 20 | 12 000 Euros | Vanilla JS, Node.js natif, DSFR |
| LeFouineur (extension) | ~2 000 | 15 | 9 000 Euros | JS vanilla, Manifest V3 |
| **TOTAL** | **~376 000** | **1 105** | **663 000 Euros** | |

> **Cout prestataire estime : 663 000 Euros** (1 105 jours-homme, equipes de 1 a 4 developpeurs)
>
> **Cout vibe coding estime : ~80 000 Euros** equivalent (130 jours-homme, 1 agent + IA)
>
> **Economie estimee : 583 000 Euros, soit 88 %** du cout prestataire
>
> Note : ces estimations n'incluent pas les couts de pilotage, contractualisation, reunions de suivi et recette qui majorent le cout prestataire reel de 20 a 40 % supplementaires.

---

## 5. Analyse qualitative du code produit

### 5.1 Standards respectes

Tous les projets front-end integrent le **DSFR**, garantissant coherence visuelle et conformite avec la charte de l'Etat. Les deploiements utilisent **Docker** avec des configurations **Traefik** conformes aux preconisations ANSSI (TLS strict, headers de securite). Plusieurs projets integrent **Albert** (IA souveraine Etalab) et se connectent exclusivement aux API publiques francaises.

### 5.2 Pratiques de developpement

- **Typage strict** : TypeScript utilise sur 5 des 8 projets, Pydantic pour la validation Python
- **Tests automatises** : plus de 1 800 tests unitaires et d'integration, completes par des tests E2E Playwright
- **Architecture** : patterns Repository/Service/Handler, monorepos avec workspaces, separation des responsabilites
- **CI/CD** : pipelines GitHub Actions (linting, tests, build Docker, scan de securite Trivy)
- **Documentation** : README detailles, ADR, documentation technique generee

### 5.3 Points de vigilance

Le vibe coding n'est pas exempt de limites. Certains fichiers presentent une taille elevee (50 Ko+) qui beneficierait d'un refactoring. La couverture de tests, significative sur les projets majeurs, reste limitee sur les POC. Ces points sont coherents avec une approche de prototypage rapide et n'alterent pas la solidite globale.

---

## 6. L'IA ne remplace pas les competences -- elle debloque ce qui etait impossible

> Aucun de ces 8 projets n'aurait ete realise sans l'IA. Non pas parce que les competences manquent, mais parce que les circuits classiques rendent leur cout et leur delai disproportionnes par rapport au besoin.

Il est essentiel de lever une ambiguite : ces outils n'ont pas ete produits par l'IA au detriment de developpeurs humains. Ils **n'auraient tout simplement jamais existe autrement**. Aucun responsable n'aurait lance un marche public de 312 000 Euros pour une plateforme de monitoring, ni mobilise 3 developpeurs pendant 5 mois pour un generateur d'organigrammes ou un comparateur de tarifs bancaires. Ces besoins sont reels, mais leur rapport cout/benefice ne justifiait pas une prestation classique.

Le vibe coding **rend viable ce qui etait deraisonnable**. Un besoin ponctuel -- habiller une consultation, visualiser un jeu de donnees, automatiser un processus du studio graphique -- trouve sa reponse en quelques jours au lieu de plusieurs mois. L'outil peut etre perenne ou jetable : peu importe, car son cout de production est devenu marginal.

Dans le circuit classique, **le temps joue contre le projet**. Le temps de specifier, rediger un cahier des charges, passer un marche, suivre le developpement et recetter, le contexte a change. L'urgence est passee, la reorganisation a eu lieu, le portail a evolue. L'outil livre six mois plus tard ne correspond plus au besoin initial.

Le vibe coding **inverse cette logique** : on repond au besoin quand il se presente, avec un outil calibre pour l'instant present. Si le besoin evolue, on adapte en quelques heures. S'il disparait, on passe a autre chose sans regret -- le cout engage reste derisoire.

C'est cette facilite de realisation qui constitue le **changement de paradigme**. Il ne s'agit pas de remplacer des prestataires ou des equipes internes, mais de faire exister des outils qui, sans cette methode, seraient restes a l'etat d'idees -- ou de lignes dans un schema directeur que personne n'aurait finance.

---

## 7. Avantages strategiques pour le service du numerique

### 7.1 Velocite de prototypage

Le POC Tarifs Bancaires -- comparateur complet avec wizard multi-etapes, integration API, export CSV, design DSFR -- a ete realise en **quelques jours**. En prestation classique : **3 a 4 semaines minimum**. Cette velocite permet de tester des hypotheses produit avant de decider d'industrialiser, reduisant considerablement le risque de projets inadaptes.

### 7.2 Reduction de la dependance aux prestataires

Le vibe coding permet a un profil metier-tech de produire des outils sans mobiliser d'equipe externe. Cela reduit :

- Les **delais** lies aux cycles de contractualisation (marches publics, bons de commande)
- Les **allers-retours** de specification
- Les **couts de pilotage**

Les prestataires restent mobilises sur les projets industriels a forte charge ; le Lab prend en charge le prototypage et l'outillage interne.

### 7.3 Qualite professionnelle du code

Contrairement aux prejuges sur le code genere par IA, les projets analyses presentent une qualite souvent **superieure** a ce qu'on observe en prestation standard : typage strict, tests presents, architecture propre, documentation generee. L'IA suit systematiquement les bonnes pratiques quand elle est correctement guidee par un profil competent.

### 7.4 Souverainete numerique

Plusieurs projets integrent **Albert** (IA souveraine Etalab) et se connectent exclusivement a des API publiques francaises (data.gouv.fr, data.economie.gouv.fr, INSEE, Annuaire du service public). Le code reste sous controle complet de l'administration, heberge sur GitHub, deployable sur infrastructure souveraine.

### 7.5 Securite et souverainete : un risque nul par construction

> Ces projets manipulent du code public, des donnees publiques, pour des usages publics. Le risque securite et RGPD est nul par conception.

L'ensemble des projets produits sont **open source** et publies sur GitHub. C'est un choix delibere, pas une contrainte : ces outils de communication sont destines a etre vus, utilises et reutilises. La publication du code source renforce la visibilite du ministere dans l'ecosysteme open source public et positionne le SNUM comme acteur de reference en matiere de developpement numerique etatique.

**Aucun de ces projets ne presente de risque de securite ni de problematique RGPD.** Les donnees manipulees sont exclusivement des donnees ouvertes (open data ministerielles, API Annuaire du service public, data.gouv.fr, INSEE). Le code ne contient ni secret, ni donnee personnelle, ni information sensible. Les outils produits sont destines a etre exposes au public : sites web, consultations citoyennes, comparateurs, organigrammes officiels. On travaille sur du code public, avec des donnees publiques, pour des choses montrees au public.

Cote deploiement, les offres cloud actuelles -- qualifiees SecNumCloud ou non -- rendent l'hebergement simple, economique et sans risque. Pour des applications de communication qui n'hebergent aucune donnee sensible (pas de SI interne, pas de donnee de sante, pas d'information classifiee), un hebergement cloud standard repond parfaitement aux exigences. Les conteneurs Docker utilises par tous les projets garantissent une **portabilite totale** : si un jour une qualification superieure etait requise, la migration se ferait sans modification du code.

L'utilisation d'outils d'IA generative (Claude, Copilot) pour la production du code ne pose pas non plus de probleme de confidentialite dans ce contexte : le code produit est public, les specifications transmises a l'IA ne contiennent aucune donnee protegee, et le resultat est systematiquement publie en open source. C'est precisement le domaine ou l'IA generative peut etre utilisee **sans reserve**.

### 7.6 Effet de levier sur les equipes existantes

Le Lab n'est pas une structure isolee : c'est un **accelerateur** au service des equipes metier. La communication a besoin d'un outil de pilotage ? Le Lab le prototype en quelques jours. Le studio graphique perd du temps sur les organigrammes ? Le Lab automatise le processus. Une direction veut valoriser un jeu de donnees ? Le Lab livre un comparateur fonctionnel avant meme que le cahier des charges n'ait ete redige.

---

## 8. Proposition : creation du Lab Vibe Coding

### 8.1 Objectif

Creer une mission dediee "Lab Vibe Coding" au sein du service du numerique, chargee de produire rapidement des prototypes et outils numeriques en exploitant les capacites de l'IA generative pour le developpement logiciel.

### 8.2 Missions

1. **Prototypage rapide** -- Valider des idees metier en quelques jours avant toute decision d'industrialisation.
2. **Outillage interne** -- Monitoring, pilotage, dataviz, automatisation de processus repetitifs, sans recours a la prestation.
3. **Composants reutilisables** -- Bibliotheque de composants DSFR (charts, themes, extensions) immediatement deployables.
4. **Veille et experimentation** -- Evaluation continue des outils IA appliques au developpement, partage de bonnes pratiques.
5. **Accompagnement** -- Formation et appui des equipes metier et techniques a l'utilisation du vibe coding.

### 8.3 Moyens demandes

- **Equipe** : 1 a 3 agents a temps plein (profils tech/produit)
  Idealement des profils qui connaissent les metiers du ministere et maitrisent les fondamentaux techniques (architecture, API, deploiement). Le vibe coding ne necessite pas d'etre developpeur senior, mais d'etre capable de guider, valider et corriger le code produit par l'IA.

- **Licences IA** : plafonnees a ~1 000 Euros/mois
  Abonnements Claude Pro ou Team (Anthropic) + GitHub Copilot, soit environ 200-350 Euros/personne/mois. Pour 3 agents : ~1 000 Euros/mois maximum.

- **Infrastructure** : existante
  Acces a l'infrastructure de deploiement deja en place (GitHub, CI/CD, Docker, hebergement). Aucun investissement supplementaire necessaire.

### 8.4 Budget annuel detaille (hors masse salariale)

| Poste de depense | Cout mensuel | Cout annuel |
| --- | --- | --- |
| Licences IA (Claude Pro/Team, Copilot) | ~1 000 Euros/mois | ~12 000 Euros/an |
| Infrastructure (CI/CD, hebergement, domaines) | ~200 Euros/mois | ~2 400 Euros/an |
| Abonnements API (si necessaire) | ~100 Euros/mois | ~1 200 Euros/an |
| **TOTAL LICENCES & INFRA** | **~1 300 Euros/mois** | **~15 600 Euros/an** |

> **Cout total hors masse salariale : ~15 600 Euros/an**
>
> Pour comparaison, l'equivalent prestataire des 8 outils deja produits est estime a 663 000 Euros. Le cout annuel du Lab represente **2,4 %** de cette somme.
>
> Autrement dit : le Lab s'autofinance des son premier mois de fonctionnement en evitement de couts prestataires.

### 8.5 Indicateurs de succes proposes

- **Production** : nombre de prototypes livres par trimestre, taux de passage en production des POC
- **Efficience** : delai moyen idee vers prototype fonctionnel, economies realisees vs. prestation equivalente
- **Adoption** : satisfaction des equipes metier utilisatrices, nombre de demandes traitees

### 8.6 Gouvernance suggeree

Le Lab serait rattache au service du numerique avec un mode de fonctionnement agile. Un cadre de gouvernance a deja ete formalise :

- **Comite de priorisation mensuel** (30 minutes, avec les directions sponsors)
- **Revue trimestrielle** (1 heure, avec le SNUM n+2)
- **Point trimestriel dedie avec BercyHub** pour eviter tout chevauchement de perimetre

**Cinq regles cardinales** encadrent le fonctionnement :

1. Pas de projet sans sponsor metier
2. Pas de projet hors perimetre (donnees publiques uniquement)
3. Maximum 5 projets actifs
4. Abandon a 4 semaines sans usage
5. Transparence totale

Une **grille d'evaluation objective** (scoring sur 50 points, 6 criteres ponderes) determine les priorites d'entree dans le backlog. Les projets a fort potentiel seraient proposes pour industrialisation sur les marches existants ou transferes a BercyHub si le besoin justifie un traitement sur donnees sensibles.

### 8.7 Articulation avec BercyHub

Le positionnement du Vibe Lab par rapport a BercyHub est celui d'un **eclaireur**, pas d'un concurrent. Le Lab prototype sur donnees publiques, valide le concept avec les utilisateurs, puis la direction arbitre : perenniser en l'etat, ou transferer a BercyHub pour industrialisation sur donnees sensibles. BercyHub gagne ainsi un **pipeline de projets deja valides par l'usage**.

La regle de demarcation est absolue : des qu'un projet touche aux SI metier, aux donnees personnelles ou a une homologation de securite, il releve de BercyHub. Cette complementarite est formalisee dans la fiche de gouvernance et fait l'objet d'un point trimestriel structure.

### 8.8 Prochaine etape : ExcelExit

Le premier projet candidat pour le Lab structure est **ExcelExit** : la migration systematique des fichiers Excel critiques du ministere vers **Grist** (grist.numerique.gouv.fr), infrastructure interministerielle operee par la DINUM. Avec un score de **47/50** sur la grille d'evaluation -- le plus eleve de tous les projets evalues -- ExcelExit repond a un probleme universel (chaque bureau a ses Excel critiques), repose sur une infrastructure gratuite et deja en place, et genere sa propre demande par l'effet vitrine.

Le principe fondamental : **la valeur repose dans les donnees et les formules Grist, pas dans l'interface**. Si l'interface disparait, les donnees restent. Le detail est documente dans la note de cadrage ExcelExit.

---

## 9. Conclusion

> Structurer le Lab Vibe Coding, c'est transformer une initiative personnelle en capacite institutionnelle. C'est positionner le service du numerique comme pionnier dans l'utilisation de l'IA generative au service de l'administration publique. Un cadre complet accompagne cette proposition : fiche de gouvernance (cycle de vie des projets, instances, roles), grille d'evaluation (criteres d'entree et de scoring), matrice des risques (8 risques identifies, 0 residuel critique), plan de communication (12 semaines pour generer la demande), et note de cadrage ExcelExit (premier projet du backlog elargi).

Les resultats de cette experimentation sont sans ambiguite : **8 produits numeriques fonctionnels**, **~376 000 lignes de code** de qualite professionnelle, produits par un seul agent en 6 mois. L'economie estimee par rapport a un developpement en prestation classique est de l'ordre de **583 000 Euros**, sans compter les couts indirects de pilotage et contractualisation.

La demande est modeste : **1 a 3 agents dedies** et environ **1 000 Euros de licences par mois**. Le retour sur investissement est immediat : chaque prototype livre evite des semaines de specification et des dizaines de milliers d'euros de prestation.

Au-dela de l'economie financiere, le Lab Vibe Coding offrirait au service du numerique un **avantage strategique** : la capacite a tester rapidement des idees, valider des hypotheses produit, et livrer de la valeur metier avant meme que les circuits classiques n'aient demarre.

---

## Annexe -- Depots GitHub

| Projet | Depot |
| --- | --- |
| Ecosysteme (G3) | https://github.com/bmatge/g3 |
| Portail Eco Browser | https://github.com/bmatge/portail-eco-browser |
| ChartsBuilder | https://github.com/bmatge/datasource-charts-webcomponents |
| LimeSurvey DSFR | https://github.com/bmatge/LimeSurvey-DSFR |
| Organigrammes | https://github.com/bmatge/org-chart-service-public |
| Prix Controle Technique | https://github.com/bmatge/prix-controle-technique |
| Tarifs Bancaires | https://github.com/bmatge/tarifs-bancaires |
| LeFouineur | https://github.com/bmatge/eco-alert-bo |
