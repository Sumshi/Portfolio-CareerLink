#!/usr/bin/python3
""" defines the base model for all classes """
import base64
from datetime import datetime, timedelta
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import urandom
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            # self.updated_at = datetime.utcnow()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, include_password=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if include_password is None or include_password is False:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)

    def set_password(self, password, new_obj=None):
        """
        Sets the password hash for the object only for updated password
        """
        if hasattr(self, 'password') and \
                (new_obj is None or new_obj is False):
            self.password = generate_password_hash(password)

    def check_password(self, password):
        """ Verifies the object's password """
        if hasattr(self, 'password'):
            return check_password_hash(self.password, password)
        return False

    def get_token(self, expires_in=3600):
        """
        Returns a token for the object. The token is generated as a random
        string that is encoded in base64
        """
        from models import storage
        now = datetime.utcnow()
        if hasattr(self, 'token') and hasattr(self, 'token_expiration'):
            if self.token and self.token_expiration > now + timedelta(seconds=60):
                return self.token
            token = base64.b64encode(urandom(24)).decode('utf-8')
            token_expiration = now + timedelta(seconds=expires_in)
            setattr(self, "token", token)
            setattr(self, "token_expiration", token_expiration)
            storage.save()
            return self.token

    def revoke_token(self):
        """
        Makes the token currently assigned to the object invalid, simply
        by setting the expiration date to one second before the current time
        """
        if hasattr(self, 'token_expiration'):
            setattr(self, "token_expiration",
                    datetime.utcnow() - timedelta(seconds=1))
