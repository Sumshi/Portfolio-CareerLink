#!/usr/bin/python3
""" Module to implement forms to pass data to application """
from collections.abc import Mapping, Sequence
from typing import Any
from flask_login import current_user
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


class RecruiterEditProfileForm(FlaskForm):
    """ Form for editing the recruiter profile """
    company = StringField('Company name', validators=[DataRequired()])
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
        # print("Username validation method called!!")
        if username.data != current_user.username:
            user = storage.get_by_attribute('username', username.data)
            if user:
                raise ValidationError(
                    'Username "{}" already used. Pick another'.format(
                        username.data)
                )

    def validate_email(self, email):
        """ Ensure that email is not used i.e unique """
        # print("Email validation method called!!")
        if email.data != current_user.email:
            user = storage.get_by_attribute("email", email.data)
            if user is not None:
                raise ValidationError(
                    'Email "{}" already used. Pick another'.format(email.data)
                )

    def validate_company(self, company):
        """ Ensure that company name is not used i.e unique """
        # print("Company name validation method called!!")
        if company.data != current_user.company:
            user = storage.get_by_attribute("comapny", company.data)
            if user is not None:
                raise ValidationError(
                    'Company name "{}" already used. Pick another'.format(
                        company.data)
                )

    def validate_phone_number(self, phone_number):
        """ Ensure that Phone Number is not used i.e unique """
        # print("Phone number validation method called!!")
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
