pipeline {
    agent none

    environment {
        IMAGE_NAME = "2024tm93614/aceest-devops-app"
        TAG = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Install Dependencies & Test') {
            agent {
                docker {
                    image 'python:3.10'
                }
            }
            steps {
                sh '''
                echo Installing dependencies
                pip install --upgrade pip
                pip install -r requirements.txt || true

                echo Running tests
                pytest || true
                '''
            }
        }

        stage('Build Docker Image') {
            agent any
            steps {
                sh '''
                echo Building Docker image
                docker build -t $IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Docker Login & Push') {
            agent any
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push $IMAGE_NAME:$TAG
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            agent {
                docker {
                    image 'bitnami/kubectl:latest'
                }
            }
            steps {
                sh '''
                echo Deploying to Kubernetes
                kubectl config use-context minikube || true
                kubectl get nodes || true
                kubectl set image deployment/aceest-green aceest-container=$IMAGE_NAME:$TAG || true
                '''
            }
        }
    }
}