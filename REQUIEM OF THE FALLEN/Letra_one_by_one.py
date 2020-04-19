import pygame,time
import Constantes as cst
constants = cst.Constants

screen=pygame.display.set_mode((300, 300))

def text(texto, coordenadas, color, fondo, tamaño, tiempo):
    basicfont = pygame.font.Font("Fonts/8bit.ttf", tamaño)
    x, y = coordenadas

    char = ''
    letra = 0
    Beep=constants.efectos.Beep
    Beep.play()
    for _ in range(len(texto)):
        pygame.event.pump() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        time.sleep(tiempo) ##change this for faster or slower text animation
        char = char + texto[letra]
        text = basicfont.render(char, False, color, fondo) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect)


        letra += 1
        if letra%8==0:
            Beep.play()


def text_name(texto, coordenadas, color, fondo,tamaño):
    basicfont = pygame.font.Font("Fonts/8bit.ttf", tamaño)
    x, y = coordenadas

    char = ''
    letra = 0

    for _ in range(len(texto)):
        pygame.event.pump() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.

        char = char + texto[letra]
        text = basicfont.render(char, False, color, fondo) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect)
        letter += 1
