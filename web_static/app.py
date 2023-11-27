from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_login import login_required
from models import storage, Recruiter, Jobseeker, Application
from models import Jobs, JobHistory
from web_static.forms import LoginForm, RecruiterSignUp, JobseekerSignUp
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this a trial web app project'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

login = LoginManager(app)
login.login_view = 'login'


@login.user_loader
def load_user(id):
    return storage.get_by_id(id)
# sign up and sign in routes


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Provides the logic to log in a user
    """
    if current_user.is_authenticated:
        redirect(url_for('joblists'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.get_by_username(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # register the user as logged in i.e any future pages the user navigates to
        #  will have the current_user variable set to that user.
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('joblists')
        return redirect(next_page)
    return render_template('logIn.html',
                           pageTitle='log In',
                           form=form
                           )


@app.route('/logout')
def logout():
    """ logout a logged in user """
    logout_user()
    redirect(url_for('index'))


@app.route('/recruiter_signup')
def recruiter_signup():
    """ Sign up or register a new recruiter user """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RecruiterSignUp()
    if form.validate_on_submit():
        user = Recruiter(
            username=form.username.data,
            email=form.email.data,
            company=form.company.data,
            phone_number=form.phone_number.data,
            password=form.password.data,
            country=form.country.data,
            state=form.state.data,
            address=form.address.data,
            street=form.address.data,
            zip_code=form.zip_code.data,
            about=form.about.data
        )
        # user.set_password(form.password.data)
        user.save()
        flash('Congratulations, {} for registering!!'.format(user.username))
        return redirect(url_for('login'))
    return render_template('recruiter_signup',
                           pageTitle='Sign Up',
                           form=form
                           )


@app.route('/jobseeker_signup')
def jobseeker_signup():
    """ Sign up or register a new jobseeker user """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = JobseekerSignUp()
    if form.validate_on_submit():
        user = Jobseeker(
            first_name=form.first_name.data,
            middle_name=form.middle_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            password=form.password.data,
            country=form.country.data,
            state=form.state.data,
            address=form.address.data,
            street=form.address.data,
            zip_code=form.zip_code.data,
            about=form.about.data
        )
        # user.set_password(form.password.data)
        user.save()
        flash('Congratulations, {} for registering!!'.format(user.username))
        return redirect(url_for('login'))
    return render_template('recruiter_signup',
                           pageTitle='Sign Up',
                           form=form
                           )
# @app.route('/signup')
# def signUp():
#     return render_template('signup.html')

# displays home page


@app.route('/')
@app.route('/home')
@login_required
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
