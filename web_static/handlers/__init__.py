#!/usr/bin/python3
from flask import Blueprint

bp = Blueprint('errors', __name__)

from web_static.handlers import errors
