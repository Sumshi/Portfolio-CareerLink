#!/usr/bin/python3
""" defines the class jobseeker """
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship, backref


class Jobseeker(BaseModel, UserMixin, Base):
    """ Represents a job seeker """
    __tablename__ = 'job_seekers'
    first_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), index=True, unique=True, nullable=False)
    phone_number = Column(String(60), unique=True, nullable=False)
    username = Column(String(128), index=True, unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    country = Column(String(60), nullable=False)
    state = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    street = Column(String(128), nullable=True)
    zip_code = Column(String(32), nullable=True)
    profile_pic = Column(String(200), nullable=True)
    about = Column(String(600), nullable=True)
    resume = Column(String(200), nullable=True)
    application = relationship('Application', backref='my_jobs')
    token = Column(String(32), index=True, unique=True)
    token_expiration = Column(DateTime)

    def __init__(self, *args, **kwargs):
        """initializes jobseekers"""
        super().__init__(*args, **kwargs)

    @staticmethod
    def check_token(token):
        """
        static method that takes a token as input and returns the user this token
        belongs to as a response. If the token is invalid or expired,
        the method returns None
        """
        from models import storage
        jobseeker = storage.get_by_token(token=token)
        if jobseeker is None or jobseeker.token_expiration < datetime.utcnow():
            return None
        return jobseeker
