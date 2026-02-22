# Dossier complet — Vibe Lab

**Laboratoire de prototypage augmenté par l'IA**
Retour d'expérience · Proposition · Gouvernance · Feuille de route

**Bertrand Matge**
MIWEB — Mission Ingénierie du Web
Service du Numérique — Ministère de l'Économie et des Finances
Février 2026

> L'objectif n'est pas de tout faire — c'est de rendre possible ce qui ne l'était pas.

---

## PARTIE I — Le constat : 6 mois d'expérimentation

### 1. Synthèse exécutive

Entre septembre 2025 et février 2026, une démarche expérimentale de **vibe coding** — développement logiciel assisté par IA générative — a été menée au sein de la MIWEB. Un seul agent, équipé de **Claude (Anthropic)** et **GitHub Copilot**, a produit **8 outils numériques fonctionnels** couvrant un spectre large : monitoring web, intelligence éditoriale, dataviz, enquêtes publiques, organigrammes, comparateurs de données ouvertes et outillage contributeur.

Ce dossier détaille les réalisations, analyse la qualité du code produit, et propose la création d'un **Vibe Lab structuré** : 1 à 3 agents dédiés à temps plein, un investissement en licences plafonné à ~1 000 €/mois, et un accès à l'infrastructure de déploiement existante.

**Chiffres clés :**

| | | |
| --- | --- | --- |
| **8 produits numériques** fonctionnels, testés, documentés | **~376 000 lignes de code** qualité professionnelle | **663 K€** coût presta. équiv. — 1 105 jours-homme |
| **~80 K€** coût réel estimé — 130 j/h, 1 agent + IA | **88 % d'économie** vs. prestation classique | **6 mois** durée totale — initiative personnelle |

### 2. Le vibe coding : un tandem humain-IA

Le vibe coding est une approche de développement dans laquelle un professionnel collabore avec un modèle d'IA générative pour produire du code. **L'humain** définit l'intention, l'architecture et les contraintes métier. **L'IA** génère, itère et corrige le code en temps réel. Ce tandem multiplie la productivité d'un profil tech/produit par un **facteur estimé entre 5 et 10**.

- **Période :** septembre 2025 – février 2026 (6 mois)
- **Ressource :** 1 agent public (profil tech/produit, responsable MIWEB)
- **Outils IA :** Claude (Anthropic) + GitHub Copilot
- **Cadre :** initiative personnelle, sans budget dédié ni équipe projet
- **Contrainte :** respect systématique du DSFR, des standards RGAA et des préconisations ANSSI

### 3. Inventaire des réalisations

#### 3.1 Écosystème (G3) — Monitoring et gouvernance web

Plateforme de monitoring de l'ensemble des sites web ministériels. Inventaire centralisé, **18 scanners automatisés** (SSL, accessibilité, performance, RGPD, DSFR), système d'alertes multi-niveaux, gestion des certificats SSL, KPI consolidés, assistant IA intégré, serveur MCP, administration complète avec RBAC.

- **~238 000 LOC** · 520 j/h · 312 000 € équiv.
- **Stack :** TypeScript 5.7, React 19, Express.js, PostgreSQL, Redis/BullMQ, Vite, DSFR, D3.js, Playwright, Docker/Traefik

#### 3.2 Portail Eco Browser — Intelligence éditoriale

Outil d'exploration du portail economie.gouv.fr. Navigation dans le contenu Drupal, analytics multi-sources (Eulerian, Cloudflare, Google Search Console), **clustering sémantique** (HDBSCAN/UMAP), recherche RAG avec embeddings, trajectoires de trafic, diagnostics SEO, assistant IA Albert.

- **~88 500 LOC** · 270 j/h · 162 000 € équiv.
- **Stack :** React 18 + TypeScript (Vite), FastAPI + SQLAlchemy, Elasticsearch, Transformers/scikit-learn, DSFR, Docker Compose

#### 3.3 ChartsBuilder (gouv-widgets) — Dataviz DSFR

Bibliothèque de **24 web components DSFR** pour la dataviz gouvernementale. 5 connecteurs API (OpenDataSoft, data.gouv.fr, Grist, INSEE, REST générique), 8 applications (builder visuel, builder IA, playground, dashboard). Zéro JavaScript requis côté intégrateur. Publié sur npm.

- **~41 500 LOC** · 200 j/h · 120 000 € équiv.

#### 3.4 Thème LimeSurvey DSFR + Plugins

