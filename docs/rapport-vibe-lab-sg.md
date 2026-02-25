# Le Vibe Lab au service du secrétariat général

**Note d'opportunité** -- Prototypage IA pour les fonctions support : RH, finances, immobilier, pilotage, coordination

**Bertrand Matge** | MIWEB -- Mission Ingenierie du Web -- SNUM | Fevrier 2026

---

> Le Vibe Lab a demontré sa valeur sur le perimetre de la communication : **16 outils en 6 mois**, **~700 K\u20ac d'equivalent prestation**, **88 % d'economie**. Cette note explore les cas d'usage pour les autres fonctions du secretariat general -- RH, finances, immobilier, DSI, coordination -- en restant strictement dans le perimetre du Vibe Lab : donnees publiques ou agregees, aucun SI sensible, complementarite totale avec BercyHub.

---

## 1. Contexte : un modele valide, un potentiel a elargir

Le Vibe Lab -- laboratoire de prototypage assiste par IA generative -- a produit en 6 mois, avec un seul agent, 16 outils numeriques fonctionnels pour le perimetre de la communication ministerielle. Les resultats sont documentes dans les notes paralleles adressees au chef du service du numerique et a la direction de la communication.

| Outils produits | Cout prestation equivalent | Economie |
| --- | --- | --- |
| **16 outils** en 6 mois, par 1 agent | **~700 K\u20ac** -- ~1 200 jours-homme | **88 %** vs. prestation classique |

Ces resultats soulevent une question naturelle : si le vibe coding est aussi efficace pour produire des outils de gouvernance web, d'intelligence editoriale et de dataviz, que pourrait-il apporter aux autres fonctions du secretariat general ?

La reponse est : **beaucoup** -- a condition de rester dans le perimetre qui fait la force du Vibe Lab. C'est l'objet de cette note.

---

## 2. Vibe Lab et BercyHub : deux approches complementaires

> Le positionnement du Vibe Lab par rapport a BercyHub n'est pas une question d'ambition, mais de **perimetre**. Les deux structures repondent a des besoins differents avec des methodes differentes. Elles ne se chevauchent pas -- elles se completent.

### 2.1 La regle de demarcation

Le Vibe Lab opere dans la « couche d'intelligence » au-dessus des SI : celle qui rend lisible ce qui existe deja dans des tableaux Excel, des PDF de 200 pages, des API publiques ou des exports anonymises. Il produit des interfaces, des tableaux de bord, des simulateurs, des outils d'aide a la decision -- pas des traitements de donnees sensibles.

| BercyHub | Vibe Lab |
| --- | --- |
| IA souveraine (modeles heberges en interne) | IA commerciale (Claude, Copilot) + souveraine (Albert) |
| Donnees sensibles et confidentielles | Donnees publiques ou agregees uniquement |
| Systemes d'information metier | Outils peripheriques (hors SI metier) |
| Homologation de securite requise | Aucune homologation necessaire |
| Projets structurants a moyen/long terme | Prototypes rapides, jetables si besoin |
| Cadre projet classique (specifications, recette) | Iteration continue, tests utilisateurs immediats |
| IA appliquee aux processus metier critiques | IA appliquee a l'outillage et au pilotage |

> **Le Vibe Lab ne touche jamais :**
>
> - aux SI metier (Chorus, SI-RH, SI Finances, applications fiscales)
> - aux donnees personnelles, fiscales ou nominatives
> - aux applications necessitant une homologation de securite
> - aux traitements de donnees classifiees ou protegees
>
> Des qu'un projet touche a l'un de ces perimetres, il releve de BercyHub. **Cette regle est absolue.**

### 2.2 Ce qui les rapproche

BercyHub et le Vibe Lab partagent une conviction : l'IA peut transformer le fonctionnement du ministere. Ils different sur la maniere, pas sur l'objectif. Un scenario naturel : le Vibe Lab prototype un outil sur donnees publiques, la direction valide le concept, BercyHub le reprend et l'industrialise sur les donnees sensibles si necessaire. Le Vibe Lab devient alors un **eclaireur** pour BercyHub.

---

## 3. Ressources humaines

> **Perimetre :** outillage autour du SIRH, jamais dedans. Donnees publiques (grilles indiciaires, RIME, circulaires RH) ou resultats d'enquetes agreges et anonymises.

### Simulateur de parcours de carriere

