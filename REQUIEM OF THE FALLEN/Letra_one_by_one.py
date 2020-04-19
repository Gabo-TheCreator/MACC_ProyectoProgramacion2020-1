import pygame,time
import Constantes as cst
constants = cst.Constants

screen=pygame.display.set_mode((300, 300))

def text(str, tuple,n, z,x,s):
    basicfont = pygame.font.Font("Fonts/8bit.ttf", x)
    x, y = tuple
    
    char = ''        
    letter = 0
    Beep=constants.efectos.Beep
    Beep.play()
    for _ in range(len(str)):
        pygame.event.pump() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        time.sleep(s) ##change this for faster or slower text animation
        char = char + str[letter]
        text = basicfont.render(char, False, n, z) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect) 
        
        
        letter += 1
        if letter%8==0:
            Beep.play()
        
            
def text_name(str, tuple,n, z,x):
    basicfont = pygame.font.Font("Fonts/8bit.ttf", x)
    x, y = tuple
    
    char = ''        
    letter = 0
    
    for _ in range(len(str)):
        pygame.event.pump() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        
        char = char + str[letter]
        text = basicfont.render(char, False, n, z) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect) 
        letter += 1