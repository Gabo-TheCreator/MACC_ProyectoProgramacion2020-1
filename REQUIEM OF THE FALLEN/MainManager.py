import pygame
from enums import Enums
from Constantes import Constants
from MainMenu import MainMenu
from about import About
from introduction import Introduction
from Common import *


class MainManager:
    screen: pygame.surface = None
    screenState: Enums.Screens = None
    session: bool = None

    def __init__(self, width=0, height=0):
        # Initialize the screen
        pygame.init()
        pygame.mixer.init()

        self.session = True

        self.screen = pygame.display.set_mode((width, height))
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

    def startGameSession(self):
        while self.session:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                self.finishGameSession()

            thisState = self.screenState
            thisWindow = self.screen
            screens = Enums.Screens

            if thisState == screens.none:
                self.finishGameSession()
            elif thisState == screens.mainMenu:
                mainMenu = MainMenu(thisWindow, self)
                mainMenu.loadView()
            elif thisState == screens.selectName:
                print("Select name - load view")
            elif thisState == screens.introduction:
                print("introduction - load view")
                introduction = Introduction(thisWindow)
                introduction.loadView()
            elif thisState == screens.about:
                print("About - load view")
                about = About(thisWindow, self)
                about.loadView()
                print("Session finished")
            elif thisState == screens.confirmExit:
                print("Confirm exit - load view")

            # Update the screen each time the "While session" do a loop
            pygame.display.update()

    def finishGameSession(self):
        print("Closing at screen ~> {0}".format(self.screenState))
        self.session = False
