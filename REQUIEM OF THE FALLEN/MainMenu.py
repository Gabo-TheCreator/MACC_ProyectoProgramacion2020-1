import pygame
from pygame.locals import *
import Common
from Constantes import Constants
from ScreenProtocol import ScreenProtocol
from enums import Enums
from MainMenuButtonsInteractor import MainMenuButtonsInteractor


class MainMenu(ScreenProtocol):

    screen: pygame.surface = None
    common = Common
    cons = Constants

    buttonsInteractor = MainMenuButtonsInteractor()


    def __init__(self, screen):
        # Initialize Screen
        self.screen = screen

    def loadView(self):
        # Initialize
        self.screen.blit(self.common.bg_tit, (0, 0))
        self.screen.blit(self.common.title, ((self.cons.generalSettings.screenWidth / 2) - 216, 100))
        self.screen.blit(self.common.PLAY_n, (125, 412.5))
        self.screen.blit(self.common.ABOUT_n, (325, 412.5))
        self.screen.blit(self.common.EXIT_n, (525, 412.5))

        event = pygame.event.wait()
        if event.type == KEYDOWN:
            key = event.key
            if key == K_LEFT:
                print("Key left")
                self.buttonsInteractor.buttonIndex = self.buttonsInteractor.validateNewIndexPosition(self.buttonsInteractor.buttonIndex,
                                                                                                     Enums.MainMenu.directions.left)
                print(self.buttonsInteractor.buttonIndex)
            elif key == K_RIGHT:
                print("Key Right")
                self.buttonsInteractor.buttonIndex = self.buttonsInteractor.validateNewIndexPosition(self.buttonsInteractor.buttonIndex,
                                                                                                     Enums.MainMenu.directions.right)
                print(self.buttonsInteractor.buttonIndex)

    def reloadSelectedButtonInIndex(self,newIndex):
        print("Update with to focus on index ~>")
        print(newIndex)

        # if left:
        #     index -= 1
        #     if index < 0:
        #         index = 2
        # elif right:
        #     index += 1
        #     if index > 2:
        #         index = 0
        # if index == 0:
        #     win.blit(awa, (100, 400))
        #     win.blit(PLAY_s, (125, 412.5))
        #     x = 100
        # elif index == 1:
        #     win.blit(awa, (300, 400))
        #     win.blit(ABOUT_s, (325, 412.5))
        #     x = 300
        # elif index == 2:
        #     win.blit(awa, (500, 400))
        #     win.blit(EXIT_s, (525, 412.5))
        #     x = 500
        # else:
        #     win.blit(awa, (x, 400))
        #     # Aquí la 'x' es para dejar el cuadro de selección en la coordenada x anterior
        # pygame.display.update()