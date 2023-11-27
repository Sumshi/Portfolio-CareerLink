#!/usr/bin/python3
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from models import Recruiter, storage
from flask import Blueprint
# from app.api.errors import error_response

auth_bp = Blueprint('auth', __name__)
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    """
    receives the username and password that the client provided
    returns the authenticated user if credentials are valid or None if not
    """
    user = storage.verify_password(username, password)
    if user:
        return user


# @basic_auth.error_handler
# def basic_auth_error(status):
#     return error_response(status)

# @token_auth.verify_token
# def verify_token(token):
#     return User.check_token(token) if token else None


# @token_auth.error_handler
# def token_auth_error(status):
#     return error_response(status)
