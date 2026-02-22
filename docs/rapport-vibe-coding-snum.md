Bertrand Matgé
Responsable MIWEB — Mission Ingénierie du Web
Sous-direction du Numérique (SNUM)
Février 2026

# 1. Synthèse exécutive
Entre septembre 2025 et février 2026, une démarche expérimentale de « vibe coding » — développement logiciel assisté par IA générative — a été menée au sein de la MIWEB. Un seul agent, équipé de Claude (Anthropic) et GitHub Copilot, a produit 8 outils numériques fonctionnels couvrant un spectre large : monitoring web, intelligence éditoriale, dataviz, enquêtes publiques, organigrammes, comparateurs de données ouvertes et outillage contributeur.

Ce rapport détaille les réalisations, analyse la qualité du code produit, et propose la création d’une mission dédiée « Lab Vibe Coding » : 1 à 3 agents à temps plein, un investissement en licences plafonné à ~1 000 €/mois, et un accès à l’infrastructure de déploiement existante.
# 2. Contexte et méthodologie
## 2.1 Le vibe coding : un tandem humain-IA
Le vibe coding est une approche de développement dans laquelle un professionnel collabore avec un modèle d’IA générative pour produire du code. L’humain définit l’intention, l’architecture et les contraintes métier. L’IA génère, itère et corrige le code en temps réel. Ce tandem multiplie la productivité d’un profil tech/produit par un facteur estimé entre 5 et 10.
## 2.2 Conditions de l’expérimentation
Période : septembre 2025 – février 2026 (6 mois). Ressource : 1 agent public (profil tech/produit, responsable MIWEB). Outils IA : Claude (Anthropic) + GitHub Copilot. Cadre : initiative personnelle, sans budget dédié ni équipe projet. Contrainte : respect systématique du DSFR, des standards RGAA et des préconisations ANSSI.
## 2.3 Méthodologie d’évaluation des coûts
Pour chaque projet, l’analyse a été réalisée directement sur les dépôts GitHub : lignes de code, fichiers, technologies, présence de tests, patterns architecturaux, conformité aux standards. L’estimation du coût prestataire est basée sur un TJM de 600 € (développeur junior/intermédiaire en marché public), intégrant spécification, développement, tests, intégration et mise en production. Ces estimations sont conservatrices ; les coûts réels de pilotage et contractualisation les majorent significativement.
# 3. Inventaire des réalisations

## 3.1 Écosystème (G3) — Monitoring et gouvernance web
Plateforme de monitoring de l’ensemble des sites web ministériels. Inventaire centralisé, 18 scanners automatisés (SSL, accessibilité, performance, RGPD, DSFR), système d’alertes multi-niveaux, gestion des certificats SSL, KPI consolidés, assistant IA intégré, serveur MCP, administration complète avec RBAC.

## 3.2 Portail Eco Browser — Intelligence éditoriale
Outil d’exploration du portail economie.gouv.fr. Navigation dans le contenu Drupal, analytics multi-sources (Eulerian, Cloudflare, Google Search Console), clustering sémantique (HDBSCAN/UMAP), recherche RAG avec embeddings, trajectoires de trafic, diagnostics SEO, assistant IA Albert.

## 3.3 ChartsBuilder (gouv-widgets) — Dataviz DSFR
Bibliothèque de 24 web components DSFR pour la dataviz gouvernementale. 5 connecteurs API (OpenDataSoft, data.gouv.fr, Grist, INSEE, REST générique), 8 applications (builder visuel, builder IA, playground, dashboard). Zéro JavaScript requis côté intégrateur. Publié sur npm.

## 3.4 Thème LimeSurvey DSFR + Plugins
Thème DSFR complet pour LimeSurvey avec plugin ConversationIA (Albert), plugin DSFRMail pour les emails ministériels, et type de question avancé (ranking). Documentation exhaustive (60 Ko+).

## 3.5 Organigrammes service public
Générateur automatique d’organigrammes à partir de l’API Annuaire du service public. Recherche par organisme, construction BFS de l’arbre hiérarchique, deux modes de rendu (HTML/CSS et D3 interactif), filtrage par catégorie, export multi-format (JSON, CSV, PNG, SVG, PDF A4/A3). Réalisé à la demande du studio graphique ministériel pour automatiser la production d’organigrammes.