Un agent saisit son grade, son echelon et son anciennete. L'outil projette sa remuneration sur 5 a 10 ans selon les differents scenarios d'avancement, a partir des grilles indiciaires publiees au Journal officiel.

- **Donnees source :** grilles indiciaires publiques, decrets statutaires
- **Aucune donnee personnelle :** l'agent saisit lui-meme ses informations, rien n'est stocke
- **Valeur :** autonomie des agents, desengorgement des bureaux RH sur les questions recurrentes

### Generateur de fiches de poste

L'IA genere une fiche de poste conforme au RIME a partir d'une description de besoin en langage naturel. Elle suggere les competences associees, le niveau requis, et produit un document formate directement utilisable.

- **Donnees source :** referentiel RIME (public), fiches metiers DGAFP
- **Gain de temps estime :** 1 a 2 heures par fiche, des centaines etablies chaque annee
- **Valeur :** homogeneite des fiches, conformite au referentiel, rapidite

### Analyse des enquetes RH internes

Clustering semantique et synthese IA des reponses ouvertes au barometre social, aux enquetes teletravail, aux consultations internes. La technique est identique a celle deja validee dans Portail Eco Browser (HDBSCAN/UMAP + RAG).

- **Donnees :** verbatims agreges et anonymises, fournis par la DRH
- **L'outil ne voit jamais de donnee nominative :** les reponses sont anonymisees en amont
- **Valeur :** 3 jours d'analyse manuelle ramenes a quelques heures

### Chatbot d'orientation RH

Un agent pose une question en langage naturel (« comment poser un CET », « quel est le delai de carence »). L'IA repond a partir de la base documentaire publique des circulaires RH, notes de service et guides pratiques.

- **Donnees source :** circulaires publiees, notes de service, guides intranet (documents non classifies)
- **Architecture RAG :** indexation des documents, recherche semantique, reponse generee avec source
- **Valeur :** reponse immediate 24/7, reduction de la charge sur le bureau RH de proximite

---

## 4. Finances et pilotage budgetaire

> **Perimetre :** pilotage et aide a la decision, jamais de traitement comptable. Donnees publiques (LOLF, PAP/RAP, data.gouv.fr) ou exports anonymises fournis par l'agent.

### Tableau de bord d'execution budgetaire

Visualisation interactive des donnees d'execution budgetaire publiees sur data.gouv.fr : credits ouverts, consommes, reports, par programme et action. Dataviz DSFR, filtrables par exercice et perimetre.

- **Donnees source :** donnees LOLF publiques, PAP/RAP, documents budgetaires (bleus, jaunes)
- **Aucune connexion a Chorus :** uniquement les donnees publiees post-execution
- **Valeur :** rendre lisible ce qui existe en PDF de 500 pages, accelerer le pilotage

### Simulateur d'impact budgetaire

L'agent saisit un scenario (« recruter 3 agents de categorie A en septembre ») et l'outil calcule l'impact sur le titre 2 a partir des baremes publics. Pas d'acces au SI comptable : le calcul repose sur les grilles et taux publies.

- **Donnees source :** baremes de remuneration publics, taux de cotisation, grilles indiciaires
- **Mode calculatrice :** l'agent fournit les hypotheses, l'outil calcule
- **Valeur :** arbitrages budgetaires acceleres, scenarios multiples en quelques minutes

### Generateur de rapports de gestion

L'agent exporte des donnees agregees depuis ses outils (CSV, Excel) et les depose dans le Vibe Lab. L'IA les met en forme : tableaux, graphiques DSFR, commentaires automatises, document pret a diffuser.

- **Le Vibe Lab ne touche pas au SI :** c'est l'agent qui fait le pont en exportant les donnees
- **Les exports sont agreges et anonymises** avant traitement
- **Valeur :** diviser par 5 le temps de production des rapports de gestion

---

## 5. Gestion immobiliere et environnement de travail

> **Perimetre :** outils de pilotage, de signalement et d'information. Aucune donnee personnelle, aucune connexion aux systemes de controle d'acces.

### Guide interactif des sites ministeriels

Portail de reference pour les agents : plans des batiments, services disponibles par site, horaires, accessibilite PMR, transports. Un « portail du quotidien » qui repond aux questions pratiques sans solliciter le standard.

- **Donnees source :** informations immobilieres publiques, plans d'etage, horaires des services
- **Aucune donnee de badge ou d'identification**
- **Valeur :** autonomie des agents, reduction des appels au standard, integration des nouveaux arrivants

