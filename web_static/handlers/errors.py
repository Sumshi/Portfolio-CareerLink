#!/usr/bin/python3
"""
Errors modules
Custom templates for error handling
"""

from flask import render_template, url_for, request
from flask_login import current_user
from models import storage, Recruiter
from web_static.handlers import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    url = request.path
    print("404 error handler called for this url: {}".format(url))
    is_recruiter = False
    if current_user.is_authenticated:
        user = storage.get_by_id(current_user.id)
        if isinstance(user, Recruiter):
            is_recruiter = True
        return render_template('404.html', is_recruiter=is_recruiter)
    # url = url_for('views.home')
    # print("url_for('home') is : {}".format(url))
    return render_template('404.html', is_recruiter=is_recruiter), 404


@bp.app_errorhandler(403)
def not_found_error(error):
    print("403 error handler called")
    is_recruiter = False
    if current_user.is_authenticated:
        user = storage.get_by_id(current_user.id)
        if isinstance(user, Recruiter):
            is_recruiter = True
        return render_template('403.html', is_recruiter=is_recruiter)
    return render_template('403.html', is_recruiter=is_recruiter), 403


@bp.app_errorhandler(500)
def internal_error(error):
    print("500 error handler called")
    storage.roll_back()
    is_recruiter = False
    if current_user.is_authenticated:
        user = storage.get_by_id(current_user.id)
        if isinstance(user, Recruiter):
            is_recruiter = True
        return render_template('500.html', is_recruiter=is_recruiter)
    return render_template('500.html', is_recruiter=is_recruiter), 500
