import pygame
import Letra_one_by_one as one

# =============================================================================
# DEFINICIÓN DE VARIABLES
index_about = 0
index = 0
index_name_x = 1
index_name_y = 1
index_casual = 1
level = 0
name = ""
letters = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",
           12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U",
           22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}

menu = True
game = True
game_width = 800
game_height = 600
count = 0

# =============================================================================

pygame.init()
pygame.display.set_caption("Requiem of the Fallen")
clock = pygame.time.Clock()
clock.tick(25)
win = pygame.display.set_mode((game_width, game_height))

# =============================================================================
# DEFINICIÓN DE SPRITES
villain = [pygame.image.load("i_Virus0.png"), pygame.image.load("i_Virus1.png"), pygame.image.load("i_Virus2.png"),
           pygame.image.load("i_Virus3.png"), pygame.image.load("i_Virus4.png")]
char = pygame.image.load("i_Virus0.png")
awa = pygame.image.load('i_square_blue.png')
title_img = pygame.image.load('i_REQUIEM.png')
play_button_norm = pygame.image.load('i_PLAYnorm.png')
play_button_select = pygame.image.load('i_PLAYselect.png')
about_button_norm = pygame.image.load('i_ABOUTnorm.png')
about_button_select = pygame.image.load('i_ABOUTselect.png')
exit_button_norm = pygame.image.load('i_EXITnorm.png')
exit_button_select = pygame.image.load('i_EXITselect.png')

bg_title = pygame.image.load('bg_stone.jpg')

# =============================================================================
# LETTER SPRITES
a = pygame.image.load('i_anorm.png')
a1 = pygame.image.load('i_aselect.png')
b = pygame.image.load('i_bnorm.png')
b1 = pygame.image.load('i_bselect.png')
c = pygame.image.load('i_cnorm.png')
c1 = pygame.image.load('i_cselect.png')
d = pygame.image.load('i_dnorm.png')
d1 = pygame.image.load('i_dselect.png')
e = pygame.image.load('i_enorm.png')
e1 = pygame.image.load('i_eselect.png')
f = pygame.image.load('i_fnorm.png')
f1 = pygame.image.load('i_fselect.png')
g = pygame.image.load('i_gnorm.png')
g1 = pygame.image.load('i_gselect.png')
h = pygame.image.load('i_hnorm.png')
h1 = pygame.image.load('i_hselect.png')
i = pygame.image.load('i_inorm.png')
i1 = pygame.image.load('i_iselect.png')
j = pygame.image.load('i_jnorm.png')
j1 = pygame.image.load('i_jselect.png')
k = pygame.image.load('i_knorm.png')
k1 = pygame.image.load('i_kselect.png')
l = pygame.image.load('i_lnorm.png')
l1 = pygame.image.load('i_lselect.png')
m = pygame.image.load('i_mnorm.png')
m1 = pygame.image.load('i_mselect.png')
nl = pygame.image.load('i_nnorm.png')
n1 = pygame.image.load('i_nselect.png')
o = pygame.image.load('i_onorm.png')
o1 = pygame.image.load('i_oselect.png')
p = pygame.image.load('i_pnorm.png')
p1 = pygame.image.load('i_pselect.png')
q = pygame.image.load('i_qnorm.png')
q1 = pygame.image.load('i_qselect.png')
r = pygame.image.load('i_rnorm.png')
r1 = pygame.image.load('i_rselect.png')
s = pygame.image.load('i_snorm.png')
s1 = pygame.image.load('i_sselect.png')
t = pygame.image.load('i_tnorm.png')
t1 = pygame.image.load('i_tselect.png')
u = pygame.image.load('i_unorm.png')
u1 = pygame.image.load('i_uselect.png')
v = pygame.image.load('i_vnorm.png')
v1 = pygame.image.load('i_vselect.png')
w = pygame.image.load('i_wnorm.png')
w1 = pygame.image.load('i_wselect.png')
xl = pygame.image.load('i_xnorm.png')
x1 = pygame.image.load('i_xselect.png')
yl = pygame.image.load('i_ynorm.png')
y1 = pygame.image.load('i_yselect.png')
z = pygame.image.load('i_znorm.png')
z1 = pygame.image.load('i_zselect.png')
delete = pygame.image.load('i_DELnorm.png')
delete1 = pygame.image.load('i_DELselect.png')
ok = pygame.image.load('i_oknorm.png')
ok1 = pygame.image.load('i_okselect.png')