## 3.6 Comparateurs de données ouvertes
Deux démonstrateurs de services grand public basés sur les open data du ministère. Prix Contrôle Technique : carte interactive choroplèthe, filtres multi-critères, observatoire statistique. Tarifs Bancaires : wizard multi-étapes, comparaison côte à côte, export CSV. Les deux branchés sur l’API data.economie.gouv.fr.

## 3.7 LeFouineur — Extension navigateur
Extension navigateur (Manifest V3) d’alerte et d’analyse qualité pour les contributeurs web. Script de contenu analysant les pages visitées, interface popup, système de messagerie inter-composants. 90 Ko, zéro dépendance externe.

# 4. Synthèse comparative des coûts

# 5. Analyse qualitative du code produit
## 5.1 Standards respectés
Tous les projets front-end intègrent le DSFR, garantissant cohérence visuelle et conformité avec la charte de l’État. Les déploiements utilisent Docker avec des configurations Traefik conformes aux préconisations ANSSI (TLS strict, headers de sécurité). Plusieurs projets intègrent Albert (IA souveraine Etalab) et se connectent exclusivement aux API publiques françaises.
## 5.2 Pratiques de développement
Typage strict : TypeScript utilisé sur 5 des 8 projets, Pydantic pour la validation Python. Tests automatisés : plus de 1 800 tests unitaires et d’intégration, complétés par des tests E2E Playwright. Architecture : patterns Repository/Service/Handler, monorepos avec workspaces, séparation des responsabilités. CI/CD : pipelines GitHub Actions (linting, tests, build Docker, scan de sécurité Trivy). Documentation : README détaillés, ADR, documentation technique générée.
## 5.3 Points de vigilance
Le vibe coding n’est pas exempt de limites. Certains fichiers présentent une taille élevée (50 Ko+) qui bénéficierait d’un refactoring. La couverture de tests, significative sur les projets majeurs, reste limitée sur les POC. Ces points sont cohérents avec une approche de prototypage rapide et n’altèrent pas la solidité globale.
# 6. L’IA ne remplace pas les compétences — elle débloque ce qui était impossible

Il est essentiel de lever une ambiguïté : ces outils n’ont pas été produits par l’IA au détriment de développeurs humains. Ils n’auraient tout simplement jamais existé autrement. Aucun responsable n’aurait lancé un marché public de 312 000 € pour une plateforme de monitoring, ni mobilisé 3 développeurs pendant 5 mois pour un générateur d’organigrammes ou un comparateur de tarifs bancaires. Ces besoins sont réels, mais leur rapport coût/bénéfice ne justifiait pas une prestation classique.
Le vibe coding rend viable ce qui était déraisonnable. Un besoin ponctuel — habiller une consultation, visualiser un jeu de données, automatiser un processus du studio graphique — trouve sa réponse en quelques jours au lieu de plusieurs mois. L’outil peut être pérenne ou jetable : peu importe, car son coût de production est devenu marginal.
Dans le circuit classique, le temps joue contre le projet. Le temps de spécifier, rédiger un cahier des charges, passer un marché, suivre le développement et recetter, le contexte a changé. L’urgence est passée, la réorganisation a eu lieu, le portail a évolué. L’outil livré six mois plus tard ne correspond plus au besoin initial.
Le vibe coding inverse cette logique : on répond au besoin quand il se présente, avec un outil calibré pour l’instant présent. Si le besoin évolue, on adapte en quelques heures. S’il disparaît, on passe à autre chose sans regret — le coût engagé reste dérisoire.
C’est cette facilité de réalisation qui constitue le changement de paradigme. Il ne s’agit pas de remplacer des prestataires ou des équipes internes, mais de faire exister des outils qui, sans cette méthode, seraient restés à l’état d’idées — ou de lignes dans un schéma directeur que personne n’aurait financé.
# 7. Avantages stratégiques pour le service du numérique
## 7.1 Vélocité de prototypage
Le POC Tarifs Bancaires — comparateur complet avec wizard multi-étapes, intégration API, export CSV, design DSFR — a été réalisé en quelques jours. En prestation classique : 3 à 4 semaines minimum. Cette vélocité permet de tester des hypothèses produit avant de décider d’industrialiser, réduisant considérablement le risque de projets inadaptés.
## 7.2 Réduction de la dépendance aux prestataires
Le vibe coding permet à un profil métier-tech de produire des outils sans mobiliser d’équipe externe. Cela réduit les délais liés aux cycles de contractualisation (marchés publics, bons de commande), aux allers-retours de spécification, et aux coûts de pilotage. Les prestataires restent mobilisés sur les projets industriels à forte charge ; le Lab prend en charge le prototypage et l’outillage interne.
## 7.3 Qualité professionnelle du code
Contrairement aux préjugés sur le code généré par IA, les projets analysés présentent une qualité souvent supérieure à ce qu’on observe en prestation standard : typage strict, tests présents, architecture propre, documentation générée. L’IA suit systématiquement les bonnes pratiques quand elle est correctement guidée par un profil compétent.
## 7.4 Souveraineté numérique
Plusieurs projets intègrent Albert (IA souveraine Etalab) et se connectent exclusivement à des API publiques françaises (data.gouv.fr, data.economie.gouv.fr, INSEE, Annuaire du service public). Le code reste sous contrôle complet de l’administration, hébergé sur GitHub, déployable sur infrastructure souveraine.
## 7.5 Sécurité et souveraineté : un risque nul par construction

