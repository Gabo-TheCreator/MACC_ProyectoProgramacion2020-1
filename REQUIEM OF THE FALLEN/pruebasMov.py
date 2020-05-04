import pygame
#Pruebas de movimiento con funciones directas de pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Trial First Game")

# walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
#              pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
#              pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

# walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
#             pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
#             pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

# bg = pygame.image.load('bg.jpg')

# char = pygame.image.load('standing.png')

clock = pygame.time.Clock()
width = 40
height = 60
x = 50
y = 400
w = 500
h = 100
r = 0
vel = 7
jumps = 0

run = True
jumpFun = False
jumpCount = 10
walkCount = 0
def music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)


def attack():
    global run, x, y, w, h, r, vel, jumps, clock, char, walkCount, jumpCount, jumpFun, music
    music("Sounds/Music/theme.mp3")
    def redrawGameWin():
        global walkCount

        pygame.draw.rect(win, (30, 202, 30), (0, 400, 500, 100))
        win.blit(bg, (0, 0))

        if walkCount + 1 >= 27:
            walkCount = 0

        if left:
            win.blit(walkLeft[walkCount // 3], (x, y + 25))
            walkCount += 1


        elif right:
            win.blit(walkRight[walkCount // 3], (x, y + 25))
            walkCount += 1

        if r == 0:
            win.blit(char, (x, y + 25))

        elif r == 1.5:
            win.blit(char, (x, y + 25))

        pygame.display.update()

    # mainloop
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        left = False
        right = False
        if keys[pygame.K_RIGHT]:
            r = 1

        if r == 1 or r == 1.5:
            x += vel

            walkCount += 1
            right = True
            if r == 1.5:
                r = 2
                pygame.time.wait(1000)

            if x > 400 and r == 1:
                walkCount = 0
                right = False

                r = 1.5
                pygame.time.wait(500)

                jumps = 0

        if r == 2:
            vel = 12
            x -= vel

            walkCount += 1
            left = True
            right = False

            if jumps <= 1:
                jumpFun = True
                jumps += 1

            if x <= 40:
                r = 0
                vel = 7

        if jumpFun:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 2
            else:
                jumpFun = False
                jumpCount = 10

        redrawGameWin()

    pygame.quit()


attack()
