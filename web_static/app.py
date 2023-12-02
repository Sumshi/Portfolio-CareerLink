from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_login import login_required
from models import storage, Recruiter, Jobseeker, Application
from models import Jobs, JobHistory
from web_static.forms import LoginForm, RecruiterSignUp, JobseekerSignUp
from web_static.forms import RecruiterEditProfileForm, JobseekerEditProfileForm
from urllib.parse import urlparse, urljoin
import os
from werkzeug.utils import secure_filename

PROFILES_FOLDER = '/web_static/static/images/profile_pics'
RESUMES_FOLDER = '/web_static/static/resumes'
COVER_LETTER_FOLDER = '/web_static/static/cover_letters'
# PROFILES_EXTENSIONS = {'png', 'jpg', 'jpeg', }

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY') or 'this is a trial web app project'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['PROFILES_FOLDER'] = os.environ.get(
    'PROFILES_FOLDER') or PROFILES_FOLDER
app.config['RESUMES_FOLDER'] = os.environ.get(
    'RESUMES_FOLDER') or RESUMES_FOLDER
app.config['COVER_LETTER_FOLDER'] = os.environ.get(
    'COVER_LETTER_FOLDER') or RESUMES_FOLDER

login = LoginManager(app)
login.login_view = 'login'


# def allowed_file(filename):
#     """Provides for """
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in PROFILES_EXTENSIONS

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
        # redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.get_by_username(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # register the user as logged in i.e any future pages the user navigates to
        # will have the current_user variable set to that user.
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
@login_required
def logout():
    """ logout a logged in user """
    logout_user()
    return redirect(url_for('home'))


@app.route('/recruiter_signup', methods=['GET', 'POST'])
def recruiter_signup():
    """ Sign up or register a new recruiter user """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
        if form.profile_pic.data:
            profile_pic = form.profile_pic.data
            filename = secure_filename(profile_pic.filename)
            filepath = os.path.join(PROFILES_FOLDER, filename)
            profile_pic.save(filepath)
        # user.set_password(form.password.data)
        user.save()
        flash('Congratulations, {} for registering!!'.format(user.username))
        return redirect(url_for('login'))
    return render_template('recruiter_signup.html',
                           pageTitle='Sign Up',
                           form=form,
                           submitButtonText='Sign Up'
                           )


@app.route('/recruiter/edit_profile', methods=['GET', 'PUT'])
@login_required
def update_recruiter_profile():
    """ Updates the profile of a recruiter """
    form = RecruiterEditProfileForm()

    if form.validate_on_submit():
        # Process form data and update the profile
        # Example: Get form data - form.company.data, form.username.data, etc.
        # Update the profile details in the database

        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.company = form.company.data
        current_user.phone_number = form.phone_number.data
        current_user.country = form.country.data
        current_user.state = form.state.data
        current_user.address = form.address.data
        current_user.street = form.address.data
        current_user.zip_code = form.zip_code.data
        current_user.about = form.about.data
        if form.profile_pic.data:
            old_profile_pic = current_user.profile_pic
            profile_pic = form.profile_pic.data
            filename = secure_filename(profile_pic.filename)
            filepath = os.path.join(PROFILES_FOLDER, filename)
            profile_pic.save(filepath)
            if os.path.exists(filepath):
                if os.path.exists(old_profile_pic):
                    os.remove(old_profile_pic)
                current_user.profile_pic = filepath
        storage.save()
        # Redirect to profile page after update
        return redirect(url_for('recruiter/profile'))
    elif request.method == 'GET':
        # Fetch the current user's profile data from the database
        # Assuming current_user is from Flask-Login
        # recruiter = storage.get_by_id(current_user.id)

        # Populate the form fields with the current data from the database
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.company.data = current_user.company
        form.phone_number.data = current_user.phone_number
        form.country.data = current_user.country
        form.state.data = current_user.state
        form.address.data = current_user.address
        form.address.data = current_user.street
        form.zip_code.data = current_user.zip_code
        form.about.data = current_user.about

    return render_template('recruiterProfile.html',
                           pageTitle='Edit Profile',
                           form=form)


