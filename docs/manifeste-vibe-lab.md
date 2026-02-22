MIWEB — Mission Ingénierie du Web
Service du Numérique — Ministère de l’Économie et des Finances
Février 2026

# 1. Ce que nous croyons
Le numérique public souffre d’un paradoxe : les idées ne manquent pas, les besoins sont identifiés, les compétences existent — mais les circuits de production sont si longs et si coûteux que la plupart des projets utiles ne voient jamais le jour. Un outil dont le développement coûte 80 000 € et prend six mois ne sera jamais commandé pour répondre à un besoin ponctuel, même légitime. Alors on s’en passe. On bricole. On reporte.
L’IA générative change cette équation. Elle ne remplace ni les développeurs, ni les designers, ni les chefs de projet. Elle rend viable ce qui était déraisonnable. Un prototype fonctionnel en quelques jours au lieu de quelques mois. Un coût marginal au lieu d’un marché public. Une itération en heures au lieu de semaines.
Le Vibe Lab existe pour exploiter cette opportunité. Pas pour faire de la technologie pour la technologie, mais pour produire des outils concrets qui servent le ministère, ses agents et ses usagers.
# 2. Nos valeurs

# 3. Nos moyens

# 4. Nos méthodes
## 4.1 Partir du besoin, pas de la techno
Chaque projet commence par une question simple : quel problème résout-on, et pour qui ? Si la réponse est floue, on ne code pas — on creuse. L’IA accélère la production, elle n’accélère pas la réflexion. Et c’est la réflexion qui fait la différence entre un outil utile et un gadget.
## 4.2 Prototyper sur du réel
Pas de maquettes Figma jetées par-dessus un mur. Le prototype est fonctionnel dès le départ : connecté aux vraies API, alimenté par de vraies données, navigable, responsive, conforme DSFR. Ce que l’utilisateur teste est ce qu’il utilisera — ou quelque chose de très proche.
## 4.3 Tester tôt, tester souvent
Un prototype non testé est une hypothèse. La mise en situation réelle — même informelle, même avec cinq utilisateurs — transforme les intuitions en décisions. Le Vibe Lab ne livre pas un produit fini : il livre une première version testable, puis itère sur la base des retours.
## 4.4 Écrire du code professionnel
Le vibe coding ne signifie pas du code jetable ou bâclé. Les projets du Lab ont du typage strict, des tests automatisés, de l’intégration continue, une documentation technique. Le code est lisible, maintenable, et publiable. Si un projet doit être industrialisé, la base est saine.
## 4.5 Respecter le design system
Tout ce qui est produit respecte le DSFR. Pas par obligation administrative, mais parce que la cohérence visuelle est une forme de respect pour l’utilisateur. Un outil ministériel doit ressembler à un outil ministériel.
## 4.6 Documenter par l’usage
La meilleure documentation, c’est un outil qui s’explique lui-même. Mais quand c’est nécessaire, on documente : README, guides de déploiement, commentaires de code. L’objectif est qu’un autre agent puisse reprendre le projet sans archéologie.

# 5. Nos garde-fous

