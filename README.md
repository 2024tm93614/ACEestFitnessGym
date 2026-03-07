# ACEest Fitness DevOps CI/CD Pipeline

This project implements a DevOps pipeline for ACEest Fitness & Gym.

## Technologies

Python Flask
Docker
GitHub Actions
Jenkins
Pytest
SQLite

## Run Application

pip install -r requirements.txt
python app.py

Open browser:

http://localhost:5000

## Run Tests

pytest

## Docker

docker build -t aceest-app .
docker run -p 5000:5000 aceest-app

## CI/CD

GitHub Actions pipeline performs:

1 Code checkout  
2 Dependency installation  
3 Syntax check  
4 Pytest execution  
5 Docker build  

## Jenkins

Jenkins pulls code from GitHub and performs build validation.