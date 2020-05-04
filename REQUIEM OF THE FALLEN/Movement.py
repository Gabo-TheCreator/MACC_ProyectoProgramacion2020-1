from Constantes import Constants
from pygame_functions import *
import pygame

#Pruebas de movimiento con funciones introducidas en pygame_functions.py
pygame.init()
wn = screenSize(800, 600)
pygame.display.set_caption("Movement trial")
main = True




#caballero = makeSprite("caballerito_idle.gif", 5)

border = Constants.extras.selection_border





nextFrame = clock()
frame = 1


def mainWindow():
    setBackgroundImage(Constants.extras.bg_2)
    wn.blit(border, (0, 0))

index = 0
menu = True
##


#x = pygame.event.Event()
#============#
mainWindow()
while main:
    ##
    if clock() > nextFrame:

        if index == 0:
            hideSprite(Constants.caballeroA)
            moveSprite(Constants.caballero, 200, 168, True)
            showSprite(Constants.caballero)
            moveSprite(Constants.Virus, 600, 168, True)
            showSprite(Constants.Virus)
            frame = (frame + 1) % 5  # Son 5 sprites los que tiene el caballerito idle
            nextFrame += 100
            changeSpriteImage(Constants.caballero, 0 * 5 + frame)
            changeSpriteImage(Constants.Virus, 0 * 5 + frame)

            if keyPressed("a"):
                hideSprite(Constants.caballero)
                index = 1

            if keyPressed("s"):
                index = 2

        if index == 1:
            moveSprite(Constants.caballeroA, 208, 168, True)
            showSprite(Constants.caballeroA)
            frame = (frame + 1) % 9  # Son 9 sprites los que tiene el caballerito attack
            nextFrame += 100
            changeSpriteImage(Constants.caballeroA, 0 * 9 + frame)
            index = 0

pygame.quit()