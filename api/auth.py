#!/usr/bin/python3
from flask_httpauth import HTTPBasicAuth
from models import Recruiter, storage
from flask import Blueprint
# from app.api.errors import error_response

auth_bp = Blueprint('auth', __name__)
basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(username, password):
    user = storage.verify_password(username, password)
    if user:
        return user


# @basic_auth.error_handler
# def basic_auth_error(status):
#     return error_response(status)
