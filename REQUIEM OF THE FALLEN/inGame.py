import pygame
import Common
from pygame.locals import *
from Utils import *
from Constantes import Constants
from ScreenProtocol import ScreenProtocol
from enums import Enums

class InGame(ScreenProtocol):
    screen: pygame.surface = None
    common = Common
    cons = Constants
    mainManager = None

    def __init__(self, screen, mainManager=None):
        self.screen = screen

        if mainManager != None:
            self.mainManager = mainManager

    def loadView(self):
        print("loadView")
        self.loadData()

    def loadData(self):
        print("loadData")
        while True:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                key = event.key
                if key == K_RETURN:
                    Common.Confirm.play()
                    waitBeforeLoadingNextActions(self.mainManager.screenState)
                    if self.redirectToScreen(0):
                        break


    def redirectToScreen(self, selectedButtonIndex):
        if selectedButtonIndex == 0: #Exit ~> go mainMenu
            self.mainManager.initMainMenu()
            return True