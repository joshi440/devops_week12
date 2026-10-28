
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Project code is available in the workspace.'
            }
        }

        stage('Check Tools') {
            steps {
                bat 'python --version'
                bat 'git --version'
                bat 'docker --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install Flask selenium webdriver-manager pytest==8.3.5 pluggy==1.5.0'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
                    start "FlaskApp" /B python app.py
                    timeout /t 5 /nobreak
                    python -m pytest -v -s tests/test_registration.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-registration:v1 .'
            }
        }
    }

    post {
        success {
            echo 'Selenium tests passed and Docker image built.'
        }

        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }
    }
}
