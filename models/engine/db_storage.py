#!/usr/bin/python3
""" A module that dedines the database storage """

from models.applications import Applications
from models.base_model import BaseModel, Base
from models.job_history import JobHistory
from models.jobseeker import Jobseeker
from models.jobs import Jobs
from models.recruiters import Recruiter
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy
import models
from werkzeug.security import generate_password_hash


classes = {"Applications": Applications, "BaseModel": BaseModel, "Jobs": Jobs,
           "JobHistory": JobHistory, "Jobseeker": Jobseeker,
           "Recruiter": Recruiter}


class DBStorage():
    """ A class that interacts with the database """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the DBStorage class """
        _user = getenv("PROJ_USER")
        _psswd = getenv("PROJ_PWD")
        _host = getenv("PROJ_HOST")
        _db = getenv("PROJ_DB")
        _env = getenv("PROJ_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{_user}:{_psswd}@{_host}/{_db}",
            pool_pre_ping=True
        )

        if _env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query the database session """
        if cls:
            res = self.__session.query(cls).all()
        else:
            res = self.__session.query(Applications).all()
            res.extend(self.__session.query(JobHistory).all())
            res.extend(self.__session.query(Jobseeker).all())
            res.extend(self.__session.query(Jobs).all())
            res.extend(self.__session.query(Recruiter).all())
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in res}

    def new(self, obj):
        """
        Add obj to the current database session
        If obj is a Recruiter object, hash the password before adding it.
        """
        if (isinstance(obj, Recruiter) or isinstance(obj, Jobseeker)) and \
                obj.password:
            # print("hashing the password{}".format(obj.password))
            obj.password = self.hash_password(obj.password)

        self.__session.add(obj)

    def save(self):
        """ Commits all changes to current database session """
        # print("session commit called!!")
        # self.__session.commit()
        try:
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise e

    def roll_back(self):
        """ Rollback in case of any database errors """
        self.__session.rollback()

    def delete(self, obj=None):
        """ Delete obj from the current database session if ! None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database
            Creates the current database session(self.__session)
                from self.__engine
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ call remove() method on the private session attribute
            (self.__session) tips or close()
            on the class Session tips
        """
        self.__session.close()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        if cls is None:
            return len(self.all())
        else:
            return len(self.all(cls))

    def search_by_attribute(self, cls, attribute, value):
        """
        Returns a list of objects of class `cls` that match the
        given attribute and value
        """
        if not hasattr(cls, attribute):
            return []  # Attribute doesn't exist in the class

        query = self.__session.query(cls).filter(
            getattr(cls, attribute) == value).all()
        return query

    def get_by_attribute(self, attribute, value):
        """
        Returns an object of class `cls` that matches the given attribute
        """
        for cls in classes.values():
            if hasattr(cls, attribute):
                query = self.__session.query(cls).filter(
                    getattr(cls, attribute) == value).first()
                if query:
                    return query
        return None

    def get_by_username(self, username):
        """
        Returns the Recruiter or Jobseeker object based on the username,
        or None if not found
        """
        user = self.__session.query(Recruiter).filter_by(
            username=username).first()
        if not user:
            user = self.__session.query(Jobseeker).filter_by(
                username=username).first()
        return user

    def get_by_token(self, token):
        """
        Returns the Recruiter or Jobseeker object based on the token,
        or None if not found
        """
        user = self.__session.query(Recruiter).filter_by(
            token=token).first()
        if not user:
            user = self.__session.query(Jobseeker).filter_by(
                token=token).first()
        return user

    def get_by_id(self, id):
        """
        Returns the Recruiter or Jobseeker object based on the id,
        or None if not found
        """
        user = self.__session.query(Recruiter).filter_by(
            id=id).first()
        if not user:
            user = self.__session.query(Jobseeker).filter_by(
                id=id).first()
        return user

    def hash_password(self, password):
        """
        Hashes the provided password using Werkzeug's hashing algorithm.
        """
        return generate_password_hash(password)

    def verify_password(self, username, password):
        """
        Verifies the password for a user given their username
        """
        user = self.get_by_username(username)

        if user:
            if isinstance(user, Recruiter) and \
                    user.check_password(password):
                return user
            elif isinstance(user, Jobseeker) and \
                    user.check_password(password):
                return user
            else:
                return None
        return None
