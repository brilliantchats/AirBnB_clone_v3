#!/usr/bin/python3
"""
Index page of our api
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """Returns status"""
    return jsonify({"status": "OK"})
