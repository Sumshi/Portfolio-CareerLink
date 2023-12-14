#!/usr/bin/python3

from flask import Blueprint

bp = Blueprint('views', __name__)

from web_static.routes import views
