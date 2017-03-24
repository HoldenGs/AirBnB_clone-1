import unittest
from datetime import datetime
from models import *


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        self.model = Amenity()
        self.model.name = 'Wifi!'
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "Wifi!")

    def tearDown(self):
        self.model.delete()


if __name__ == "__main__":
    unittest.main()
