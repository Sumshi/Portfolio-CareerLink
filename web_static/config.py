#!/usr/bin/python3
""" Import os environment variables """
import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a trial web app project'
JSONIFY_PRETTYPRINT_REGULAR = True
PROFILES_FOLDER = os.environ.get(
    'PROFILES_FOLDER') or 'images/profile_pics'
RESUMES_FOLDER = os.environ.get('RESUMES_FOLDER') or 'resumes'
COVER_LETTER_FOLDER = os.environ.get(
    'COVER_LETTER_FOLDER') or 'cover_letters'
