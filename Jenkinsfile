pipeline {
    agent any

    environment {
        DOCKER_CREDS = credentials('docker-hub-creds')  // Use the ID you configured in Jenkins
        DOCKER_USERNAME = "${DOCKER_CREDS_USR}"         // Automatically populated by Jenkins
        DOCKER_PASSWORD = "${DOCKER_CREDS_PSW}"         // Automatically populated by Jenkins
        IMAGE_NAME = 'yuvalbenar/flasksqlgifbase'       // Your Docker image name
        IMAGE_TAG = 'v1.0.0'                            // Your Docker image tag
        WAIT_FOR_IT = '/var/lib/jenkins/workspace/CI Pipeline base/wait-for-it.sh' // Path to the script
    }

    stages {
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

        stage('Clean Up Docker Containers') {
            steps {
                echo "Cleaning up Docker containers..."
                sh '''
                    docker-compose down || true   # Stop any running containers
                    docker ps -aq --filter "name=gif-db" --filter "name=flaskgif" | xargs -r docker rm -f || true
                '''
            }
        }

        stage('Wait for Database') {
            steps {
                echo "Waiting for MySQL to be ready..."
                sh '''
                    $WAIT_FOR_IT gif-db:3306 --timeout=60 --strict -- echo "MySQL is ready!"
                '''
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
                echo "Deploying application..."
                sh '''
                    set -e
                    docker-compose up -d --build         # Start containers in detached mode
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
