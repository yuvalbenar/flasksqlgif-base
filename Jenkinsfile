pipeline {
    agent any

    triggers {
        // No periodic polling, remove to avoid unnecessary load.
        // Add webhooks instead for better efficiency if needed.
    }

    stages {
        stage('Clone') {
            steps {
                echo "Cloning repository into the 'flasksqlgif-base' directory..."
                sh '''
                    rm -rf flasksqlgif-base || true  # Clean up if the folder already exists
                    git clone https://github.com/yuvalbenar/flasksqlgif-base.git flasksqlgif-base
                '''
            }
        }

        stage('Build') {
            steps {
                dir('flasksqlgif-base') {
                    echo "Building application..."
                    sh '''
                        docker-compose down || true
                        docker-compose build
                        docker-compose up -d
                        docker-compose ps
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                dir('flasksqlgif-base') {
                    echo "Testing application..."
                    sh '''
                        docker-compose up -d
                        for i in {1..30}; do
                            curl -f http://192.168.3.84:5000 && break || sleep 2
                        done
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('flasksqlgif-base') {
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
