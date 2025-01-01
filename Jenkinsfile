pipeline {
    agent any

    environment {
        // Load environment variables from Jenkins credentials
        ENV_FILE_CONTENT = credentials('env-file') // ID of the secret text in Jenkins
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
                    // Ensure the working directory matches Jenkins workspace
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
            docker-compose -f /var/lib/jenkins/workspace/CI Pipeline base/docker-compose.yaml down || true
            docker-compose -f /var/lib/jenkins/workspace/CI Pipeline base/docker-compose.yaml build
            docker-compose -f /var/lib/jenkins/workspace/CI Pipeline base/docker-compose.yaml up -d
        '''
    }
}


        stage('Test') {
            steps {
                echo "Testing application..."
                sh '''
                    set -e
                    docker-compose up -d         # Start the application in detached mode
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
                    docker-compose down || true  # Stop running containers
                    docker-compose up -d         # Start containers again in detached mode
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up environment..."
            sh 'docker-compose down || true' // Ensure resources are cleaned after pipeline
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}