Thème DSFR complet pour LimeSurvey avec plugin **ConversationIA** (Albert), plugin **DSFRMail** pour les emails ministériels, et type de question avancé (ranking). Documentation exhaustive (60 Ko+).

- **45 j/h** · 27 000 € équiv.

#### 3.5 Organigrammes service public

Générateur automatique d'organigrammes à partir de l'API Annuaire du service public. Recherche par organisme, construction BFS de l'arbre hiérarchique, deux modes de rendu (HTML/CSS et D3 interactif), filtrage par catégorie, export multi-format.

- **~500 LOC** · 10 j/h · 6 000 € équiv.

#### 3.6 Comparateurs de données ouvertes

Deux démonstrateurs de services grand public basés sur les open data du ministère :

- **Prix Contrôle Technique :** carte choroplèthe, filtres multi-critères, observatoire statistique
- **Tarifs Bancaires :** wizard multi-étapes, comparaison côte à côte, export CSV

Les deux branchés sur l'API data.economie.gouv.fr.

- **~5 500 LOC** · 45 j/h · 27 000 € équiv.

#### 3.7 LeFouineur — Extension navigateur

Extension navigateur (Manifest V3) d'alerte et d'analyse qualité pour les contributeurs web. Script de contenu analysant les pages visitées, interface popup, système de messagerie inter-composants. 90 Ko, zéro dépendance externe.

- **~2 000 LOC** · 15 j/h · 9 000 € équiv.

### 4. Synthèse des coûts

| Projet | LOC | J/H | Coût presta. |
| --- | --- | --- | --- |
| Écosystème (G3) | ~238 000 | 520 | 312 000 € |
| Portail Eco Browser | ~88 500 | 270 | 162 000 € |
| ChartsBuilder | ~41 500 | 200 | 120 000 € |
| LimeSurvey DSFR | — | 45 | 27 000 € |
| Organigrammes | ~500 | 10 | 6 000 € |
| Comparateurs (x2) | ~5 500 | 45 | 27 000 € |
| LeFouineur | ~2 000 | 15 | 9 000 € |
| **TOTAL** | **~376 000** | **1 105** | **663 000 €** |

> **Coût prestataire estimé : 663 000 €** (1 105 jours-homme)
> **Coût vibe coding estimé : ~80 000 €** (130 jours-homme, 1 agent + IA)
> **Économie estimée : 583 000 €**, soit **88 %** du coût prestataire
>
> Note : hors coûts de pilotage et contractualisation (+20 à 40 % en réalité).

### 5. Qualité du code et standards

Tous les projets front-end intègrent le **DSFR**, garantissant cohérence visuelle et conformité avec la charte de l'État. Les déploiements utilisent **Docker** avec des configurations Traefik conformes aux préconisations ANSSI. Plusieurs projets intègrent **Albert** (IA souveraine Etalab) et se connectent exclusivement aux API publiques françaises.

- **Typage strict :** TypeScript sur 5/8 projets, Pydantic côté Python
- **Tests :** 1 800+ tests unitaires et d'intégration + E2E Playwright
- **CI/CD :** GitHub Actions (linting, tests, build Docker, scan Trivy)
- **Documentation :** README détaillés, ADR, documentation technique générée

### 6. L'IA ne remplace pas les compétences — elle débloque ce qui était impossible

Ces outils n'ont pas été produits au détriment de développeurs humains. Ils n'auraient tout simplement **jamais existé** autrement. Aucun responsable n'aurait lancé un marché public de 312 000 € pour une plateforme de monitoring, ni mobilisé 3 développeurs pendant 5 mois pour un générateur d'organigrammes. Le vibe coding rend viable ce qui était déraisonnable.

Le vibe coding inverse la logique des projets classiques : on répond au besoin quand il se présente, avec un outil calibré pour l'instant présent. Si le besoin évolue, on adapte en quelques heures. S'il disparaît, on passe à autre chose sans regret — le coût engagé reste dérisoire.

> Aucun de ces 8 projets n'aurait été réalisé sans l'IA. Non pas parce que les compétences manquent, mais parce que les circuits classiques rendent leur coût et leur délai disproportionnés par rapport au besoin.

---

## PARTIE II — La proposition : le Vibe Lab

### 7. Manifeste : valeurs et positionnement

Le Vibe Lab est un **laboratoire de prototypage augmenté par l'IA**, rattaché à la MIWEB. Il produit des outils numériques qui n'auraient jamais existé par les circuits classiques. Il ne remplace ni les prestataires, ni les développeurs internes — il comble l'espace entre le besoin et le possible.

