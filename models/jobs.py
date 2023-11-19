#!/usr/bin/python3
""" defines the class Jobs """
from datetime import datetime, date
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship, backref


class Jobs(BaseModel, Base):
    """ Represents a job listing """
    __tablename__ = 'jobs'
    recruiters_id = Column(String(60), ForeignKey(
        'recruiters.id'), nullable=False)
    job_title = Column(String(128), nullable=False)
    job_description = Column(String(1000), nullable=False)
    job_type = Column(String(128), default='onsite')
    application_instr = Column(String(1000), nullable=False)
    company_name = Column(String(128), nullable=False)
    contact = Column(String(60), nullable=False)
    deadline = Column(Date, nullable=False)
    country = Column(String(60), nullable=False)
    state = Column(String(128), nullable=False)
    salary = Column(Integer, nullable=True)
    recruiter = relationship('Recruiter', backref=backref(
        'job_listings', cascade="all, delete"))
    job_seeker = relationship('Application', backref='applicants')

    def __init__(self, *args, **kwargs):
        """initializes Jobs"""
        super().__init__(*args, **kwargs)
