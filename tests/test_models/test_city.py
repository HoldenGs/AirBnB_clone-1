import unittest
from datetime import datetime
from models import *


class Test_CityModel(unittest.TestCase):
    """
    Test the city model class
    """

    def setUp(self):
        self.state = State()
        self.state.name = 'whatever'
        self.state.save()

        self.model = City()
        self.model.name = 'Tallahassee'
        self.model.state_id = self.state.id
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertEqual(self.model.name, 'Tallahassee')
        self.assertEqual(self.model.state_id, self.state.id)

    def tearDown(self):
        self.model.delete()
        self.state.delete()


if __name__ == "__main__":
    unittest.main()