@app.route('/jobseeker_signup', methods=['GET', 'POST'])
def jobseeker_signup():
    """ Sign up or register a new jobseeker user """
    if current_user.is_authenticated:
        return redirect(url_for('joblists'))
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

        # process the profile pic
        if form.profile_pic.data:
            # Retrieve the uploaded file object from form field
            profile_pic = form.profile_pic.data
            # Ensure the filename is secure
            filename = secure_filename(profile_pic.filename)
            filepath = os.path.join(PROFILES_FOLDER, filename)
            # save the uploaded picture to the server's file system
            profile_pic.save(filepath)
            user.profile_pic = filepath

        # process the resume
        if form.resume.data:
            # Retrieve the uploaded file object from form field
            resume = form.profile_pic.data
            # Ensure the filename is secure
            filename = secure_filename(resume.filename)
            filepath = os.path.join(RESUMES_FOLDER, filename)
            # save the uploaded picture to the server's file system
            resume.save(filepath)
            user.resume = filepath
        # user.set_password(form.password.data)
        user.save()
        flash('Congratulations, {} for registering!!'.format(user.username))
        return redirect(url_for('login'))
    return render_template('jobseeker_signup.html',
                           pageTitle='Sign Up',
                           form=form,
                           submitButtonText='Sign Up'
                           )


@app.route('/jobseeker/edit_profile', methods=['GET', 'PUT'])
@login_required
def update_jobseeker_profile():
    """ Updates the profile of a jobseeker """
    form = JobseekerEditProfileForm()

    if form.validate_on_submit():
        # Process form data and update the profile
        # Example: Get form data - form.company.data, form.username.data, etc.
        # Update the profile details in the database

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.middle_name = form.middle_name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        current_user.country = form.country.data
        current_user.state = form.state.data
        current_user.address = form.address.data
        current_user.street = form.address.data
        current_user.zip_code = form.zip_code.data
        current_user.about = form.about.data
        if form.profile_pic.data:
            old_profile_pic = current_user.profile_pic
            profile_pic = form.profile_pic.data
            filename = secure_filename(profile_pic.filename)
            filepath = os.path.join(PROFILES_FOLDER, filename)
            profile_pic.save(filepath)
            if os.path.exists(filepath):
                if os.path.exists(old_profile_pic):
                    os.remove(old_profile_pic)
                current_user.profile_pic = filepath
        if form.resume.data:
            old_resume = current_user.resume
            resume = form.resume.data
            filename = secure_filename(resume.filename)
            filepath = os.path.join(RESUMES_FOLDER, filename)
            resume.save(filepath)
            if os.path.exists(filepath):
                if os.path.exists(old_resume):
                    os.remove(old_resume)
                current_user.resume = filepath
        storage.save()
        # Redirect to profile page after update
        return redirect(url_for('jobseeker/profile'))
    elif request.method == 'GET':
        # Fetch the current user's profile data from the database
        # Assuming current_user is from Flask-Login
        # recruiter = storage.get_by_id(current_user.id)

        # Populate the form fields with the current data from the database
        form.first_name.data = current_user.first_name
        form.middle_name.data = current_user.middle_name
        form.last_name.data = current_user.last_name
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.phone_number.data = current_user.phone_number
        form.country.data = current_user.country
        form.state.data = current_user.state
        form.address.data = current_user.address
        form.address.data = current_user.street
        form.zip_code.data = current_user.zip_code
        form.about.data = current_user.about

    return render_template('edit_jobseeker_profile.html',
                           pageTitle='Edit Profile',
                           form=form)

# @app.route('/signup')
# def signUp():
#     return render_template('signup.html')

# displays home page


@app.route('/')
@app.route('/home')
# @login_required
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/discover')
# def discover():
#     return render_template('discover.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/jobseekerProfile', methods=['GET'])
@login_required
def jobseekerProfile():
    """ Display the current logged in User progile """
    user = storage.get_by_id(current_user.id)
    job_history = user.prev_jobs
    return render_template('jobseekerProfile.html',
                           name=user.username,
                           user=user,
                           job_history=job_history
                           )


