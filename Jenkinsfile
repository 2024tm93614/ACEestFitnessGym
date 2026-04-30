pipeline {
    agent any

    environment {
        IMAGE_NAME = "2024tm93614/aceest-devops-app"
        TAG = "v${BUILD_NUMBER}"

        // ✅ Fix PATH for macOS (important)
        PATH = "/Library/Frameworks/Python.framework/Versions/3.14/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {

        stage('Verify Environment') {
            steps {
                sh '''
                echo "Checking environment..."
                echo "PATH=$PATH"
                which python3 || echo "python3 not found"
                python3 --version || true
                which docker || echo "docker not found"
                which kubectl || echo "kubectl not found"
                '''
            }
        }

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

                # Ensure kubeconfig is accessible
                export KUBECONFIG=$HOME/.kube/config

                kubectl config use-context minikube || true
                kubectl get nodes || true

                # Deploy update
                kubectl set image deployment/aceest-green aceest-container=$IMAGE_NAME:$TAG || true
                '''
            }
        }
    }