

class ScreenProtocol:

    def __init__(self):
        raise NotImplementedError("__init__ Needs to be implemented in all subclasses")

    def loadScreen(self):
        raise NotImplementedError("loadScreen Needs to be implemented in all subclasses")