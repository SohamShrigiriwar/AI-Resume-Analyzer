pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python --version'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m py_compile resume_analyzer.py'
            }
        }

        stage('Package') {
            steps {
                echo 'Python application checked successfully.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
