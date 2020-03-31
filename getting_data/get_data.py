from getting_data.get_data_interface import GettingDataInterface
from constants.constants import Constants
from interface import implements
import sys
import json


# This class is used to read various data from different files.
class GettingData(implements(GettingDataInterface)):

    # Initializing the path of configuration file through constructor.
    def __init__(self, input_file_path):
        self.__config_file_path = Constants.staticConfigFilePath
        self.__input_file_path = input_file_path

    # This function is used to read the key - value pair of kingdom and their respective animal from the json file
    # and return them.
    def get_emblems_dict(self):
        try:
            with open(self.__config_file_path) as f:
                file = json.load(f)
            return file[Constants.staticEmblems]
        except:
            print("Oops!", sys.exc_info()[0], " error occurred while reading configuration file.")
            sys.exit(-1)

    # This function is used to read all the input text from the input text file and returns a list with each line
    # of the input file as element of the list.
    def get_input_data(self):
        try:
            with open(self.__input_file_path, "r") as f:
                text = f.readlines()
            return text
        except:
            print("Oops!", sys.exc_info()[0], " error occurred while reading input text file.")
            sys.exit(-1)