L’ensemble des projets produits sont open source et publiés sur GitHub. C’est un choix délibéré, pas une contrainte : ces outils de communication sont destinés à être vus, utilisés et réutilisés. La publication du code source renforce la visibilité du ministère dans l’écosystème open source public et positionne le SNUM comme acteur de référence en matière de développement numérique étatique.
Aucun de ces projets ne présente de risque de sécurité ni de problématique RGPD. Les données manipulées sont exclusivement des données ouvertes (open data ministérielles, API Annuaire du service public, data.gouv.fr, INSEE). Le code ne contient ni secret, ni donnée personnelle, ni information sensible. Les outils produits sont destinés à être exposés au public : sites web, consultations citoyennes, comparateurs, organigrammes officiels. On travaille sur du code public, avec des données publiques, pour des choses montrées au public.
Côté déploiement, les offres cloud actuelles — qualifiées SecNumCloud ou non — rendent l’hébergement simple, économique et sans risque. Pour des applications de communication qui n’hébergent aucune donnée sensible (pas de SI interne, pas de donnée de santé, pas d’information classifiée), un hébergement cloud standard répond parfaitement aux exigences. Les conteneurs Docker utilisés par tous les projets garantissent une portabilité totale : si un jour une qualification supérieure était requise, la migration se ferait sans modification du code.
L’utilisation d’outils d’IA générative (Claude, Copilot) pour la production du code ne pose pas non plus de problème de confidentialité dans ce contexte : le code produit est public, les spécifications transmises à l’IA ne contiennent aucune donnée protégée, et le résultat est systématiquement publié en open source. C’est précisément le domaine où l’IA générative peut être utilisée sans réserve.
## 7.6 Effet de levier sur les équipes existantes
Le Lab n’est pas une structure isolée : c’est un accélérateur au service des équipes métier. La communication a besoin d’un outil de pilotage ? Le Lab le prototype en quelques jours. Le studio graphique perd du temps sur les organigrammes ? Le Lab automatise le processus. Une direction veut valoriser un jeu de données ? Le Lab livre un comparateur fonctionnel avant même que le cahier des charges n’ait été rédigé.

# 8. Proposition : création du Lab Vibe Coding
## 8.1 Objectif
Créer une mission dédiée « Lab Vibe Coding » au sein du service du numérique, chargée de produire rapidement des prototypes et outils numériques en exploitant les capacités de l’IA générative pour le développement logiciel.
## 8.2 Missions
1. Prototypage rapide — Valider des idées métier en quelques jours avant toute décision d’industrialisation.
2. Outillage interne — Monitoring, pilotage, dataviz, automatisation de processus répétitifs, sans recours à la prestation.
3. Composants réutilisables — Bibliothèque de composants DSFR (charts, thèmes, extensions) immédiatement déployables.
4. Veille et expérimentation — Évaluation continue des outils IA appliqués au développement, partage de bonnes pratiques.
5. Accompagnement — Formation et appui des équipes métier et techniques à l’utilisation du vibe coding.
## 8.3 Moyens demandés

