import pygame
import Common
from MainMenuButtonsInteractor import MainMenuButtonsInteractor
from ScreenProtocol import ScreenProtocol
from Constantes import Constants
from enums import Enums
from pygame.locals import *

class MainMenu(ScreenProtocol):
    screen: pygame.surface = None
    common = Common
    cons = Constants
    mainManager = None

    buttonsInteractor = MainMenuButtonsInteractor()

    def __init__(self, screen, mainManager = None):
        # Initialize Screen
        self.screen = screen
        self.reloadViewsForSelectedButtonInIndex(self.buttonsInteractor.buttonIndex, True)
        if mainManager == None:
            print("Exit")
        else:
            self.mainManager = mainManager

    def loadView(self):
        while True:
            # Initialize
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                key = event.key
                if key == K_LEFT:
                    print("Key left")
                    self.buttonsInteractor.buttonIndex = self.buttonsInteractor.validateNewIndexPosition(
                        self.buttonsInteractor.buttonIndex,
                        Enums.MainMenu.directions.left)
                    self.reloadViewsForSelectedButtonInIndex(self.buttonsInteractor.buttonIndex, True)
                elif key == K_RIGHT:
                    print("Key Right")
                    self.buttonsInteractor.buttonIndex = self.buttonsInteractor.validateNewIndexPosition(
                        self.buttonsInteractor.buttonIndex,
                        Enums.MainMenu.directions.right)
                    self.reloadViewsForSelectedButtonInIndex(self.buttonsInteractor.buttonIndex, True)
                elif key == K_RETURN:
                    if self.redirectToScreen(self.buttonsInteractor.buttonIndex):
                        print("Finishing this session")
                        break
                    else:
                        print("Could not finish the session")

            pygame.display.update()

    def reloadViewsForSelectedButtonInIndex(self, newIndex, withSound):

        # Unselected Views
        self.screen.blit(self.common.bg_tit, (0, 0))
        self.screen.blit(self.common.title, ((self.cons.generalSettings.screenWidth / 2) - 216, 100))
        self.screen.blit(self.common.PLAY_n, (125, 412.5))
        self.screen.blit(self.common.ABOUT_n, (325, 412.5))
        self.screen.blit(self.common.EXIT_n, (525, 412.5))

        if withSound:
            self.common.EndLine.play()

        selectedButton = self.buttonsInteractor.buttons[newIndex]

        if selectedButton == self.buttonsInteractor.buttons[0]:
            print("Play")
            self.screen.blit(self.common.awa, (100, 400))
            self.screen.blit(self.common.PLAY_s, (125, 412.5))
        elif selectedButton == self.buttonsInteractor.buttons[1]:
            print("About")
            self.screen.blit(self.common.awa, (300, 400))
            self.screen.blit(self.common.ABOUT_s, (325, 412.5))

        elif selectedButton == self.buttonsInteractor.buttons[2]:
            print("Exit")
            self.screen.blit(self.common.awa, (500, 400))
            self.screen.blit(self.common.EXIT_s, (525, 412.5))

    def redirectToScreen(self,screenIndex):
        # -screenIndex: is the index that we should go to based on all the buttons indexes

        if screenIndex == 0: #PLAY
            print("Play")
            return True
        elif screenIndex == 1: #ABOUT
            self.mainManager.initAbout()
            return True
        elif  screenIndex == 2: #EXIT
            print("Exit")
            return True

        return False