import pygame
import Common
from pygame.locals import *
from Utils import *
from Constantes import Constants
from ScreenProtocol import ScreenProtocol
from IngameConstantes import *
from pygame_functions import *
from enums import Enums
from Character import Character
from Item import Item
from Ataque import Ataque

class InGame(ScreenProtocol):
    screen: pygame.surface = None
    common = Common
    cons = Constants
    mainManager = None
    player = Character(100, 100, 1.0, "Caballerito", [health_potion, mana_potion, boost_potion, empty_potion], [slash_attack, magic_player], Enums.CharacterType.player)
    enemy = Character(500, 500, 1.0, "Kho'wid", [], [slash_attack, magic_enemy, miss], Enums.CharacterType.enemy)

    def __init__(self, screen, mainManager=None):
        self.screen = screen


        if mainManager != None:
            self.mainManager = mainManager

    def loadView(self):
        nextFrame = clock()
        frame = 1
        index = 0
        index_a = 0
        print("loadView")
        setBackgroundImage(img + bg + "stone.png")
        self.screen.blit(border, (0, 0))
        pygame.display.update()

        while True:
            if clock() > nextFrame:

                if index == 0:
                    hideSprite(caballeroA)
                    hideSprite(Slash)
                    moveSprite(caballero, 200, 168, True)
                    showSprite(caballero)
                    moveSprite(virus, 600, 168, True)
                    showSprite(virus)
                    frame = (frame + 1) % 5  # Son 5 sprites los que tiene el caballerito idle
                    nextFrame += 100
                    changeSpriteImage(caballero, 0 * 5 + frame)
                    changeSpriteImage(virus, 0 * 5 + frame)

                    if keyPressed("a"):
                        hideSprite(caballero)
                        index = 1
                        index_a = 1

                    if keyPressed("s"):
                        index = 2

                if index == 1:
                    moveSprite(caballeroA, 208, 168, True)
                    showSprite(caballeroA)
                    frame = (frame + 1) % 9  # Son 9 sprites los que tiene el caballerito attack
                    nextFrame += 100
                    changeSpriteImage(caballeroA, 0 * 9 + frame)
                    if index_a == 1:
                        moveSprite(Slash, 600, 158, True)
                        showSprite(Slash)
                        frame = (frame + 1) % 8
                        nextFrame += 5
                        changeSpriteImage(Slash, 0 * 8 + frame)
                        index = 0
        #AQUÍ HERMOSURAS, AQUÍ!!!
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