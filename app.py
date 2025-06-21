from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello():
    app.logger.info("Root endpoint was accessed")
    return "✅ Hello from Jenkins CI/CD Pipeline! Deployed Successfully."

if __name__ == "__main__":
    app.logger.info("Starting Flask application...")
    app.run(host="0.0.0.0", port=5000)
