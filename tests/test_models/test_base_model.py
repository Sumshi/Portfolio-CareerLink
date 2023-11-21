#!/usr/bin/python3
""" Module test_base_model """
from models.base_model import BaseModel
from models import base_model
import unittest
import datetime
from uuid import UUID
import json
import pep8


class test_basemodel(unittest.TestCase):
    """ Defines test cases for the BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Initialize a BaseModel class used in the tests """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_default(self):
        """default testing of base class """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ test instance creation from kwargs dictionary """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ tests the type of values passed in kwargs """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skip('file storage not suported')
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ test string representation of class """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ test the to_dict method of class """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ test that wrong key and val in kwargs raises TypeError """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ tests that only attributes in class are updated """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertTrue('Name' in new.to_dict())

    def test_id(self):
        """ test that the id attribute is a string obj """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test that the created_at attribute is a datetime obj"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test the created_at time is different from updated_at time """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        # new = BaseModel(**n)
        # self.assertFalse(new.created_at == new.updated_at)

    def test_documentation(self):
        """
        Test module documentation
        """
        self.assertGreater(len(base_model.__doc__), 3)
        self.assertGreater(len(BaseModel.__doc__), 3)
        self.assertGreater(len(BaseModel.__init__.__doc__), 3)
        self.assertGreater(len(self.__doc__), 3)

    def test_pep8_base_model(self):
        """
        Pep8 compliance in base_model.py
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["models/base_model.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_pep8_test_base_model(self):
        """
        Pep8 compliance in test_console.py
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tests/test_models/test_base_model.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')
