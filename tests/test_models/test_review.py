import unittest
from datetime import datetime
from models import *
from os import getenv


class Test_ReviewModel(unittest.TestCase):
    """
    Test the review model class
    """

    def test_var_initialization(self):
        self.model = Review()
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertEqual(self.model.place_id, None)
            self.assertEqual(self.model.user_id, None)
            self.assertEqual(self.model.text, None)
        else:
            self.assertEqual(self.model.place_id, "")
            self.assertEqual(self.model.user_id, "")
            self.assertEqual(self.model.text, "")


if __name__ == "__main__":
    unittest.main()