**Ce que le Vibe Lab fait :**

- **Prototypage rapide :** du besoin au prototype fonctionnel en 1 à 2 semaines
- **Outillage interne :** monitoring, pilotage, dataviz, automatisation
- **Composants réutilisables :** bibliothèques DSFR, thèmes, web components
- **Veille et expérimentation :** évaluation continue des outils IA
- **Accompagnement :** formation et appui des équipes métier au vibe coding

**Ce que le Vibe Lab ne fait pas :**

- Pas de SI métier (Chorus, SI-RH, applications fiscales)
- Pas de données personnelles, fiscales ou nominatives
- Pas d'applications nécessitant une homologation de sécurité
- Pas de traitements de données classifiées ou protégées

Dès qu'un projet touche à l'un de ces périmètres, il relève de **BercyHub**. Cette règle de démarcation est absolue.

**Un périmètre sécurisé par construction**

L'ensemble des projets sont open source et publiés sur GitHub. Les données manipulées sont exclusivement des données ouvertes (open data ministérielles, API Annuaire, data.gouv.fr, INSEE). Le code ne contient ni secret, ni donnée personnelle, ni information sensible. L'utilisation d'outils d'IA générative pour la production du code ne pose aucun problème de confidentialité dans ce contexte.

> Ces projets manipulent du code public, des données publiques, pour des usages publics. Le risque sécurité et RGPD est nul par conception.

### 8. Ce que le Vibe Lab apporte à chaque périmètre

#### 8.1 Direction de la Communication

Les 8 outils déjà produits couvrent les trois dimensions du **design ministériel** :

- **Design visuel :** ChartsBuilder, thème LimeSurvey, organigrammes, cohérence de marque
- **Design de service :** comparateurs grand public, Écosystème, LeFouineur, parcours utilisateur
- **Design éditorial :** Portail Eco Browser, LeFouineur contributeurs, ChartsBuilder rédacteurs

Le Lab donne à la communication la capacité de **piloter les sites du ministère par les données** (Écosystème : 18 critères, alertes automatiques), de **produire de la dataviz conforme sans prestataire** (ChartsBuilder), et de tester sur du réel plutôt que sur des maquettes Figma.

#### 8.2 MIWEB — De l'ingénierie à l'intelligence du web

Le Vibe Lab permet à la MIWEB de passer de **l'ingénierie du web** à **l'intelligence du web** :

- **Intelligence éditoriale :** Portail Eco Browser — connaissance fine du contenu publié
- **Intelligence de gouvernance :** Écosystème — pilotage par les données
- **Intelligence du design :** prototypage rapide, tests sur outils réels, itération continue
- **Intelligence de l'accessibilité :** audit automatisé permanent, recommandations IA, contrôle qualité embarqué

Le prototypage sur du réel — pas sur du Figma — change radicalement l'équation. En quelques jours, on produit un prototype connecté aux vraies API, affichant de vraies données, responsive, conforme DSFR. Ce prototype peut être mis en ligne immédiatement et testé par de vrais utilisateurs.

#### 8.3 Fonctions support du secrétariat général

Le modèle validé sur la communication s'applique aux autres fonctions du SG, en restant strictement dans le périmètre données publiques ou agrégées. **16 cas d'usage** ont été identifiés :

- **RH :** simulateur de carrière (grilles indiciaires publiques), générateur de fiches de poste (RIME), analyse d'enquêtes (verbatims anonymisés), chatbot d'orientation (circulaires publiques)
- **Finances :** tableau de bord d'exécution budgétaire (LOLF/PAP/RAP publics), simulateur d'impact (barèmes publics), générateur de rapports de gestion
- **Immobilier :** guide interactif des sites, calculateur d'empreinte carbone (données ADEME), outil de signalement
- **DSI :** catalogue IT intelligent (RAG), générateur de documentation technique, élargissement d'Écosystème au parc applicatif
- **Coordination :** agrégateur de veille réglementaire (JORF/Légifrance), tableau de bord du SG, comparateur interministériel

> 16 cas d'usage identifiés. 16 à 100 % dans le périmètre Vibe Lab. 0 interférence avec BercyHub.

### 9. Articulation avec BercyHub : le modèle éclaireur

> Le positionnement du Vibe Lab par rapport à BercyHub n'est pas une question d'ambition, mais de périmètre. Les deux structures répondent à des besoins différents avec des méthodes différentes. Elles ne se chevauchent pas — elles se complètent.

**Le scénario d'articulation :**