## 8.4 Budget annuel détaillé (hors masse salariale)

## 8.5 Indicateurs de succès proposés
Production : nombre de prototypes livrés par trimestre, taux de passage en production des POC. Efficience : délai moyen idée → prototype fonctionnel, économies réalisées vs. prestation équivalente. Adoption : satisfaction des équipes métier utilisatrices, nombre de demandes traitées.
## 8.6 Gouvernance suggérée
Le Lab serait rattaché au service du numérique avec un mode de fonctionnement agile. Un cadre de gouvernance a déjà été formalisé : comité de priorisation mensuel (30 minutes, avec les directions sponsors), revue trimestrielle (1 heure, avec le SNUM n+2), et point trimestriel dédié avec BercyHub pour éviter tout chevauchement de périmètre. Cinq règles cardinales encadrent le fonctionnement : pas de projet sans sponsor métier, pas de projet hors périmètre (données publiques uniquement), maximum 5 projets actifs, abandon à 4 semaines sans usage, transparence totale. Une grille d’évaluation objective (scoring sur 50 points, 6 critères pondérés) détermine les priorités d’entrée dans le backlog. Les projets à fort potentiel seraient proposés pour industrialisation sur les marchés existants ou transférés à BercyHub si le besoin justifie un traitement sur données sensibles.
## 8.7 Articulation avec BercyHub
Le positionnement du Vibe Lab par rapport à BercyHub est celui d’un éclaireur, pas d’un concurrent. Le Lab prototyppe sur données publiques, valide le concept avec les utilisateurs, puis la direction arbitre : pérenniser en l’état, ou transférer à BercyHub pour industrialisation sur données sensibles. BercyHub gagne ainsi un pipeline de projets déjà validés par l’usage. La règle de démarcation est absolue : dès qu’un projet touche aux SI métier, aux données personnelles ou à une homologation de sécurité, il relève de BercyHub. Cette complémentarité est formalisée dans la fiche de gouvernance et fait l’objet d’un point trimestriel structuré.
## 8.8 Prochaine étape : ExcelExit
Le premier projet candidat pour le Lab structuré est ExcelExit : la migration systématique des fichiers Excel critiques du ministère vers Grist (grist.numerique.gouv.fr), infrastructure interministérielle opérée par la DINUM. Avec un score de 47/50 sur la grille d’évaluation — le plus élevé de tous les projets évalués — ExcelExit répond à un problème universel (chaque bureau a ses Excel critiques), repose sur une infrastructure gratuite et déjà en place, et génère sa propre demande par l’effet vitrine. Le principe fondamental : la valeur repose dans les données et les formules Grist, pas dans l’interface. Si l’interface disparaît, les données restent. Le détail est documenté dans la note de cadrage ExcelExit.
# 9. Conclusion
Les résultats de cette expérimentation sont sans ambiguïté : 8 produits numériques fonctionnels, ~376 000 lignes de code de qualité professionnelle, produits par un seul agent en 6 mois. L’économie estimée par rapport à un développement en prestation classique est de l’ordre de 583 000 €, sans compter les coûts indirects de pilotage et contractualisation.
La demande est modeste : 1 à 3 agents dédiés et environ 1 000 € de licences par mois. Le retour sur investissement est immédiat : chaque prototype livré évite des semaines de spécification et des dizaines de milliers d’euros de prestation.
Au-delà de l’économie financière, le Lab Vibe Coding offrirait au service du numérique un avantage stratégique : la capacité à tester rapidement des idées, valider des hypothèses produit, et livrer de la valeur métier avant même que les circuits classiques n’aient démarré.

# Annexe — Dépôts GitHub
Écosystème (G3) : https://github.com/bmatge/g3
Portail Eco Browser : https://github.com/bmatge/portail-eco-browser
ChartsBuilder : https://github.com/bmatge/datasource-charts-webcomponents
LimeSurvey DSFR : https://github.com/bmatge/LimeSurvey-DSFR
Organigrammes : https://github.com/bmatge/org-chart-service-public
Prix Contrôle Technique : https://github.com/bmatge/prix-controle-technique
Tarifs Bancaires : https://github.com/bmatge/tarifs-bancaires
LeFouineur : https://github.com/bmatge/eco-alert-bo

