pipeline{
    agent any

    environment {
        DOCKER_CREDS = credentials('docker-hub-creds')  // Use the ID you configured in Jenkins
        DOCKER_USERNAME = "${DOCKER_CREDS_USR}"         // Automatically populated by Jenkins
        DOCKER_PASSWORD = "${DOCKER_CREDS_PSW}"         // Automatically populated by Jenkins
        IMAGE_NAME = 'yuvalbenar/flasksqlgifbase'       // Your Docker image name
                                   
    }

    stages{
        stage("checkout code"){
            steps{
                checkout scm
            }
        }

        stage("build docker image"){
            steps{
                script{
                    dockerImage=docker.build("${IMAGE_NAME}:latest", ".")
                    dockerImage.tag("v1.0.${env.BUILD_NUMBER}")
                }
            }
        }

        stage("unit testing"){
            steps{
                script{
                    echo "testing..."
                }
                
            }
        }

        stage("push docker image"){
            when{
                branch "develop"
            }
            steps{
                script{
                    docker.withRegistry("https://registry.hub.docker.com", "docker-hub-creds"){
                        dockerImage.push("latest")
                        dockerImage.push("v1.0.${env.BUILD_NUMBER}")
                    }
                }
            }
        }
    }
}