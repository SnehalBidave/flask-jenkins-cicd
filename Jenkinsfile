pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo '📥 Cloning GitHub Repository...'
                git 'https://github.com/SnehalBidave/flask-jenkins-cicd.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '🐍 Setting up Python virtual environment...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Stop Previous App') {
            steps {
                echo '🛑 Stopping previous app (if running)...'
                sh 'pkill -f gunicorn || true'
            }
        }

        stage('Run Flask App with Gunicorn') {
            steps {
                echo '🚀 Starting Flask app using Gunicorn...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    nohup gunicorn -w 4 -b 0.0.0.0:8000 app:app > gunicorn.log 2>&1 &
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ CI/CD pipeline failed. Please check the console logs.'
        }
        success {
            echo '✅ CI/CD pipeline completed successfully.'
        }
    }
}
