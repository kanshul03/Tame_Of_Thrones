from unittest import TestCase
from counting_occurrences.count_occurrence import CountingOccurrence
from checking_data.check_data import CheckAlliance
from constants.constants import Constants


class TestCheckAlliance(TestCase):

    def setUp(self):
        self.counting_occurrence_obj = CountingOccurrence()
        self.occurrence_count = [Constants.staticDefaultCountValue] * Constants.staticTotalAlphabets
        self.counting_occurrence_obj.animal_character_occurrence("PANDA", self.occurrence_count)
        self.counting_occurrence_obj.message_character_occurrence("AVDERENJJAVHVP", self.occurrence_count)
        self.check_alliance_obj = CheckAlliance()
        self.allies = ['ICE', 'FIRE']
        self.kingdom = 'LAND'

    def test_check_message(self):
        assert len(self.check_alliance_obj.check_message(self.allies, self.occurrence_count, self.kingdom)) == 3

    def test_check_alliance(self):
        assert self.check_alliance_obj.check_allies(self.allies) == Constants.staticLosingResult
