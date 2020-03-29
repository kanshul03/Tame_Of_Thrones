from Interface import Interface


class CheckAllianceInterface(Interface):
    def check_message(self, allies, occurrence_count, kingdom):
        raise NotImplementedError

    def check_allies(self, allies):
        raise NotImplementedError
