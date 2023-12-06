"""
Module app
Starts the Flask application
"""
from web_static import app, PROFILES_FOLDER, COVER_LETTER_FOLDER
from web_static import RESUMES_FOLDER
from datetime import date
from flask import Flask, render_template, redirect, url_for, flash, request
from flask import jsonify
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_login import login_required
# Import the errors file with error handlers
# from web_static.handlers import errors
from models import storage, Recruiter, Jobseeker, Applications
from models import Jobs, JobHistory
from web_static.forms import LoginForm, RecruiterSignUp, JobseekerSignUp
from web_static.forms import RecruiterEditProfileForm
from web_static.forms import JobseekerEditProfileForm, PostJob, PostJobHistory
from urllib.parse import urlparse, urljoin
import os
from werkzeug.utils import secure_filename

# PROFILES_FOLDER = 'static/images/profile_pics'
# RESUMES_FOLDER = 'static/resumes'
# COVER_LETTER_FOLDER = 'static/cover_letters'
# # PROFILES_EXTENSIONS = {'png', 'jpg', 'jpeg', }

# app = Flask(__name__)

# app.config['SECRET_KEY'] = os.environ.get(
#     'SECRET_KEY') or 'this is a trial web app project'
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.config['PROFILES_FOLDER'] = os.environ.get(
#     'PROFILES_FOLDER') or PROFILES_FOLDER
# app.config['RESUMES_FOLDER'] = os.environ.get(
#     'RESUMES_FOLDER') or RESUMES_FOLDER
# app.config['COVER_LETTER_FOLDER'] = os.environ.get(
#     'COVER_LETTER_FOLDER') or COVER_LETTER_FOLDER

# # Import the errors file with error handlers
# from web_static.handlers import bp as errors_bp
# app.register_blueprint(errors_bp)

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
        print('current user {} is authenticated'.format(current_user.username))
        if isinstance(current_user, Jobseeker):
            return redirect(url_for('joblists'))
        else:
            return redirect(url_for('recruiterDashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.get_by_username(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # register the user as logged in i.e any future pages the user
        # navigates to will have the current_user variable set to that user.
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            if isinstance(current_user, Jobseeker):
                next_page = url_for('joblists')
            else:
                # next_page = url_for('my_posted_jobs')
                next_page = url_for('recruiterDashboard')
        return redirect(next_page)
    return render_template('logIn.html',
                           pageTitle='log In',
                           form=form
                           )

# displays home page


@app.route('/')
@app.route('/home')
# @login_required
def home():
    """ Route to display the home page """
    return render_template('index.html')


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


@app.route('/recruiterProfile', methods=['GET', 'POST'])
@login_required
def update_recruiter_profile():
    """ Updates the profile of a recruiter """
    user = storage.get_by_id(current_user.id)
    if not isinstance(user, Recruiter):
        return render_template('403.html')
    jobs = user.job_listings
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
        current_user.street = form.street.data
        current_user.zip_code = form.zip_code.data
        current_user.about = form.about.data
        if form.profile_pic.data:
            # print("data in profile pic")
            old_profile_pic = current_user.profile_pic
            profile_pic = form.profile_pic.data
            filename = current_user.id + '_' + \
                secure_filename(profile_pic.filename)
            filepath = os.path.join(PROFILES_FOLDER, filename)
            save_filepath = os.path.join('web_static/', filepath)
            # print("new file path = {}".format(filepath))
            profile_pic.save(save_filepath)
            if os.path.exists(save_filepath):
                if old_profile_pic and os.path.exists('web_static/' +
                                                      old_profile_pic):
                    os.remove('web_static/' + old_profile_pic)
                current_user.profile_pic = filepath
        storage.save()
        print('POST HTTPS request called')
        # Redirect to profile page after update
        return redirect(url_for('update_recruiter_profile'))
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
        form.street.data = current_user.street
        form.zip_code.data = current_user.zip_code
        form.about.data = current_user.about

    return render_template('recruiterProfile.html',
                           user=user,
                           name=user.username,
                           form=form,
                           jobs=jobs)


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
            print("profile pic filepath = {}".format(filepath))
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
        if user is not None:
            user.save()
        else:
            return redirect(url_for('jobseeker_signup'))
        if storage.get_by_username(user.username):
            flash('Congratulations, {} for registering!!'.format(user.username))
            return redirect(url_for('login'))
    return render_template('jobseeker_signup.html',
                           pageTitle='Sign Up',
                           form=form,
                           submitButtonText='Sign Up'
                           )


@app.route('/jobseekerProfile', methods=['GET', 'POST'])
@login_required
def update_jobseeker_profile():
    """ Updates the profile of a jobseeker """
    user = storage.get_by_id(current_user.id)
    if not isinstance(user, Jobseeker):
        return render_template('403.html')
    job_history = user.prev_jobs
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
        current_user.street = form.street.data
        current_user.zip_code = form.zip_code.data
        current_user.about = form.about.data

        # process the profile picture
        if form.profile_pic.data:
            # print("data in profile pic")
            old_profile_pic = current_user.profile_pic
            profile_pic = form.profile_pic.data
            filename = current_user.id + '_' + \
                secure_filename(profile_pic.filename)
            filepath = os.path.join(PROFILES_FOLDER, filename)
            save_filepath = os.path.join('web_static/', filepath)
            # print("new file path = {}".format(filepath))
            profile_pic.save(save_filepath)
            if os.path.exists(save_filepath):
                if old_profile_pic and os.path.exists('web_static/' +
                                                      old_profile_pic):
                    os.remove('web_static/' + old_profile_pic)
                current_user.profile_pic = filepath

        # process the resume
        if form.resume.data:
            old_resume = current_user.resume
            resume = form.resume.data
            filename = current_user.id + '_' + \
                secure_filename(resume.filename)
            filepath = os.path.join(RESUMES_FOLDER, filename)
            save_filepath = os.path.join('web_static/', filepath)
            resume.save(save_filepath)
            if os.path.exists(save_filepath):
                if old_resume and os.path.exists('web_static/' +
                                                 old_resume):
                    os.remove('web_static/' + old_resume)
                current_user.resume = filepath

        # save the new information in database
        storage.save()
        print('POST HTTPS request called')
        # Redirect to profile page after update
        return redirect(url_for('update_jobseeker_profile'))
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
        form.street.data = current_user.street
        form.zip_code.data = current_user.zip_code
        form.about.data = current_user.about

    return render_template('jobseekerProfile.html',
                           name=user.username,
                           user=user,
                           job_history=job_history,
                           form=form)

# @app.route('/signup')
# def signUp():
#     return render_template('signup.html')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/discover')
# def discover():
#     return render_template('discover.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# @app.route('/jobseekerProfile', methods=['GET'])
# @login_required
# def jobseekerProfile():
#     """ Display the current logged in User progile """
#     user = storage.get_by_id(current_user.id)
#     job_history = user.prev_jobs
#     return render_template('jobseekerProfile.html',
#                            name=user.username,
#                            user=user,
#                            job_history=job_history
#                            )


# @app.route('/recruiterProfile', methods=['GET'])
# @login_required
# def recruiterProfile():
#     """ Display the current logged in User profile """
#     user = storage.get_by_id(current_user.id)
#     jobs = user.job_listings
#     return render_template('recruiterProfile.html',
#                            name=user.username,
#                            user=user,
#                            jobs=jobs
#                            )


@app.route('/userDashboard', methods=['GET'])
@login_required
def userDashboard():
    """ Display the dashboard of the Jobseeker """
    user = storage.get_by_id(current_user.id)
    if not isinstance(user, Jobseeker):
        return render_template('403.html')
    jobs = []
    for job in storage.all(Jobs, order='date_posted').values():
        jobs.append(job.to_dict())
    return render_template('userDashboard.html', jobs=jobs[:10], user=user)


@app.route('/applicationForm/<string:id>', methods=['GET', 'POST'])
@login_required
def applicationForm(id):
    """ To apply for a job """
    job = storage.get(Jobs, id)
    today = date.today()

    # Apply on if the job exists or the deadline is not yet passed
    # if job and today <= job.deadline:
    if job:
        print("job object available")
        if request.method == 'POST':
            print("POST request made")
            # Ensure the required form fields are present
            required_fields = ['first_name',
                               'last_name', 'email']
            if not all(field in request.form for field in required_fields):
                flash('All fields are required')
                return redirect(url_for('applicationForm', id=id))
            user = storage.get_by_id(current_user.id)
            application = Applications(
                job_seeker_id=user.id,
                job_id=job.id,
                first_name=request.form['first_name'],
                middle_name=request.form.get('middle_name', ''),
                last_name=request.form['last_name'],
                email=request.form['email'],
            )
            # process the resume
            if user.resume:
                application.resume = user.resume
            else:
                application.resume = 'not available'
            # process the cover letter
            if 'cover_letter' in request.files and request.files['cover_letter']:
                print("cover letter in request.files")
                cover_letter = request.files['cover_letter']
                # Save the resume file to a folder
                cover_letter_name = secure_filename(cover_letter.filename)
                file_path = os.path.join(
                    COVER_LETTER_FOLDER, cover_letter_name)
                save_file_path = os.path.join('web_static/', file_path)
                print("cover_letter file path = {}".format(file_path))
                cover_letter.save(save_file_path)
                application.cover_letter = file_path
            else:
                flash('Cover letter is required')
                return redirect(url_for('applicationForm', id=id))

            # Save the application if cover letter exists or has content
            if getattr(application, 'cover_letter', None):
                if application is not None:
                    application.save()
                    flash("job application submitted")
                    return redirect(url_for('joblists'))
                else:
                    flash("Application submitted with errors. Apply again")
                    return redirect(url_for('applicationForm', id=id))
            else:
                flash('Cover letter is required')
                return redirect(url_for('applicationForm', id=id))

    return render_template('application_form.html',
                           job=job)


@app.route('/jobHistory', methods=['GET', 'POST'])
@login_required
def jobHistory():
    """ Route to display Job seeker's history """
    form = PostJobHistory()
    user = storage.get_by_id(current_user.id)
    if user is not None:
        if not isinstance(user, Jobseeker):
            flash('Not allowed to post a job history')
            return redirect(url_for('recruiterDashboard'))

        if form.validate_on_submit():
            history = JobHistory(
                job_seeker_id=user.id,
                company_name=form.company_name.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                job_title=form.job_title.data,
                job_description=form.job_description.data,
                country=form.country.data,
                state=form.state.data,
                salary=form.salary.data
            )
            if history is not None:
                history.save()
                return redirect(url_for('update_jobseeker_profile'))
            else:
                return redirect(url_for('jobHistory'))

    return render_template('job_history.html', form=form)


@app.route('/jobPosting', methods=['GET', 'POST'])
@login_required
def jobPosting():
    """ Route to post a new job by recruiter """
    print('jobPosting method called!!')
    form = PostJob()
    user = storage.get_by_id(current_user.id)
    if not isinstance(user, Recruiter):
        flash("Not allowed to post a jod")
        return redirect(url_for('joblists'))
    if form.validate_on_submit():
        # Extract the information and create a Job instance
        job = Jobs(
            recruiters_id=user.id,
            title=form.title.data,
            description=form.description.data,
            type=form.type.data,
            application=form.application.data,
            company=form.company.data,
            contact=form.contact.data,
            deadline=form.deadline.data,
            country=form.country.data,
            town=form.town.data,
            salary=form.salary.data,
            open_position=form.open_position.data,
            skills_required=form.skills_required.data
        )
        if job is not None:
            job.save()
            return redirect(url_for('job_details', id=job.id))

    return render_template('job_posting_form.html',
                           form=form)


@app.route('/recruiterDashboard', methods=['GET'])
@login_required
def recruiterDashboard():
    """ Route to display dashboard for a recruiter page """
    user = storage.get_by_id(current_user.id)
    if not isinstance(user, Recruiter):
        return render_template('403.html')
    my_jobs = user.job_listings
    return render_template('recruiterDashboard.html',
                           my_jobs=my_jobs,
                           user=user)


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
    # check if it is a recruiter
    is_recruiter = False
    user = storage.get_by_id(current_user.id)
    if isinstance(user, Recruiter):
        is_recruiter = True
    job = storage.get(Jobs, id)
    applicants = job.job_seeker
    recruiter = job.recruiter
    return render_template('job_details.html',
                           applicants=applicants,
                           job=job,
                           recruiter=recruiter,
                           is_recruiter=is_recruiter)


if __name__ == '__main__':
    app.run(debug=True)
