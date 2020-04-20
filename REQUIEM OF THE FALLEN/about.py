from ScreenProtocol import ScreenProtocol

class About(ScreenProtocol):

    def __init__(self):
        print("Init")

    def loadView(self):
        print("loadView")

    def loadData(self):
        print("loadData")