1. **Le Vibe Lab explore.** Le Lab identifie un besoin, produit un prototype fonctionnel sur données publiques, teste avec les utilisateurs, valide le concept.
2. **La direction arbitre.** Si le prototype est validé et que le besoin justifie un traitement sur données sensibles, le projet est transféré à BercyHub.
3. **BercyHub industrialise.** BercyHub reprend le concept validé, le connecte aux SI métier et aux données sensibles, dans le cadre d'une homologation.

Le Vibe Lab devient un **éclaireur** : il dérisque les projets avant qu'ils ne mobilisent des moyens lourds. BercyHub gagne un pipeline de projets déjà validés par l'usage. Un point trimestriel structuré entre les deux équipes garantit la cohérence.

**Comparaison BercyHub / Vibe Lab :**

| | BercyHub | Vibe Lab |
| --- | --- | --- |
| **IA** | Souveraine (modèles hébergés) | Commerciale + souveraine (Albert) |
| **Données** | Sensibles et confidentielles | Publiques ou agrégées uniquement |
| **Périmètre** | SI métier | Outils périphériques (hors SI) |
| **Sécurité** | Homologation requise | Aucune homologation nécessaire |
| **Projets** | Structurants, moyen/long terme | Prototypes rapides, jetables si besoin |
| **Méthode** | Spécifications, recette | Itération continue, tests immédiats |

### 10. ExcelExit : la prochaine frontière

Le premier projet candidat pour le Lab structuré est **ExcelExit** : la migration systématique des fichiers Excel critiques du ministère vers **Grist** (grist.numerique.gouv.fr), infrastructure interministérielle opérée par la DINUM.

L'architecture repose sur trois couches indépendantes : les **données** (Grist — pérenne, partageable, versionnable), la **logique** (formules Grist + API REST), et l'**interface** (HTML/DSFR générée par le Lab — jetable et remplaçable). C'est l'exact inverse du modèle Excel où données, logique et interface sont fusionnées dans un objet opaque.

> **Principe fondamental d'ExcelExit :**
> Si l'interface meurt, les données vivent.
> La valeur repose dans les données et les formules Grist, pas dans l'interface web.

**Niveaux de fichiers :**

1. **Niveau 1 — Fichiers de suivi simples :** migration vers Grist en quelques heures
2. **Niveau 2 — Fichiers à formules complexes :** 1 à 2 semaines, interface DSFR complète
3. **Niveau 3 — Fichiers d'agrégation multi-sources :** 2 à 4 semaines, connecteurs API
4. **Niveau 4 — Fichiers à données sensibles :** HORS PÉRIMÈTRE, signalés à BercyHub

Avec un score de **47/50** sur la grille d'évaluation — le plus élevé de tous les projets évalués — ExcelExit entre en **priorité absolue** dans le backlog.

---

## PARTIE III — Le cadre : gouvernance et garde-fous

### 11. Gouvernance

Le Vibe Lab est un laboratoire, pas un programme. Sa gouvernance est conçue pour être **légère, rapide et transparente**.

**Cycle de vie d'un projet (4 à 8 semaines) :**

1. **Phase 1 — Demande.** Une direction identifie un besoin et le soumet via un canal unique. Le Lab vérifie les critères d'entrée (6 critères obligatoires).
2. **Phase 2 — Évaluation.** La grille de scoring (50 points, 6 critères pondérés) classe le projet dans le backlog.
3. **Phase 3 — Prototypage.** Sprint de 1 à 2 semaines. Livrable : prototype fonctionnel testable.
4. **Phase 4 — Test et itération.** Test utilisateur avec la direction sponsor. Itération rapide.
5. **Phase 5 — Bilan.** Le prototype est-il adopté ? Usage réel ? Valeur démontrée ?
6. **Phase 6 — Décision.** Trois issues : pérenniser, transférer à BercyHub, ou abandonner.

**Instances :**

- **Comité de priorisation** (mensuel, 30 min) : responsable Vibe Lab + sponsors métier. Revue du backlog, décision d'entrée, point d'avancement.
- **Revue trimestrielle** (1h) : responsable Vibe Lab + SNUM n+2. Bilan des projets, indicateurs, arbitrages stratégiques.
- **Point BercyHub** (trimestriel) : revue des projets en cours, identification des transferts possibles, cohérence des périmètres.

**Cinq règles cardinales :**

1. Pas de projet sans **sponsor métier** identifié
2. Pas de projet **hors périmètre** (données publiques ou agrégées uniquement)
3. Maximum **5 projets actifs** simultanément
4. **Abandon à 4 semaines** sans usage
5. **Transparence totale** : code sur GitHub, métriques dans le tableau de bord, bilans dans la revue trimestrielle