# =============================================================================
# THEMES/SOUND EFFECTS

theme = pygame.mixer.music.load('m_theme.mp3')
pygame.mixer.music.play(-1)

# =============================================================================

bg_title = pygame.transform.scale(bg_title, (game_width, game_height))

select_1 = pygame.transform.scale(play_button_select, (150, 75))
select_2 = pygame.transform.scale(about_button_select, (150, 75))
select_3 = pygame.transform.scale(exit_button_select, (150, 75))
exit_1 = pygame.transform.scale(select_3, (80, 45))
exit_2 = pygame.transform.scale(exit_button_norm, (80, 45))
ok_2 = pygame.transform.scale(ok1, (80, 45))
ok_1 = pygame.transform.scale(ok, (80, 45))
x = 100
# win.blit(t, t_rect)
pygame.display.flip()

keys = pygame.key.get_pressed()


# =============================================================================

def mainMenu():
    global fuego
    global awa
    global x
    global index
    global titleImg
    global theme
    # render text
    # 

    if left:
        index -= 1
        if index < 0:
            index = 2

    elif right:
        index += 1
        if index > 2:
            index = 0

    if index == 1:

        awa = pygame.transform.scale(awa, (200, 100))
        win.blit(awa, (300, 400))
        win.blit(select_2, (325, 412.5))
        x = 300

    elif index == 0:

        awa = pygame.transform.scale(awa, (200, 100))
        win.blit(awa, (100, 400))
        win.blit(select_1, (125, 412.5))
        x = 100

    elif index == 2:

        awa = pygame.transform.scale(awa, (200, 100))
        win.blit(awa, (500, 400))
        win.blit(select_3, (525, 412.5))
        x = 500
    else:

        awa = pygame.transform.scale(awa, (200, 100))
        win.blit(awa, (x, 400))

    pygame.display.update()


# =============================================================================
# =============================================================================

def creditMenu():
    global awa
    global x
    global index_about
    global titleImg
    global theme
    # render text
    # 

    if left:
        index_about -= 1
        if index_about < 0:
            index_about = 1

    elif right:
        index_about += 1
        if index_about > 1:
            index_about = 0

    if index_about == 1:

        win.blit(select_3, (425, 412.5))

    elif index_about == 0:

        win.blit(select_1, (225, 412.5))

    pygame.display.update()


# ============================================================================

