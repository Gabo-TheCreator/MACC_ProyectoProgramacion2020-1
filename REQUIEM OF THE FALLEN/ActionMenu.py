import pygame
import Common
from Constantes import Constants

class ActionMenu:

    cons = Constants
    common = Common

    thisPlayer = None
    thisEnemy = None
    thisScreen = None

    def __init__(self, player, enemy, screen):
        if player != None and enemy != None and screen != None:
            self.thisPlayer = player
            self.thisEnemy = enemy
            self.thisScreen = screen

    def displayMenu(self):
        print("displayMenu")

    def actionMenuScreenCorrectPosition(self, xpos, ypos):

        baseX = 100
        baseY = 250

        newx = xpos + baseX
        newy = ypos + baseY

        return newx, newy

    def reloadBaseMenu(self, newIndex, withSound):
        # Unselected view
        self.thisScreen.blit(self.cons.botones.INVENTORY_n, (self.actionMenuScreenCorrectPosition(80, 90)))
        self.thisScreen.blit(self.cons.botones.ATTACK_n, ((self.actionMenuScreenCorrectPosition(360, 90))))

        if withSound:
            self.common.EndLine.play()

        pygame.display.update()