### 12. Grille d'évaluation

**Critères d'entrée (tous obligatoires) :**

1. **Sponsor métier identifié** — une direction ou un bureau porte le besoin
2. **Données publiques ou agrégées** — aucune donnée personnelle ou sensible
3. **Hors périmètre BercyHub** — pas de connexion à un SI métier
4. **Pas de solution existante** — pas de doublon avec un outil en service
5. **Prototypable en ≤ 4 semaines** — si plus, c'est un projet SI classique
6. **Alignement avec les missions du Lab** — outillage, pilotage, communication

**Scoring de priorisation (sur 50 points) :**

| Critère | Poids | Description |
| --- | --- | --- |
| Impact utilisateur | x2 (max 10) | Nombre d'agents concernés, fréquence d'usage |
| Alignement stratégique | x2 (max 10) | Lien avec les priorités SNUM, SG, BercyHub |
| Faisabilité technique | x2 (max 10) | Données disponibles, API existantes, complexité |
| Effet vitrine | x1 (max 5) | Visibilité, démonstration de la valeur du Lab |
| Réutilisabilité | x1 (max 5) | Applicabilité à d'autres directions/ministères |
| Urgence métier | x2 (max 10) | Deadline réglementaire, perte de données, blocage |

**Exemples de scoring :**

- **Écosystème (G3) : 44/50** — Pérennisé. En production depuis décembre 2025.
- **ExcelExit : 47/50** — Entrée prioritaire. Score le plus élevé de tous les projets évalués.

### 13. Matrice des risques

8 risques identifiés, classés par probabilité et impact. Aucun risque résiduel critique après application des mesures d'atténuation.

| Risque | Probabilité | Impact brut | Mesure d'atténuation | Résiduel |
| --- | --- | --- | --- | --- |
| Dépendance IA commerciale | Élevée | Modéré | Architecture multi-modèles + Albert | Faible |
| Confusion périmètre BercyHub | Élevée | Critique | Règle absolue + point trimestriel | Faible |
| Qualité du code généré | Modérée | Modéré | Revue systématique, tests, CI/CD | Faible |
| Effet tunnel (projets sans fin) | Modérée | Modéré | Abandon à 4 semaines sans usage | Faible |
| Dépendance à un seul agent | Élevée | Élevé | Documentation, scoring objectif | Modéré |
| Rejet institutionnel | Modérée | Élevé | Communication ciblée, victoires rapides | Modéré |
| Obsolescence des outils IA | Faible | Modéré | Veille continue, architecture modulaire | Faible |
| Dérive du périmètre | Modérée | Modéré | 5 règles cardinales, max 5 projets actifs | Faible |

> **6 risques sur 8** à résiduel faible — maîtrisés par l'architecture et les règles de gouvernance.
> **2 risques à résiduel modéré** — atténués par la gouvernance, à surveiller via KPI.

### 14. Plan de communication (12 semaines)

Le plan de communication vise à transformer la visibilité du Lab pour générer la demande entrante. Principe fondamental : **ne jamais communiquer sur ce que le Lab pourrait faire — communiquer sur ce qu'il a déjà fait**.

**Six audiences, six messages :**

| Audience | Ce qu'ils redoutent | Le message clé |
| --- | --- | --- |
| SNUM / Direction | Risque, coût, doublon BercyHub | 663 K€ de valeur, 1 agent, ~1 000 €/mois, 0 interférence |
| BercyHub | Confusion de périmètre | On est votre éclaireur, pas votre concurrent |
| DSI / Architectes | Shadow IT, dette technique | Tout est open source, CI/CD, Docker, DSFR natif |
| Directions métier | Un gadget de plus | Un outil construit pour vous en 2 semaines |
| Agents contributeurs | Encore un outil à apprendre | Ça résout votre problème du quotidien |
| Interministériel / DINUM | Pas assez sérieux pour eux | Composants DSFR, Grist, Albert, open source |

**Calendrier :**

- **Semaines 1–4 (Fondations) :** note SNUM, rendez-vous BercyHub, démo aux sponsors, publication GitHub
- **Semaines 5–8 (Visibilité) :** retour de démo DIRCOM, premier ExcelExit livré, article intranet, micro-événement
- **Semaines 9–12 (Demande entrante) :** bilan T+3, formulaire de demande, présentation au CODIR, publication interministérielle

---

