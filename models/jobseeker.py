#!/usr/bin/python3
""" defines the class jobseeker """
from hashlib import md5
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship, backref


class Jobseeker(BaseModel, Base):
    """ Represents a job seeker """
    __tablename__ = 'job_seekers'
    first_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    phone_number = Column(String(60), nullable=False)
    username = Column(String(128), nullable=False)
    password = Column(String(200), nullable=False)
    country = Column(String(60), nullable=False)
    state = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    street = Column(String(128), nullable=True)
    zip_code = Column(Integer, nullable=True)
    profile_pic = Column(String(200), nullable=True)
    about = Column(String(600), nullable=True)
    resume = Column(String(200), nullable=True)
    application = relationship('Application', backref='my_jobs')

    __table_args__ = (
        UniqueConstraint('username'),
        UniqueConstraint('email'),
        UniqueConstraint('phone_number')
    )

    def __init__(self, *args, **kwargs):
        """initializes jobseekers"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = generate_password_hash(value)
        super().__setattr__(name, value)

    def check_jobseeker_password(self, passw):
        return check_password_hash(self.password, passw)
