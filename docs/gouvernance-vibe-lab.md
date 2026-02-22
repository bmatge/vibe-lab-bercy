# Fiche de gouvernance -- Vibe Lab

*Vibe Lab -- MIWEB / SNUM*
*Ministere de l'Economie et des Finances -- Fevrier 2026*
*Cycle de vie des projets, instances, articulation BercyHub*

> Ce document definit les regles de fonctionnement du Vibe Lab : comment les projets entrent, vivent, sont evalues et meurent. Une gouvernance legere, adaptee a un laboratoire d'experimentation, pas a un programme informatique.

---

## 1. Principes de gouvernance

Le Vibe Lab est un laboratoire, pas un programme. Sa gouvernance est concue pour etre **legere**, **rapide** et **transparente**. Elle repose sur trois principes :

1. **Decider vite** -- un projet entre ou sort en une reunion, pas en trois mois
2. **Rendre des comptes** -- chaque projet a des metriques, chaque trimestre a un bilan
3. **Ne pas empiler** -- le Lab porte **3 a 5 projets actifs maximum** a la fois

---

## 2. Instances

### 2.1 Comite de priorisation mensuel

| | |
| --- | --- |
| **Frequence** | Mensuel -- 30 minutes maximum |
| **Participants** | Responsable Vibe Lab + 1 representant par direction sponsor (DRH, DAF, DIRCOM, DSI selon perimetre actif) |
| **Ordre du jour** | 1. Revue des projets actifs (5 min/projet) -- 2. Propositions de nouveaux projets -- 3. Arbitrage entrees/sorties |
| **Livrable** | Backlog mis a jour, avec statut de chaque projet (actif / en attente / abandonne / perennise) |
| **Regle** | Si un projet n'a pas de sponsor metier present, il ne rentre pas dans le backlog |

### 2.2 Revue trimestrielle

| | |
| --- | --- |
| **Frequence** | Trimestriel -- 1 heure |
| **Participants** | SNUM (n+2) + directions concernees + BercyHub (optionnel) |
| **Contenu** | Bilan chiffre du trimestre : projets livres, KPI, couts evites, retours utilisateurs, projets abandonnes (et pourquoi) |
| **Decisions** | Perennisation de projets matures, transferts vers BercyHub, ouverture de nouveaux perimetres |

### 2.3 Point BercyHub

Un point trimestriel dedie avec l'equipe BercyHub pour partager les projets en cours, identifier les transferts possibles, et eviter tout chevauchement de perimetre. Ce point peut etre couple a la revue trimestrielle.

---

## 3. Cycle de vie d'un projet

**Duree totale typique** d'un cycle complet : **4 a 8 semaines**, de la demande a la decision.

| Phase | Description | Duree |
| --- | --- | --- |
| **1. Demande** | Un besoin est identifie par un metier. Un sponsor est nomme. | 1 semaine |
| **2. Evaluation** | Le Lab verifie la faisabilite : donnees disponibles, perimetre Vibe Lab (pas BercyHub), pas de solution existante. | 2-3 jours |
| **3. Prototype** | Developpement du prototype fonctionnel. DSFR, tests, donnees reelles. | 1-2 semaines |
| **4. Test** | Mise en situation avec 5-20 utilisateurs reels. Collecte des retours. | 1-2 semaines |
| **5. Iteration** | Amelioration sur la base des retours. Cycles courts (jours). | 1-4 semaines |
| **6. Decision** | Perenniser, transferer a BercyHub, ou abandonner. | Comite mensuel |

---

## 4. Roles et responsabilites

| Role | Responsabilites | Rattachement |
| --- | --- | --- |
| **Responsable Vibe Lab** | Priorise le backlog, produit les prototypes, anime les instances, rend compte des resultats | MIWEB |
| **Sponsor metier** | Porte le besoin, valide les orientations, fournit les utilisateurs testeurs, decide de la perennisation | Direction concernee |
| **SNUM (n+2)** | Valide le cadre general, arbitre les priorites strategiques, porte le Lab aupres du SG | Direction SNUM |
| **Referent BercyHub** | Verifie l'absence de chevauchement, identifie les transferts, partage les retours d'experience | BercyHub |

---

## 5. Regles cardinales

1. **Pas de projet sans sponsor metier identifie**
   Si personne ne porte le besoin cote metier, le Lab ne demarre pas. Un outil sans utilisateur est un gadget.

2. **Pas de projet hors perimetre**
   Donnees personnelles, SI metier, homologation requise -> BercyHub. Pas d'exception.

3. **Maximum 5 projets actifs simultanement**
   Au-dela, la qualite baisse. Un nouveau projet entre quand un autre sort.

4. **Un projet sans usage a 4 semaines est abandonne**
   Si apres un mois de mise a disposition personne ne l'utilise, on arrete. Cout engage : quelques jours. Lecon apprise : inestimable.

5. **Tout est public**
   Code sur GitHub, metriques dans le tableau de bord, bilans dans la revue trimestrielle. La transparence est la meilleure protection.

---

## 6. Application : ExcelExit comme premier projet du backlog elargi

Le projet **ExcelExit** -- migration systematique des fichiers Excel critiques vers Grist (grist.numerique.gouv.fr) -- est le premier projet a avoir ete evalue sur la grille de priorisation du Vibe Lab. Avec un score de **47/50** (le plus eleve de tous les projets evalues), il entre en priorite dans le backlog.

Il repond a tous les criteres d'entree :

- **Sponsor metier identifie** (toute direction possedant des Excel critiques)
- **Donnees publiques ou agregees**
- **Hors perimetre BercyHub** (les fichiers de niveau 4 contenant des donnees sensibles sont explicitement exclus et signales a BercyHub)
- **Pas de solution existante**
- **Prototypable en 2 semaines**

ExcelExit illustre l'application concrete du cycle de vie et des regles cardinales definis dans cette fiche de gouvernance.

---

## 7. Documents associes

Cette fiche de gouvernance s'articule avec les documents suivants du Vibe Lab :

- le **Manifeste** (valeurs et positionnement)
- la **Grille d'evaluation** (criteres d'entree et scoring de priorisation)
- la **Matrice des risques** (8 risques identifies et mesures d'attenuation)
- la **Note de cadrage ExcelExit** (premier projet du backlog elargi)
- le **Plan de communication** (12 semaines pour generer la demande)

L'ensemble forme un dossier coherent de structuration du Lab.
