#!/usr/bin/python3
"""
Task 04: Simple API using Flask

Endpoints:
- GET  /                -> "Welcome to the Flask API!"
- GET  /status          -> "OK"
- GET  /data            -> JSON list of usernames
- GET  /users/<username>-> JSON user object or 404 {"error":"User not found"}
- POST /add_user        -> add user with JSON body and return 201
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# NOTE: Checker warning: do not include testing data when pushing.
# Start empty; tests will POST to add users.
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # Return list of usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # silent=True => returns None if invalid JSON (instead of raising an error)
    payload = request.get_json(silent=True)

    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store full object; ensure username is included in the stored user
    user_obj = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }

    users[username] = user_obj
    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    # Default host/port are fine; checker typically uses flask CLI anyway.
    app.run()
