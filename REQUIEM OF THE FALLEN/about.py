import pygame
import Common
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
#Aquí se genera una conexión al main manager, que es el que generará la ruta al momento de
    #cambiar de pantalla

    def loadView(self):
        # Initialize


        self.common.Confirm.play()
        pygame.time.wait(1000)
        music(self.common.about_mus, -1)
        #Se inicia la música propia de la pantalla "about", tras el beep al seleccionar
        waitBeforeLoadingNextActions(self.mainManager.screenState)
        self.screen.blit(self.common.bg_tit, (0, 0))
        #Coloca el fondo en la pantalla
        pygame.display.update()
        drawText(self.screen, "ABOUT", (300, 100), self.cons.colors.lightPurple, self.cons.colors.trasparent, 60, 200, Enums.TextAnimations.typewriter)
        drawText(self.screen, "JUAN MANUEL DAVILA RIVERA", (100, 200), self.cons.colors.white, self.cons.colors.trasparent, 40, 100, Enums.TextAnimations.typewriter)
        drawText(self.screen, "GABRIELA LINARES CHAVEZ", (100, 240), self.cons.colors.white, self.cons.colors.trasparent, 40, 100, Enums.TextAnimations.typewriter)
        drawText(self.screen, "JOSE GABRIEL CUADROS CARDENAS", (100, 280), self.cons.colors.white, self.cons.colors.trasparent, 40, 100, Enums.TextAnimations.typewriter)
        drawText(self.screen, "ALL RIGHTS RESERVED. 2020.", (10, 570), self.cons.colors.lightPurple, self.cons.colors.trasparent, 30, 1, Enums.TextAnimations.none)
        drawText(self.screen, "PURO MACC", (650, 570), self.cons.colors.cyan, self.cons.colors.trasparent, 30, 1, Enums.TextAnimations.none)
        drawText(self.screen, "v 1.0", (10, 550), self.cons.colors.lightPurple, self.cons.colors.trasparent, 30, 1, Enums.TextAnimations.none)
        #Se añaden las líneas de texto, con los parámetros de
        #Pantalla, texto, coordenadas, color de letra, color de fondo, tamaño, tiempo en milisegundos de animación
        #tipo de animación
        self.screen.blit(Common.BACK_s, (300, 400))
        #Coloca el botón de texto en la pantalla
        pygame.display.update()

        # Clear all the queued elements that were loaded in the mean while the text was getting drawed
        pygame.event.clear()
        #Elimina cualquier evento de la fila si el jugador presionó dos o más veces ENTER


        while True:
            pygame.event.wait()
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                self.screen.blit(Common.BACK_n, (300, 400))
                Common.exit_sfx.play()
                waitBeforeLoadingNextActions(self.mainManager.screenState)
                if self.redirectToScreen(0):
                    break
            #Espera a que el jugador presione enter en la pantalla, y al hacerlo da la vía para
            #que se cambie de pantalla con el proceso "redirectToScreen".

    def loadData(self):
        print("loadData")

    def redirectToScreen(self, selectedButtonIndex):
        if selectedButtonIndex == 0: #Exit ~> go mainMenu
            self.mainManager.initMainMenu()
            return True
