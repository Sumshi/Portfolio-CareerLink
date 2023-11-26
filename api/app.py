#!/usr/bin/python3
""" Flask Application """
from api.auth import auth_bp
from api.tokens import tokens_bp
from flasgger.utils import swag_from
from flasgger import Swagger
from flask_cors import CORS
from flask import Flask, render_template, make_response, jsonify
from os import environ
from models import storage
# from api.v1.views import app_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this a trial web app project'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Register the auth Blueprint
app.register_blueprint(auth_bp)
# Register the tokens Blueprint
app.register_blueprint(tokens_bp)
# app.register_blueprint(app_views)


def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('CAREER_API_HOST')
    port = environ.get('CAREER_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)
