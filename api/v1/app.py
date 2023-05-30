#!/usr/bin/python3
"""
Main interface to api
"""

from flask import Flask
from models import storage
from os import getenv
from api.v1.views import app_views

"""Create instance of Flask and register blueprints"""
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def app_teardown(error):
    """Closes storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', '5000'), threaded=True)
