#!/usr/bin/python3
"""
Flask Application
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the storage connection
    """
    storage.close()


if __name__ == "__main__":
    """
    Run the Flask application
    """
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