## PARTIE IV — La demande : moyens et calendrier

### 15. Moyens demandés

**Équipe : 1 à 3 agents à temps plein** (profils tech/produit)

Des profils qui connaissent les métiers du ministère et maîtrisent les fondamentaux techniques. Le vibe coding ne nécessite pas d'être développeur senior, mais de savoir guider, valider et corriger le code produit par l'IA.

**Licences IA : plafonnées à ~1 000 €/mois**

Claude Pro/Team (Anthropic) + GitHub Copilot, soit ~200-350 €/personne/mois.

**Infrastructure : existante**

GitHub, CI/CD, Docker, hébergement — tout est déjà en place. Aucun investissement supplémentaire.

**Budget annuel (hors masse salariale) :**

| Poste | Mensuel | Annuel |
| --- | --- | --- |
| Licences IA (Claude, Copilot) | ~1 000 € | ~12 000 € |
| Infrastructure (CI/CD, hébergement) | ~200 € | ~2 400 € |
| Abonnements API | ~100 € | ~1 200 € |
| **TOTAL** | **~1 300 €** | **~15 600 €** |

> Le coût annuel du Lab (15 600 €) représente **2,4 %** de l'équivalent prestataire des 8 outils déjà produits (663 000 €). Le Lab s'autofinance dès son premier mois.

### 16. Montée en charge progressive

| Phase | Périmètre | Moyens |
| --- | --- | --- |
| T0 – T+6 | Communication (acquis) + ExcelExit + 2-3 projets RH/formation | 1 agent + licences existantes |
| T+6 – T+12 | + Finances/pilotage + coordination interministérielle | 2 agents + backlog partagé |
| T+12 – T+18 | + Immobilier + DSI + périmètre complet SG | 3 agents + gouvernance complète |

### 17. Indicateurs de succès

- **Production :** nombre de prototypes livrés par trimestre, taux de passage en production des POC
- **Efficience :** délai moyen idée → prototype fonctionnel, économies réalisées vs. prestation équivalente
- **Adoption :** satisfaction des équipes métier, nombre de demandes entrantes, taux d'utilisation réelle
- **Qualité :** couverture de tests, conformité DSFR/RGAA, résultats Écosystème sur les propres outils du Lab

### 18. Conclusion

Les résultats de cette expérimentation sont sans ambiguïté : **8 produits numériques fonctionnels**, **~376 000 lignes de code** de qualité professionnelle, produits par un seul agent en 6 mois. L'économie estimée est de l'ordre de **583 000 €**, sans compter les coûts indirects de pilotage et contractualisation.

La demande est modeste : **1 à 3 agents dédiés** et environ **1 000 € de licences par mois**. Le retour sur investissement est immédiat. Le cadre est formalisé : gouvernance légère, grille d'évaluation objective, matrice des risques maîtrisée, articulation BercyHub documentée, plan de communication structuré. Et le prochain projet — **ExcelExit, 47/50** — est prêt.

> Structurer le Vibe Lab, c'est transformer une initiative personnelle en capacité institutionnelle. C'est un investissement modeste pour un effet de levier considérable sur la production, le positionnement et la visibilité du ministère.

---

## Annexes

### Dépôts GitHub

- **Écosystème (G3) :** github.com/bmatge/g3
- **Portail Eco Browser :** github.com/bmatge/portail-eco-browser
- **ChartsBuilder :** github.com/bmatge/datasource-charts-webcomponents
- **LimeSurvey DSFR :** github.com/bmatge/LimeSurvey-DSFR
- **Organigrammes :** github.com/bmatge/org-chart-service-public
- **Prix Contrôle Technique :** github.com/bmatge/prix-controle-technique
- **Tarifs Bancaires :** github.com/bmatge/tarifs-bancaires
- **LeFouineur :** github.com/bmatge/eco-alert-bo

### Documents de référence

- Manifeste Vibe Lab — Valeurs et positionnement
- Fiche de gouvernance — Cycle de vie, instances, règles cardinales
- Grille d'évaluation — Critères d'entrée et scoring
- Matrice des risques — 8 risques identifiés et mesures d'atténuation
- Note de cadrage ExcelExit — Premier projet du backlog élargi
- Plan de communication — 12 semaines pour générer la demande
- Note SNUM — Rapport détaillé pour le chef du service du numérique
- Note MIWEB — Opportunité pour la mission ingénierie du web
- Note DIRCOM — Rapport pour la direction de la communication
- Note SG — Élargissement aux fonctions support du secrétariat général