### Calculateur d'empreinte carbone des batiments

Visualisation et simulation de l'empreinte energetique des sites ministeriels a partir des donnees de consommation publiees dans les bilans carbone et les DPE. Comparaison entre sites, tendances annuelles, scenarios de reduction.

- **Donnees source :** bilans carbone publics, diagnostics de performance energetique, donnees ADEME
- **Valeur :** pilotage de la transition ecologique, conformite au decret tertiaire

### Outil de signalement et suivi des interventions

Un agent signale un probleme dans un bureau (panne, degradation, amenagement). L'outil categorise, route vers le bon service et permet le suivi. Sans donnee personnelle : le signalement porte sur un lieu, pas sur une personne.

- **Pas de connexion au SI technique des batiments**
- **Donnees :** localisation du signalement (batiment, etage, bureau), description, categorie
- **Valeur :** tracabilite, desengorgement du standard technique, historique des interventions par site

---

## 6. DSI et outillage informatique

> **Perimetre :** outillage peripherique, documentation, interfaces. Aucun acces a l'infrastructure, aux annuaires techniques ou aux donnees d'authentification.

### Catalogue de services IT intelligent

Portail de recherche en langage naturel sur le catalogue des services informatiques. L'agent decrit son besoin (« j'ai besoin d'un outil pour faire des visioconferences a 50 personnes ») et l'IA suggere le service existant ou identifie un besoin non couvert.

- **Donnees source :** catalogue de services publie sur l'intranet (non classifie)
- **Architecture RAG :** indexation du catalogue, recherche semantique
- **Valeur :** reduction du shadow IT, meilleure adoption des outils existants

### Generateur de documentation technique

Documentation automatisee des API internes non classifiees : l'IA lit une specification OpenAPI et genere une documentation lisible par des non-techs. Generateur de guides utilisateurs : a partir de captures d'ecran, l'IA produit un tutoriel pas-a-pas.

- **Donnees source :** specifications techniques non classifiees, captures d'ecran d'interfaces
- **Valeur :** reduction de la dette documentaire, autonomie des equipes metier

### Elargissement d'Ecosysteme au perimetre DSI

Ecosysteme (G3) surveille deja les sites web ministeriels sur 18 criteres. Le meme outil, etendu au perimetre des applications web publiques de la DSI, fournirait un tableau de bord de la dette technique, de la conformite DSFR et de la performance.

- **Perimetre :** applications web accessibles publiquement, pas les SI internes
- **Valeur :** vision consolidee de la qualite du parc applicatif web, pilotage par les donnees

---

## 7. Coordination interministerielle et pilotage

> **Perimetre :** veille, synthese et visualisation de donnees exclusivement publiques (JORF, Legifrance, rapports publies, indicateurs de performance publique).

### Agregateur de veille reglementaire

Surveillance automatisee des textes publies au Journal officiel et sur Legifrance qui concernent le perimetre du ministere. Resume IA de chaque texte, categorisation par thematique, alertes par direction concernee.

- **Donnees source :** API Legifrance (publique), JORF, data.gouv.fr
- **Valeur :** ne plus decouvrir un decret qui impacte le ministere apres sa date d'application

### Tableau de bord du secretariat general

Croisement des indicateurs publics du ministere : effectifs (donnees DGAFP), budget (LOLF), immobilier (France Domaine), numerique (observatoire des demarches en ligne), accessibilite (taux de conformite RGAA publie). Un cockpit de pilotage alimente exclusivement par des donnees publiques.

- **Donnees source :** 6+ sources publiques croisees (data.gouv.fr, INSEE, DGAFP, DINUM)
- **Valeur :** vision consolidee, indicateurs actualises automatiquement, plus de tableaux Excel manuels

### Comparateur de pratiques interministerielles

Benchmark automatise des pratiques des autres ministeres sur les sujets transverses : accessibilite, DSFR, open data, ecoconception, qualite web. L'outil scanne les sites et portails publics des autres ministeres et produit un tableau comparatif.

- **Perimetre :** sites web publics uniquement, aucune donnee interne
- **Extension naturelle d'Ecosysteme (G3)** au perimetre interministeriel
- **Valeur :** se positionner, identifier les bonnes pratiques, nourrir la coordination

---

## 8. Formation et montee en competences

### Plateforme de micro-learning genere par IA

