#!/usr/bin/python3
""" Module to implement forms to pass data to application """
from collections.abc import Mapping, Sequence
from datetime import date
from typing import Any
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, EmailField, DateField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from wtforms.validators import Length
from models import storage


class LoginForm(FlaskForm):
    """ Implementation of the Log In page """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')

# A general class to implement a Sign Up


class SignUp(FlaskForm):
    """ Implementation of a Sign Up or Register """
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    profile_pic = FileField(
        'Profile picture',
        validators=[
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!'),
            FileSize(max_size=(2 * 1024 * 1024))
        ]
    )
    phone_number = StringField('Phone No.', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    country = StringField('Country', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    street = StringField('Street')
    zip_code = StringField('Zip Code')
    about = TextAreaField(
        ('About Company'), validators=[Length(min=0, max=300)]
    )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """ Ensure that username is not used i.e unique """
        user = storage.get_by_attribute('username', username.data)
        if user:
            raise ValidationError(
                'Username "{}" already used. Pick another'.format(
                    username.data)
            )

    def validate_email(self, email):
        """ Ensure that email is not used i.e unique """
        user = storage.get_by_attribute("email", email.data)
        if user:
            raise ValidationError(
                'Email "{}" already used. Pick another'.format(email.data)
            )

    # def validate_company(self, company):
    #     """ Ensure that company name is not used i.e unique """
    #     user = storage.get_by_attribute("comapny", company.data)
    #     if user:
    #         raise ValidationError(
    #             'Company name "{}" already used. Pick another'.format(
    #                 company.data)
    #         )

    def validate_phone_number(self, phone_number):
        """ Ensure that Phone Number is not used i.e unique """
        user = storage.get_by_attribute("phone_number", phone_number.data)
        if user:
            raise ValidationError(
                'Phone number "{}" already used. Pick another'.format(
                    phone_number.data)
            )


# A general class to implement a Profile Edit
class EditProfileForm(FlaskForm):
    """ Form for editing the profile """
    # company = StringField('Company name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    profile_pic = FileField(
        'Profile picture',
        validators=[
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!'),
            FileSize(max_size=(2 * 1024 * 1024))
        ]
    )
    phone_number = StringField('Phone No.', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    street = StringField('Street')
    zip_code = StringField('Zip Code')
    about = TextAreaField(
        ('About Company'), validators=[Length(min=0, max=300)]
    )
    submit = SubmitField('Update Profile')

    def validate_username(self, username):
        """ Ensure that username is not used i.e unique """
        print("Username validation method called!!")
        if username.data != current_user.username:
            user = storage.get_by_attribute('username', username.data)
            if user:
                raise ValidationError(
                    'Username "{}" already used. Pick another'.format(
                        username.data)
                )

    def validate_email(self, email):
        """ Ensure that email is not used i.e unique """
        print("Email validation method called!!")
        if email.data != current_user.email:
            user = storage.get_by_attribute("email", email.data)
            if user is not None:
                raise ValidationError(
                    'Email "{}" already used. Pick another'.format(email.data)
                )

    # def validate_company(self, company):
    #     """ Ensure that company name is not used i.e unique """
    #     # print("Company name validation method called!!")
    #     if company.data != current_user.company:
    #         user = storage.get_by_attribute("comapny", company.data)
    #         if user is not None:
    #             raise ValidationError(
    #                 'Company name "{}" already used. Pick another'.format(
    #                     company.data)
    #             )

    def validate_phone_number(self, phone_number):
        """ Ensure that Phone Number is not used i.e unique """
        print("Phone number validation method called!!")
        if phone_number.data != current_user.phone_number:
            user = storage.get_by_attribute("phone_number", phone_number.data)
            if user is not None:
                raise ValidationError(
                    'Phone number "{}" already used. Pick another'.format(
                        phone_number.data)
                )

    def validate_profile_pic(self, profile_pic):
        """ Set and save the profile pic """
        # print("Profile pic validation method called")
        pass


# A class that implements a Recruiter Sign Up & Inherits from SignUp class
class RecruiterSignUp(SignUp, FlaskForm):
    """ Implementation of a Recruiter Sign Up or Register """
    company = StringField('Company name', validators=[DataRequired()])

    def validate_company(self, company):
        """ Ensure that company name is not used i.e unique """
        user = storage.get_by_attribute("comapny", company.data)
        if user:
            raise ValidationError(
                'Company name "{}" already used. Pick another'.format(
                    company.data)
            )


class RecruiterEditProfileForm(EditProfileForm, FlaskForm):
    """ Form for editing the recruiter profile """
    company = StringField('Company name', validators=[DataRequired()])

    def validate_company(self, company):
        """ Ensure that company name is not used i.e unique """
        print("Company name validation method called!!")
        if company.data != current_user.company:
            user = storage.get_by_attribute("comapny", company.data)
            if user is not None:
                raise ValidationError(
                    'Company name "{}" already used. Pick another'.format(
                        company.data)
                )

# A class that implements a Jobseeker Sign Up & Inherits from SignUp class


class JobseekerSignUp(SignUp, FlaskForm):
    """ Implementation of a Jobseeker Sign Up or Register """
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name', validators=[DataRequired()])
    resume = FileField(
        'Resume',
        validators=[
            FileAllowed(['pdf']), FileSize(max_size=(2 * 1024 * 1024))
        ]
    )


class JobseekerEditProfileForm(EditProfileForm, FlaskForm):
    """ Form for editing the job seeker profile """
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name', validators=[DataRequired()])
    resume = FileField(
        'Resume',
        validators=[
            FileAllowed(['pdf']), FileSize(max_size=(2 * 1024 * 1024))
        ]
    )


# class to implement job posting
class PostJob(FlaskForm):
    """ Implements job posting form """
    title = StringField('Job Title', validators=[DataRequired()])
    description = TextAreaField("Job Description", validators=[
                                DataRequired(), Length(max=1000)])
    type = SelectField('Job Type', choices=[
                       'Full Time', 'Part Time', 'Contract', 'Remote Work'])
    application = TextAreaField('Application Instruction', validators=[
                                DataRequired(), Length(max=500)])
    company = StringField('Company Name', validators=[DataRequired()])
    contact = StringField('Contact Info', validators=[DataRequired()])
    deadline = DateField('Application Deadline', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    town = StringField('City/State', validators=[DataRequired()])
    salary = StringField('Salary', default='0', validators=[DataRequired()])
    open_position = StringField(
        'Open Positions', default='1', validators=[DataRequired()])
    skills_required = TextAreaField(
        'Skills Needed', default="No skillls needed", validators=[DataRequired()])
    submit = SubmitField('Post Job')

    def validate_company(self, company):
        """ Validate the company name and ensure company is not another's """
        print("Company name validation method called!!")
        if company.data != current_user.company:
            user = storage.get_by_attribute("comapny", company.data)
            if user is not None:
                raise ValidationError(
                    'Company name "{}" is invalid'.format(
                        company.data)
                )

# A class to implement job history posting


class PostJobHistory(FlaskForm):
    """ Implements form to post a job history """
    company_name = StringField('Company Name', validators=[DataRequired()])
    start_date = DateField('From', validators=[DataRequired()])
    end_date = DateField('To', default=date.today(),
                         validators=[DataRequired()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    job_description = TextAreaField(
        'Job Description', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    state = StringField('City/State/Town', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    submit = SubmitField('Add Previous Job')
