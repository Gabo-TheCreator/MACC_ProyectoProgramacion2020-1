from pygame_functions import *
from Item import Item
from Ataque import Ataque
from inGame import *

# =============== SHORTCUTS =================== #

img = "Images/"
spr = "Sprites/"
bg = "BackGround/"
txt = "Text/"
lett = "Letters/"
but = "Buttons/"
bg = "BackGround/"
snd = "Sounds/"
mus = "Music/"
sfx = "Effects/"
att = "Attack/"
idle = "Idle/"
cab = "Caballero/"
vir = "Virus/"
inv = "Inventory/"
slash = "Slash/"
mag = "Magic/"

# =============== SCREEN STUFF =================== #

wn = screenSize(800, 600)
border = pygame.image.load(img + bg + "selection_border.png")

# ================ CHARACTER SPRITES ================== #

caballero = makeSprite(img + spr + idle + cab + "caballerito_idle0.png")
addSpriteImage(caballero, img + spr + idle + cab + "caballerito_idle1.png")
addSpriteImage(caballero, img + spr + idle + cab + "caballerito_idle2.png")
addSpriteImage(caballero, img + spr + idle + cab + "caballerito_idle3.png")
addSpriteImage(caballero, img + spr + idle + cab + "caballerito_idle4.png")
#Define los sprites del caballero en reposo

caballeroA = makeSprite(img + spr + att + cab + "caballerito_attack0.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack1.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack2.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack3.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack4.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack5.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack6.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack7.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack8.png")
#Define los sprites del caballero en ataque


virus = makeSprite(img + spr + idle + vir + "Virus_idle0.png")
addSpriteImage(virus, img + spr + idle + vir + "Virus_idle1.png")
addSpriteImage(virus, img + spr + idle + vir + "Virus_idle2.png")
addSpriteImage(virus, img + spr + idle + vir + "Virus_idle3.png")
addSpriteImage(virus, img + spr + idle + vir + "Virus_idle4.png")
#Define los sprites del virus en reposo

# =============== ATTACK EFFECTS AND OBJECT CREATION =================== #

Slash = makeSprite(img + spr + sfx + slash + "slash0.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash1.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash2.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash3.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash4.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash5.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash6.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash7.png")
#Define los sprites del espadazo

Magic = makeSprite(img + spr + sfx + mag + "magic_effect0.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect1.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect2.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect3.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect4.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect5.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect6.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect7.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect8.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect9.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect10.png")
addSpriteImage(Magic, img + spr + sfx + mag + "magic_effect11.png")
#Define los sprites del hechizo

slash_attack = Ataque(10, 0, "Slash", 1.0)
magic_enemy = Ataque(15, 0, "Magic Spell", 1.0)
magic_player = Ataque(30, 10, "Magic Spell", 1.0)
miss = Ataque(0, 0, "Miss!", 1.0)
#define los tipos de ataques
# =============== ITEM SPRITES AND OBJECT CREATION =================== #

health_bottle = pygame.image.load(img + spr + inv + "Botella_health.png")
boost_bottle = pygame.image.load(img + spr + inv + "Botella_boost.png")
empty_bottle = pygame.image.load(img + spr + inv + "Botella_vacia.png")
mana_bottle = pygame.image.load(img + spr + inv + "Botella_mana.png")

health_potion = Item(50, 0, 0, "Health Potion", health_bottle)
boost_potion = Item(0, 0, 1.5, "Boost Potion", boost_bottle)
empty_potion = Item(0, 0, 0, "Empty Bottle", empty_bottle)
mana_potion = Item(0, 50, 0, "Mana Potion", mana_bottle)

#Define los valores de las pociones (Inutilizado)

# =============== ANIMATION FUNCTIONS =================== #
nextFrame = clock()
frame = 1
#Inicia el tiempo y el frame
def idleAnimations():
    global frame, nextFrame
    hideSprite(caballeroA)
    hideSprite(Magic)
    hideSprite(Slash)
    hideSprite(Magic)
    moveSprite(caballero, 200, 168, True)
    showSprite(caballero)
    moveSprite(virus, 600, 168, True)
    showSprite(virus)
    frame = (frame + 1) % 5  # Son 5 sprites los que tiene el caballerito idle
    nextFrame += 0
    changeSpriteImage(caballero, 0 * 5 + frame)
    changeSpriteImage(virus, 0 * 5 + frame)
    pygame.time.wait(100)
    #Genera la animación simultánea del enemigo y el jugador

def attackAnimations(SpriteName, xcor, ycor, pngnum, frameaddition, waitTime):
    global frame, nextFrame
    moveSprite(SpriteName, xcor, ycor, True)
    showSprite(SpriteName)
    frame = (frame + 1) % pngnum  # El número de imágenes o frames por cada animación
    nextFrame += frameaddition
    changeSpriteImage(SpriteName, 0 * pngnum + frame)
    pygame.time.wait(waitTime)
    #Muestra la animación del personajer seleccionado, con los argumentos dados


def effectAnimations(EffectName, xcor, ycor, pngnum, frameaddition, waitTime):
    global frame, nextFrame
    moveSprite(EffectName, xcor, ycor, True)
    showSprite(EffectName)
    frame = (frame + 1) % pngnum
    nextFrame += frameaddition
    changeSpriteImage(EffectName, 0 * pngnum + frame)
    pygame.time.wait(waitTime)
    #Muestra la animación del efecto seleccionado con los argumentos dados
