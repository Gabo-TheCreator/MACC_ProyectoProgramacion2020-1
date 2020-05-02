from pygame_functions import *

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
#==================================#
wn = screenSize(800, 600)
border = pygame.image.load(img + bg + "selection_border.png")
#==================================#

caballero = makeSprite(img + spr + idle + cab + "caballerito_idle0.png")
addSpriteImage(caballero, img + spr + idle + cab + "caballerito_idle1.png")
addSpriteImage(caballero, img + spr + idle + cab + "caballerito_idle2.png")
addSpriteImage(caballero, img + spr + idle + cab + "caballerito_idle3.png")
addSpriteImage(caballero, img + spr + idle + cab + "caballerito_idle4.png")

caballeroA = makeSprite(img + spr + att + cab + "caballerito_attack0.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack1.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack2.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack3.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack4.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack5.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack6.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack7.png")
addSpriteImage(caballeroA, img + spr + att + cab + "caballerito_attack8.png")

virus = makeSprite(img + spr + idle + vir + "Virus_idle0.png")
addSpriteImage(virus, img + spr + idle + vir + "Virus_idle1.png")
addSpriteImage(virus, img + spr + idle + vir + "Virus_idle2.png")
addSpriteImage(virus, img + spr + idle + vir + "Virus_idle3.png")
addSpriteImage(virus, img + spr + idle + vir + "Virus_idle4.png")
#==================================#

Slash = makeSprite(img + spr + sfx + slash + "slash0.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash1.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash2.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash3.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash4.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash5.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash6.png")
addSpriteImage(Slash, img + spr + sfx + slash + "slash7.png")
