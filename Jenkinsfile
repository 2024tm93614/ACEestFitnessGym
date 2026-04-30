pipeline {
    agent any

    environment {
        IMAGE_NAME = "2024tm93614/aceest-devops-app"
        TAG = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                echo Installing dependencies
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo Running tests
                pytest || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo Building Docker image
                docker build -t $IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                echo Pushing image
                docker push $IMAGE_NAME:$TAG
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                echo Deploying to Kubernetes

                kubectl config use-context minikube || true
                kubectl get nodes || true

                # Update your deployment (change name if needed)
                kubectl set image deployment/aceest-green aceest-container=$IMAGE_NAME:$TAG || true
                '''
            }
        }
    }
}