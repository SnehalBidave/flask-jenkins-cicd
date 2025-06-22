pipeline {
    agent any

    environment {
        FLASK_PORT = '8000'
        VENV_PATH = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo "📥 Cloning GitHub Repository..."
                git branch: 'main', url: 'https://github.com/SnehalBidave/flask-jenkins-cicd.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "🐍 Setting up Python virtual environment..."
                sh '''
                    sudo apt update && sudo apt install -y python3-venv
                    python3 -m venv $VENV_PATH
                    source $VENV_PATH/bin/activate
                    $VENV_PATH/bin/pip install --upgrade pip
                    $VENV_PATH/bin/pip install -r requirements.txt
                    $VENV_PATH/bin/pip install gunicorn
                '''
            }
        }

        stage('Stop Previous App') {
            steps {
                echo "🛑 Stopping any existing Gunicorn process..."
                sh '''
                    pkill gunicorn || true
                '''
            }
        }

        stage('Run Flask App with Gunicorn') {
            steps {
                echo "🚀 Starting Flask app using Gunicorn..."
                sh '''
                    source $VENV_PATH/bin/activate
                    nohup $VENV_PATH/bin/gunicorn -w 4 -b 0.0.0.0:$FLASK_PORT app:app > gunicorn.log 2>&1 &
                    sleep 5
                '''
            }
        }
    }

    post {
        success {
            echo "🎉 CI/CD pipeline executed successfully!"
        }
        failure {
            echo "❌ CI/CD pipeline failed. Please check the console logs."
        }
    }
}
