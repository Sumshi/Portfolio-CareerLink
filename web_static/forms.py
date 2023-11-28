#!/usr/bin/python3
""" Module to implement forms to pass data to application """
from collections.abc import Mapping, Sequence
from typing import Any
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField
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
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone No.', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    password2 = StringField(
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

    def confirm_username(self, username):
        """ Ensure that username is not used i.e unique """
        user = storage.get_by_username(username)
        if user:
            raise ValidationError(
                'Username "{}" already used. Pick another'.format(
                    username.data)
            )

    def confirm_email(self, email):
        """ Ensure that email is not used i.e unique """
        user = storage.get_by_attribute("email", email.data)
        if user:
            raise ValidationError(
                'Email "{}" already used. Pick another'.format(email.data)
            )

    def confirm_company(self, company):
        """ Ensure that company name is not used i.e unique """
        user = storage.get_by_attribute("comapny", company.data)
        if user:
            raise ValidationError(
                'Company name "{}" already used. Pick another'.format(
                    company.data)
            )

    def confirm_phone_number(self, phone_number):
        """ Ensure that Phone Number is not used i.e unique """
        user = storage.get_by_attribute("phone_number", phone_number.data)
        if user:
            raise ValidationError(
                'Phone number "{}" already used. Pick another'.format(
                    phone_number.data)
            )


class JobseekerSignUp(FlaskForm):
    """ Implementation of a Jobseeker Sign Up or Register """
    first_name = StringField('First name', validators=[DataRequired()])
    middle_name = StringField('Middle name')
    last_name = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone No.', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    password2 = StringField(
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
    submit = SubmitField('Sign Up')

    def confirm_username(self, username):
        """ Ensure that username is not used i.e unique """
        user = storage.get_by_username(username)
        if user:
            raise ValidationError(
                'Username "{}" already used. Pick another'.format(
                    username.data)
            )

    def confirm_email(self, email):
        """ Ensure that email is not used i.e unique """
        user = storage.get_by_attribute("email", email.data)
        if user:
            raise ValidationError(
                'Email "{}" already used. Pick another'.format(email.data)
            )

    def confirm_phone_number(self, phone_number):
        """ Ensure that Phone Number is not used i.e unique """
        user = storage.get_by_attribute("phone_number", phone_number.data)
        if user:
            raise ValidationError(
                'Phone number "{}" already used. Pick another'.format(
                    phone_number.data)
            )
    # profile_pic = Column(String(200), nullable=True)
    # resume = Column(String(200), nullable=True)
