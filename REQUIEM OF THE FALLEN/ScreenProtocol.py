

class ScreenProtocol:

    def __init__(self):
        raise NotImplementedError("__init__ Needs to be implemented in all subclasses")

    def loadView(self):
        raise NotImplementedError("loadView Needs to be implemented in all subclasses")

    def loadData(self):
        raise NotImplementedError("loadData Needs to be implemented in all subclasses")
#Comprobante de que las funciones necesitadas están definidas