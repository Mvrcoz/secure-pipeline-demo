"""A small demo web app with a security-scanned CI/CD pipeline.

Built as a portfolio project for a cybersecurity career path:
every push is automatically scanned by CodeQL and Trivy.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "service": "secure-pipeline-demo",
            "status": "ok",
            "message": "Every push to this repo is scanned by CodeQL and Trivy.",
        }
    )


@app.get("/health")
def health():
    return jsonify({"healthy": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
