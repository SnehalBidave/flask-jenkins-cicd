pipeline {
    agent any

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
                    python3 -m venv venv
                    bash -c "source venv/bin/activate && pip install -r requirements.txt && pip install gunicorn"
                '''
            }
        }

        stage('Stop Previous App') {
            steps {
                echo '🛑 Stopping previous Gunicorn processes (if any)...'
                sh 'pkill gunicorn || true'
            }
        }

        stage('Run Flask App with Gunicorn') {
            steps {
                echo '🚀 Running Flask app with Gunicorn...'
                sh '''
                    bash -c "source venv/bin/activate && nohup gunicorn -w 4 -b 0.0.0.0:8000 app:app &"
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
