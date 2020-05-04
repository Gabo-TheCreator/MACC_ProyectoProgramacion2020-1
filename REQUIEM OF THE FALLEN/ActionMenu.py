import pygame
import Common
from Constantes import Constants
from inGameButtonsInteractor import inGameButtonsInteractor
from pygame_functions import *
from enums import Enums

class ActionMenu:

    cons = Constants
    common = Common

    thisPlayer = None
    thisEnemy = None
    thisScreen = None

    menuState = None

    buttonsInteractor = inGameButtonsInteractor()

    def __init__(self):
        self.initBaseMenu()

    def initBaseMenu(self):
        self.menuState = Enums.inGame.Menu.States.baseState

    def initInventory(self):
        self.menuState = Enums.inGame.Menu.States.inventory

    def initAttack(self):
        self.menuState = Enums.inGame.Menu.States.attack

    def updateMenuData(self, player, enemy, screen):
        if player != None and enemy != None and screen != None:
            self.thisPlayer = player
            self.thisEnemy = enemy
            self.thisScreen = screen

    def displayMenu(self):
        print("displayMenu")

        if self.menuState == Enums.inGame.Menu.States.baseState:
            self.reloadBaseMenu(self.buttonsInteractor.baseButtonsIndex, False)
            if keyPressed("right"):
                self.buttonsInteractor.baseButtonsIndex = self.buttonsInteractor.validateBaseButtonsNewIndexPosition(self.buttonsInteractor.baseButtonsIndex, Enums.inGame.Menu.baseState.directions.right)
                self.reloadBaseMenu(self.buttonsInteractor.baseButtonsIndex, True)
            elif keyPressed("left"):
                self.buttonsInteractor.baseButtonsIndex = self.buttonsInteractor.validateBaseButtonsNewIndexPosition(self.buttonsInteractor.baseButtonsIndex, Enums.inGame.Menu.baseState.directions.left)
                self.reloadBaseMenu(self.buttonsInteractor.baseButtonsIndex, True)
            elif keyPressed("return"):
                self.redirectToMenu(self.buttonsInteractor.baseButtonsIndex)
        elif self.menuState == Enums.inGame.Menu.States.inventory:
            if keyPressed("right"):
                print("Inventory")
            elif keyPressed("left"):
                print("Inventory")
            elif keyPressed("return"):
                print("Inventory")
        elif self.menuState == Enums.inGame.Menu.States.attack:
            self.reloadAttackMenu(self.buttonsInteractor.attackButtonsIndex, False)
            if keyPressed("right"):
                print("Attack")
            elif keyPressed("left"):
                print("Attack")
            elif keyPressed("return"):
                print("Attack")

    def actionMenuScreenCorrectPosition(self, xpos, ypos):

        baseX = 100
        baseY = 250

        newx = xpos + baseX
        newy = ypos + baseY

        return newx, newy

    def reloadBaseMenu(self, newIndex, withSound):

        self.generalReload()
        self.thisScreen.blit(self.cons.botones.INVENTORY_n, (self.actionMenuScreenCorrectPosition(80, 90)))
        self.thisScreen.blit(self.cons.botones.ATTACK_n, ((self.actionMenuScreenCorrectPosition(360, 90))))

        if withSound:
            self.common.EndLine.play()

        selectedButton = self.buttonsInteractor.baseButtons[newIndex]

        if selectedButton == self.buttonsInteractor.baseButtons[0]:
            self.thisScreen.blit(self.cons.botones.INVENTORY_s, (self.actionMenuScreenCorrectPosition(80, 90)))
        elif selectedButton == self.buttonsInteractor.baseButtons[1]:
            self.thisScreen.blit(self.cons.botones.ATTACK_s, ((self.actionMenuScreenCorrectPosition(360, 90))))

    def generalReload(self):

        self.thisScreen.blit(self.common.bg_cut, (0, 600 - 360))
        self.thisScreen.blit(self.common.selection_border, (0, 0))
        pygame.display.update()

    def reloadAttackMenu(self, newIndex, withSound):

        self.generalReload()
        self.thisScreen.blit(self.cons.botones.SLASH_n, (self.actionMenuScreenCorrectPosition(20, 20)))
        self.thisScreen.blit(self.cons.botones.SPELL_n, (self.actionMenuScreenCorrectPosition(140, 20)))

        if withSound:
            self.common.EndLine.play()

    def redirectToMenu(self, selectedButtonIndex):
        if selectedButtonIndex == 0:
            print("Inventory")
            self.initInventory()
        elif selectedButtonIndex == 1:
            print("Attack")
            self.initAttack()

