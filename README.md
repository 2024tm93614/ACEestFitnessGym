# ACEest Fitness Gym – DevOps Assignment

This repository contains a small Flask application created to demonstrate a basic DevOps workflow.
The goal of the project is to show how a simple Python application can be tested, containerized, and validated using CI tools.

The project includes:

* A Flask web application
* Automated tests using Pytest
* Docker containerization
* Continuous integration using GitHub Actions
* A Jenkins build job that runs tests and builds the Docker image

The repository is organized so that another developer can easily clone the project, run the app, and reproduce the CI process.

---

## Project Structure

ACEestFitnessGym/
├── app.py               # Flask application

├── requirements.txt     # Python dependencies

├── Dockerfile           # Container configuration

├── README.md            # Project documentation
├── tests/
│   └── test_app.py      # Pytest test cases
└── .github/
    └── workflows/
        └── ci.yml       # GitHub Actions workflow
---

## Running the Application Locally

First clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ACEestFitnessGym.git
cd ACEestFitnessGym
```

Install the required dependencies:

```
pip3 install -r requirements.txt
```

Run the Flask application:

```
python3 app.py
```

Once the application starts, open the browser and go to:

```
http://localhost:5000
```

You should see the application running locally.

---

## Running the Tests

The project uses Pytest for automated testing.

To run the test suite manually:

```
python3 -m pytest
```

All tests should pass successfully.
These tests check the main functionality of the Flask application and confirm that the endpoints respond correctly.

---

## Running the Application with Docker

Docker is used to package the application so it can run consistently on any system.

Build the Docker image:

```
docker build -t aceest-app .
```

Run the container:

```
docker run -p 5000:5000 aceest-app
```

After the container starts, the application will be available at:

```
http://localhost:5000
```

---

## GitHub Actions Workflow

The repository includes a simple CI workflow using GitHub Actions.
The workflow runs automatically whenever code is pushed to the repository.

The pipeline performs the following steps:

1. Check out the repository
2. Set up the Python environment
3. Install dependencies
4. Run the Pytest test suite

If all tests pass, the workflow finishes successfully and a green check mark appears in the Actions tab of the repository.

---

## Jenkins Build

In addition to GitHub Actions, Jenkins is used locally to validate the build process.

The Jenkins job clones the repository and performs the following steps:

* Install project dependencies
* Run the test suite
* Build the Docker image

The build commands used in Jenkins are:

```
pip3 install -r requirements.txt
python3 -m pytest
docker build -t aceest-app .
```

A successful build confirms that the project can be tested and packaged automatically.

## Jenkins Build Result

The Jenkins job successfully installs dependencies, runs the test suite,
and builds the Docker image.

Build status: Finished: SUCCESS

---

## CI/CD Workflow Overview

The project uses a simple continuous integration workflow to automatically test and validate changes.

When code is pushed to the repository, the following process occurs:

Developer pushes code to GitHub  
↓  
GitHub Actions pipeline runs automatically  
↓  
Dependencies are installed and tests are executed  
↓  
If tests pass, the build is marked successful  
↓  
Jenkins pulls the repository and runs the build job  
↓  
Jenkins executes tests and builds the Docker image

This workflow helps ensure that the application is always tested and validated whenever new changes are introduced.
---

## Summary

This project demonstrates a simple CI workflow for a Python web application.
The repository combines version control, automated testing, containerization, and build automation.

Key tools used in the project include:

* Python and Flask
* Pytest
* Docker
* GitHub Actions
* Jenkins

Together, these tools help ensure that changes to the application are tested and validated before deployment.
