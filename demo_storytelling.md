# Diaporama / Démo - Mon Projet Billetterie

## Pourquoi j’ai choisi cette architecture ?

J’ai opté pour un cluster MariaDB Galera car je voulais garantir la haute disponibilité et la tolérance aux pannes. Cela permet à la base de données de continuer à fonctionner même si un nœud tombe, grâce au failover live.

Pour le backend, j’ai choisi Flask car c’est un framework léger et flexible, idéal pour créer une API rapidement, et il se déploie facilement avec Docker.

Pour le frontend, React me semblait parfait pour construire une interface utilisateur moderne, réactive et facile à maintenir.

Enfin, Docker Compose m’a permis d’orchestrer tous ces services simplement et efficacement.

## Comment j’ai appliqué KISS, DDD, SOLID et TDD ?

- Avec **KISS (Keep It Simple, Stupid)**, j’ai veillé à garder une architecture claire, simple et modulaire, sans complexité inutile.

- Pour **DDD (Domain-Driven Design)**, j’ai bien séparé les différents domaines métier, comme les utilisateurs, les événements et les réservations.

- J’ai respecté les principes **SOLID** dans le backend, en m’assurant que chaque fonction ou classe ait une responsabilité unique.

- Enfin, j’ai utilisé le **TDD (Test-Driven Development)** pour développer, en écrivant des tests pour mon API et le frontend, afin d’assurer la qualité du code.

## Le failover live des bases de données

Grâce à MariaDB Galera, le cluster réplique les données entre plusieurs nœuds en temps réel. Si un nœud tombe, un autre prend le relais instantanément sans interruption, ce qui garantit une disponibilité continue du service.

