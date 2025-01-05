stage('Wait for Database') {
    steps {
        echo "Waiting for MySQL to be ready..."
        script {
            def waitForItPath = '/var/lib/jenkins/workspace/CI Pipeline base/wait-for-it.sh'

            // Diagnostic logging
            echo "Current working directory: ${pwd()}"
            echo "Checking if wait-for-it.sh exists: "
            sh "ls -l '${waitForItPath}'"  // Use single quotes to prevent path splitting due to spaces

            // Now attempt to run the script
            sh """
                echo "Running wait-for-it.sh with path: ${waitForItPath}"
                bash -c '${waitForItPath} gif-db:3306 --timeout=60 --strict -- echo MySQL is ready!'
            """
        }
    }
}
