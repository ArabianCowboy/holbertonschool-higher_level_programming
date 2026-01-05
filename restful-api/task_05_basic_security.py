#!/usr/bin/python3
"""
Task 05: API Security and Authentication Techniques (Flask)

Implements:
- Basic Auth protected route: GET /basic-protected
- JWT login: POST /login  -> returns {"access_token": "..."}
- JWT protected route: GET /jwt-protected
- Role-based route: GET /admin-only (admin only)

Important:
- All JWT authentication errors MUST return 401 (missing/invalid/expired/etc.)
- Non-admin on /admin-only returns 403 with {"error": "Admin access required"}
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

app = Flask(__name__)

# Use a strong key in real life. For this project/tests, a constant is fine.
app.config["JWT_SECRET_KEY"] = "holberton-restful-api-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users store (matches required structure)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# ---------------------------
# Basic Auth setup
# ---------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user
    return None


@auth.error_handler
def basic_auth_error(status):
    # Ensure consistent 401 for missing/invalid basic auth
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ---------------------------
# JWT error handlers (MUST return 401)
# ---------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ---------------------------
# JWT routes
# ---------------------------
@app.route("/login", methods=["POST"])
def login():
    payload = request.get_json(silent=True)
    if payload is None:
        # Invalid JSON body
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        # Keep it simple and predictable for tests
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Put identity info in JWT (including role for authorization)
    identity = {"username": user["username"], "role": user["role"]}
    access_token = create_access_token(identity=identity)

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()  # {"username": "...", "role": "..."} as set above
    role = None
    if isinstance(identity, dict):
        role = identity.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
