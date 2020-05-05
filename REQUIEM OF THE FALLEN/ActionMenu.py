import pygame
import Common
from Constantes import Constants
from inGameButtonsInteractor import inGameButtonsInteractor
from pygame_functions import *
from enums import Enums
from Character import Character
from IngameConstantes import *


class ActionMenu:

    cons = Constants
    common = Common
    #Se renombran los módulos para hacerlos más sencillos
    thisPlayer: Character = None
    updatedPlayer: Character = None
    thisEnemy: Character = None
    updatedEnemy: Character = None
    thisScreen = None

    menuState = None
    lastAttack = None

    buttonsInteractor = inGameButtonsInteractor()
    #Se definen los argumentos sin valor alguno, para ser cambiados en el código
    def __init__(self):
        self.initBaseMenu()

    def initBaseMenu(self):
        self.menuState = Enums.inGame.Menu.States.baseState

    def initInventory(self):
        self.menuState = Enums.inGame.Menu.States.inventory

    def initAttack(self):
        self.menuState = Enums.inGame.Menu.States.attack
    #Se inicializan dichos argumentos

    def updateMenuData(self, player, enemy, screen):
        if player != None and enemy != None and screen != None:
            self.thisPlayer = player
            self.thisEnemy = enemy
            self.thisScreen = screen

    def displayMenu(self, completionForAttack, completionForItem, whosTurn):
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
                self.common.EndLine.play()

        elif self.menuState == Enums.inGame.Menu.States.inventory:
            if keyPressed("right"):
                print("Inventory")
            elif keyPressed("left"):
                print("Inventory")
            elif keyPressed("return"):
                print("Inventory")
                self.initBaseMenu()
                completionForItem()
        elif self.menuState == Enums.inGame.Menu.States.attack:
            self.reloadAttackMenu(self.buttonsInteractor.attackButtonsIndex, False)
            if keyPressed("right"):
                self.buttonsInteractor.attackButtonsIndex = self.buttonsInteractor.validateAttackButtonsNewIndexPosition(self.buttonsInteractor.attackButtonsIndex, Enums.inGame.Menu.attack.directions.right)
                self.reloadAttackMenu(self.buttonsInteractor.attackButtonsIndex, True)
            elif keyPressed("left"):
                self.buttonsInteractor.attackButtonsIndex = self.buttonsInteractor.validateAttackButtonsNewIndexPosition(self.buttonsInteractor.attackButtonsIndex, Enums.inGame.Menu.attack.directions.left)
                self.reloadAttackMenu(self.buttonsInteractor.attackButtonsIndex, True)
            elif keyPressed("return"):
                if self.selectAttack(self.buttonsInteractor.attackButtonsIndex):
                    if self.updateCharactersBasedOnAttack(whosTurn):
                        self.common.EndLine.play()
                        pygame.time.wait(100)
                        self.initBaseMenu()
                        completionForAttack()