def namingScreen():
    global letters, exit_1, exit_2
    global index_name_x, index_name_y
    global a, b, c, d, e, f, g, h, i, j, k, l, m, nl, o, p, q, r, s, t, u, v, w, xl, yl, z, ok, delete
    global a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1, q1, r1, s1, t1, u1, v1, w1, x1, y1, z1, ok1, delete1

    y = 200

    if left:
        effect = pygame.mixer.Sound('s_EndLine.wav')
        effect.play()
        index_name_x -= 1
        if index_name_x < 1:
            index_name_x = 6
        elif index_name_x == 3 and index_name_y == 5:
            index_name_x -= 1
        elif index_name_x == 5 and index_name_y == 5:
            index_name_x -= 1

    elif right:
        effect = pygame.mixer.Sound('s_EndLine.wav')
        effect.play()
        index_name_x += 1
        if index_name_x > 6:
            index_name_x = 1
        elif index_name_x == 4 and index_name_y == 5:
            index_name_x += 1
        elif index_name_x == 6 and index_name_y == 5:
            index_name_x += 1

    elif up:
        effect = pygame.mixer.Sound('s_EndLine.wav')
        effect.play()
        index_name_y -= 1
        if index_name_y < 1:
            index_name_y = 5

    elif down:
        effect = pygame.mixer.Sound('s_EndLine.wav')
        effect.play()
        index_name_y += 1
        if index_name_y > 5:
            index_name_y = 1

    if index_name_y == 1:
        if index_name_x == 1:
            win.blit(a1, (200, y))

        elif index_name_x == 2:
            win.blit(b1, (248, y))

        elif index_name_x == 3:
            win.blit(c1, (296, y))

        elif index_name_x == 4:
            win.blit(d1, (344, y))

        elif index_name_x == 5:
            win.blit(e1, (392, y))

        elif index_name_x == 6:
            win.blit(f1, (440, y))

    elif index_name_y == 2:
        if index_name_x == 1:
            win.blit(g1, (200, y + 40))

        elif index_name_x == 2:
            win.blit(h1, (248, y + 40))

        elif index_name_x == 3:
            win.blit(i1, (296, y + 40))

        elif index_name_x == 4:
            win.blit(j1, (344, y + 40))

        elif index_name_x == 5:
            win.blit(k1, (392, y + 40))

        elif index_name_x == 6:
            win.blit(l1, (440, y + 40))

    if index_name_y == 3:
        if index_name_x == 1:
            win.blit(m1, (200, y + 80))

        elif index_name_x == 2:
            win.blit(n1, (248, y + 80))

        elif index_name_x == 3:
            win.blit(o1, (296, y + 80))

        elif index_name_x == 4:
            win.blit(p1, (344, y + 80))

        elif index_name_x == 5:
            win.blit(q1, (392, y + 80))

        elif index_name_x == 6:
            win.blit(r1, (440, y + 80))

    if index_name_y == 4:
        if index_name_x == 1:
            win.blit(s1, (200, y + 120))

        elif index_name_x == 2:
            win.blit(t1, (248, y + 120))

        elif index_name_x == 3:
            win.blit(u1, (296, y + 120))

        elif index_name_x == 4:
            win.blit(v1, (344, y + 120))

        elif index_name_x == 5:
            win.blit(w1, (392, y + 120))

        elif index_name_x == 6:
            win.blit(x1, (440, y + 120))

    if index_name_y == 5:
        if index_name_x == 1:
            win.blit(y1, (200, y + 160))

        elif index_name_x == 2:
            win.blit(z1, (248, y + 160))

        elif index_name_x == 3:
            win.blit(ok1, (296, y + 160))

        elif index_name_x == 4:
            win.blit(ok1, (296, y + 160))

        elif index_name_x == 5:
            win.blit(delete1, (392, y + 160))

        elif index_name_x == 6:
            win.blit(delete1, (392, y + 160))

    pygame.display.update()


# =============================================================================

