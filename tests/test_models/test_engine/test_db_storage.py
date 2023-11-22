#!/usr/bin/python3
"""
unittests for db_storage module
"""
from console import HBNBCommand
from io import StringIO
from models.engine.db_storage import DBStorage
from models.engine import db_storage
from models import storage, Jobs
from os import getenv
from models import Jobs, Recruiter
import MySQLdb
import pep8
import sys
import unittest
from unittest.mock import patch

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
        uname = getenv("PROJ_USER")
        passw = getenv("PROJ_PWD")
        dbhost = getenv("PROJ_HOST")
        dbname = getenv("PROJ_DB")
        # env = getenv("PROJ_ENV")
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

    def test_dbstorage_all(self):
        """ Test the all method of DBStorage """
        storage.reload()

        # get the initial objects
        result = storage.all(Jobs)
        cur = self.test_engine.cursor()
        cur.execute("SELECT * FROM jobs;")
        init_objs = cur.fetchall()
        self.assertTrue(len(result) == len(init_objs))

        # create a new object and commit transaction to save the new object
        # Create a new object and capture the ID printed to stdout
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd(
                'create Recruiter company="Soft dev" \
                email="info@softdev.com" phone_number="0712345675" \
                username="softdev" password="test_pwd" country="Kenya" \
                state="Nairobi" address="00311" street="Juja Rd" \
                zip_code="00200" profile_pic="present" about="Hardworking"'
            )
            self.test_engine.commit()
            # Get the printed ID
            created_output = fake_output.getvalue().strip()

        # Use the captured ID to create a Jobs object
        if created_output:
            with patch('sys.stdout', new=StringIO()):
                self.command.onecmd(
                    'create Jobs recruiters_id="{}" title="Engineer" \
                    description="good job" application="send email" \
                    company="Career Link" contact="1023456" \
                    deadline="2023-12-15" country="Kenya" \
                    town="Nairobi"'.format(created_output)
                )
                self.test_engine.commit()

                # Retrieve the data
                cur.execute("SELECT * FROM jobs;")
                new_objs = cur.fetchall()
                result = storage.all(Jobs)

                # Confirm the results
                self.assertTrue(len(result) == len(new_objs))
                self.assertIsInstance(result, dict)
        else:
            # Handle the case where the ID couldn't be captured
            self.fail("Failed to capture the ID of the created object")

    def test_dbstorage_new(self):
        """ Test the new method of DBStorage """
        storage.reload()

        # confirm that no data in the tables
        cur = self.test_engine.cursor()
        cur.execute("SELECT * FROM recruiters;")
        objs = cur.fetchall()
        self.assertTrue(len(objs), 0)

        # create a new object
        new_obj = Recruiter(
            company="Soft dev", email="info@softdev.com",
            phone_number="0712345675", username="softdev",
            password="test_pwd", country="Kenya", state="Nairobi",
            address="00311", street="Juja Rd", zip_code="00200",
            profile_pic="present", about="Hardworking"
        )
        storage.new(new_obj)
        self.test_engine.commit()
        cur.execute("SELECT * FROM recruiters;")
        objs = cur.fetchall()
        self.assertGreater(len(objs), 0)

    def test_dbstorage_delete(self):
        """ Test the delete method of DBStorage """
        storage.reload()

        # create new object and update
        new_obj = Recruiter(
            company="Electromag", email="info@elemag.com",
            phone_number="0712345691", username="emag",
            password="test_pwd_1", country="Kenya", state="Nairobi",
            address="00312", street="Juja Rd", zip_code="00200",
            profile_pic="present", about="Electrical installation"
        )
        storage.new(new_obj)
        storage.save()
        self.test_engine.commit()

        # confirm object added to the database
        cur = self.test_engine.cursor()
        cur.execute("SELECT * FROM recruiters;")
        objs = cur.fetchall()
        self.assertTrue(len(objs), 1)

        # delete the object and confirm no objects
        storage.delete(new_obj)
        self.test_engine.commit()
        cur.execute("SELECT * FROM recruiters;")
        objs = cur.fetchall()
        self.assertTrue(len(objs), 0)

    def test_relationship(self):
        """ Test relationship in DBStorage """
        storage.reload()
        # create Recruiter object
        recruiter = Recruiter(
            company="Builders", email="info@builders.com",
            phone_number="0722345691", username="builders",
            password="test_pwd_2", country="Kenya", state="Nairobi",
            address="00313", street="Juja Rd", zip_code="00200",
            profile_pic="present", about="Civil engineers"
        )
        storage.new(recruiter)
        storage.save()
        # self.test_engine.commit()
        recruiter_id = recruiter.id

        # update the Recruiter relationship backref
        job_1 = Jobs(
            recruiters_id=recruiter_id, title="Engineer",
            description="good job", application="send email",
            company="Builders", contact="0722345691",
            deadline="2023-12-15", country="Kenya", town="Nairobi"
        )
        storage.new(job_1)
        job_2 = Jobs(
            recruiters_id=recruiter_id, title="Technician",
            description="good job", application="send email",
            company="Builders", contact="0722345691",
            deadline="2023-12-15", country="Kenya", town="Nairobi"
        )
        storage.new(job_2)
        self.test_engine.commit()

    #     print("create a new city object")

    #     # city1 = City(name="San_Jose", state_id=state_id)
    #     # storage.new(city1)
    #     # city1_id = city1.id
    #     # city2 = City(name="San_Francisco", state_id=state_id)
    #     # storage.new(city2)
    #     # city2_id = city2.id
    #     storage.new(state)

    #     storage.save()

        # confirm jobs table updated
        cur = self.test_engine.cursor()
        cur.execute("SELECT * FROM jobs;")
        job_lists = cur.fetchall()
        self.assertTrue(len(job_lists), 2)

        # check the relationship
        print("display the relationships")
        job_listing = recruiter.job_listings
        self.assertIn(job_1, job_listing)
        self.assertIn(job_2, job_listing)

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