@app.route('/recruiterProfile', methods=['GET'])
@login_required
def recruiterProfile():
    """ Display the current logged in User profile """
    user = storage.get_by_id(current_user.id)
    jobs = user.job_listings
    return render_template('recruiterProfile.html',
                           name=user.username,
                           user=user,
                           jobs=jobs
                           )


@app.route('/userDashboard', methods=['GET'])
@login_required
def userDashboard():
    return render_template('userDashboard.html')


@app.route('/applicationForm/<string:id>', methods=['GET', 'POST'])
@login_required
def applicationForm(id):
    """ To apply for a job """
    job = storage.get(Jobs, id)
    if job:
        if request.method == 'POST':
            # Ensure the required form fields are present
            required_fields = ['first_name',
                               'last_name', 'email', 'cover_letter']
            if not all(field in request.form for field in required_fields):
                flash('All fields are required')
                return redirect(url_for('applicationForm', id=id))
            user = storage.get_by_id(current_user.id)
            application = Application(
                job_seeker_id=user.id,
                job_id=job.id,
                first_name=request.form['first_name'],
                middle_name=request.form.get('middle_name', ''),
                last_name=request.form['last_name'],
                email=request.form['email'],
                resume=user.resume,
            )
            # process the cover letter
            if 'cover_letter' in request.files:
                cover_letter = request.files['cover_letter']
                # Save the resume file to a folder
                cover_letter_name = secure_filename(cover_letter.filename)
                file_path = os.path.join(
                    app.config['COVER_LETTER_FOLDER'], cover_letter_name)
                cover_letter.save(file_path)
                application.cover_letter = file_path
            application.save()

            return redirect(url_for('joblists'))

    return render_template('application_form.html')


@app.route('/jobHistory', methods=['GET'])
@login_required
def jobHistory():
    """ Route to display Job seeker's history """
    return render_template('job_history.html')


@app.route('/jobPosting', methods=['GET', 'POST'])
@login_required
def jobPosting():
    """ Route to post a new job by recruiter """
    return render_template('job_posting_form.html')


@app.route('/recruiterDashboard', methods=['GET'])
@login_required
def recruiterDashboard():
    """ Route to display dashboard for a recruiter page """
    recruiter = storage.get_by_id(current_user.id)
    my_jobs = recruiter.job_listings
    return render_template('recruiterDashboard.html',
                           my_jobs=my_jobs,
                           recruiter=recruiter)


@app.route('/joblists', methods=['GET'])
@login_required
def joblists():
    """ Route to display all the jobs posted """
    jobs = []
    for job in storage.all(Jobs).values():
        jobs.append(job.to_dict())
    return render_template('joblists.html',
                           jobs=jobs)


@app.route('/posted_jobs', methods=['GET'])
@login_required
def my_posted_jobs():
    """ Route to retrieve a recruiter's posted jobs """
    recruiter = storage.get_by_id(current_user.id)
    my_jobs = recruiter.job_listings
    return render_template('posted_jobs.html',
                           my_jobs=my_jobs,
                           recruiter=recruiter)

# jobseeker


@app.route('/applied_jobs', methods=['GET'])
@login_required
def my_applied_jobs():
    """ Route to retrieve a jobseeker's applied jobs """
    user = storage.get_by_id(current_user.id)
    applications = user.application
    jobs = []
    for aplic in applications:
        job = storage.get(Jobs, aplic.job_id)
        if job:
            jobs.append(job)
    for job in jobs:
        print("current job id is: {}".format(job.id))

    print(jobs)
    num = len(jobs)
    return render_template('applied_jobs.html',
                           jobs=jobs,
                           user=user,
                           num=num)


@app.route('/job/<string:id>', methods=['GET'])
@login_required
def job_details(id):
    """ Retrieve details for a specific job """
    job = storage.get(Jobs, id)
    applicants = job.job_seeker
    recruiter = job.recruiter
    return render_template('job_details.html',
                           applicants=applicants,
                           job=job,
                           recruiter=recruiter,
                           user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
