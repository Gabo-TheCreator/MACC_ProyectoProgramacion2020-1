from MainManager import MainManager
from Constantes import Constants

mainManager = MainManager(Constants.generalSettings.screenWidth, Constants.generalSettings.screenHeight)
mainManager.initMainMenu()
mainManager.startGameSession()

#Bloque principal del juego

#Para sesiones de prueba, se cambia el .init--- dependiendo de la pantalla que se desee probar