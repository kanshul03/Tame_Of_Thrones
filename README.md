## To run the program -
1. Extract Zip folder.
2. Open Command Prompt(cmd).
3. Move to project folder.
4. Run the following command - 
	+ pip install -r requirements.txt

___

## To test the program -
1. Extract Zip folder.
2. Open Command Prompt(cmd).
3. Move to project folder in cmd.
4. Run the following command - 
	+ python -m unittest

___

## To check coverage of unittests -
1. Extract Zip folder.
2. Open Command Prompt(cmd).
3. Move to project folder in cmd.
4. Run the following command - 
	+ coverage run -m unittest
	+ coverage html
5. In __htmlcov__ folder, open **index.html** file. 
 
___

# About Project -

This project is used to find out if the Kingdom of Space gets the majority allegiance(at least 3) to win or not.
For that purpose, multiple subpackages named tot, getting_data, decrypting_data, counting_occurrences and checking_data are created which are then imported in the main file(geektrust.py). Some other libraries such as json, sys, os, interface are used as well in the main file and sub-packages. A constants sub-package is created where all the constant values are stored and then used in the project as per needs.
It follows OOP principles like Dependency Inversion, etc.

#### In the geektrust.py file -
1. It is checked if the file running is the main file. If yes, then -
	+ Input text file path is taken as an argument from the command line as saved in a variable.
	+ If the path exists in the OS, then the sub-packages as well as the GeekTrust class are instantiated and start_program method is called.
	+ Else, Program exits with a message that path does not exist.



#### In tot subpackage(tame_of_thrones.py) -
1. Class TameOfThrones implements TameOfThronesInterface
2. An empty list is created in which all the allies will be added if the secret message for that kingdom meets the criteria.
3. Using getting_data subpackage's get_data module, we get the key-value pair of kingdom name and animal name and assign it to variable emblems.
4. Also using getting_data subpackage's get_data module, we get the data from the input text file and save it as a list in a variable named text.
5. A for loop is used to iterate over each element of the text, i.e., over each message.
	+ First, the next-line character ("\n") is removed.
	+ Then, the line input is separated into two parts, mainly kingdom name and the secret message sent to that kingdom.
	+ Kingdom name of the current element from text is assigned to the variable kingdom.
	+ A list containing each character of secret message for the current kingdom is assigned to variable secret_msg.
	+ secret_msg list is filtered out to remove any spaces if present.
	+ Animal name of the current kingdom is assigned to variable animal_name using the emblems dict created earlier.
	+ Key for decrypting secret message is assigned to variable key.
	+ Using the decrypting_data subpackage, each element of secret_msg is decrypted and stored back in secret_msg
	+ A list of length 26 with every element as default 0 is created to keep a check of character occurrences count and assigned to variable occurrence_count.
	+ Using counting_occurrences subpackage, character's value in animal name is incremented in occurrence_count while character's value in secret_msg is decremented.
	+ Using checking_data subpackage, it is checked if the current kingdom will become an ally or not.
6. At last, also using checking_data subpackage, it is checked it the Space kingdom have enough allies or not and the result is returned accordingly.



#### In getting_data subpackage (get_data.py) -
1. Function get_emblems_dict opens the configuration(config.json) file whose path is defined in the constructor, and gives out the value of emblems key from the json file. The value emblems key in the json file is a pre-defined dictionary with kingdom names as keys and their respective animals names as values.

2. Function get_input_data opens the input text file(test.txt) whose path is initialized through constructor and read all the data inside the file and return a list with each line in the file as an element of the list.



#### In decrypting subpackage (decrypt_data.py) -
1. Function decrypt takes parameter key and secret_msg and decrypt each element of the secret_msg using the key. For the decryption process, secret_msg character is rotated key positions in anti-clock wise direction on a wheel of alphabets to find the corresponding decrypted character.



#### In counting_occurrences subpackage (count_occurrence.py) -
This subpackage basically deals with a character occurrence count list named occurrence_count. This list is of length 26 with each index representing an alphabet from A-Z corresponding to 0-26. Default count for each alphabet is 0.

1. Function animal_character_occurrence takes animal name and occurrence_count as arguments and then for each character in animal name, it increases the count of character in the occurrence_count list.

2. Function message_character_occurrence takes secret_msg and occurrence_count as arguments and then for each character in secret_msg, it decreases the count of character in the occurrence_count list.



#### In checking_data subpackage (check_data.py) -
1. Function check_message takes allies list, occurrence_count list and kingdom name as arguments and checks if all the values/count in the occurrence_count list are less than equal to 0. If they are, then it means that all the characters in the animal name are present in the decrypted message as well, and hence it will add the kingdom name to the allies list.

2. Function check_allies takes allies list as argument and checks if at least 3 allies are present in the list. If number of allies are less then 3, then it returns a string "None", else it will return a string consisting of "SPACE" as well as other ally kingdom's names in a single line, separated with spaces.



#### In constants subpackage (constants.py) -
1. All the constant values that are used across the project are saved here as static variables and then later are called in the places as per required.



#### In the test subpackage - 
1. Unit tests for all the subpackages are created and stored in this subpackage.