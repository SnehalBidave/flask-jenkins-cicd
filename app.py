from flask import Flask
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Define routes
@app.route("/")
def hello():
    app.logger.info("✅ Root endpoint accessed from Jenkins deployment")
    return "✅ Hello from Jenkins CI/CD Pipeline! Deployed Successfully via Gunicorn."

# Only for development server use (not used when running via gunicorn)
if __name__ == "__main__":
    app.logger.info("🚀 Starting Flask development server...")
    app.run(host="0.0.0.0", port=5000, debug=False)
