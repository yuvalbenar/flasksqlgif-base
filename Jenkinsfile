pipeline {
    agent any

    environment {
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
                echo "Setting up environment..."
                sh '''
                    echo "$ENV_FILE_CONTENT" > .env
                '''
            }
        }

        stage('Build') {
            steps {
                echo "Building application..."
                sh '''
                    docker-compose down || true
                    docker-compose build
                    docker-compose up -d
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Testing application..."
                sh '''
                    sleep 10
                    curl -f http://192.168.3.84:5000 || exit 1
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                sh '''
                    docker-compose down || true
                    docker-compose up -d
                '''
            }
        }
    }
}
