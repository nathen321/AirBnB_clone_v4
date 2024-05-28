#!/usr/bin/python3
"""
A simple  minimal Flask application
"""
from models import storage
from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status")
def statue():
    status = {"status": "OK"}
    return jsonify(status)

@app_views.route("/stats")
def count():
    form = {}
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    for cls in classes:
        form[cls] = storage.count(cls)
    return jsonify(form)
