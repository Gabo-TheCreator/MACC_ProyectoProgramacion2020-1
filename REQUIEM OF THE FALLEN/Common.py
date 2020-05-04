import pygame
import Constantes

# Init Constantes.Constants() in cons
cons = Constantes.Constants()

# Init all needed variables
# ======= SPRITES =========================================================

#A lo largo de toda esta página, se recogen los archivos más utilizados desde el módulo
#Constantes.py para utilizarse más eficientemente
# ======= BOTONES =========================================================
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
bg_cut = cons.extras.bg_cut
selection_border = cons.extras.selection_border

BACK_n = cons.botones.BACK_n
BACK_s = cons.botones.BACK_s
SLASH_n = cons.botones.SLASH_n
SLASH_s = cons.botones.SLASH_s
SPELL_n  = cons.botones.SPELL_n
SPELL_s  = cons.botones.SPELL_s
HEALTH_n = cons.botones.HEALTH_n
HEALTH_s = cons.botones.HEALTH_s
BOOST_n = cons.botones.BOOST_n
BOOST_s = cons.botones.BOOST_s
EMPTY_n = cons.botones.EMPTY_n
EMPTY_s = cons.botones.EMPTY_s
MANA_n = cons.botones.MANA_n
MANA_s = cons.botones.MANA_s

# ======= THEMES/SOUND EFFECTS =============================================

mus = cons.musica.mus
main_theme = "theme.mp3"
menu_theme = "name.mp3"
battle = "battle.mp3"
about_mus = "About_mus.mp3"
low_mana = cons.efectos.low_mana
low_hp = cons.efectos.low_hp
exit_sfx = cons.efectos.exit_sfx
error = cons.efectos.error
EndLine = cons.efectos.EndLine
Dial_o = cons.efectos.Dial_o
Dial_c = cons.efectos.Dial_c
Confirm = cons.efectos.Confirm
Beep = cons.efectos.Beep

# ======= LETRAS ===========================================================
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
