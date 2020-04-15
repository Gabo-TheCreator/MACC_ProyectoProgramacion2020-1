import pygame,time


screen=pygame.display.set_mode((300, 300))

def text(str, tuple,n, z,x,s):
    basicfont = pygame.font.Font("8bit_2.ttf", x)
    x, y = tuple
    
    char = ''        
    letter = 0
    effect = pygame.mixer.Sound('s_beep.wav')
    effect.play()
    for i in range(len(str)):
        pygame.event.pump() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        time.sleep(s) ##change this for faster or slower text animation
        char = char + str[letter]
        text = basicfont.render(char, False, n, z) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect) 
        
        
        letter += 1
        if letter%8==0:
            effect = pygame.mixer.Sound('s_beep.wav')
            effect.play()
        
            
def text_name(str, tuple,n, z,x):
    basicfont = pygame.font.Font("8bit_2.ttf", x)
    x, y = tuple
    
    char = ''        
    letter = 0
    
    for i in range(len(str)):
        pygame.event.pump() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        
        char = char + str[letter]
        text = basicfont.render(char, False, n, z) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect) 
        letter += 1
    
        
 
