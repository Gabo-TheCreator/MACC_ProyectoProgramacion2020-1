from MainManager import MainManager
from Constantes import Constants

mainManager = MainManager(Constants.generalSettings.screenWidth, Constants.generalSettings.screenHeight)
mainManager.initInGame()
mainManager.startGameSession()