import unittest
from datetime import datetime
from models import *


class Test_PlaceModel(unittest.TestCase):
    """
    Test the place model class
    """

    def test_simple_initialization(self):
        """initialization without arguments"""
        model = Place()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "city_id"))
        self.assertTrue(hasattr(model, "user_id"))
        self.assertTrue(hasattr(model, "name"))
        self.assertTrue(hasattr(model, "description"))
        self.assertTrue(hasattr(model, "number_rooms"))
        self.assertTrue(hasattr(model, "number_bathrooms"))
        self.assertTrue(hasattr(model, "max_guest"))
        self.assertTrue(hasattr(model, "price_by_night"))
        self.assertTrue(hasattr(model, "latitude"))
        self.assertTrue(hasattr(model, "longitude"))

    def test_var_initialization(self):
        """Check default type"""
        model = Place()
        self.assertIsInstance(model.created_at, datetime)

if __name__ == "__main__":
    unittest.main()
