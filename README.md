# Orange County Lettings

Orange County Lettings is a real estate rental and user profile management web application built with Django.

This project (Version 2.0) introduces a modern, modular architecture, transitioning from a monolithic structure to independent Django apps (`lettings`, `profiles`, and `oc_lettings_site`). It also integrates DevOps practices, including automated testing, CI/CD pipelines, containerization, and error tracking.

## Features & Upgrades (v2.0)
* **Modular Architecture**: Codebase separated into logical Django apps for better maintainability.
* **Code Quality**: Enforced PEP8 standards using `Flake8` and comprehensive unit testing via `Pytest` (Coverage > 80%).
* **Error Tracking**: Integrated with **Sentry** for real-time error logging and performance monitoring.
* **Containerization**: Fully Dockerized application for consistent environments across local and production.
* **CI/CD Pipeline**: Automated testing, building, and deployment using **GitHub Actions**.
* **Documentation**: Project documentation generated with **Sphinx** and hosted on **Read the Docs**.

---

## 💻 Local Installation

### Prerequisites
* Python 3.10
* Git
* Docker (optional, for local container testing)

### Setup Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Mnr04/OCLettings.git
   cd oclettings
   ```

2. **Create and activate a virtual environment:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate

  #On Windows use:
  venv\Scripts\activate
   ```

3. **Install dependencies:**

  ```bash
  pip install -r requirements.txt
   ```

4. **Set up environment variables:**

 ```python
  SECRET_KEY=your_local_secret_key
  SENTRY_DSN=your_sentry_dsn_url
  ```

5. **Run the application:**

 ```python
  python manage.py runserver
  ```

The site will be available at http://localhost:8000.

### Testing and Linting

This project uses pytest for unit testing and flake8 for linting.

Run tests and check coverage:

```Bash
pytest --cov=.
```

Run linting:
```Bash
flake8
```

### Documentation
The technical documentation is built with Sphinx and hosted on Read the Docs.
To build the documentation locally:

```Bash
cd doc
make html
```

Open doc/build/html/index.html in your browser to view it.

### Deployment
The deployment process is fully automated using GitHub Actions, Docker Hub, and Render.

High-Level Architecture
1. Continuous Integration (CI): On every push or pull request to any branch, GitHub Actions runs flake8 to check code style and pytest to ensure test coverage is above 80%.

2. Continuous Delivery/Deployment (CD): If a push is made to the master branch and the tests pass, GitHub Actions builds a Docker image and pushes it to Docker Hub. Finally, it triggers a webhook to inform Render that a new image is available.

3. Hosting: Render pulls the latest Docker image from Docker Hub and deploys the updated application. Static files are served efficiently using WhiteNoise.

Required Configuration

For the deployment pipeline to work, the following secrets must be configured in your GitHub

Repository Secrets:

- DOCKER_USERNAME: Your Docker Hub username.

- DOCKER_PASSWORD: Your Docker Hub access token.

- RENDER_DEPLOY_HOOK: The unique deploy hook URL provided by Render.

Additionally, the following environment variables must be configured in your Render Web Service settings:

- SECRET_KEY: A strong, random secret key for Django production.

- SENTRY_DSN: Your Sentry DSN key for error tracking.

How to Deploy
To release a new version of the application:

1. Create a new branch for your feature or bug fix (git checkout -b feature-name).

2. Commit your changes and push the branch to GitHub.

3. Verify that the GitHub Actions tests pass on your branch.

4. Merge your branch into the master branch.

5. The pipeline handles the rest! Monitor the GitHub Actions tab to watch the build, and check your Render dashboard to see the app go live.

