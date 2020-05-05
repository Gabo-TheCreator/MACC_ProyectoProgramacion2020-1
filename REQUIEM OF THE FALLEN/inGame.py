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
import random

index = 0
index_a = 0
#Define el valor inicial de las variables de selección
class InGame(ScreenProtocol):
    screen: pygame.surface = None
    common = Common
    cons = Constants
    mainManager = None

    player = Character(100, 100, 1.0, "Caballerito", [health_potion, mana_potion, boost_potion, empty_potion],
                       [slash_attack, magic_player], Enums.CharacterType.player)
    enemy = Character(250, 500, 1.0, "Kho'wid", [], [slash_attack, miss, magic_enemy], Enums.CharacterType.enemy)
    actionMenu = None
    whosTurn: Enums.CharacterType = None
    #Define como un atributo de la clase a el jugador, enemigo, turno

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
        music(self.common.battle, -1)
        #Muestra la pantalla inicial
        while True:
            if clock() > nextFrame:
                pygame.draw.rect(self.screen, Constants.colors.black, (0, 0, 200, 20))
                pygame.draw.rect(self.screen, Constants.colors.black, (0, 20, 200, 20))
                pygame.draw.rect(self.screen, Constants.colors.green, (0, 0, 2 * (self.player.vida), 20))
                pygame.draw.rect(self.screen, Constants.colors.cyan, (0, 20, 2 * (self.player.mana), 20))
                pygame.draw.rect(self.screen, Constants.colors.black, (600, 0, 200, 20))
                pygame.draw.rect(self.screen, Constants.colors.red, (600+(200-self.enemy.vida/1.25), 0, self.enemy.vida/1.25, 20))
                pygame.draw.rect(self.screen, Constants.colors.lightGreen, (200, 0, 100, 20))
                pygame.draw.rect(self.screen, Constants.colors.lightBlue, (200, 20, 100, 20))
                pygame.draw.rect(self.screen, Constants.colors.lightRed, (530, 0, 70, 20))
                drawLabel(self.screen, "HP: " + str(self.player.vida), constants.colors.black, constants.colors.trasparent, 20, (202,3))
                drawLabel(self.screen, "Mana: " + str(self.player.mana), constants.colors.black, constants.colors.trasparent, 20, (202, 23))
                drawLabel(self.screen, "HP: " + str(self.enemy.vida), constants.colors.black, constants.colors.trasparent, 20, (532, 3))
                #Genera las imágenes inmóviles pero cambiantes de la pantalla, como la barra de vida
                #maná, con su respectivo valor
                if self.player.vida <= 0:
                    index = 3
                    pygame.mixer.music.stop()
                    pygame.time.wait(500)
                    Common.exit_sfx.play()
                    pygame.time.wait(1000)
                    break
                elif self.enemy.vida <= 0:
                    index = 4
                    pygame.mixer.music.stop()
                    pygame.time.wait(500)
                    Common.Confirm.play()
                    pygame.time.wait(1000)
                    break
                #Ambos condicionales sirven para sacar del ciclo de juego al jugador cuando algún personaje muere
                if self.player.mana <= 30:
                    drawLabel(self.screen, "LOW!", constants.colors.cyan, constants.colors.trasparent, 20, (150, 23))
                    Constants.efectos.low_mana.play()
                if self.player.vida <= 30:
                    drawLabel(self.screen, "LOW!", constants.colors.green, constants.colors.trasparent, 20, (150, 3))
                    Constants.efectos.low_hp.play()
                #Ambas condiciones indican, visual y auditivamente, que el valor de vida y maná están bajos

                if index == 0:
                    idleAnimations()
                #Cuando el índice de "selección" está en cero, se inicia la animación neutra

                if index == 1:
                    attackAnimations(caballeroA, 208, 168, 9, 100, 50)
                    #Da la animación de ataque
                    if index_a == 1:
                        effectAnimations(Slash, 600, 158, 8, 100, 100)
                        index = 0
                        if self.player.mana <= 95:
                            self.player.mana += 5
                        #Anima el efecto del espadazo, y aumenta levemente el maná del jugador
                    if self.player.mana > -1:
                        luck = random.randrange(20)
                        if index_a == 2:
                            effectAnimations(Magic, 600, 158, 8, 100, 100)
                            index = 0
                            if self.player.vida <= 95 and luck <= 4:
                                self.player.vida += 5
                        #Anima el efecto del hechizo, y tiene un 20% de probabilidad de
                        #aumentar la vida del jugador

                    else:
                        Common.error.play()
                        index = 0
                        self.player.mana += 10
                        self.enemy.vida += 30
                    #Si el jugador no tiene suficiente maná, no permite realizar la acción de hechizo

                    if self.player.vida <= 0:
                        self.player.vida = 0
                    elif self.enemy.vida <= 0:
                        self.enemy.vida = 0
                    #Si la vida del enemigo termina en cero o menor a cero, define el valor en cero
                    #por estética, simplemente, para que el condicional de cierre de ciclo se active
                    #en la siguiente iteración



            self.loadData()
        if index == 3:
            setBackgroundImage(img + bg + "stone.png")
            drawLabel(self.screen, "GAME OVER", Constants.colors.white, Constants.colors.trasparent, 80, (250, 250))
            pygame.display.update()
            music(self.common.about_mus, -1)
            pygame.time.wait(7000)
            self.mainManager.finishGameSession()
            #Pantalla de GAME OVER, con música y fondo
        elif index == 4:
            setBackgroundImage(img + bg + "stone.png")
            drawLabel(self.screen, "YOU WIN!", Constants.colors.white, Constants.colors.trasparent, 80, (270, 250))
            pygame.display.update()
            music(self.common.about_mus, -1)
            pygame.time.wait(7000)
            self.mainManager.finishGameSession()
            #Pantalla de victoria, con música y fondo


    def loadData(self):
        self.actionMenu.updateMenuData(self.player, self.enemy, self.screen)
        self.actionMenu.displayMenu(self.completionForSelectedAttack, self.completionForSelectedItem, self.whosTurn)
        return True

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

        #Data needs to be reloaded before the enemy can auto-select an attack
        if self.loadData():
            self.makeDesitionForTheEnemy()
    #Proceso de ejecución interna del ataque

    def completionForSelectedItem(self):
        print("The user select an item")

    def redirectToScreen(self, selectedButtonIndex):
        if selectedButtonIndex == 0:  # Exit ~> go mainMenu
            self.mainManager.initMainMenu()
            return True
    #Redirección (inutilizada) al menú principal

    # Enemy's turn
    def makeDesitionForTheEnemy(self):
        print("enemy's turn")
        enemyAttacks = self.enemy.getAttacks()
        totalAttacks = len(enemyAttacks)

        randomAttack = int(random.uniform(0, totalAttacks))

        self.actionMenu.attackAsEnemy(self.getAttackFromName(enemyAttacks[randomAttack].getName()))
        player, enemy = self.actionMenu.retriveUpdatedCharecters()
        self.player = player
        self.enemy = enemy
    #Retorna los valores de los personajes tras el ataque y defensa
    def getAttackFromName(self, name):
        if name == "Slash":
            return Enums.inGame.Menu.Attacks.slash
        elif name == "Magic Spell":
            return Enums.inGame.Menu.Attacks.miss
        elif name == "Miss!":
            return Enums.inGame.Menu.Attacks.magicEnemy
        else:
            print("Unexpected error decoding the attack based on the name, please check the literal strings that is getting compared with.")
            raise
    #Tipo de ataque que realiza dependiendo del nombre de este