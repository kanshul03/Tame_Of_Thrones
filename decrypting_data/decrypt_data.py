from decrypting_data.decrypt_data_interface import DataDecryptionInterface
from constants.constants import Constants
from Interface import implements


# This class is used to decrypt the secret message.
class DataDecryption(implements(DataDecryptionInterface)):

    # This function decrypts a list containing each character of the secret message and returns a list containing
    # decrypted characters.
    def decrypt(self, key, secret_msg):
        secret_msg = [chr(ord(i) - key) if (ord(i) - key) in range(Constants.staticAsciiValueOfA,
                                                                   Constants.staticAsciiValueOfZ)
                      else chr(ord(i) - key + Constants.staticTotalAlphabets) for i in secret_msg]
        return secret_msg