## 5.1 Sécurité : le risque est nul par construction
Les projets du Vibe Lab travaillent sur du code public, avec des données publiques, pour des usages publics. Il n’y a pas de données personnelles, pas de connexion à des SI sensibles, pas de secrets. Le périmètre d’intervention est celui de la communication et des outils éditoriaux — pas celui des systèmes d’information critiques.
Les applications sont déployées dans des conteneurs Docker portables. Aucune donnée sensible n’est hébergée. Le passage d’un hébergeur à un autre — cloud public, cloud souverain, on-premise — se fait sans friction.
## 5.2 RGPD : rien à déclarer
Aucun des outils produits ne collecte, ne stocke, ni ne traite de données personnelles. Les sources de données sont exclusivement des API publiques : data.gouv.fr, INSEE, Annuaire du service public, data.economie.gouv.fr. Il n’y a pas de formulaire utilisateur, pas de tracking nominatif, pas de base de données personnelles.
Si un futur projet devait manipuler des données personnelles, il ferait l’objet d’une analyse d’impact préalable et serait soumis aux circuits habituels du ministère. Le Vibe Lab ne contourne aucune règle — il opère dans un périmètre où ces règles ne s’appliquent pas, parce qu’il n’y a rien à protéger.
## 5.3 IA et confidentialité : pas de sujet
Les prompts envoyés à l’IA contiennent des spécifications fonctionnelles, pas des données protégées. Les résultats produits sont du code source publié en open source. Rien dans la chaîne de production ne présente de risque de fuite : il n’y a rien à fuiter.
Les modèles souverains (Albert, via Etalab) sont intégrés quand c’est pertinent — notamment pour le traitement de contenus éditoriaux. Le choix du modèle se fait au cas par cas, en fonction du besoin, sans dogmatisme.
## 5.4 Ce que le Vibe Lab ne fait pas
## 5.5 Articulation avec BercyHub : le modèle éclaireur
Le Vibe Lab et BercyHub ne se chevauchent pas — ils se complètent. BercyHub opère sur les données sensibles, les SI métier et les applications nécessitant une homologation de sécurité. Le Vibe Lab opère sur les données publiques ou agrégées, l’outillage périphérique et le prototypage rapide. L’articulation suit un modèle en trois temps : le Vibe Lab explore et prototyppe sur données publiques, la direction valide le concept, BercyHub industrialise sur données sensibles si nécessaire. Le Vibe Lab devient ainsi un éclaireur qui dérisque les projets avant qu’ils ne mobilisent des moyens lourds. Un point trimestriel structuré entre les deux équipes garantit la cohérence.
## 5.6 Une gouvernance légère et transparente
Le Vibe Lab s’est doté d’un cadre de gouvernance formalisé, conçu pour rester léger tout en garantissant la transparence. Il repose sur cinq règles cardinales : pas de projet sans sponsor métier identifié, pas de projet hors périmètre (données publiques uniquement), maximum 5 projets actifs simultanément, abandon à 4 semaines sans usage, et transparence totale (code sur GitHub, métriques dans le tableau de bord, bilans trimestriels). Le cycle de vie d’un projet — de la demande à la décision — dure 4 à 8 semaines. Les instances comprennent un comité de priorisation mensuel et une revue trimestrielle. Une grille d’évaluation objective (scoring sur 50 points, 6 critères pondérés) détermine les priorités et protège le Lab contre l’arbitraire. Ces cadres sont détaillés dans les fiches de gouvernance et d’évaluation associées.
## 5.7 ExcelExit : la prochaine frontière
Le projet ExcelExit illustre l’ambition du Vibe Lab au-delà du périmètre communication. Chaque direction du ministère a ses dizaines de fichiers Excel critiques — sans versioning, sans partage, sans interface. ExcelExit propose leur migration systématique vers Grist (grist.numerique.gouv.fr), infrastructure interministérielle opérée par la DINUM, avec des interfaces web DSFR générées par le Lab. Le principe fondamental : la valeur repose dans les données et les formules Grist, pas dans l’interface. Si l’interface disparaît, les données restent. Avec un score de 47/50 sur la grille d’évaluation (le plus élevé de tous les projets évalués), ExcelExit est la première entrée prioritaire du backlog élargi.

# 6. Nos cas d’usage privilégiés

# 7. En résumé

C’est un laboratoire, pas une usine. On y teste des idées, on y produit des preuves de concept, on y fabrique des outils qui servent. Ceux qui marchent sont pérennisés. Ceux qui ne marchent pas sont abandonnés sans regret.

Vibe Lab — MIWEB — Ministère de l’Économie et des Finances

| MANIFESTE
Vibe Lab
Laboratoire de prototypage augmenté par l’IA |
| --- |

| L’objectif n’est pas de tout faire — c’est de rendre possible ce qui ne l’était pas. |
| --- |

| Créer de la valeur, pas de la documentation
Un prototype fonctionnel vaut mieux qu’un cahier des charges parfait. Nous produisons des outils qui marchent, pas des spécifications qui décrivent ce que des outils pourraient faire. La valeur se mesure à l’usage, pas au volume de livrables intermédiaires. |
| --- |

| Itérer vite, corriger vite, abandonner vite
La vitesse n’est pas un luxe — c’est la condition pour que les retours utilisateurs arrivent avant que le besoin n’ait changé. On livre une première version en jours, on écoute, on ajuste. Si le projet n’a plus de sens, on l’arrête sans regret : le coût engagé est dérisoire. |
| --- |

| Montrer, pas raconter
On ne vend pas des concepts. On montre des prototypes. On teste avec de vrais utilisateurs sur de vrais outils connectés à de vraies données. L’écart entre « ce qu’on montre » et « ce qui sera livré » doit tendre vers zéro. |
| --- |

| L’IA augmente, elle ne remplace pas
Aucun outil du Vibe Lab n’a été produit au détriment d’un agent ou d’un prestataire. Ils n’auraient jamais existé autrement. L’IA est un multiplicateur de capacité pour des équipes qui savent ce qu’elles veulent produire. Le jugement métier, la vision produit et la rigueur restent humains. |
| --- |

| Le code public est un acte de communication
Tout ce que nous produisons est publié en open source. Ce n’est pas un choix technique, c’est un choix politique : un ministère qui publie son code contribue à l’écosystème numérique public, se rend auditable, et offre ses outils à ceux qui en ont besoin. |
| --- |

| Le Vibe Lab fonctionne avec des moyens délibérément limités. C’est une contrainte, mais c’est aussi une force : quand l’investissement est faible, le risque l’est aussi. On peut essayer, échouer, recommencer. |
| --- |

