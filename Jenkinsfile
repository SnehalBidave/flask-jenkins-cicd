pipeline {
    agent any

    environment {
        FLASK_PORT = '5000'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo "📥 Cloning GitHub Repository..."
                git branch: 'main', url: 'https://github.com/SnehalBidave/flask-jenkins-cicd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 Installing Python and Flask dependencies..."
                sh '''
                    sudo apt update
                    sudo apt install -y python3-pip
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Stop Previous App (if running)') {
            steps {
                echo "🛑 Stopping any previously running Flask apps..."
                sh '''
                    pkill -f app.py || true
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                echo "🚀 Starting Flask app..."
                sh '''
                    nohup python3 app.py > output.log 2>&1 &
                    sleep 3
                    echo "✅ Flask app started on port $FLASK_PORT"
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
