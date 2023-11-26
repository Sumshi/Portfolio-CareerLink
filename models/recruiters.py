#!/usr/bin/python3
""" defines the class Recruiter """
import base64
from datetime import datetime, timedelta
from hashlib import md5
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship, backref
from os import urandom


class Recruiter(BaseModel, Base):
    """ Represents a recruiter """
    __tablename__ = 'recruiters'
    company = Column(String(128), index=True, unique=True, nullable=False)
    email = Column(String(128), index=True, unique=True, nullable=False)
    phone_number = Column(String(60), unique=True, nullable=False)
    username = Column(String(128), index=True, unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    country = Column(String(60), nullable=False)
    state = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    street = Column(String(128), nullable=True)
    zip_code = Column(Integer, nullable=True)
    profile_pic = Column(String(200), nullable=True)
    about = Column(String(600), nullable=True)
    token = Column(String(32), index=True, unique=True)
    token_expiration = Column(DateTime)

    def __init__(self, *args, **kwargs):
        """initializes Recruiters"""
        super().__init__(*args, **kwargs)

    # def __setattr__(self, name, value):
    #     """sets a password with md5 encryption"""
    #     if name == "password":
    #         print("set password for {} is {}".format(self.username, value))
    #         value = generate_password_hash(value)
    #     super().__setattr__(name, value)
    # def set_password(self, password):
    #     """ Sets the password hash for the recruiter """
    #     self.password = generate_password_hash(password)

    def check_recruiter_password(self, passw):
        print("chcheck_recruiter_password method called with password {}".format(passw))
        res = check_password_hash(self.password, passw)
        print("result of check_password = {}".format(res))
        return res

    def get_token(self, expires_in=3600):
        from models import storage
        print("get_token method called")
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        token = base64.b64encode(urandom(24)).decode('utf-8')
        token_expiration = now + timedelta(seconds=expires_in)
        self.__setattr__("token", token)
        self.__setattr__("token_expiration", token_expiration)
        storage.save()
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        recruiter = Recruiter.query.filter_by(token=token).first()
        if recruiter is None or recruiter.token_expiration < datetime.utcnow():
            return None
        return recruiter

    # def __setattr__(self, name, value):
    #     """sets a password with md5 encryption"""
    #     if name == "password":
    #         value = md5(value.encode()).hexdigest()
    #     super().__setattr__(name, value)
