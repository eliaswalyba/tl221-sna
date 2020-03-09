# TL221-SNA
TL221-SNA est un projet communautaire qui a pour objectif d'offrir une meilleure visibilité sur l'interraction sociale entre les twittos sénégalais en utilisant des outils d'analyse des réseaux sociaux tels que les graphes et les cercles sociaux.


## Objectifs
- Détecter les communautés ou clans sur twitter
- Identifier les influenceurs et fantomes


## Tech Stack & Conception
- `Neo4j` comme base de données
    * Pros: Adapté au use case, right tool for the job
    * Cons: Déploiement couteux en production. Solution: aller vers du docker
- Source de données
    - Twitter API:
        * Pros: simple d'utilisation
        * Cons: Limitant en taille de données et nombre de requêtes
    - Scrapping avec `Scrapy`
        * Pros: Allows recursive looping without any limit
- Server: 
    - Express/NodeJS
        * Pros: Javascript accessible à beaucoup de part sa syntax
    - Flask/Python
        * Pros: same as above. S'intègre bien avec les librairies déjà disponible sur python

## Contributions
On a besoin de data scientist pour analyser, traiter et visualiser les données et de développeurs web ou mobiles pour le déploiement des résultats pour le grand public.
Le projet peut nous être bénéfique à tous: sociologues, les entrepreneurs, ...


## Socials
- Slack: https://galsenai.slack.com/join/shared_invite/zt-7wueq674-22H2NJE5Cf4_BfjRN3eCLw
- Youtube: https://www.youtube.com/channel/UCz3ZL9x0jxQNyis8Ss3Vz2Q

## Licence
[GPL-3](LICENSE)
