import pygame
import Common
from MainMenuButtonsInteractor import MainMenuButtonsInteractor
from ScreenProtocol import ScreenProtocol
from Constantes import Constants
from enums import Enums
from Utils import *
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
        if mainManager != None:
            self.mainManager = mainManager

    def loadView(self):
        music(Common.main_theme, -1)
        while True:
            # Initialize
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                key = event.key
                if key == K_LEFT:
                    print("Key left")
                    self.buttonsInteractor.buttonIndex = self.buttonsInteractor.validateNewIndexPosition(self.buttonsInteractor.buttonIndex, Enums.MainMenu.directions.left)
                    self.reloadViewsForSelectedButtonInIndex(self.buttonsInteractor.buttonIndex, True)
                elif key == K_RIGHT:
                    print("Key Right")
                    self.buttonsInteractor.buttonIndex = self.buttonsInteractor.validateNewIndexPosition(self.buttonsInteractor.buttonIndex, Enums.MainMenu.directions.right)
                    self.reloadViewsForSelectedButtonInIndex(self.buttonsInteractor.buttonIndex, True)
                elif key == K_RETURN:
                    if self.redirectToScreen(self.buttonsInteractor.buttonIndex):
                        break
            #Dentro del menú principal, espera el evento y lo enlaza con las acciones definidas en
            #MainMenuButtonsInteractor(), (derecha, izquierda, ENTER)
            pygame.display.update()

    def reloadViewsForSelectedButtonInIndex(self, newIndex, withSound):
        # Unselected Views
        self.screen.blit(self.common.bg_tit, (0, 0))
        self.screen.blit(self.common.title, ((self.cons.generalSettings.screenWidth / 2) - 216, 100))
        self.screen.blit(self.common.PLAY_n, (125, 412.5))
        self.screen.blit(self.common.ABOUT_n, (325, 412.5))
        self.screen.blit(self.common.EXIT_n, (525, 412.5))
        #Genera la pantalla principal
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
        #Genera una imagen específica para cada caso en que se señale alguna opción
    def redirectToScreen(self, selectedButtonIndex):
        # -screenIndex: is the index that we should go to based on all the buttons indexes
        if selectedButtonIndex == 0: #PLAY
            self.mainManager.initIntroduction()
            #Need to be implemented
            return True
        elif selectedButtonIndex == 1: #ABOUT
            self.mainManager.initAbout()
            return True
        elif  selectedButtonIndex == 2: #EXIT
            self.common.exit_sfx.play()
            pygame.time.wait(1000)
            self.mainManager.finishGameSession()
            return True
        #Al seleccionar una opción, se redirige a la pantalla a la que está enlazada
        #O acaba el juego, como es el caso de EXIT

        return False