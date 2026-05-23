import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # DigitalOcean App Platform (and other PaaS) often injects configuration
    # via environment variables. This demonstrates reading one.
    app_name = os.getenv("APP_NAME", "DigitalOcean App Platform Demo")
    return f"Hello from {app_name}! This is a simple Python Flask app."

if __name__ == '__main__':
    # PaaS platforms typically expose a PORT environment variable
    # for the application to bind to. We default to 8080 for local testing.
    port = int(os.getenv("PORT", 8080))
    # Binding to 0.0.0.0 makes the app accessible from outside the container/localhost,
    # which is necessary for PaaS deployments.
    app.run(host='0.0.0.0', port=port)
