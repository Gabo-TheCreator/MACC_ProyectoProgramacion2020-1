import pygame
import Letra_one_by_one as one
import Constantes
# =============================================================================
# DEFINICIÓN DE VARIABLES
index_about = 0  #Valor único para la selección del botón en la pantalla de créditos
index = 0  #Valor que va de 0 a 2 para seleccionar alguno de los botones
index_name_x = 1 #Valor en x del menú de selección de nombre
index_name_y = 1 #Valor en y del menú de selección de nombre
index_casual = 1 #No tiene uso. Planeado para usar cuando el jugador seleccione en la pantalla de presentación del juego
level = 0  #Seguramente planeado para seleccionar el nivel implícitamente
name = ""
letters = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",
           12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U",
           22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
menu = True  #Proceso del menú principal
game = True  #Proceso del juego en sí
game_width = 800
game_height = 600
count = 0  #Conteo para la selección de fotograma
cons = Constantes.Constants()
x = 100  #Valor en x cuyo uso cambia dependiendo de donde se invoque


# =============================================================================

pygame.init()

pygame.display.set_caption("Requiem of the Fallen")
clock = pygame.time.Clock()
clock.tick(25)  #El juego anda a 25 FPS, creo
win = pygame.display.set_mode((game_width, game_height)) #Se invoca la pantalla
keys = pygame.key.get_pressed() #Proceso donde se reciben las teclas (tal vez se puedan omitir las que vienen después)

# =============================================================================
# SPRITES
Virus = cons.sprites.virusIdle.ani_1

# =============================================================================

#BOTONES
awa = cons.botones.awa
title = cons.extras.title
PLAY_n = cons.botones.PLAY_n
PLAY_s = cons.botones.PLAY_s
ABOUT_n = cons.botones.ABOUT_n
ABOUT_s = cons.botones.ABOUT_s
EXIT_n = cons.botones.EXIT_n
EXIT_s = cons.botones.EXIT_s
OK_n = cons.botones.OK_n
OK_s = cons.botones.OK_s
DEL_n = cons.botones.DEL_n
DEL_s = cons.botones.DEL_s
bg_tit = cons.extras.bg_tit
bg_tit = pygame.transform.scale(bg_tit, (game_width, game_height))
BACK_n = cons.botones.BACK_n
BACK_s = cons.botones.BACK_s
ATTACK_n = cons.botones.ATTACK_n
ATTACK_s = cons.botones.ATTACK_s
INVENTORY_n = cons.botones.INVENTORY_n
INVENTORY_s = cons.botones.INVENTORY_s
selection_border = cons.extras.selection_border
# =============================================================================

# THEMES/SOUND EFFECTS
mus = cons.música.mus
main_theme = "theme.mp3"
menu_theme = "name.mp3"
low_mana = cons.efectos.low_mana
low_hp = cons.efectos.low_hp
exit_sfx = cons.efectos.exit_sfx
error = cons.efectos.error
EndLine = cons.efectos.EndLine
Dial_o = cons.efectos.Dial_o
Dial_c = cons.efectos.Dial_c
Confirm = cons.efectos.Confirm


# =============================================================================
#LETRAS

a_n = cons.letras.a_n 
a_s = cons.letras.a_s
b_n = cons.letras.b_n 
b_s = cons.letras.b_s
c_n = cons.letras.c_n
c_s = cons.letras.c_s
d_n = cons.letras.d_n 
d_s = cons.letras.d_s
e_n = cons.letras.e_n 
e_s = cons.letras.e_s
f_n = cons.letras.f_n 
f_s = cons.letras.f_s
g_n = cons.letras.g_n 
g_s = cons.letras.g_s
h_n = cons.letras.h_n 
h_s = cons.letras.h_s
i_n = cons.letras.i_n
i_s = cons.letras.i_s
j_n = cons.letras.j_n 
j_s = cons.letras.j_s
k_n = cons.letras.k_n 
k_s = cons.letras.k_s
l_n = cons.letras.l_n 
l_s = cons.letras.l_s
m_n = cons.letras.m_n 
m_s = cons.letras.m_s
n_n = cons.letras.n_n 
n_s = cons.letras.n_s
o_n = cons.letras.o_n 
o_s = cons.letras.o_s
p_n = cons.letras.p_n
p_s = cons.letras.p_s
q_n = cons.letras.q_n 
q_s = cons.letras.q_s
r_n = cons.letras.r_n 
r_s = cons.letras.r_s
s_n = cons.letras.s_n 
s_s = cons.letras.s_s
t_n = cons.letras.t_n 
t_s = cons.letras.t_s
u_n = cons.letras.u_n 
u_s = cons.letras.u_s
v_n = cons.letras.v_n 
v_s = cons.letras.v_s
w_n = cons.letras.w_n 
w_s = cons.letras.w_s
x_n = cons.letras.x_n 
x_s = cons.letras.x_s
y_n = cons.letras.y_n 
y_s = cons.letras.y_s
z_n = cons.letras.z_n 
z_s = cons.letras.z_s

