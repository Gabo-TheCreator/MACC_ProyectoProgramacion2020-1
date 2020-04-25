import pygame
import Common
from pygame.locals import *
from Utils import *
from Constantes import Constants
from ScreenProtocol import ScreenProtocol
from enums import Enums


class About(ScreenProtocol):

    screen: pygame.surface = None
    common = Common
    cons = Constants
    mainManager = None

    def __init__(self, screen, mainManager = None):

        self.screen = screen

        if mainManager != None:
            self.mainManager = mainManager

    def loadView(self):
        # Initialize
        while True:
            self.screen.blit(self.common.bg_tit, (0, 0))

            drawText(self.screen, "ABOUT", (300, 100), self.cons.colors.lightPurple, self.cons.colors.trasparent, 60, 2, Enums.TextAnimations.typewriter)
            drawText(self.screen, "JUAN MANUEL DAVILA RIVERA", (100, 200), self.cons.colors.white, self.cons.colors.trasparent, 40, 1, Enums.TextAnimations.typewriter)
            drawText(self.screen, "GABRIELA LINARES CHAVEZ", (100, 240), self.cons.colors.white, self.cons.colors.trasparent, 40, 1, Enums.TextAnimations.typewriter)
            drawText(self.screen, "JOSE GABRIEL CUADROS CARDENAS", (100, 280), self.cons.colors.white, self.cons.colors.trasparent, 40, 1, Enums.TextAnimations.typewriter)
            drawText(self.screen, "ALL RIGHTS RESERVED. 2020.", (10, 570), self.cons.colors.lightPurple, self.cons.colors.trasparent, 30, 1, Enums.TextAnimations.none)
            drawText(self.screen, "PURO MACC", (650, 570), self.cons.colors.cyan, self.cons.colors.trasparent, 30, 1, Enums.TextAnimations.none)
            self.screen.blit(Common.BACK_s, (300, 400))
            pygame.display.update()

            # Clear all the queued elements that were loaded in the mean while the text was getting drawed
            pygame.event.clear()

            event = pygame.event.wait()
            if event.type == KEYDOWN:
                key = event.key
                if key == K_RETURN:
                    self.screen.blit(Common.BACK_n, (300, 400))
                    Common.exit_sfx.play()
                    if self.redirectToScreen(0):
                        break

    def loadData(self):
        print("loadData")

    def redirectToScreen(self, selectedButtonIndex):
        if selectedButtonIndex == 0: #Exit ~> go mainMenu
            self.mainManager.initMainMenu()
            return True
