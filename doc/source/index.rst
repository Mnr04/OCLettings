Bienvenue dans la documentation de Orange County Lettings !
===========================================================

.. toctree::
   :maxdepth: 2
   :caption: Table des matières:

Description du projet
=====================
Le projet est une application web permettant de consulter des profils d'utilisateurs et des annonces de location immobilière.

Installation du projet
======================
1. Clonez le dépôt GitHub.
2. Créez un environnement virtuel : `python -m venv venv`.
3. Activez l'environnement et installez les dépendances : `pip install -r requirements.txt`.

Guide de démarrage rapide
=========================
Pour lancer le projet localement :
Exécutez `python manage.py runserver` et rendez-vous sur `http://localhost:8000`.

Technologies et langages
========================
- Python 3.x
- Django 3.x
- SQLite (local)
- Docker / GitHub Actions / Render

Structure de la base de données
===============================
La base de données est divisée en deux applications principales :
- **Lettings** : Contient les modèles `Address` et `Letting`.
- **Profiles** : Contient le modèle `Profile` lié au modèle `User` de Django.

Guide d'utilisation
===================
- **Utilisateurs** : Naviguez sur la page d'accueil, consultez la liste des locations et des profils.
- **Administrateurs** : Connectez-vous sur `/admin` pour ajouter ou modifier des locations et des profils.

Déploiement et gestion
======================
Le déploiement est automatisé via un pipeline CI/CD sur GitHub Actions. À chaque push sur la branche `master`, le code est testé, une image Docker est construite puis poussée sur Docker Hub, et l'application est déployée sur Render.