import pygame
from enums import Enums
from Constantes import Constants
from MainMenu import MainMenu
from about import About
from introduction import Introduction
from inGame import InGame
from Common import *
from pygame_functions import *
from IngameConstantes import *
#Centro de control del juego

class MainManager:
    screen: pygame.surface = None
    screenState: Enums.Screens = None
    session: bool = None

    def __init__(self, width=0, height=0):
        # Initialize the screen
        pygame.init()
        pygame.mixer.init()
        #Se inicializa el "mixer" que reproduce cualquier audio
        self.session = True
        #Define que el juego está activo

        self.screen = screenSize(width, height)
        #self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(Constants.generalSettings.screenTitle)


    def initMainMenu(self):
        print("set .mainMenu as actual screen")
        self.screenState = Enums.Screens.mainMenu

    def initSelectName(self):
        print("set .selectName as actual screen")
        self.screenState = Enums.Screens.selectName

    def initAbout(self):
        print("set .about as actual screen")
        self.screenState = Enums.Screens.about

    def initIntroduction(self):
        print("set .about as actual screen")
        self.screenState = Enums.Screens.introduction

    def initInGame(self):
        print("set .inGame as actual screen")
        self.screenState = Enums.Screens.inGame

    #Al invocar cualquiera de estas funciones, se redirige a la pantalla a la que está vinculada

    def startGameSession(self):
        while self.session:
            thisState = self.screenState
            thisWindow = self.screen
            screens = Enums.Screens

            if thisState == screens.none:
                self.finishGameSession()
            elif thisState == screens.mainMenu:
                mainMenu = MainMenu(thisWindow, self)
                mainMenu.loadView()
            #Se inicia el menú principal
            elif thisState == screens.selectName:
                print("Select name - load view")
            # Se inicia la pantalla de selección de nombre (no implementada)
            elif thisState == screens.introduction:
                print("introduction - load view")
                introduction = Introduction(thisWindow, self)
                introduction.loadView()
            # Se inicia la pantalla de introducción
            elif thisState == screens.about:
                print("About - load view")
                about = About(thisWindow, self)
                about.loadView()
                print("Session finished")
            # Se inicia la pantalla de créditos
            elif thisState == screens.confirmExit:
                print("Confirm exit - load view")
            elif thisState == screens.inGame:
                ingame = InGame(wn, self)
                ingame.loadView()
            # Se inicia el juego

            # Update the screen each time the "While session" do a loop
            pygame.display.update()

    def finishGameSession(self):
        print("Closing at screen ~> {0}".format(self.screenState))
        self.session = False
    #Al invocarse, cierra el juego
