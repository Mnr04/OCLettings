Welcome to the Orange County Lettings documentation!
======================================================

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents:

Project Description
===================
The project is a web application that allows users to browse user profiles and real estate rental listings.

Project Installation
====================
1. Clone the GitHub repository.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the environment and install dependencies: `pip install -r requirements.txt`.

Quick Start Guide
=================
To run the project locally:
Execute `python manage.py runserver` and go to `http://localhost:8000`.

Technologies and Languages
==========================
- Python 3.x
- Django 3.x
- SQLite (local)
- Docker / GitHub Actions / Render

Database Structure
==================
The database is divided into two main applications:
- **Lettings**: Contains the `Address` and `Letting` models.
- **Profiles**: Contains the `Profile` model linked to the Django `User` model.

Programming Interfaces (Docstrings)
===================================

Profiles Application
--------------------

**Views**

.. autofunction:: profiles.views.index
.. autofunction:: profiles.views.profile

**Models**

.. autoclass:: profiles.models.Profile


Lettings Application
--------------------

**Views**

.. autofunction:: lettings.views.index
.. autofunction:: lettings.views.letting

**Models**

.. autoclass:: lettings.models.Address
.. autoclass:: lettings.models.Letting

User Guide
==========
- **Users**: Browse the home page, view the list of lettings and profiles.
- **Administrators**: Log in to `/admin` to add or modify lettings and profiles.

Deployment and Management
=========================
Deployment is automated via a CI/CD pipeline on GitHub Actions.
On every push to the `master` branch, the code is tested, a Docker image is built and pushed to Docker Hub, and the application is deployed on Render.