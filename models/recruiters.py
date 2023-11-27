#!/usr/bin/python3
""" defines the class Recruiter """
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship, backref


class Recruiter(BaseModel, UserMixin, Base):
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

    # def set_password(self, password, new_obj=None):
    #     """
    #     Sets the password hash for the recruiter only for updated password
    #     """
    #     if new_obj:
    #         pass    # do not do anything i.e maintain password
    #     else:       # update the password
    #         self.password = generate_password_hash(password)

    # def check_recruiter_password(self, passw):
    #     """ verifys the Recruiter object password """
    #     return check_password_hash(self.password, passw)

    # def get_token(self, expires_in=3600):
    #     """
    #     returns a token for the user. The token is generated as a random
    #     string that is encoded in base64
    #     """
    #     from models import storage
    #     now = datetime.utcnow()
    #     if self.token and self.token_expiration > now + timedelta(seconds=60):
    #         return self.token
    #     token = base64.b64encode(urandom(24)).decode('utf-8')
    #     token_expiration = now + timedelta(seconds=expires_in)
    #     self.__setattr__("token", token)
    #     self.__setattr__("token_expiration", token_expiration)
    #     storage.save()
    #     return self.token

    # def revoke_token(self):
    #     """
    #     makes the token currently assigned to the user invalid, simply
    #     by setting the expiration date to one second before the current time.
    #     """
    #     self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        """
        static method that takes a token as input and returns the user this token
        belongs to as a response. If the token is invalid or expired,
        the method returns None
        """
        from models import storage
        recruiter = storage.get_by_token(token=token)
        if recruiter is None or recruiter.token_expiration < datetime.utcnow():
            return None
        return recruiter
