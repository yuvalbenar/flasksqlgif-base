pipeline {
    agent any

    triggers {
        // Polls the SCM (GitHub) for changes every minute
        pollSCM('* * * * *')
    }

    stages {
       

        stage('Clone') {
            steps {
                echo "Cloning repository..."
                sh 'git clone https://github.com/yuvalbenar/flasksqlgif-base.git'
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
                        sleep 10
                        curl -f http://192.168.3.84:5000 || exit 1
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
