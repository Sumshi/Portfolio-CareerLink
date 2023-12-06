#!/usr/bin/python3
"""
Errors modules
Custom templates for error handling
"""

from flask import render_template
from models import storage
from web_static.handlers import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    print("404 error handler called")
    return render_template('404.html'), 404


@bp.app_errorhandler(403)
def not_found_error(error):
    print("403 error handler called")
    return render_template('403.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    print("500 error handler called")
    storage.roll_back()
    return render_template('500.html'), 500
