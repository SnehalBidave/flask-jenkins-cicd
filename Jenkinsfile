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
                    python3 -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Restart Flask App') {
            steps {
                echo '🔁 Restarting Gunicorn via systemd...'
                sh '''
                    sudo systemctl restart gunicorn-flask
                    sudo systemctl status gunicorn-flask --no-pager
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
