from flask import Blueprint, request, jsonify

from database.db import db
from database.models import User

from security.auth_utils import (
    hash_password,
    verify_password
)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({
            "error": "All fields are required."
        }), 400

    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return jsonify({
            "error": "Email already exists."
        }), 400

    new_user = User(
        username=username,
        email=email,
        password=hash_password(password)
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "Registration Successful."
    })


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(
        email=email
    ).first()

    if user is None:
        return jsonify({
            "error": "Invalid Email."
        }), 401

    if not verify_password(
        user.password,
        password
    ):
        return jsonify({
            "error": "Incorrect Password."
        }), 401

    return jsonify({
        "message": "Login Successful.",
        "user_id": user.id,
        "username": user.username
    })