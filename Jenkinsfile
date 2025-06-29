pipeline {
    agent any

    environment {
        APP_PORT = '8000'
        VENV_PATH = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo '📥 Cloning GitHub Repository...'
                git url: 'https://github.com/SnehalBidave/flask-jenkins-cicd.git', branch: 'main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '🐍 Setting up Python virtual environment...'
                sh '''
                    #!/bin/bash
                    python3 -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Stop Previous App') {
            steps {
                echo '🛑 Stopping any existing Gunicorn process...'
                sh '''
                    pkill -f "gunicorn" || true
                '''
            }
        }

        stage('Run Flask App with Gunicorn') {
            steps {
                echo '🚀 Launching Flask app with Gunicorn...'
                sh '''
                    #!/bin/bash
                    . ${VENV_PATH}/bin/activate
                    nohup gunicorn -w 4 -b 0.0.0.0:${APP_PORT} app:app > gunicorn.log 2>&1 &
                    disown
                '''
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD pipeline completed successfully.'
        }
        failure {
            echo '❌ CI/CD pipeline failed. Please check the console logs.'
        }
    }
}
