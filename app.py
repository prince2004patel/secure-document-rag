from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return jsonify({
        "message": "Secure Document Query System Backend Running",
        "status": "success"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/upload", methods=["POST"])
def upload():
    return jsonify({
        "message": "Upload endpoint ready"
    })


@app.route("/query", methods=["POST"])
def query():
    return jsonify({
        "message": "Query endpoint ready"
    })


if __name__ == "__main__":
    app.run(debug=True)