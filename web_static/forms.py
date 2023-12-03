#!/usr/bin/python3
""" Module to implement forms to pass data to application """
from collections.abc import Mapping, Sequence
from typing import Any
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from wtforms.validators import Length
from models import storage


class LoginForm(FlaskForm):
    """ Implementation of the Log In page """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')


class RecruiterSignUp(FlaskForm):
    """ Implementation of a Recruiter Sign Up or Register """
    company = StringField('Company name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    profile_pic = FileField(
        'Profile picture',
        validators=[
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!'),
            FileSize(max_size=(2 * 1024))
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
        user = storage.get_by_username(username)
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

    def validate_company(self, company):
        """ Ensure that company name is not used i.e unique """
        user = storage.get_by_attribute("comapny", company.data)
        if user:
            raise ValidationError(
                'Company name "{}" already used. Pick another'.format(
                    company.data)
            )

    def validate_phone_number(self, phone_number):
        """ Ensure that Phone Number is not used i.e unique """
        user = storage.get_by_attribute("phone_number", phone_number.data)
        if user:
            raise ValidationError(
                'Phone number "{}" already used. Pick another'.format(
                    phone_number.data)
            )


class RecruiterEditProfileForm(RecruiterSignUp):
    """ Form for editing the recruiter profile """

    password = None  # Exclude password field from profile editing
    password2 = None
    submit = SubmitField('Update Profile')


class JobseekerSignUp(FlaskForm):
    """ Implementation of a Jobseeker Sign Up or Register """
    first_name = StringField('First name', validators=[DataRequired()])
    middle_name = StringField('Middle name')
    last_name = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    profile_pic = FileField(
        'Profile picture',
        validators=[
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!'),
            FileSize(max_size=(2 * 1024))
        ]
    )
    email = EmailField('Email', validators=[DataRequired(), Email()])
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
        ('About Me'), validators=[Length(min=0, max=300)]
    )
    resume = FileField(
        'Resume',
        validators=[
            FileAllowed(['pdf']), FileSize(max_size=(2 * 1024))
        ]
    )
    submit = SubmitField('Sign Up')

    # When you add any methods that match the pattern validate_<field_name>,
    # WTForms takes those as custom validators and invokes them in addition
    # to the stock validators.
    def validate_username(self, username):
        """ Ensure that username is not used i.e unique """
        user = storage.get_by_username(username)
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

    def validate_phone_number(self, phone_number):
        """ Ensure that Phone Number is not used i.e unique """
        user = storage.get_by_attribute("phone_number", phone_number.data)
        if user:
            raise ValidationError(
                'Phone number "{}" already used. Pick another'.format(
                    phone_number.data)
            )


class JobseekerEditProfileForm(JobseekerSignUp):
    """ Form for editing the job seeker profile """

    password = None  # Exclude password field from profile editing
    submit = SubmitField('Update Profile')
