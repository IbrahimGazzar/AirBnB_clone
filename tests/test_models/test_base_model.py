#!/usr/bin/python3
"""
Unittest module used for testing the BaseModel class
"""

from datetime import datetime
from models.base_model import BaseModel
from models import storage
import os
import unittest


class TestBase(unittest.TestCase):
    """
    The class used for all tests relating the BaseModel
    class
    """
    def setUp(self):
        """
        Set up function for all the needed tests
        """
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_base_1_create(self):
        """
        Tests whether base objects are created correctly
        or not
        """
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertTrue(hasattr(self.bm1, "created_at"))
        self.assertTrue(hasattr(self.bm1, "updated_at"))
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertIsInstance(self.bm1.id, str)
        self.assertIsInstance(self.bm1.created_at, datetime)
        self.assertIsInstance(self.bm1.updated_at, datetime)

    def test_base_2_save(self):
        """
        Tests the save function's updation of the updated_at
        attribute of base model
        """
        datte1 = self.bm1.updated_at
        self.bm1.save()
        self.assertNotEqual(datte1, self.bm1.updated_at)
        datte2 = self.bm2.updated_at
        self.bm2.save()
        self.assertNotEqual(datte2, self.bm2.updated_at)

    def test_base_3_dict(self):
        """
        Tests base model's to_dict function
        """
        dicti = self.bm1.to_dict()
        self.assertIsInstance(dicti, dict)
        self.assertNotEqual(dicti, self.bm1.__dict__)
        self.assertEqual(dicti['__class__'], "BaseModel")
        self.assertIsInstance(dicti['created_at'], str)
        self.assertIsInstance(dicti['updated_at'], str)

    def test_base_4_create_from_dict(self):
        """
        Tests the method of creating a base model
        using a dictionary extracted from another base
        model using its to_dict function
        """
        dicti = self.bm2.to_dict()
        bm3 = BaseModel(**dicti)
        self.assertIsInstance(bm3, BaseModel)
        self.assertNotEqual(self.bm2, bm3)
        self.assertEqual(self.bm2.id, bm3.id)
        self.assertEqual(self.bm2.created_at, bm3.created_at)
        self.assertEqual(self.bm2.updated_at, bm3.updated_at)

    def TearDown(self):
        """
        Deletes objects after testing
        """
        del self.bm1
        del self.bm2
        if os.path.exists("file.json"):
            os.remove("file.json")
