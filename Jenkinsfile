pipeline {
    agent any

    environment {
        DOCKER_CREDS = credentials('docker-hub-creds')  // Use the ID you configured in Jenkins
        DOCKER_USERNAME = "${DOCKER_CREDS_USR}"         // Automatically populated by Jenkins
        DOCKER_PASSWORD = "${DOCKER_CREDS_PSW}"         // Automatically populated by Jenkins
        IMAGE_NAME = 'yuvalbenar/flasksqlgifbase'       // Your Docker image name
        IMAGE_TAG = 'v1.0.0'                            // Your Docker image tag
    }

    stages {
        stage('Clone') {
            steps {
                echo "Cloning repository..."
                git branch: 'develop', url: 'https://github.com/yuvalbenar/flasksqlgif-base.git'
            }
        }

        stage('Set up environment') {
            steps {
                script {
                    // Fetch the secret from Jenkins credentials and write to .env
                    withCredentials([string(credentialsId: 'flasksqlgif-env-credentials', variable: 'ENV_FILE_CONTENT')]) {
                        sh '''
                            echo "$ENV_FILE_CONTENT" > .env
                        '''
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building application..."
                sh '''
                    set -x
                    echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                    docker build -t $IMAGE_NAME:$IMAGE_TAG .
                    docker push $IMAGE_NAME:$IMAGE_TAG
                    set +x
                '''
            }
        }

        stage('Deploy') {
            steps {
               '''
                        docker-compose up -d
                    
            '''
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean up workspace after pipeline runs
        }
    }
}
