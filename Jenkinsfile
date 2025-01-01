pipeline {
    agent any

    environment {
        ENV_FILE_CONTENT = credentials('env-file') // ID of the secret text in Jenkins
        DOCKER_USERNAME = 'yuvalbenar'             // DockerHub username
        DOCKER_PASSWORD = 'Nami1234!'             // DockerHub password (use credentials in production)
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
                    writeFile file: '.env', text: "${ENV_FILE_CONTENT}"
                    echo "DEBUG: .env file content:"
                    sh 'cat .env'
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building application..."
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

        stage('Test') {
            steps {
                echo "Testing application..."
                sh '''
                    set -e
                    docker-compose down || true   # Stop running containers if any
                    docker-compose up -d          # Start the application in detached mode
                    echo "Waiting for application to start..."
                    sleep 10
                    curl -f http://192.168.3.84:5000 || exit 1
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
            sh 'docker-compose down || true' // Clean resources after pipeline
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}
