pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}/venv"
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
                    python3 -m venv $VENV_PATH
                    $VENV_PATH/bin/pip install --upgrade pip
                    $VENV_PATH/bin/pip install -r requirements.txt
                    $VENV_PATH/bin/pip install gunicorn
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
                    nohup $VENV_PATH/bin/gunicorn -w 4 -b 0.0.0.0:8000 app:app > gunicorn.log 2>&1 &
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
