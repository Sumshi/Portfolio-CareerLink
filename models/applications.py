#!/usr/bin/python3
""" defines the class Application """
from datetime import datetime, date
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship, backref


class Application(BaseModel, Base):
    """ Represents a job application """
    __tablename__ = 'applications'
    job_seeker_id = Column(String(60), ForeignKey(
        'job_seekers.id'), nullable=False)
    job_id = Column(String(60), ForeignKey(
        'jobs.id'), nullable=False)
    first_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), index=True, nullable=False)
    resume = Column(String(200), nullable=False)
    cover_letter = Column(String(200), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Applications"""
        super().__init__(*args, **kwargs)
