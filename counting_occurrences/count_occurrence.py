from counting_occurrences.count_occurrence_interface import CountingOccurrenceInterface
from constants.constants import Constants
from Interface import implements
import sys


# This class is used to update the character occurrence count list(occurrence_count).
# occurrence_count is basically a list of length 26, denoting all alphabets with a default value of 0, which means the
# character hasn't occurred anywhere yet. If a character occurs in animal name, we give it's value an increment.
# If it occurs in decrypted message, then we give it's value a decrement. In the end, if all the values are zero or
# negative in character occurrence count list, then it means that all the characters in the animal name has occurred
# in the decrypted message as well.
class CountingOccurrence(implements(CountingOccurrenceInterface)):

    # This function will increment the value of each character present in animal name.
    def animal_character_occurrence(self, animal_name, occurrence_count):
        try:
            for char in animal_name:
                occurrence_count[ord(char) - Constants.staticAsciiValueOfA] += 1
            return occurrence_count
        except:
            print("Oops!", sys.exc_info()[0], " error occurred due to animal name.")
            sys.exit(-1)

    # This function will decrement the value of each character present in secret message.
    def message_character_occurrence(self, secret_msg, occurrence_count):
        try:
            for char in secret_msg:
                occurrence_count[ord(char) - Constants.staticAsciiValueOfA] -= 1
            return occurrence_count
        except:
            print("Oops!", sys.exc_info()[0], " error occurred due to decrypted message.")
            sys.exit(-1)
