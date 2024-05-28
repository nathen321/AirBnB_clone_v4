#!/usr/bin/python3
"""
A simple  minimal Flask application
"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status")
def statue():
    status = {"status": "OK"}
    return jsonify(status)
