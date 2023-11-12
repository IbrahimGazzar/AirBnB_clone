#!/usr/bin/python3
"""
This unit test module is used for tests regarding
the file storage class and its functionalities
"""
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import os
import unittest


class TestStorage(unittest.TestCase):
    """
    This class contains the tests for the file storage
    class
    """
    def setUp(self):
        """
        Set up function for all the needed tests
        """
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_storage_1_init(self):
        """
        Tests whether base models are saved correctly in the
        json file or not
        """
        self.assertIsInstance(storage.all(), dict)
        self.assertNotEqual(len(storage.all()), 0)
        for name, dicti in storage.all().items():
            self.assertRegex(name, '^BaseModel')
            self.assertTrue('__class__' in dicti)
            self.assertTrue('updated_at' in dicti)
            self.assertTrue('created_at' in dicti)
            self.assertTrue('id' in dicti)

    def test_storage_2_save(self):
        """
        Tests if the base model's save function correctly calls
        FileStorage's save function
        """
        dict_dicts = storage.all()
        self.bm1.save()
        self.assertTrue(os.path.exists("file.json"))
        storage.reload()
        self.assertEqual(dict_dicts, storage.all())
        bm3 = BaseModel(**(self.bm1.to_dict()))
        bm3.save()
        storage.reload()
        self.assertEqual(dict_dicts, storage.all())
        bm4 = BaseModel()
        bm4.save()
        storage.reload()
        self.assertNotEqual(dict_dicts, storage.all())

    def TearDown(self):
        """
        Deletes objects after testing
        """
        del self.bm1
        del self.bm2
        if os.path.exists("file.json"):
            os.remove("file.json")
