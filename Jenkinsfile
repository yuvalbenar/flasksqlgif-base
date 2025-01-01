pipeline {
    agent any

    environment {
        ENV_FILE_CONTENT = credentials('env-file') // Load .env content from Jenkins credentials
        IMAGE_NAME = 'yuvalbenar/flasksqlgifbase' // Docker image name
        IMAGE_TAG = 'v1.0.0'                      // Docker image tag
    }

    stages {
        stage('Clone') {
            steps {
                echo "Cloning repository..."
                git branch: 'develop', url: 'https://github.com/yuvalbenar/flasksqlgif-base.git'
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    echo "Setting up environment..."
                    writeFile file: '.env', text: "${ENV_FILE_CONTENT}" // Create .env file in workspace
                    echo "DEBUG: .env file created successfully."
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                echo "Building and pushing Docker image..."
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                            # Authenticate DockerHub
                            echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                            
                            # Build and tag the Docker image
                            docker build -t $IMAGE_NAME:$IMAGE_TAG .

                            # Push the image to DockerHub
                            docker push $IMAGE_NAME:$IMAGE_TAG
                        '''
                    }
                }
            }
        }

        stage('Test Application') {
            steps {
                echo "Testing application..."
                sh '''
                    set -e
                    docker-compose down || true   # Stop running containers
                    docker-compose up -d          # Start application in detached mode
                    echo "Waiting for application to start..."
                    sleep 10
                    curl -f http://localhost:5000 || exit 1  # Adjust test URL if needed
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                sh '''
                    set -e
                    docker-compose down || true   # Stop running containers
                    docker-compose up -d          # Start containers in detached mode
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up environment..."
            sh 'docker-compose down || true' // Clean up resources after pipeline
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}
