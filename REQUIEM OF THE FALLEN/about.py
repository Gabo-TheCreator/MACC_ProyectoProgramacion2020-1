from ScreenProtocol import ScreenProtocol

class About(ScreenProtocol):

    def __init__(self):
        print("Init")

    def loadScreen(self):
        print("loadScreen")