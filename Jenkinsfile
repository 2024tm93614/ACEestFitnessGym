pipeline {
    agent none

    environment {
        IMAGE_NAME = "2024tm93614/aceest-devops-app"
        TAG = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Install & Test') {
            agent {
                dockerContainer {
                    image 'python:3.10'
                }
            }
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt || true
                pytest || true
                '''
            }
        }

        stage('Build Image') {
            agent any
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Push Image') {
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

        stage('Deploy') {
            agent {
                dockerContainer {
                    image 'bitnami/kubectl:latest'
                }
            }
            steps {
                sh '''
                kubectl get nodes || true
                kubectl set image deployment/aceest-green aceest-container=$IMAGE_NAME:$TAG || true
                '''
            }
        }
    }
}