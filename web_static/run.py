#!/usr/bin/python3
""" Instatiate and run the app application """
from web_static import create_app
from models import storage
from flask_login import LoginManager

app = create_app()


@app.teardown_appcontext
def teardown_session(exception=None):
    """
    Terminate an SQLAlchemy session
    """
    storage.close()


login = LoginManager(app)
login.login_view = 'views.login'


@login.user_loader
def load_user(id):
    return storage.get_by_id(id)


if __name__ == '__main__':
    app.run(debug=True)