A partir d'une circulaire, d'une note de service ou d'un guide pratique, l'IA produit automatiquement un parcours de formation : quiz interactif, fiches memo, cas pratiques. Deja experimente avec succes sur les formations accessibilite RGAA.

- **Donnees source :** documents internes non classifies (circulaires, guides, notes de service)
- **Valeur :** formation au fil de l'eau, sans mobiliser de formateur pour les sujets proceduraux

### Base de connaissance intelligente

Recherche en langage naturel sur l'ensemble des procedures du secretariat general. L'agent pose une question, l'IA retrouve la procedure pertinente, la resume et cite ses sources. Meme architecture que le chatbot RH, appliquee a un perimetre plus large.

- **Architecture RAG :** indexation de la documentation interne non classifiee
- **Valeur :** reduire le temps de recherche d'information, capitaliser les connaissances

### Auto-evaluation des competences numeriques

Questionnaire interactif permettant a chaque agent d'evaluer ses competences numeriques, avec recommandations de formation personnalisees. Aucune donnee nominative stockee : le resultat est affiche a l'ecran, pas enregistre.

- **Referentiel :** cadre europeen DigComp (public), referentiel PIX
- **Valeur :** diagnostic individuel immediat, orientation vers les formations IGPDE existantes

---

## 9. Synthese des cas d'usage

Le tableau ci-dessous recapitule les cas d'usage identifies, leur source de donnees et leur positionnement par rapport a BercyHub.

| Cas d'usage | Source de donnees | Nature des donnees | Qui |
| --- | --- | --- | --- |
| Simulateur de carriere | Grilles indiciaires (JO) | Donnees publiques | Vibe Lab |
| Generateur fiches de poste | RIME, DGAFP | Referentiels publics | Vibe Lab |
| Analyse enquetes RH | Verbatims anonymises | Agrege / anonymise | Vibe Lab |
| Chatbot RH | Circulaires, notes de service | Documents non classifies | Vibe Lab |
| TB execution budgetaire | LOLF, PAP/RAP | Donnees publiques | Vibe Lab |
| Simulateur budget | Baremes publics | Donnees publiques | Vibe Lab |
| Generateur rapports | Exports CSV anonymises | Agrege / anonymise | Vibe Lab |
| Guide des sites | Infos immobilieres | Donnees publiques | Vibe Lab |
| Empreinte carbone | Bilans carbone, ADEME | Donnees publiques | Vibe Lab |
| Signalements batiment | Localisations (bat./bureau) | Pas de donnee perso. | Vibe Lab |
| Catalogue IT | Catalogue de services | Non classifie | Vibe Lab |
| Doc. technique | Specs OpenAPI | Non classifie | Vibe Lab |
| Veille reglementaire | JORF, Legifrance | Donnees publiques | Vibe Lab |
| TB secretariat general | data.gouv.fr, INSEE, DGAFP | Donnees publiques | Vibe Lab |
| Micro-learning | Circulaires, guides | Non classifie | Vibe Lab |
| Base de connaissance | Procedures SG | Non classifie | Vibe Lab |

> **16 cas d'usage identifies. 16 a 100 % dans le perimetre Vibe Lab. 0 interference avec BercyHub.**

---

## 10. Scenario d'articulation avec BercyHub

L'articulation entre les deux structures peut suivre un modele simple et vertueux :

1. **Etape 1 -- Le Vibe Lab explore.** Le Lab identifie un besoin, produit un prototype fonctionnel sur donnees publiques ou agregees, teste avec les utilisateurs, et valide le concept.
2. **Etape 2 -- La direction arbitre.** Si le prototype est valide et que le besoin justifie un traitement sur donnees sensibles, le projet est transfere a BercyHub pour industrialisation souveraine.
3. **Etape 3 -- BercyHub industrialise.** BercyHub reprend le concept valide, le connecte aux SI metier et aux donnees sensibles, dans le cadre d'une homologation de securite.

Le Vibe Lab devient un **eclaireur** : il derisque les projets avant qu'ils ne mobilisent des moyens lourds. BercyHub gagne un **pipeline de projets deja valides par l'usage**.

### Exemple concret : chatbot RH

| Aujourd'hui | Avec le Vibe Lab |
| --- | --- |
| BercyHub developpe un chatbot RH souverain connecte au SIRH. Projet de 6 a 12 mois, homologation requise, budget significatif. **Risque :** le besoin est mal cadre ou l'interface ne convient pas. | Le Vibe Lab produit en **2 semaines** un chatbot sur la documentation RH publique. 50 agents le testent. On identifie les 20 questions les plus frequentes et les lacunes documentaires. BercyHub reprend ces retours pour cibler son developpement souverain. |

