from checking_data.check_data_interface import CheckAllianceInterface
from constants.constants import Constants
from Interface import implements


# This class is used to check whether the required conditions for alliance are met or not.
class CheckAlliance(implements(CheckAllianceInterface)):

    # This function will check if all the animal name character are present in the secret message after decoding it.
    # For that purpose it will use occurrence_count, if any element of occurrence_count is positive that means either
    # a character is not present in the secret message or its count is less than required in the message. If all values
    # are less then or equal to zero in occurrence_count then it will append that kingdom name to the allies list.
    def check_message(self, allies, occurrence_count, kingdom):
        if (all(char <= Constants.staticRequiredCharValue for char in occurrence_count)) and kingdom not in allies:
            allies.append(kingdom)
        return allies

    # This function will check if the required condition of majority for winning(i.e, at least 3 allies) is met or not,
    # If 3 allies are not there, then it will return "None", otherwise it will return the name of "SPACE" kingdom with
    # that of allies kingdoms in a single line, separated by space.
    def check_allies(self, allies):
        if len(allies) < Constants.staticMinimumAllies:
            return Constants.staticLosingResult
        else:
            return Constants.staticWinningResult + " ".join(allies)
