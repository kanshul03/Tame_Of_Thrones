from interface import Interface


class CountingOccurrenceInterface(Interface):
    def animal_character_occurrence(self, animal_name, occurrence_count):
        raise NotImplementedError

    def message_character_occurrence(self, secret_msg, occurrence_count):
        raise NotImplementedError
