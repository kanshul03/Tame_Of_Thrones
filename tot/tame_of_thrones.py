from tot.tame_of_thrones_interface import TameOfThronesInterface
from constants.constants import Constants
from interface import implements


# This class is used to apply the logic of the project.
class TameOfThrones(implements(TameOfThronesInterface)):

    def __init__(self, getting_data_i, data_decryption_i, counting_occurrence_i, alliance_checking_i):
        self.__getting_data_i = getting_data_i
        self.__data_decryption_i = data_decryption_i
        self.__counting_occurrence_i = counting_occurrence_i
        self.__alliance_checking_i = alliance_checking_i

    def tame_of_thrones(self):
        allies = []                         # Empty list to append ally kingdom's names.

        emblems = self.__getting_data_i.get_emblems_dict()
        text = self.__getting_data_i.get_input_data()

        for each_line in text:              # Iterating over each message in input text.
            each_line = each_line[:-1]      # Removing new line character.
            each = each_line.split(" ", 1)  # Splitting input text into respective kingdom name and its secret message.

            kingdom = each[0]               # Assigning kingdom name to variable kingdom.

            # Making list of all characters of secret message as elements and assigning it to variable secret message.
            secret_msg = list(each[1])

            # Filtering secret_msg to remove any space present in it.
            secret_msg = filter(lambda a: a != " ", secret_msg)

            # Assigning animal name of the kingdom for which secret message is being read to variable animal_name.
            animal_name = emblems[kingdom]

            key = len(animal_name)               # Assigning the decrypting key for current kingdom to variable key.

            secret_msg = self.__data_decryption_i.decrypt(key, secret_msg)

            # Creating a character occurrence count list with default value 0 for each character.
            occurrence_count = [Constants.staticDefaultCountValue] * Constants.staticTotalAlphabets
            occurrence_count = self.__counting_occurrence_i.animal_character_occurrence(animal_name, occurrence_count)
            occurrence_count = self.__counting_occurrence_i.message_character_occurrence(secret_msg, occurrence_count)

            allies = self.__alliance_checking_i.check_message(allies, occurrence_count, kingdom)

        result = self.__alliance_checking_i.check_allies(allies)
        return result