| RAPPORT D’OPPORTUNITÉ
Le vibe coding au service
du ministère
Retour d’expérience sur 6 mois de prototypage
assisté par IA — Proposition de création d’un Lab |
| --- |

| En 6 mois, 1 agent équipé d’IA générative a produit 8 outils numériques de qualité professionnelle représentant ~376 000 lignes de code — soit l’équivalent de ~663 K€ en prestation, pour un coût réel inférieur à 80 K€.

Ce rapport propose la création d’un Lab Vibe Coding : 1 à 3 agents dédiés + ~1 000 €/mois de licences. |
| --- |

| 8
produits numériques
fonctionnels, testés, documentés | ~376 000
lignes de code
qualité professionnelle | 663 K€
coût presta. équiv.
1 105 jours-homme |
| --- | --- | --- |

| ~80 K€
coût réel estimé
130 j/h, 1 agent + IA | 88 %
d’économie
vs. prestation classique | 6 mois
durée totale
initiative personnelle |
| --- | --- | --- |

| Écosystème (G3)
~238 000 LOC
520 j/h j/h → 312 000 € | Stack
TypeScript 5.7, React 19, Express.js, PostgreSQL, Redis/BullMQ, Vite, DSFR, D3.js, Playwright, Docker/Traefik | Qualité
Monorepo pnpm, 25 modules, 63 migrations SQL, 456 fichiers de tests, architecture en couches, EventBus, TypeScript strict, CI/CD GitHub Actions, déploiement Docker conforme ANSSI |
| --- | --- | --- |

| Portail Eco Browser
~88 500 LOC
270 j/h j/h → 162 000 € | Stack
React 18 + TypeScript (Vite), FastAPI + SQLAlchemy, Elasticsearch, Transformers/scikit-learn, DSFR, Docker Compose | Qualité
Architecture modulaire FastAPI, 28 services métier, 1 290 tests backend (pytest) + 22 suites frontend (Vitest), typage strict Pydantic, CI/CD avec Ruff + Trivy |
| --- | --- | --- |

| ChartsBuilder
~41 500 LOC
200 j/h j/h → 120 000 € | Stack
TypeScript 5.3, Lit 3.1, DSFR Chart 2.0, Vite, Tauri, D3-Geo, npm workspaces | Qualité
Monorepo npm, composants Lit encapsulés, pattern adapter/registry, accessibilité RGAA/WCAG AA native, build ESM + UMD (~50 KB gzippé), 83 specs de tests |
| --- | --- | --- |

| LimeSurvey DSFR
23 fichiers custom + assets DSFR LOC
45 j/h j/h → 27 000 € | Stack
PHP/Yii (LimeSurvey), Twig, JavaScript, CSS/SCSS, DSFR, Gulp, Docker | Qualité
Plugins structurés (config.xml), 1000+ icônes, 22 familles de polices, Prettier + ESLint + Stylelint, plan d’accessibilité dédié |
| --- | --- | --- |

| Organigrammes
~500 LOC
10 j/h j/h → 6 000 € | Stack
JavaScript vanilla, HTML5, CSS3, DSFR, D3-org-chart, API Annuaire service-public.gouv.fr | Qualité
Zéro framework, zéro build, page statique déployée sur GitHub Pages, CI/CD intégré |
| --- | --- | --- |

| Prix CT + Tarifs Bancaires
~5 500 LOC
45 j/h j/h → 27 000 € | Stack
React 18, Leaflet, Zustand, Fuse.js, Vanilla JS, Node.js natif, DSFR, Docker/Nginx/Traefik | Qualité
Architecture React moderne, optimisation performance, zéro dépendance framework (Tarifs), clés API côté serveur, headers sécurité, HTML sémantique accessible |
| --- | --- | --- |

| LeFouineur
~2 000 LOC
15 j/h j/h → 9 000 € | Stack
JavaScript vanilla, HTML5, CSS3, Manifest V3, SVG | Qualité
Architecture modulaire (content script / popup / config), branding professionnel (logo SVG, icônes multi-résolution) |
| --- | --- | --- |