# =============================================================================
#FUNCIONES

def music(song, t): #Añadir música
    global mus
    pygame.mixer.music.load(mus+song)
    pygame.mixer.music.play(t)
def mainMenu(): #Índice menú principal
    global awa
    global index
    global titleImg
    global theme
    global x
    if left:
        index -= 1
        if index < 0:
            index = 2
    elif right:
        index += 1
        if index > 2:
            index = 0
    if index == 0:
        win.blit(awa, (100, 400))
        win.blit(PLAY_s, (125, 412.5))
        x = 100
    elif index == 1:
        win.blit(awa, (300, 400))
        win.blit(ABOUT_s, (325, 412.5))
        x = 300
    elif index == 2:
        win.blit(awa, (500, 400))
        win.blit(EXIT_s, (525, 412.5))
        x = 500
    else:
        win.blit(awa, (x, 400))
        #Aquí la 'x' es para dejar el cuadro de selección en la coordenada x anterior
    pygame.display.update()
def creditMenu(): #Índice del menú de créditos 
    global awa
    global x
    global index_about
    global titleImg
    global theme

    if index_about == 0:
        win.blit(BACK_s, ((game_width / 2) - 59, 412.5))
    pygame.display.update()
def namingScreen(): #Índice de la selección de nombre
    global letters
    global index_name_x, index_name_y
    global a_n, b_n, c_n, d_n, e_n, f_n, g_n, h_n, i_n, j_n, k_n, l_n, m_n, n_n, o_n, p_n, q_n, r_n, s_n, t_n, u_n, v_n, w_n, x_n, y_n, z_n 
    global a_s, b_s, c_s, d_s, e_s, f_s, g_s, h_s, i_s, j_s, k_s, l_s, m_s, n_s, o_s, p_s, q_s, r_s, s_s, t_s, u_s, v_s, w_s, x_s, y_s, z_s 
    global  OK_n, DEL_n, OK_s, DEL_s
    y = 200 #Valor en y predeterminado para la letra en el menú de selección de nombre
    if left:
        EndLine.play()
        index_name_x -= 1
        if index_name_x < 1:
            index_name_x = 6
        elif index_name_x == 3 and index_name_y == 5:
            index_name_x -= 1
        elif index_name_x == 5 and index_name_y == 5:
            index_name_x -= 1
    elif right:
        EndLine.play()
        index_name_x += 1
        if index_name_x > 6:
            index_name_x = 1
        elif index_name_x == 4 and index_name_y == 5:
            index_name_x += 1
        elif index_name_x == 6 and index_name_y == 5:
            index_name_x += 1
    elif up:
        EndLine.play()
        index_name_y -= 1
        if index_name_y < 1:
            index_name_y = 5
    elif down:
        EndLine.play()
        index_name_y += 1
        if index_name_y > 5:
            index_name_y = 1
    if index_name_y == 1:
        if index_name_x == 1:
            win.blit(a_s, (200, y))
        elif index_name_x == 2:
            win.blit(b_s, (248, y))
        elif index_name_x == 3:
            win.blit(c_s, (296, y))
        elif index_name_x == 4:
            win.blit(d_s, (344, y))
        elif index_name_x == 5:
            win.blit(e_s, (392, y))
        elif index_name_x == 6:
            win.blit(f_s, (440, y))
    elif index_name_y == 2:
        if index_name_x == 1:
            win.blit(g_s, (200, y + 40))
        elif index_name_x == 2:
            win.blit(h_s, (248, y + 40))
        elif index_name_x == 3:
            win.blit(i_s, (296, y + 40))
        elif index_name_x == 4:
            win.blit(j_s, (344, y + 40))
        elif index_name_x == 5:
            win.blit(k_s, (392, y + 40))
        elif index_name_x == 6:
            win.blit(l_s, (440, y + 40))
    if index_name_y == 3:
        if index_name_x == 1:
            win.blit(m_s, (200, y + 80))
        elif index_name_x == 2:
            win.blit(n_s, (248, y + 80))
        elif index_name_x == 3:
            win.blit(o_s, (296, y + 80))
        elif index_name_x == 4:
            win.blit(p_s, (344, y + 80))
        elif index_name_x == 5:
            win.blit(q_s, (392, y + 80))
        elif index_name_x == 6:
            win.blit(r_s, (440, y + 80))
    if index_name_y == 4:
        if index_name_x == 1:
            win.blit(s_s, (200, y + 120))
        elif index_name_x == 2:
            win.blit(t_s, (248, y + 120))
        elif index_name_x == 3:
            win.blit(u_s, (296, y + 120))
        elif index_name_x == 4:
            win.blit(v_s, (344, y + 120))
        elif index_name_x == 5:
            win.blit(w_s, (392, y + 120))
        elif index_name_x == 6:
            win.blit(x_s, (440, y + 120))
    if index_name_y == 5:
        if index_name_x == 1:
            win.blit(y_s, (200, y + 160))
        elif index_name_x == 2:
            win.blit(z_s, (248, y + 160))
        elif index_name_x == 3:
            win.blit(OK_s, (296, y + 160))
        elif index_name_x == 4:
            win.blit(OK_s, (296, y + 160))
        elif index_name_x == 5:
            win.blit(DEL_s, (392, y + 160))
        elif index_name_x == 6:
            win.blit(DEL_s, (392, y + 160))
    pygame.display.update()
