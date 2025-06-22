pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}/venv"
        FLASK_APP_MODULE = "app:app"
        FLASK_PORT = "8000"
        LOG_FILE = "gunicorn.log"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo '📥 Cloning GitHub Repository...'
                git branch: 'main', url: 'https://github.com/SnehalBidave/flask-jenkins-cicd.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '🐍 Setting up Python virtual environment...'
                sh '''
                    python3 -m venv "$VENV_PATH"
                    source "$VENV_PATH/bin/activate"
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Stop Previous App') {
            steps {
                echo '🛑 Stopping previous Gunicorn processes (if any)...'
                sh 'pkill -f gunicorn || true'
            }
        }

        stage('Run Flask App with Gunicorn') {
            steps {
                echo '🚀 Running Flask app with Gunicorn...'
                sh '''
                    source "$VENV_PATH/bin/activate"
                    nohup gunicorn -w 4 -b 0.0.0.0:$FLASK_PORT $FLASK_APP_MODULE > $LOG_FILE 2>&1 &
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ CI/CD pipeline failed. Please check the console logs.'
        }
        success {
            echo '✅ CI/CD pipeline completed successfully!'
        }
    }
}