# =============================================================================
def idle_menu(pj, x, y):
    global count
    global index

    if count + 1 >= 25:
        count = 0

    if idle:
        win.blit(pj[count // 5], (x, y))
        count += 1

    pygame.display.update()


# =============================================================================

# =============================================================================

while game:
    while menu:
        win.blit(bg_title, (0, 0))
        win.blit(title_img, ((game_width / 2) - 216, 100))
        play_button_norm = pygame.transform.scale(play_button_norm, (150, 75))
        win.blit(play_button_norm, (125, 412.5))
        about_button_norm = pygame.transform.scale(about_button_norm, (150, 75))
        win.blit(about_button_norm, (325, 412.5))
        exit_button_norm = pygame.transform.scale(exit_button_norm, (150, 75))
        win.blit(exit_button_norm, (525, 412.5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            effect = pygame.mixer.Sound('s_EndLine.wav')
            effect.play()
            left = True

        elif keys[pygame.K_RIGHT]:
            effect = pygame.mixer.Sound('s_EndLine.wav')
            effect.play()
            right = True
            left = False

        elif keys[pygame.K_RETURN]:
            menu = False
            effect = pygame.mixer.Sound('s_EndLine.wav')
            effect.play()
        else:
            left = False
            right = False

        pygame.time.delay(150)
        mainMenu()
    pygame.mixer.music.stop()
    if index == 0:
        theme = pygame.mixer.music.load("name.mp3")
        pygame.mixer.music.play(-1)
        win.blit(bg_title, (0, 0))
        one.text_name("                                ", (175, 100), (255, 255, 255), (0, 0, 0), 60)
        pygame.display.update()

        while index == 0:  # Menú de selección de nombre

            win.blit(a, (200, 200))
            win.blit(b, (248, 200))
            win.blit(c, (296, 200))
            win.blit(d, (344, 200))
            win.blit(e, (392, 200))
            win.blit(f, (440, 200))

            win.blit(g, (200, 240))
            win.blit(h, (248, 240))
            win.blit(i, (296, 240))
            win.blit(j, (344, 240))
            win.blit(k, (392, 240))
            win.blit(l, (440, 240))

            win.blit(m, (200, 280))
            win.blit(nl, (248, 280))
            win.blit(o, (296, 280))
            win.blit(p, (344, 280))
            win.blit(q, (392, 280))
            win.blit(r, (440, 280))

            win.blit(s, (200, 320))
            win.blit(t, (248, 320))
            win.blit(u, (296, 320))
            win.blit(v, (344, 320))
            win.blit(w, (392, 320))
            win.blit(xl, (440, 320))

            win.blit(yl, (200, 360))
            win.blit(z, (248, 360))
            win.blit(ok, (296, 360))
            win.blit(delete, (392, 360))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:

                left = True

            elif keys[pygame.K_UP]:
                up = True
                down = False

            elif keys[pygame.K_DOWN]:
                down = True
                up = False

            elif keys[pygame.K_RIGHT]:

                right = True
                left = False

            elif keys[pygame.K_RETURN]:  # Selección de la letra para el nombre

                n = index_name_x + (6 * (index_name_y - 1))
                if len(name) < 10 and len(name) > 0:

                    if n <= 26:
                        effect = pygame.mixer.Sound('s_EndLine.wav')
                        effect.play()
                        L = letters[n]
                        name += L
                        print(name)
                        one.text_name(name, (175, 100), (255, 255, 255), (0, 0, 0), 60)

                    elif n == 27 or n == 28 and len(name) > 0:
                        effect = pygame.mixer.Sound('s_Confirm.wav')
                        effect.play()
                        index = -1
                        menu = False

                    elif n == 29 or n == 30:

                        if len(name) > 0:
                            effect = pygame.mixer.Sound('s_EndLine.wav')
                            effect.play()
                            name = name[:-1]
                            one.text_name(name + "    ", (175, 100), (255, 255, 255), (0, 0, 0), 60)
                            print(name)
                        else:
                            effect = pygame.mixer.Sound('s_error.wav')
                            effect.play()



                elif len(name) == 10:

                    if n == 29 or n == 30:

                        name = name[:-1]

                        one.text_name(name + "    ", (175, 100), (255, 255, 255), (0, 0, 0), 60)
                        print(name)

                    elif n == 27 or n == 28:
                        index = -1
                        menu = False

                    else:
                        effect = pygame.mixer.Sound('s_error.wav')
                        effect.play()

                elif len(name) == 0:
                    if n <= 26:
                        effect = pygame.mixer.Sound('s_EndLine.wav')
                        effect.play()
                        L = letters[n]
                        name += L
                        print(name)
                        one.text_name(name, (175, 100), (255, 255, 255), (0, 0, 0), 60)

                    elif n == 27 or n == 28 or n == 29 or n == 30:
                        effect = pygame.mixer.Sound('s_error.wav')
                        effect.play()


            else:
                left = False
                right = False
                up = False
                down = False

            pygame.time.delay(150)
            namingScreen()

    if index == 1:
        effect = pygame.mixer.Sound('s_Confirm.wav')
        effect.play()
        pygame.time.wait(1000)
        win.blit(bg_title, (0, 0))
        pygame.display.update()
        one.text("ABOUT", (340, 100), (56, 5, 217), (0, 0, 0), 70, 0.2)

        one.text("JUAN MANUEL DAVILA RIVERA", (40, 200), (255, 255, 255), (0, 0, 0), 40, 0.05)
        one.text("GABRIELA LINARES CHAVEZ", (40, 240), (255, 255, 255), (0, 0, 0), 40, 0.05)
        one.text("JOSE GABRIEL CUADROS CARDENAS", (40, 280), (255, 255, 255), (0, 0, 0), 40, 0.05)

        one.text("Todos los derechos reservados", (10, 580), (5, 175, 217), (0, 0, 0), 20, 0.1)
        one.text("2020", (720, 580), (5, 175, 217), (0, 0, 0), 20, 0.1)

        while index == 1:

            play_button_norm = pygame.transform.scale(play_button_norm, (150, 75))
            win.blit(play_button_norm, (225, 412.5))
            exit_button_norm = pygame.transform.scale(exit_button_norm, (150, 75))
            win.blit(exit_button_norm, (425, 412.5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                effect = pygame.mixer.Sound('s_EndLine.wav')
                effect.play()
                left = True

            elif keys[pygame.K_RIGHT]:
                effect = pygame.mixer.Sound('s_EndLine.wav')
                effect.play()
                right = True
                left = False

            elif keys[pygame.K_RETURN]:
                if index_about == 0:
                    effect = pygame.mixer.Sound('s_Confirm.wav')
                    effect.play()
                    pygame.time.wait(2000)
                    index = 0
                elif index_about == 1:

                    index = 2

            else:
                left = False
                right = False

            pygame.time.delay(150)
            creditMenu()
    if index == 2:
        effect = pygame.mixer.Sound('s_exit.wav')
        effect.play()
        pygame.time.wait(2000)
        win.blit(bg_title, (0, 0))
        pygame.display.update()
        one.text("TURNING OFF...", (300, 300), (255, 255, 255), (0, 0, 0), 40, 0.1)

        win.blit(bg_title, (0, 0))
        game = False

    if index == -1:
        win.blit(bg_title, (0, 0))
        pygame.display.update()
        one.text("Bienvenido a "'Requiem of the Fallen'", un", (40, 40), (255, 255, 255), (0, 0, 0), 40, 0.1)
        one.text("juego del tipo RPG por turnos en que tendras", (40, 80), (255, 255, 255), (0, 0, 0), 40, 0.1)
        one.text("que SALVAR AL MUNDO.", (40, 120), (255, 255, 255), (0, 0, 0), 50, 0.2)
        one.text(("Ahora, " + name), (40, 170), (255, 255, 255), (0, 0, 0), 40, 0.1)
        one.text(("este sera tu caballero, con el que"), (40, 210), (255, 255, 255), (0, 0, 0), 40, 0.1)
        one.text(("te enfrentaras a las garras del mal."), (40, 250), (255, 255, 255), (0, 0, 0), 40, 0.1)

        while index == -1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:

                effect = pygame.mixer.Sound('s_Confirm.wav')
                effect.play()
                x = 300
                y = 300
                while x < 650:
                    if count + 1 >= 25:
                        count = 0
                    x += 10
                    win.blit(villain[count // 5], (x, y))
                    count += 1

                    pygame.display.update()
                index = -2

            else:
                idle = True

            idle_menu(villain, 300, 300)

pygame.quit()