def idle_menu(pj, x, y): #Aquí va el proceso de animación en la pantalla antes del tutorial
    global count
    global index
    if count + 1 >= 25:
        count = 0
    if idle:
        win.blit(pj[count // 5], (x, y))
        count += 1 #Apenas aumenta este conteo, se seleccióna el nuevo sprite cada 5 frames
    pygame.display.update()

# =============================================================================

# =============================================================================
music(main_theme, -1)
while game: #Procesos del juego
    while menu:
        win.blit(bg_tit, (0, 0))
        win.blit(title, ((game_width / 2) - 216, 100))
        win.blit(PLAY_n, (125, 412.5))
        win.blit(ABOUT_n, (325, 412.5))
        win.blit(EXIT_n, (525, 412.5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            EndLine.play()
            left = True
        elif keys[pygame.K_RIGHT]:
            EndLine.play()
            right = True
            left = False
        elif keys[pygame.K_RETURN]:
            menu = False
            EndLine.play()
        else:
            left = False
            right = False
        pygame.time.delay(150)
        mainMenu()
        pygame.mixer.stop()
    if index == 0:
        music(main_theme,-1)
        win.blit(bg_tit, (0, 0))
        one.text_name("                                ", (175, 100), (255, 255, 255), (0, 0, 0), 60)
        pygame.display.update()
        while index == 0:  # Menú de selección de nombre
            win.blit(a_n, (200, 200)); win.blit(b_n, (248, 200)); win.blit(c_n, (296, 200))
            win.blit(d_n, (344, 200)); win.blit(e_n, (392, 200)); win.blit(f_n, (440, 200))
            win.blit(g_n, (200, 240)); win.blit(h_n, (248, 240));  win.blit(i_n, (296, 240))
            win.blit(j_n, (344, 240)); win.blit(k_n, (392, 240)); win.blit(l_n, (440, 240))
            win.blit(m_n, (200, 280)); win.blit(n_n, (248, 280)); win.blit(o_n, (296, 280))
            win.blit(p_n, (344, 280)); win.blit(q_n, (392, 280)); win.blit(r_n, (440, 280))
            win.blit(s_n, (200, 320));  win.blit(t_n, (248, 320)); win.blit(u_n, (296, 320))
            win.blit(v_n, (344, 320)); win.blit(w_n, (392, 320)); win.blit(x_n, (440, 320))
            win.blit(y_n, (200, 360)); win.blit(z_n, (248, 360))
            win.blit(OK_n, (296, 360)); win.blit(DEL_n, (392, 360))
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
                n = index_name_x + (6 * (index_name_y - 1)) #A cada letra en el diccionario de arriba se le asigna un número
                if len(name) < 10 and len(name) > 0:
                    if n <= 26:
                        EndLine.play()
                        L = letters[n]
                        name += L
                        print(name)
                        one.text_name(name, (175, 100), (255, 255, 255), (0, 0, 0), 60)
                    elif n == 27 or n == 28 and len(name) > 0:
                        Confirm.play()
                        index = -1
                        menu = False
                    elif n == 29 or n == 30:
                        if len(name) > 0:
                            EndLine.play()
                            name = name[:-1]
                            one.text_name(name + "    ", (175, 100), (255, 255, 255), (0, 0, 0), 60)
                            print(name)
                        else:
                            error.play()
                elif len(name) == 10:
                    if n == 29 or n == 30:
                        name = name[:-1]
                        one.text_name(name + "    ", (175, 100), (255, 255, 255), (0, 0, 0), 60)
                        print(name)
                    elif n == 27 or n == 28:
                        index = -1
                        menu = False
                    else:
                        error.play()
                elif len(name) == 0:
                    if n <= 26:
                        EndLine.play()
                        L = letters[n]
                        name += L
                        print(name)
                        one.text_name(name, (175, 100), (255, 255, 255), (0, 0, 0), 60)
                    elif n == 27 or n == 28 or n == 29 or n == 30:
                        error.play()
            else:
                left = False
                right = False
                up = False
                down = False
            pygame.time.delay(150)
            namingScreen()
    if index == 1:
        Confirm.play()
        pygame.time.wait(1000)
        win.blit(bg_tit, (0, 0))
        pygame.display.update()
        one.text("ABOUT", (340, 100), (56, 5, 217), (110, 1100), 70, 0.2)
        one.text("JUAN MANUEL DAVILA RIVERA", (40, 200), (255, 255, 255), (110, 1100), 40, 0.05)
        one.text("GABRIELA LINARES CHAVEZ", (40, 240), (255, 255, 255), (110, 1100), 40, 0.05)
        one.text("JOSE GABRIEL CUADROS CARDENAS", (40, 280), (255, 255, 255), (110, 1100), 40, 0.05)
        one.text("Todos los derechos reservados", (10, 580), (5, 175, 217), (110, 1100), 20, 0.1)
        one.text("2020", (720, 580), (5, 175, 217), (110, 1100), 20, 0.1)
        while index == 1:
            win.blit(BACK_n, ((game_width / 2)- 59, 412.5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                if index_about == 0:
                    Confirm.play()
                    pygame.time.wait(2000)
                    index = 200
                    menu = True
            else:
                left = False
                right = False
            pygame.time.delay(150)
            creditMenu()
    if index == 2:
        exit_sfx.play()
        pygame.time.wait(2000)
        win.blit(bg_tit, (0, 0))
        pygame.display.update()
        one.text("TURNING OFF...", (300, 300), (255, 255, 255), (110, 1100), 40, 0.1)
        win.blit(bg_tit, (0, 0))
        pygame.time.wait(2000)
        game = False
    if index == -1:
        win.blit(bg_tit, (0, 0))
        pygame.display.update()
        one.text("Bienvenido a "'Requiem of the Fallen'", un", (40, 40), (255, 255, 255), (110, 1100), 40, 0.1)
        one.text("juego del tipo RPG por turnos en que tendras", (40, 80), (255, 255, 255), (110, 1100), 40, 0.1)
        one.text("que SALVAR AL MUNDO.", (40, 120), (255, 255, 255), (110, 1100), 50, 0.2)
        one.text(("Ahora, " + name), (40, 170), (255, 255, 255), (110, 1100), 40, 0.1)
        one.text(("este sera tu caballero, con el que"), (40, 210), (255, 255, 255), (110, 1100), 40, 0.1)
        one.text(("te enfrentaras a las garras del mal."), (40, 250), (255, 255, 255), (110, 1100), 40, 0.1)
        while index == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                Confirm.play()
                x = 300
                y = 300
                while x < 650:
                    if count + 1 >= 25:
                        count = 0
                    x += 10
                    win.blit(Virus[count // 5], (x, y))
                    count += 1
                    pygame.display.update()
                index = -2
            else:
                idle = True
            idle_menu(Virus, 300, 300)
pygame.quit()
