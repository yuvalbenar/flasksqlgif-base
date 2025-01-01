pipeline {
    agent any

    environment {
        ENV_FILE_CONTENT = credentials('env-file') // ID of the secret text in Jenkins
    }

    stages {
        stage('Clone') {
            steps {
                echo "Cloning repository..."
                sh 'git clone https://github.com/yuvalbenar/flasksqlgif-base.git /var/lib/jenkins/workspace/CI-Pipeline-Base'
            }
        }

        stage('Setup Environment') {
            steps {
                dir('/var/lib/jenkins/workspace/CI-Pipeline-Base') {
                    echo "Setting up environment..."
                    sh '''
                        echo "$ENV_FILE_CONTENT" > .env
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                dir('/var/lib/jenkins/workspace/CI-Pipeline-Base') {
                    echo "Building application..."
                    sh '''
                        docker-compose down || true
                        docker-compose build
                        docker-compose up -d
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                dir('/var/lib/jenkins/workspace/CI-Pipeline-Base') {
                    echo "Testing application..."
                    sh '''
                        sleep 10
                        curl -f http://192.168.3.84:5000 || exit 1
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('/var/lib/jenkins/workspace/CI-Pipeline-Base') {
                    echo "Deploying application..."
                    sh '''
                        docker-compose down || true
                        docker-compose up -d
                    '''
                }
            }
        }
    }
}
