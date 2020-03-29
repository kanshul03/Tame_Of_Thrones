from Interface import Interface


class GettingDataInterface(Interface):
    def get_emblems_dict(self):
        raise NotImplementedError

    def get_input_data(self):
        raise NotImplementedError