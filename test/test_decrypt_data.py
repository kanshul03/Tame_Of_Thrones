from unittest import TestCase
from decrypting_data.decrypt_data import DataDecryption


class TestDataDecryption(TestCase):

    def setUp(self):
        self.data_decryption_obj = DataDecryption()

    def test_decrypt(self):
        self.assertEqual(self.data_decryption_obj.decrypt(5, "FAIJWJSOOFAMAU"), list("AVDERENJJAVHVP"))


# if __name__ == '__main__':
#     unittest.main()
