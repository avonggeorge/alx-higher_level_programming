#!/usr/bin/python3

"""
import modules
"""

import unittest
from models.base import Base

"""
class Testbase checking for unittest cases
"""

class TestBase(unittest.TestCase):
    def setUp(self):
        self.x = Base()
        self.y = Base(56)

    def test_equalsto(self):
        self.assertEqual(self.x.id, 1)
        self.assertEqual(self.y.id, 56)

    def test_Datatype(self):
        x = Base()
        y = Base()
        self.assertNotIsInstance(x,int)
        self.assertNotIsInstance(y,int)

    def tearDown(self):
        Base._Base__nb_objects = 0

if __name__ ==  '__main__':
    unittest.main
