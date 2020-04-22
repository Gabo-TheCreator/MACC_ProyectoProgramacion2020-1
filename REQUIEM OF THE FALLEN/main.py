from MainManager import MainManager
from Constantes import Constants

mainManager = MainManager(Constants.generalSettings.screenWidth,
                          Constants.generalSettings.screenHeight)
#mainManager.initMainMenu()
#mainManager.initAbout()
mainManager.initIntroduction()
mainManager.startGameSession()
