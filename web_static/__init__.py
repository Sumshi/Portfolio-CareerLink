#!/usr/bin/python3
"""
Initialize the Flask application
"""
from flask import Flask
import os

PROFILES_FOLDER = 'static/images/profile_pics'
RESUMES_FOLDER = 'static/resumes'
COVER_LETTER_FOLDER = 'static/cover_letters'
# PROFILES_EXTENSIONS = {'png', 'jpg', 'jpeg', }

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY') or 'this is a trial web app project'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['PROFILES_FOLDER'] = os.environ.get(
    'PROFILES_FOLDER') or PROFILES_FOLDER
app.config['RESUMES_FOLDER'] = os.environ.get(
    'RESUMES_FOLDER') or RESUMES_FOLDER
app.config['COVER_LETTER_FOLDER'] = os.environ.get(
    'COVER_LETTER_FOLDER') or COVER_LETTER_FOLDER

# Import the errors file with error handlers
from web_static.handlers import bp as errors_bp
app.register_blueprint(errors_bp)
