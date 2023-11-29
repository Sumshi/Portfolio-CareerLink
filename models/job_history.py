#!/usr/bin/python3
""" defines the class JobHistory """
from datetime import datetime, date
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship, backref


class JobHistory(BaseModel, Base):
    """ Represents a job seekers job history """
    __tablename__ = 'job_history'
    job_seeker_id = Column(String(60), ForeignKey(
        'job_seekers.id'), nullable=False)
    company_name = Column(String(128), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, default=date.today())
    job_title = Column(String(128), nullable=False)
    job_description = Column(String(1000), nullable=False)
    country = Column(String(60), nullable=False)
    state = Column(String(128), nullable=False)
    salary = Column(Integer, nullable=True)
    job_seeker = relationship('Jobseeker', backref=backref(
        'prev_jobs', cascade="all, delete"))

    def __init__(self, *args, **kwargs):
        """initializes JobHistory"""
        super().__init__(*args, **kwargs)
