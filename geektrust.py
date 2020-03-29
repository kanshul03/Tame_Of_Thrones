from counting_occurrences.count_occurrence import CountingOccurrence
from checking_data.check_data import CheckAlliance
from tot.tame_of_thrones import TameOfThrones
from decrypting_data.decrypt_data import DataDecryption
from getting_data.get_data import GettingData
import sys
import os


# Main class.
class GeekTrust:

    def __init__(self, tame_of_thrones_i):
        self.__tame_of_thrones_i = tame_of_thrones_i

    def start_program(self):
        result = self.__tame_of_thrones_i.tame_of_thrones()
        print(result)


if __name__ == "__main__":
    input_file_path = sys.argv[1]                           # Command line argument for taking path of input text file.
    if os.path.exists(input_file_path):
        getting_data_obj = GettingData(input_file_path)     # Initializing all the modules.
        counting_occurrence_obj = CountingOccurrence()
        data_decryption_obj = DataDecryption()
        alliance_checking_obj = CheckAlliance()
        tame_of_thrones_obj = TameOfThrones(getting_data_i=getting_data_obj, data_decryption_i=data_decryption_obj,
                                            counting_occurrence_i=counting_occurrence_obj,
                                            alliance_checking_i=alliance_checking_obj)
        geek_trust_obj = GeekTrust(tame_of_thrones_i=tame_of_thrones_obj)
        geek_trust_obj.start_program()
    else:
        print("Path not exist.")
        sys.exit(-1)
