pipeline {
    agent any

   environment {
    DOCKER_CREDS = credentials('docker-hub-creds') // Use the ID you configured in Jenkins
    DOCKER_USERNAME = "${DOCKER_CREDS_USR}"    // Automatically populated by Jenkins
    DOCKER_PASSWORD = "${DOCKER_CREDS_PSW}"    // Automatically populated by Jenkins
    IMAGE_NAME = 'yuvalbenar/flasksqlgifbase'  // Your Docker image name
    IMAGE_TAG = 'v1.0.0'                       // Your Docker image tag
}


    stages {
        stage('Clone') {
            steps {
                echo "Cloning repository..."
                git branch: 'develop', url: 'https://github.com/yuvalbenar/flasksqlgif-base.git'
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
                    docker-compose down || true   # Stop running containers
                    docker-compose up -d          # Start containers in detached mode
                '''
            }
        }
    }

    
}
