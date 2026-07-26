from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

from database.db import db
from security.auth_utils import bcrypt

from routes.auth import auth_bp
from routes.upload import upload_bp
from routes.query import query_bp

load_dotenv()

app = Flask(__name__)

CORS(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

bcrypt.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(query_bp)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return jsonify({
        "message": "Secure Document Query System Backend Running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)