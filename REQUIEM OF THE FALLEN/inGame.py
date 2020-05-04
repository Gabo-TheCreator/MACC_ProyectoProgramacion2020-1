import pygame
import Common
from Utils import *
from Constantes import Constants
from ScreenProtocol import ScreenProtocol
from IngameConstantes import *
from pygame_functions import *
from enums import Enums
from Character import Character
from ActionMenu import ActionMenu

index = 0
index_a = 0

class InGame(ScreenProtocol):
    screen: pygame.surface = None
    common = Common
    cons = Constants
    mainManager = None

    player = Character(100, 100, 1.0, "Caballerito", [health_potion, mana_potion, boost_potion, empty_potion], [slash_attack, magic_player], Enums.CharacterType.player)
    enemy = Character(500, 500, 1.0, "Kho'wid", [], [slash_attack, magic_enemy, miss], Enums.CharacterType.enemy)
    actionMenu = None
    whosTurn: Enums.CharacterType = None

    def __init__(self, screen, mainManager=None):
        self.screen = screen
        self.actionMenu = ActionMenu()
        self.whosTurn = Enums.CharacterType.player

        if mainManager != None:
            self.mainManager = mainManager

    def loadView(self):
        global index, index_a
        print("loadView")
        setBackgroundImage(img + bg + "stone.png")
        self.screen.blit(border, (0, 0))
        pygame.display.update()


        while True:
            if clock() > nextFrame:
                pygame.draw.rect(self.screen, Constants.colors.black, (0, 0, 200, 20))
                pygame.draw.rect(self.screen, Constants.colors.black, (0, 20, 200, 20))
                pygame.draw.rect(self.screen, Constants.colors.green, (0, 0, 2 * (self.player.vida), 20))
                pygame.draw.rect(self.screen, Constants.colors.cyan, (0, 20, 2 * (self.player.mana), 20))
                pygame.draw.rect(self.screen, Constants.colors.black, (600, 0, 200, 20))
                pygame.draw.rect(self.screen, Constants.colors.red, (600+(200-self.enemy.vida/2.5), 0, self.enemy.vida/2.5, 20))
                pygame.draw.rect(self.screen, Constants.colors.lightGreen, (200, 0, 100, 20))
                pygame.draw.rect(self.screen, Constants.colors.lightBlue, (200, 20, 100, 20))
                pygame.draw.rect(self.screen, Constants.colors.lightRed, (530, 0, 70, 20))
                drawLabel(self.screen, "HP: " + str(self.player.vida), constants.colors.black, constants.colors.trasparent, 20, (202,3))
                drawLabel(self.screen, "Mana: " + str(self.player.mana), constants.colors.black, constants.colors.trasparent, 20, (202, 23))
                drawLabel(self.screen, "HP: " + str(self.enemy.vida), constants.colors.black, constants.colors.trasparent, 20, (532, 3))

                if self.player.mana <= 50:
                    drawLabel(self.screen, "LOW!", constants.colors.cyan, constants.colors.trasparent, 20, (150, 23))
                if self.player.vida <= 50:
                    drawLabel(self.screen, "LOW!", constants.colors.green, constants.colors.trasparent, 20, (150, 3))

                if index == 0:
                    idleAnimations()

                if index == 1:
                    attackAnimations(caballeroA, 208, 168, 9, 100, 50)

                    if index_a == 1:
                        effectAnimations(Slash, 600, 158, 8, 100, 100)
                        index = 0
                        
                    if index_a == 2:
                        effectAnimations(Magic, 600, 158, 8, 100, 100)
                        index = 0

            self.loadData()

    def loadData(self):
        self.actionMenu.updateMenuData(self.player, self.enemy, self.screen)
        self.actionMenu.displayMenu(self.completionForSelectedAttack, self.completionForSelectedItem, self.whosTurn)

    def completionForSelectedAttack(self):
        global index, index_a
        print("The user select an attack")
        lastAttack = self.actionMenu.retriveLastAttack()
        player, enemy = self.actionMenu.retriveUpdatedCharecters()
        self.player = player
        self.enemy = enemy

        if lastAttack == Enums.inGame.Menu.Attacks.slash:
            print("Execute animations for slash attack")
            hideSprite(caballero)
            index = 1
            index_a = 1
        elif lastAttack == Enums.inGame.Menu.Attacks.magicPlayer:
            print("Execute animations for Magic attack")
            hideSprite(caballero)
            index = 1
            index_a = 2

    def completionForSelectedItem(self):
        print("The user select an item")

    def redirectToScreen(self, selectedButtonIndex):
        if selectedButtonIndex == 0: #Exit ~> go mainMenu
            self.mainManager.initMainMenu()
            return True