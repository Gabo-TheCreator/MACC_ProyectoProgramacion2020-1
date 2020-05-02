import pygame
import Common
from pygame.locals import *
from Utils import *
from Constantes import Constants
from ScreenProtocol import ScreenProtocol
from enums import Enums
from pygame_functions import *


class Introduction(ScreenProtocol):

    screen: pygame.surface = None
    common = Common
    cons = Constants
    mainManager = None

    def __init__(self, screen, mainManager=None):

        self.screen = screen

        if mainManager != None:
            self.mainManager = mainManager


    def loadView(self):
        # Initialize
        self.common.Confirm.play()
        waitBeforeLoadingNextActions(self.mainManager.screenState)
        self.screen.blit(Constants.extras.bg_2, (0, 0))
        pygame.display.update()
        drawText(self.screen, "REQUIEM OF THE FALLEN", (110,100), self.cons.colors.lightPurple, self.cons.colors.trasparent,60,0.2,
                   Enums.TextAnimations.none)
        drawText(self.screen, "In the year 2020, a new lifeform has risen from the", (90, 200), self.cons.colors.white, self.cons.colors.trasparent, 30, 100,
                   Enums.TextAnimations.typewriter)
        drawText(self.screen, "ashes of those who died full of remorse.", (90, 220),self.cons.colors.white, self.cons.colors.trasparent, 30, 100,
                 Enums.TextAnimations.typewriter)
        drawText(self.screen, "That new lifeform, led by the evil Kho'wid, has", (90, 240), self.cons.colors.white, self.cons.colors.trasparent, 30, 100,
                 Enums.TextAnimations.typewriter)
        drawText(self.screen, "the evil purpose of deleting humans from earth.", (90, 260), self.cons.colors.white, self.cons.colors.trasparent, 30, 100,
                 Enums.TextAnimations.typewriter)
        drawText(self.screen, "Now, the human race", (90, 300), self.cons.colors.cyan, self.cons.colors.trasparent, 50, 100,
                 Enums.TextAnimations.typewriter)
        drawText(self.screen, "relies on you.", (90, 340), self.cons.colors.cyan, self.cons.colors.trasparent, 50, 100,
                 Enums.TextAnimations.typewriter)
        self.screen.blit(Common.PLAY_s, (300, 500))
        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                key = event.key
                if key == K_RETURN:
                    self.screen.blit(Common.PLAY_n, (300, 500))
                    Common.Confirm.play()
                    waitBeforeLoadingNextActions(self.mainManager.screenState)
                    break
        
        self.screen.blit(Constants.extras.bg_2, (0, 0))
        pygame.display.update()
        drawText(self.screen, "TUTORIAL", (280, 100), self.cons.colors.lightPurple,
                 self.cons.colors.trasparent, 60, 0.2,
                 Enums.TextAnimations.none)
        drawText(self.screen, "Requiem of the Fallen is a turn-based RPG, where", (90, 200), self.cons.colors.white,
                 self.cons.colors.trasparent, 30, 100,
                 Enums.TextAnimations.typewriter)
        drawText(self.screen, "you'll control this little knight.", (90, 220), self.cons.colors.white,
                 self.cons.colors.trasparent, 30, 100,
                 Enums.TextAnimations.typewriter)
        self.screen.blit(Constants.caballero_1, (376, 240))
        pygame.display.update()
        drawText(self.screen, "All you have to do is take your pick on your turn:", (90, 350), self.cons.colors.white,
                 self.cons.colors.trasparent, 30, 100,
                 Enums.TextAnimations.typewriter)
        pygame.time.wait(500)
        self.screen.blit(Constants.botones.INVENTORY_n, (146.6, 400))
        Common.Beep.play()
        pygame.display.update()
        pygame.time.wait(1000)
        self.screen.blit(Constants.botones.ATTACK_n, (451.3, 400))
        Common.Beep.play()
        pygame.display.update()
        pygame.time.wait(1000)
        self.screen.blit(Constants.botones.awa, (287.5, 487.5))
        Common.EndLine.play()
        pygame.display.update()
        self.screen.blit(Common.PLAY_s, (312.5, 500))
        pygame.display.update()
        while True:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                key = event.key
                if key == K_RETURN:
                    self.screen.blit(Common.PLAY_n, (312.5, 500))
                    Common.Confirm.play()
                    waitBeforeLoadingNextActions(self.mainManager.screenState)
                    if self.redirectToScreen(0):
                        break

    def loadData(self):
        print("loadData")

    def redirectToScreen(self, selectedButtonIndex):
        if selectedButtonIndex == 0: #Exit ~> go mainMenu
            self.mainManager.initInGame()
            return True