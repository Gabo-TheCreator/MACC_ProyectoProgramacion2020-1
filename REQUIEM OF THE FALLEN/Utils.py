import pygame, time
import Constantes as cst
import Common as common
from enums import Enums

constants = cst.Constants

#Funciones que se utilizan a lo largo del juego
# ======= DRAW TEXT IN COORDS =========================================================
def drawText(screen, text, coords, color, backgroundColor, size, __time, animationType=Enums.TextAnimations.none):
    shouldBeep = True

    if animationType == Enums.TextAnimations.none:
        # Disable Animations when the TextAnimation state is equal to .none
        __time = 0
        shouldBeep = False
    elif animationType == Enums.TextAnimations.typewriter:
        # Enable Animations when the TextAnimation state is equal to .typewriter
        __time = __time
        shouldBeep = True

    basicfont = pygame.font.Font(constants.generalSettings.generalFont, size)
    x, y = coords
    char = ""
    letter = 0
    if shouldBeep:
        common.Beep.play()

    for _ in range(len(text)):
        pygame.event.pump()  ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        pygame.time.delay(__time) ##change this for faster or slower text animation
        char = char + text[letter]
        txt = basicfont.render(char, False, color, backgroundColor)  # First tuple is text color, second tuple is background color
        textrect = txt.get_rect(topleft=(x, y))  ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(txt, textrect)
        pygame.display.update(textrect)

        letter += 1
        if letter % 8 == 0:
            if shouldBeep:
                common.Beep.play()

    if shouldBeep:
        common.EndLine.play()
#Función que muestra un texto un caracter a la vez, con una animación determinada en "none" si se desea la animación más rápida poisble
#o "typewriter" si se desea regular la velocidad
#Reproduce un sonido cada 8 caracteres para no saturar las salidas de audio ni al jugador

# ======= PLAY MUSIC =========================================================
def music(song, times): #Añadir música
    print("PLaying music")
    pygame.mixer.music.load(constants.musica.mus+song)
    pygame.mixer.music.play(times)
#Simplificación de la función para reproducir música
def waitBeforeLoadingNextActions(screen):
    if screen == Enums.Screens.about:
        pygame.time.wait(1000)

    elif screen == Enums.Screens.introduction:
        pygame.time.wait(2000)

    elif screen == Enums.Screens.inGame:
        pygame.time.wait(1000)
#Simplificación de añadir un tiempo de espera, dependiendo de la pantalla en que se encuentre
def drawLabel(screen, text, color, background, size, coord):
    font = pygame.font.Font(constants.generalSettings.generalFont, size)
    showText = font.render(text, True, color, background)
    screen.blit(showText, coord)
#Similar al drawText, esta función muestra un texto sin animación alguna