---

## 11. Ce que ca demande

L'elargissement du Vibe Lab aux fonctions support du secretariat general ne necessite pas un changement de modele. Le meme dispositif s'applique :

- **1,5 a 3 ETP dedies a temps plein.** Les memes profils que pour le perimetre communication, avec une connaissance elargie des metiers du secretariat general. La premiere annee, le Lab peut fonctionner avec 1,5 ETP en mobilisant deux ou trois agents deja en poste qui consacreront d'un tiers a deux tiers de leur temps au sujet. Le recrutement peut se faire progressivement : 1 agent supplementaire par perimetre ouvert.
- **~1 000 /mois de licences IA.** Montant inchange : les licences sont par agent, pas par projet. Ajouter des cas d'usage ne coute pas plus cher en licences.
- **Un backlog partage avec les directions.** Chaque direction concernee (DRH, DAF, SG Immobilier, DSI) propose des besoins. Le Vibe Lab priorise avec un comite mensuel. Les prototypes sont livres en sprints de 1 a 2 semaines.
- **Une coordination legere avec BercyHub.** Un point trimestriel suffit : revue des projets en cours, identification des transferts possibles, partage des retours d'experience. Pas de gouvernance lourde.

### 11.1 Montee en charge progressive

L'elargissement n'a pas besoin d'etre simultane. Un scenario realiste :

| Phase | Perimetre | Moyens |
| --- | --- | --- |
| T0 -- T+6 | Communication (acquis) + 2-3 projets RH/formation | 1,5 ETP (2-3 agents a temps partiel) + licences existantes |
| T+6 -- T+12 | + Finances/pilotage + coordination interministerielle | 2 ETP + backlog partage |
| T+12 -- T+18 | + Immobilier + DSI + perimetre complet SG | 3 ETP + gouvernance legere |

### 11.2 Gouvernance et cadre operationnel

L'elargissement aux fonctions support s'appuie sur le cadre de gouvernance deja formalise pour le Vibe Lab : comite de priorisation mensuel avec les directions sponsors, revue trimestrielle avec le SNUM n+2, grille d'evaluation objective (scoring sur 50 points, 6 criteres ponderes), et matrice des risques documentee (8 risques identifies, 0 residuel critique). Les cinq regles cardinales s'appliquent : pas de projet sans sponsor metier, perimetre donnees publiques, maximum 5 projets actifs, abandon a 4 semaines sans usage, transparence totale.

### 11.3 ExcelExit : premier projet transversal

Parmi les 16 cas d'usage identifies, **ExcelExit** constitue le premier projet concret transversal. Chaque direction du secretariat general a ses dizaines de fichiers Excel critiques -- suivi RH, reporting budgetaire, planification immobiliere. ExcelExit propose leur migration systematique vers **Grist** (grist.numerique.gouv.fr), infrastructure interministerielle operee par la DINUM, avec des interfaces DSFR generees par le Lab. Avec un score de **47/50** sur la grille d'evaluation (le plus eleve de tous les projets evalues), ExcelExit est immediatement realisable, a cout marginal, et demontre la valeur du Lab pour l'ensemble des fonctions support.

> Le principe fondamental : la valeur repose dans les donnees et les formules Grist, pas dans l'interface. Si l'interface disparait, les donnees restent.

---

## 12. Conclusion

Le secretariat general dispose de dizaines de problemes concrets dont la solution existe dans des donnees publiques, des referentiels ouverts et des documents non classifies. Ces problemes n'ont jamais ete traites parce que le cout d'un projet classique etait disproportionne.

**Le Vibe Lab change cette equation.** Il ne demande presque rien -- et il a deja prouve qu'il delivre.

> Le Vibe Lab a demontre son modele sur la communication. L'etendre aux fonctions support du secretariat general, c'est multiplier l'impact sans changer la recette :
>
> - **Memes moyens** (1,5 a 3 ETP, ~1 000 /mois)
> - **Meme perimetre securise** (donnees publiques, aucun SI sensible)
> - **Meme methode** (prototype rapide, test utilisateur, iteration)
> - **Complementarite totale avec BercyHub** (pas de chevauchement)
>
> **16 cas d'usage immediatement realisables, 0 risque de securite, 0 interference avec les projets IA souverains.**