| Projet | LOC | J/H | Coût presta. | Stack principale |
| --- | --- | --- | --- | --- |
| Écosystème (G3) | ~238 000 | 520 | 312 000 € | TypeScript, React 19, Express, PostgreSQL, Redis, Docker |
| Portail Eco Browser | ~88 500 | 270 | 162 000 € | React 18, FastAPI, Elasticsearch, ML/NLP |
| ChartsBuilder (gouv-widgets) | ~41 500 | 200 | 120 000 € | TypeScript, Lit 3, DSFR Chart, Tauri |
| Thème LimeSurvey DSFR | — | 45 | 27 000 € | PHP/Yii, Twig, DSFR, Docker |
| Organigrammes service public | — | 10 | 6 000 € | JS vanilla, D3, API Annuaire, DSFR |
| Prix Contrôle Technique | ~3 300 | 25 | 15 000 € | React 18, Leaflet, Zustand, DSFR |
| Tarifs Bancaires | ~2 100 | 20 | 12 000 € | Vanilla JS, Node.js natif, DSFR |
| LeFouineur (extension) | ~2 000 | 15 | 9 000 € | JS vanilla, Manifest V3 |
| TOTAL | ~376 000 | 1 105 | 663 000 € |  |

| COÛT PRESTATAIRE ESTIMÉ : 663 000 € (1 105 jours-homme, équipes de 1 à 4 développeurs)

COÛT VIBE CODING ESTIMÉ : ~80 000 € équivalent (130 jours-homme, 1 agent + IA)

ÉCONOMIE ESTIMÉE : 583 000 €, soit 88 % du coût prestataire

Note : ces estimations n’incluent pas les coûts de pilotage, contractualisation, réunions de suivi et recette qui majorent le coût prestataire réel de 20 à 40 % supplémentaires. |
| --- |

| Aucun de ces 8 projets n’aurait été réalisé sans l’IA. Non pas parce que les compétences manquent, mais parce que les circuits classiques rendent leur coût et leur délai disproportionnés par rapport au besoin. |
| --- |

| Ces projets manipulent du code public, des données publiques, pour des usages publics. Le risque sécurité et RGPD est nul par conception. |
| --- |

| DEMANDE

Équipe : 1 à 3 agents à temps plein (profils tech/produit)
Idéalement des profils qui connaissent les métiers du ministère et maîtrisent les fondamentaux techniques (architecture, API, déploiement). Le vibe coding ne nécessite pas d’être développeur senior, mais d’être capable de guider, valider et corriger le code produit par l’IA.

Licences IA : plafonnées à ~1 000 €/mois
Abonnements Claude Pro ou Team (Anthropic) + GitHub Copilot, soit environ 200-350 €/personne/mois. Pour 3 agents : ~1 000 €/mois maximum.

Infrastructure : existante
Accès à l’infrastructure de déploiement déjà en place (GitHub, CI/CD, Docker, hébergement). Aucun investissement supplémentaire nécessaire. |
| --- |

| Poste de dépense | Coût mensuel | Coût annuel |
| --- | --- | --- |
| Licences IA (Claude Pro/Team, Copilot) | ~1 000 €/mois | ~12 000 €/an |
| Infrastructure (CI/CD, hébergement, domaines) | ~200 €/mois | ~2 400 €/an |
| Abonnements API (si nécessaire) | ~100 €/mois | ~1 200 €/an |
| TOTAL LICENCES & INFRA | ~1 300 €/mois | ~15 600 €/an |

| Coût total hors masse salariale : ~15 600 €/an

Pour comparaison, l’équivalent prestataire des 8 outils déjà produits est estimé à 663 000 €. Le coût annuel du Lab représente 2,4 % de cette somme.

Autrement dit : le Lab s’autofinance dès son premier mois de fonctionnement en évitement de coûts prestataires. |
| --- |

| Structurer le Lab Vibe Coding, c’est transformer une initiative personnelle en capacité institutionnelle. C’est positionner le service du numérique comme pionnier dans l’utilisation de l’IA générative au service de l’administration publique. Un cadre complet accompagne cette proposition : fiche de gouvernance (cycle de vie des projets, instances, rôles), grille d’évaluation (critères d’entrée et de scoring), matrice des risques (8 risques identifiés, 0 résiduel critique), plan de communication (12 semaines pour générer la demande), et note de cadrage ExcelExit (premier projet du backlog élargi). |
| --- |