#Líneas 46-83 #Se dan las acciones posibles en el menú dentro del juego (arriba, abajo y ENTER)

    def actionMenuScreenCorrectPosition(self, xpos, ypos):

        baseX = 100
        baseY = 250

        newx = xpos + baseX
        newy = ypos + baseY

        return newx, newy
    #Define coordenadas base de 'x' y 'y'

    def reloadBaseMenu(self, newIndex, withSound):

        self.generalReload()
        drawLabel(self.thisScreen, "Coming Soon!", Constants.colors.white, Constants.colors.trasparent, 20, (226.5, 420))

        self.thisScreen.blit(self.cons.botones.INVENTORY_n, (self.actionMenuScreenCorrectPosition(80, 90)))
        self.thisScreen.blit(self.cons.botones.ATTACK_n, ((self.actionMenuScreenCorrectPosition(360, 90))))

        if withSound:
            self.common.EndLine.play()

        selectedButton = self.buttonsInteractor.baseButtons[newIndex]

        if selectedButton == self.buttonsInteractor.baseButtons[0]:
            self.thisScreen.blit(self.cons.botones.INVENTORY_s, (self.actionMenuScreenCorrectPosition(80, 90)))
        elif selectedButton == self.buttonsInteractor.baseButtons[1]:
            self.thisScreen.blit(self.cons.botones.ATTACK_s, ((self.actionMenuScreenCorrectPosition(360, 90))))
    #Genera un estado base en el menú de juego, para que cambie respecto a cual está señalado, menú inicial de juego

    def reloadAttackMenu(self, newIndex, withSound):

        self.generalReload()
        self.thisScreen.blit(self.cons.botones.SLASH_n, (self.actionMenuScreenCorrectPosition(80, 90)))
        self.thisScreen.blit(self.cons.botones.SPELL_n, (self.actionMenuScreenCorrectPosition(360, 90)))

        if withSound:
            self.common.EndLine.play()

        selectedButton = self.buttonsInteractor.attackButtons[newIndex]

        if selectedButton == self.buttonsInteractor.attackButtons[0]:
            self.thisScreen.blit(self.cons.botones.SLASH_s, (self.actionMenuScreenCorrectPosition(80, 90)))
        elif selectedButton == self.buttonsInteractor.attackButtons[1]:
            self.thisScreen.blit(self.cons.botones.SPELL_s, (self.actionMenuScreenCorrectPosition(360, 90)))
    #Genera un estado base en el menú de juego, para que cambie respecto a cual está señalado, menú de ataque del juego


    def reloadInventoryMenu(self, newIndex, withSound):

        self.redirectToMenu()

        if withSound:
            self.common.EndLine.play()

    #Espacio para implementar inventario

    def redirectToMenu(self, selectedButtonIndex):
        if selectedButtonIndex == 0:
            print("Inventory")
            #self.initInventory()
            Common.error.play()
        elif selectedButtonIndex == 1:
            print("Attack")
            self.initAttack()
    #Redirección al submenú dependiendo del índice dentro del menú anterior

    def selectAttack(self, indexPos):
        if indexPos == Enums.inGame.Menu.attack.Button.slash.value:
            self.lastAttack = Enums.inGame.Menu.Attacks.slash
            return True
        elif indexPos == Enums.inGame.Menu.attack.Button.magic.value:
            self.lastAttack = Enums.inGame.Menu.Attacks.magicPlayer
            return True
        return False
    #Selección interna del ataque del jugador dependiendo de su selección externa

    def retriveLastAttack(self):
        if self.lastAttack != None:
            return self.lastAttack
        else:
            return None
    #Deja señalado el último ataque utilizado por el jugador

    def retriveUpdatedCharecters(self):
        if self.updatedPlayer != None and self.updatedEnemy != None:
            self.thisPlayer = None
            self.thisEnemy = None
            return self.updatedPlayer, self.updatedEnemy
        else:
            return None, None
    #Devuelve los estados de los dos personajes (jugador y enemigo)

    def updateCharactersBasedOnAttack(self, whosTurn):

        attackEnum = self.lastAttack

        player = self.thisPlayer
        enemy = self.thisEnemy

        uPlayer = None
        uEnemy = None

        ## Convert from attack enum to attack value
        attack = None
        if attackEnum == Enums.inGame.Menu.Attacks.slash:
            attack = slash_attack
        elif attackEnum == Enums.inGame.Menu.Attacks.magicPlayer:
            attack = magic_player
        elif attackEnum == Enums.inGame.Menu.Attacks.magicEnemy:
            attack = magic_enemy
        elif attackEnum == Enums.inGame.Menu.Attacks.miss:
            attack = miss

        # Evaluate with the attack
        if whosTurn == Enums.CharacterType.player:

            # Player
            pNewMana = int(player.getMana()) - int(attack.getManaCost())

            uPlayer = Character(player.getHealth(),
                                pNewMana,
                                player.getBoost(),
                                player.getName(),
                                player.getItems(),
                                player.getAttacks(),
                                player.getType())

            # Enemy
            eNewHealth = int(enemy.getHealth()) - int(attack.getDamage())
            uEnemy = Character(eNewHealth,
                               enemy.getMana(),
                               enemy.getBoost(),
                               enemy.getName(),
                               enemy.getItems(),
                               enemy.getAttacks(),
                               enemy.getType())

        elif whosTurn == Enums.CharacterType.enemy:
            # Player
            pNewHealth = int(player.getHealth()) - int(attack.getDamage())
            uPlayer = Character(pNewHealth,
                                player.getMana(),
                                player.getBoost(),
                                player.getName(),
                                player.getItems(),
                                player.getAttacks(),
                                player.getType())

            # Enemy
            eNewMana = int(enemy.getMana()) - int(attack.getManaCost())
            uEnemy = Character(enemy.getHealth(),
                               eNewMana,
                               enemy.getBoost(),
                               enemy.getName(),
                               enemy.getItems(),
                               enemy.getAttacks(),
                               enemy.getType())

        self.updatedPlayer = uPlayer
        self.updatedEnemy = uEnemy

        return True

    def generalReload(self):
        self.thisScreen.blit(self.common.bg_cut, (0, 600 - 360))
        self.thisScreen.blit(self.common.selection_border, (0, 0))
    #Recarga la pantalla del juego, con fondo y borde de selección

    def attackAsEnemy(self, attack):
        self.lastAttack = attack
        self.updateCharactersBasedOnAttack(Enums.CharacterType.enemy)