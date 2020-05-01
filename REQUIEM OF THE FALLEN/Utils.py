import pygame, time
import Constantes as cst
import Common as common
from enums import Enums

constants = cst.Constants


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

# ======= PLAY MUSIC =========================================================
def music(song, times): #Añadir música
    print("PLaying music")
    pygame.mixer.music.load(constants.musica.mus+song)
    pygame.mixer.music.play(times)

def waitBeforeLoadingNextActions(screen):
    if screen == Enums.Screens.about:
        pygame.time.wait(1000)

    elif screen == Enums.Screens.introduction:
        pygame.time.wait(2000)

    elif screen == Enums.Screens.inGame:
        pygame.time.wait(1000)