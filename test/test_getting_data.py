from unittest import TestCase
from getting_data.get_data import GettingData

class TestGettingData(TestCase):

    def setUp(self):
        self.getting_data_obj = GettingData("sample_input1.txt")

    def test_get_emblems_dict(self):
        self.assertIsInstance(self.getting_data_obj.get_emblems_dict(), dict)

    def test_get_input_data(self):
        self.assertIsInstance(self.getting_data_obj.get_input_data(), list)