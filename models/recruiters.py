#!/usr/bin/python3
""" defines the class Recruiter """
from hashlib import md5
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship, backref


class Recruiter(BaseModel, Base):
    """ Represents a recruiter """
    __tablename__ = 'recruiters'
    company = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    pnone_number = Column(String(60), nullable=False)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    country = Column(String(60), nullable=False)
    state = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    street = Column(String(128), nullable=True)
    zip_code = Column(Integer, nullable=True)
    profile_pic = Column(String(200), nullable=True)
    about = Column(String(600), nullable=True)

    __table_args__ = (
        UniqueConstraint('company'),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
        UniqueConstraint('phone_number')
    )

    def __init__(self, *args, **kwargs):
        """initializes Recruiters"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
