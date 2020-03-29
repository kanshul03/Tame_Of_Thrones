from unittest import TestCase
from counting_occurrences.count_occurrence import CountingOccurrence
from constants.constants import Constants


class TestCountingOccurrence(TestCase):

    def setUp(self):
        self.counting_occurrence_obj = CountingOccurrence()
        self.occurrence_count = [Constants.staticDefaultCountValue] * Constants.staticTotalAlphabets

    def test_animal_character_occurrence(self):
        assert sum(self.counting_occurrence_obj.animal_character_occurrence("OWL", self.occurrence_count)) > 0

    def test_message_character_occurrence(self):
        assert sum(self.counting_occurrence_obj.message_character_occurrence("OLWO", self.occurrence_count)) < 0
