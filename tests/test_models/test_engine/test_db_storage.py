#!/usr/bin/python3
"""
unittests for db_storage module
"""
import unittest
from models.engine.db_storage import DBStorage
from models.engine import db_storage
from models import storage, Jobs
from os import getenv
from models import Jobs, Recruiter
from console import HBNBCommand
import MySQLdb
import pep8

# db = getenv("HBNB_TYPE_STORAGE")


class test_my_storage(unittest.TestCase):
    """
    Testing my_storage class

    Args:
        unittest (_type_): _description_
    """

    @classmethod
    def setUpClass(cls):
        """ Set up test environment """
        cls.my_storage = DBStorage()
        cls.command = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """ Tear down the test environment
        """
        del cls.my_storage

    def setUp(self):
        """ create a MySQLdb connection """
        uname = 'admin_test'
        passw = 'careerLink_password_test'
        dbhost = 'localhost'
        dbname = 'careerLink_DB_test'
        self.test_engine = MySQLdb.connect(
            host=dbhost,
            user=uname,
            password=passw,
            database=dbname
        )

    def tearDown(self):
        """ close the db connection """
        self.test_engine.close()

    def test_my_storage_methods(self):
        """
            Check methods exists
        """
        self.assertTrue(hasattr(self.my_storage, "all"))
        self.assertTrue(hasattr(self.my_storage, "__init__"))
        self.assertTrue(hasattr(self.my_storage, "new"))
        self.assertTrue(hasattr(self.my_storage, "save"))
        self.assertTrue(hasattr(self.my_storage, "delete"))
        self.assertTrue(hasattr(self.my_storage, "reload"))

    def test_model_storage(self):
        """ Test storage is an instance of DBStorage """
        self.assertTrue(isinstance(storage, DBStorage))

    def test_create(self):
        """ Test adding a new object """
        # initialize sqlalchemy connection
        storage.reload()

        # get the initial objects
        cur = self.test_engine.cursor()
        cur.execute("SELECT * FROM recruiters;")
        init_objs = cur.fetchall()

        # create a new object and commit transaction to save the new object
        self.command.onecmd(
            'create Recruiter company="Career Link" \
            email="info@careerlink.com" phone_number="0712345678" \
            username="CareerLink" password="test_pwd" country="Kenya" \
            state="Nairobi" address="00111" street="Komarock Rd" \
            zip_code="00100" profile_pic="present" about="Hardworking"'
        )
        self.test_engine.commit()

        # Retrieve the data
        cur.execute("SELECT * FROM recruiters;")
        new_objs = cur.fetchall()

        # Confirm the results
        self.assertTrue(len(new_objs) > len(init_objs))

    def test_new_obj(self):
        """ Test that a new object is created """
        new_obj = Jobs()
        self.assertTrue(new_obj)
        self.assertTrue(hasattr(new_obj, 'id'))
        self.assertTrue(hasattr(new_obj, 'updated_at'))
        self.assertTrue(hasattr(new_obj, 'created_at'))

    # def test_dbstorage_all(self):
    #     """ Test the all method of DBStorage """
    #     storage.reload()

    #     # get the initial objects
    #     result = storage.all()
    #     cur = self.test_engine.cursor()
    #     cur.execute("SELECT * FROM jobs;")
    #     init_objs = cur.fetchall()
    #     self.assertTrue(len(result) == len(init_objs))

    #     # create a new object and commit transaction to save the new object
    #     self.command.onecmd(
    #         'create Jobs recruiter_id="6789" title="Engineer"\
    #         description="good job" application="send email"\
    #         comapny="Career Link" contact="1023456" deadline="25-12-2023"\
    #         country="Kenya" town="Nairobi"'
    #     )
    #     self.test_engine.commit()

    #     # Retrieve the data
    #     cur.execute("SELECT * FROM jobs;")
    #     new_objs = cur.fetchall()
    #     result = storage.all()

    #     # Confirm the results
    #     self.assertTrue(len(result) == len(new_objs))
    #     self.assertIsInstance(result, dict)

    # def test_dbstorage_new(self):
    #     """ Test the new method of DBStorage """
    #     storage.all()

    #     # confirm that no data in the tables
    #     cur = self.test_engine.cursor()
    #     cur.execute("SELECT * FROM jobs;")
    #     objs = cur.fetchall()
    #     self.assertTrue(len(objs), 0)

    #     # create a new object
    #     new_obj = Jobs(
    #         recruiter_id="6789", title="Engineer", description="good job",
    #         application="call", comapny="Career Link", contact="1023456",
    #         deadline="25-12-2023", country="Kenya", town="Nairobi"
    #     )
    #     storage.new(new_obj)
    #     cur.execute("SELECT * FROM jobs;")
    #     objs = cur.fetchall()
    #     self.assertGreater(len(objs), 0)

    # def test_dbstorage_delete(self):
    #     """ Test the delete method of DBStorage """
    #     storage.all()

    #     # create new object and update
    #     state = Jobs(name="California")
    #     storage.new(state)
    #     storage.save()

    #     # confirm object added to the database
    #     cur = self.test_engine.cursor()
    #     cur.execute("SELECT * FROM states;")
    #     objs = cur.fetchall()
    #     self.assertTrue(len(objs), 1)

    #     # delete the object and confirm no objects
    #     storage.delete(state)
    #     cur.execute("SELECT * FROM states;")
    #     objs = cur.fetchall()
    #     self.assertTrue(len(objs), 0)

    # def test_dbstorage_repr(self):
    #     """ Test that objects are saved as a dict """
    #     storage.reload()

    #     # create objects
    #     state = Jobs(name="California")
    #     storage.new(state)
    #     storage.save()
    #     key = "{}.{}".format(state.__class__.__name__, state.id)
    #     objs = storage.all()
    #     self.assertIsInstance(objs, dict)
    #     self.assertIs(objs[key], state)

    # def test_relationship(self):
    #     """ Test relationship in DBStorage """
    #     state = Jobs(name="California")
    #     state_id = state.id
    #     state.cities = [
    #         City(name="San_Jose", state_id=state_id),
    #         City(name="San_Francisco", state_id=state_id)
    #     ]

    #     print("create a new city object")

    #     # city1 = City(name="San_Jose", state_id=state_id)
    #     # storage.new(city1)
    #     # city1_id = city1.id
    #     # city2 = City(name="San_Francisco", state_id=state_id)
    #     # storage.new(city2)
    #     # city2_id = city2.id
    #     storage.new(state)

    #     storage.save()

    #     # confirm cities table updated
    #     cur = self.test_engine.cursor()
    #     cur.execute("SELECT * FROM cities;")
    #     cities = cur.fetchall()
    #     self.assertTrue(len(cities), 2)

    #     # check the relationship
    #     # print("display the relationships")
    #     # state_cities = state.cities
    #     # self.assertIn(city1, state_cities)
    #     # self.assertIn(city2, state_cities)

    def test_documentation(self):
        """
        Test module documentation
        """
        self.assertGreater(len(db_storage.__doc__), 3)
        self.assertGreater(len(DBStorage.__doc__), 3)
        self.assertGreater(len(DBStorage.close.__doc__), 3)
        self.assertGreater(len(DBStorage.all.__doc__), 3)
        self.assertGreater(len(DBStorage.delete.__doc__), 3)
        self.assertGreater(len(DBStorage.new.__doc__), 3)
        self.assertGreater(len(DBStorage.reload.__doc__), 3)
        self.assertGreater(len(DBStorage.save.__doc__), 3)
        self.assertGreater(len(DBStorage.__init__.__doc__), 3)
        self.assertGreater(len(self.__doc__), 3)

    def test_pep8_db_storage(self):
        """
        Pep8 compliance in db_storage.py
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["models/engine/db_storage.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_pep8_test_db_storage(self):
        """
        Pep8 compliance in test_db_storage.py
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tests/test_models/test_engine/test_db_storage.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')
