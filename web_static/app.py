from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user
from models import storage
from web_static.forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this a trial web app project'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

login = LoginManager(app)
# print(login.__dict__)


@login.user_loader
def load_user(id):
    return storage.get_by_id(id)
# sign up and sign in routes


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('joblists'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.get_by_username(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('joblists'))
    return render_template('logIn.html',
                           pageTitle='log In',
                           form=form
                           )
    # return render_template('signUp.html',
    #                        pageTitle='Sign In',
    #                        formMethod='post',
    #                        submitButtonText='Log In',
    #                        alternateButtonText='Sign Up')
# @app.route('/signup')
# def signUp():
#     return render_template('signup.html')

# displays home page


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/discover')
def discover():
    return render_template('discover.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/joblists')
def joblists():
    return render_template('joblists.html')


if __name__ == '__main__':
    app.run(debug=True)