| Des agents, pas des prestataires
1 à 3 personnes qui connaissent les métiers du ministère, maîtrisent les outils d’IA générative, et savent faire le lien entre un besoin métier et une solution technique. Le vibe coding ne nécessite pas d’être développeur senior, mais de savoir guider l’IA avec une vision claire et un socle technique solide. | Des licences, pas des marchés
Claude, GitHub Copilot, Cursor — environ 350 €/personne/mois. Pour trois agents, le budget annuel complet en licences est inférieur à 16 000 €. C’est moins que le coût d’une seule journée de TMA sur un marché cadre. |
| --- | --- |

| L’infrastructure existante
GitHub pour le code, les CI/CD pour l’intégration continue, Docker pour le déploiement, les API publiques pour les données. Rien à acheter, rien à provisionner. On utilise ce qui est déjà là. | Le droit à l’expérimentation
Certains projets marcheront, d’autres non. Un outil peut être pérenne ou jetable. L’important n’est pas que chaque tentative aboutisse — c’est que le coût de chaque tentative soit suffisamment bas pour qu’on puisse en lancer beaucoup. |
| --- | --- |

| Le Vibe Lab opère dans un périmètre où le risque est nul par construction : code public, données publiques, usages publics. Aucun SI sensible, aucune donnée personnelle, aucun secret. |
| --- |

| Le périmètre est clair. Le Vibe Lab ne touche pas :

→  aux systèmes d’information du ministère (Chorus, SI-RH, applications métier)
→  aux données personnelles ou fiscales
→  aux applications nécessitant une homologation de sécurité
→  aux traitements de données classifiées ou sensibles

Le Lab opère dans la couche de communication, d’éditorial et d’outillage interne. C’est un espace d’expérimentation, pas un raccourci vers la production critique. Dès qu’un projet touche à l’un de ces périmètres sensibles, il relève de BercyHub. Cette règle de démarcation est absolue et documentée dans la fiche de gouvernance. |
| --- |

| Création et refonte d’applications web
Un site a un design désuet. Un outil interne est devenu inutilisable. Un besoin nouveau émerge. Le Vibe Lab produit un prototype fonctionnel en quelques jours, teste avec les utilisateurs, et itère. Si le projet est validé, il peut être industrialisé. Sinon, le coût engagé est négligeable. | Amélioration des interfaces utilisateur
Aligner un formulaire sur le DSFR. Refondre la navigation d’un portail. Proposer une alternative à un tableau Excel devenu illisible. Le Lab produit des prototypes d’interface testables immédiatement, sans mobiliser une équipe de développement pendant des semaines. |
| --- | --- |

| Intégration de l’IA dans les processus
Analyse sémantique de contenus éditoriaux, clustering de retours utilisateurs, génération de synthèses, recommandations de correction accessibilité — l’IA générative ouvre des possibilités nouvelles pour les métiers du ministère. Le Lab est l’endroit où ces possibilités sont testées et mises en œuvre. | Automatisation de l’accessibilité
Audit RGAA automatisé à l’échelle de l’écosystème web. Recommandations de correction générées par l’IA. Contrôle qualité embarqué pour les contributeurs. L’accessibilité est un chantier colossal — l’IA permet de le traiter à l’échelle, en continu. |
| --- | --- |

| Dataviz et outils éditoriaux
Bibliothèques de composants DSFR pour la visualisation de données. Générateurs d’organigrammes. Thèmes conformes pour les outils de sondage. Le Lab produit des briques réutilisables qui enrichissent la boîte à outils des équipes de communication et des rédacteurs. | Recherche UX et tests utilisateurs
Prototypes fonctionnels testables dès la première semaine. Analyse automatisée des verbatims. Génération de grilles d’entretien. Croisement données quantitatives et qualitatives. Le Lab accélère chaque étape de la recherche UX. |
| --- | --- |

| Gouvernance et pilotage web
Tableaux de bord de suivi des sites ministériels. Détection d’anomalies. Monitoring de la conformité DSFR, de la performance, de l’accessibilité, des certificats SSL. Le Lab fournit les outils pour piloter la qualité web par les données, pas par l’intuition. |
| --- |

| Le Vibe Lab, c’est :

→  des outils concrets produits en jours, pas en mois
→  un coût marginal qui rend l’expérimentation sans risque
→  du code professionnel publié en open source
→  un périmètre maîtrisé, complémentaire de BercyHub, qui n’interfère avec aucun SI sensible
→  une méthode centrée sur l’usage réel, pas sur les livrables intermédiaires
→  une gouvernance légère (comité mensuel, grille de scoring, revue trimestrielle)
→  une articulation claire avec BercyHub : éclaireur en amont, pas concurrent |
| --- |

| L’objectif n’est pas de tout faire — c’est de rendre possible ce qui ne l’était pas. |
| --- |
