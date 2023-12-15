#!/usr/bin/python3
"""
Create the Flask application
"""
from flask import Flask
from flask_login import LoginManager
from models import storage
# from web_static.routes import auth, logout, about, application
# from web_static.routes import applied_jobs, contact, job_details, job_history
# from web_static.routes import jobs, jobseeker_dashboard, jobseeker_profile
# from web_static.routes import jobseeker_signup, post_job, posted_jobs
# from web_static.routes import recruiter_dashboard, recruiter_profile
# from web_static.routes import recruiter_signup
# from web_static.routes.index import home_bp


def create_app():
    """ Initialize and create the Flask app """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    # Disable strict slashes
    app.url_map.strict_slashes = False

    # Import the errors file with error handlers
    from web_static.handlers import bp as errors_bp
    app.register_blueprint(errors_bp)

    # Register blueprints for routes
    from web_static.routes import bp as views_bp
    app.register_blueprint(views_bp)

    # @app.teardown_appcontext
    # def teardown_session(exception=None):
    #     """
    #     Terminate an SQLAlchemy session
    #     """
    #     storage.close()

    # login = LoginManager(app)
    # login.login_view = 'login'

    # @login.user_loader
    # def load_user(id):
    #     return storage.get_by_id(id)

    return app
