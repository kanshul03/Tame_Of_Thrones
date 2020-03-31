from interface import Interface


class DataDecryptionInterface(Interface):
    def decrypt(self, key, secret_msg):
        raise NotImplementedError
