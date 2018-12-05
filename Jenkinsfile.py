pipeline {
    agent { docker { image 'python:3.7.32' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
