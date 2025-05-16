# Projet Billetterie avec Cluster MariaDB Galera

## Description

Ce projet est une application de billetterie permettant de consulter des événements et de réserver des places.  
Le backend est développé en Flask avec une base de données MariaDB en cluster Galera.  
Le frontend est une application React.

---

## Structure du projet
event-booking-project/
├── backend/ 
│ ├── app.py
│ ├── Dockerfile
│ ├── requirements.txt
│ └── ...
├── frontend/ 
│ ├── package.json
│ ├── src/
│ ├── public/
│ └── ...
├── docker-compose.yml 
└── README.md 

---

## Prérequis

- Docker & Docker Compose installés  
- Node.js & npm installés (pour le frontend)  
- Accès au terminal Linux/WSL

---

## Installation et lancement

1. Lancer les services Docker :

-docker compose up --build -d

Cela démarre le cluster MariaDB Galera, l’API Flask et Adminer.

Installer les dépendances frontend et lancer React :

Cela démarre le cluster MariaDB Galera, l’API Flask et Adminer.

cd frontend
npm install
npm start

Accès aux services
Frontend React : http://localhost:3000

API Flask : http://localhost:5001

Interface Adminer (gestion base) : http://localhost:8080

Fonctionnalités principales
Consultation des événements et utilisateurs

Réservation de places avec formulaire interactif

Gestion du failover live via MariaDB Galera

Notes importantes
Assurez-vous que les ports 3000, 5001, 8080 et 3307-3309 ne sont pas utilisés par d’autres services.

Pour arrêter proprement :

docker compose down

Merci de votre attention !