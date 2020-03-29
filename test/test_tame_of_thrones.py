from unittest import TestCase
from counting_occurrences.count_occurrence import CountingOccurrence
from decrypting_data.decrypt_data import DataDecryption
from checking_data.check_data import CheckAlliance
from getting_data.get_data import GettingData
from tot.tame_of_thrones import TameOfThrones


class TestTameOfThrones(TestCase):

    def setUp(self):
        self.getting_data_obj = GettingData("sample_input2.txt")
        self.data_decryption_obj = DataDecryption()
        self.counting_occurrence_obj = CountingOccurrence()
        self.check_alliance_obj = CheckAlliance()
        self.tame_of_thrones_obj = TameOfThrones(self.getting_data_obj, self.data_decryption_obj,
                                                 self.counting_occurrence_obj, self.check_alliance_obj)

    def test_tame_of_thrones(self):
        assert self.tame_of_thrones_obj.tame_of_thrones() == "SPACE LAND ICE FIRE"
