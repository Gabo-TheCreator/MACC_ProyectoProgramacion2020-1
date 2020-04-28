import pygame

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
pygame.mixer.init()


# # ====================================================================
class Constants:
    # =====  LETRAS MENÚ  ==================================================
    class letras:
        a_n = pygame.image.load(img + txt + lett + "anorm.png")
        a_s = pygame.image.load(img + txt + lett + "aselect.png")
        b_n = pygame.image.load(img + txt + lett + "bnorm.png")
        b_s = pygame.image.load(img + txt + lett + "bselect.png")
        c_n = pygame.image.load(img + txt + lett + "cnorm.png")
        c_s = pygame.image.load(img + txt + lett + "cselect.png")
        d_n = pygame.image.load(img + txt + lett + "dnorm.png")
        d_s = pygame.image.load(img + txt + lett + "dselect.png")
        e_n = pygame.image.load(img + txt + lett + "enorm.png")
        e_s = pygame.image.load(img + txt + lett + "eselect.png")
        f_n = pygame.image.load(img + txt + lett + "fnorm.png")
        f_s = pygame.image.load(img + txt + lett + "fselect.png")
        g_n = pygame.image.load(img + txt + lett + "gnorm.png")
        g_s = pygame.image.load(img + txt + lett + "gselect.png")
        h_n = pygame.image.load(img + txt + lett + "hnorm.png")
        h_s = pygame.image.load(img + txt + lett + "hselect.png")
        i_n = pygame.image.load(img + txt + lett + "inorm.png")
        i_s = pygame.image.load(img + txt + lett + "iselect.png")
        j_n = pygame.image.load(img + txt + lett + "jnorm.png")
        j_s = pygame.image.load(img + txt + lett + "jselect.png")
        k_n = pygame.image.load(img + txt + lett + "knorm.png")
        k_s = pygame.image.load(img + txt + lett + "kselect.png")
        l_n = pygame.image.load(img + txt + lett + "lnorm.png")
        l_s = pygame.image.load(img + txt + lett + "lselect.png")
        m_n = pygame.image.load(img + txt + lett + "mnorm.png")
        m_s = pygame.image.load(img + txt + lett + "mselect.png")
        n_n = pygame.image.load(img + txt + lett + "nnorm.png")
        n_s = pygame.image.load(img + txt + lett + "nselect.png")
        o_n = pygame.image.load(img + txt + lett + "onorm.png")
        o_s = pygame.image.load(img + txt + lett + "oselect.png")
        p_n = pygame.image.load(img + txt + lett + "pnorm.png")
        p_s = pygame.image.load(img + txt + lett + "pselect.png")
        q_n = pygame.image.load(img + txt + lett + "qnorm.png")
        q_s = pygame.image.load(img + txt + lett + "qselect.png")
        r_n = pygame.image.load(img + txt + lett + "rnorm.png")
        r_s = pygame.image.load(img + txt + lett + "rselect.png")
        s_n = pygame.image.load(img + txt + lett + "snorm.png")
        s_s = pygame.image.load(img + txt + lett + "sselect.png")
        t_n = pygame.image.load(img + txt + lett + "tnorm.png")
        t_s = pygame.image.load(img + txt + lett + "tselect.png")
        u_n = pygame.image.load(img + txt + lett + "unorm.png")
        u_s = pygame.image.load(img + txt + lett + "uselect.png")
        v_n = pygame.image.load(img + txt + lett + "vnorm.png")
        v_s = pygame.image.load(img + txt + lett + "vselect.png")
        w_n = pygame.image.load(img + txt + lett + "wnorm.png")
        w_s = pygame.image.load(img + txt + lett + "wselect.png")
        x_n = pygame.image.load(img + txt + lett + "xnorm.png")
        x_s = pygame.image.load(img + txt + lett + "xselect.png")
        y_n = pygame.image.load(img + txt + lett + "ynorm.png")
        y_s = pygame.image.load(img + txt + lett + "yselect.png")
        z_n = pygame.image.load(img + txt + lett + "znorm.png")
        z_s = pygame.image.load(img + txt + lett + "zselect.png")

    # =======================================================================
    # ========  BOTONES MENÚ  ================================================
    class botones:
        ABOUT_n = pygame.image.load(img + txt + but + "ABOUTnorm.png")
        ABOUT_s = pygame.image.load(img + txt + but + "ABOUTselect.png")
        DEL_n = pygame.image.load(img + txt + but + "DELnorm.png")
        DEL_s = pygame.image.load(img + txt + but + "DELselect.png")
        EXIT_n = pygame.image.load(img + txt + but + "EXITnorm.png")
        EXIT_s = pygame.image.load(img + txt + but + "EXITselect.png")
        OK_n = pygame.image.load(img + txt + but + "oknorm.png")
        OK_s = pygame.image.load(img + txt + but + "okselect.png")
        PLAY_n = pygame.image.load(img + txt + but + "PLAYnorm.png")
        PLAY_s = pygame.image.load(img + txt + but + "PLAYselect.png")
        BACK_n = pygame.image.load(img + txt + but + "BACKnorm.png")
        BACK_s = pygame.image.load(img + txt + but + "BACKselect.png")
        BACK_n = pygame.transform.scale(BACK_n, (150, 75))
        BACK_s = pygame.transform.scale(BACK_s, (150, 75))
        PLAY_n = pygame.transform.scale(PLAY_n, (150, 75))
        ABOUT_n = pygame.transform.scale(ABOUT_n, (150, 75))
        EXIT_n = pygame.transform.scale(EXIT_n, (150, 75))
        PLAY_s = pygame.transform.scale(PLAY_s, (150, 75))
        ABOUT_s = pygame.transform.scale(ABOUT_s, (150, 75))
        EXIT_s = pygame.transform.scale(EXIT_s, (150, 75))
        OK_n = pygame.transform.scale(OK_n, (80, 45))
        OK_s = pygame.transform.scale(OK_s, (80, 45))
        awa = pygame.image.load(img + txt + but + "square_blue.png")
        awa = pygame.transform.scale(awa, (200, 100))
        ATTACK_n = pygame.image.load(img + txt + but + "ATTACKnorm.png")
        ATTACK_s = pygame.image.load(img + txt + but + "ATTACKselect.png")
        ATTACK_n = pygame.transform.scale(ATTACK_n, (150, 75))
        ATTACK_s = pygame.transform.scale(ATTACK_s, (150, 75))
        INVENTORY_n = pygame.image.load(img + txt + but + "INVENTORYnorm.png")
        INVENTORY_s = pygame.image.load(img + txt + but + "INVENTORYselect.png")
        INVENTORY_n = pygame.transform.scale(INVENTORY_n, (150, 75))
        INVENTORY_s = pygame.transform.scale(INVENTORY_s, (150, 75))
    # ========================================================================
    # ========  IMÁGENES  ====================================================
    class extras:
        bg_tit = pygame.image.load(img + bg + "stone2.jpg")
        bg_2 = pygame.image.load(img + bg + "stone.jpg")
        title = pygame.image.load(img + txt + "REQUIEM.png")
        selection_border = pygame.image.load(img + bg + "selection_border.png")

    # ========================================================================
    # ========== SONIDOS  ====================================================
    class musica:
        mus = snd + mus

    class efectos:
        low_mana = pygame.mixer.Sound(snd + sfx + "low_mana.wav")
        low_hp = pygame.mixer.Sound(snd + sfx + "low_hp.wav")
        exit_sfx = pygame.mixer.Sound(snd + sfx + "exit.wav")
        error = pygame.mixer.Sound(snd + sfx + "error.wav")
        EndLine = pygame.mixer.Sound(snd + sfx + "EndLine.wav")
        Dial_o = pygame.mixer.Sound(snd + sfx + "dialogo_o.wav")
        Dial_c = pygame.mixer.Sound(snd + sfx + "dialogo_c.wav")
        Confirm = pygame.mixer.Sound(snd + sfx + "Confirm.wav")
        Beep = pygame.mixer.Sound(snd + sfx + "beep.wav")

        class slashEffect:
            ani_1 = [pygame.image.load(img + spr + sfx + slash + "slash0.png"),
                     pygame.image.load(img + spr + sfx + slash + "slash1.png"),
                     pygame.image.load(img + spr + sfx + slash + "slash2.png"),
                     pygame.image.load(img + spr + sfx + slash + "slash3.png"),
                     pygame.image.load(img + spr + sfx + slash + "slash4.png"),
                     pygame.image.load(img + spr + sfx + slash + "slash5.png"),
                     pygame.image.load(img + spr + sfx + slash + "slash6.png"),
                     pygame.image.load(img + spr + sfx + slash + "slash7.png")]

        class magicEffect:
            ani_1 =  [pygame.image.load(img + spr + sfx + mag + "magic_effect0.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect1.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect2.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect3.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect4.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect5.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect6.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect7.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect8.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect9.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect10.png"),
                      pygame.image.load(img + spr + sfx + mag + "magic_effect11.png")]

    # ========================================================================
    # ========  SPRITES  =====================================================
    class sprites:
        class Inventory:
            health_potion = pygame.image.load(img + spr + inv + "Botella_health.png")
            boost_potion = pygame.image.load(img + spr + inv + "Botella_boost.png")
            empty_potion = pygame.image.load(img + spr + inv + "Botella_vacia.png")
            mana_potion = pygame.image.load(img + spr + inv + "Botella_mana.png")

        class virusIdle:
            ani_l = [pygame.image.load(img + spr + idle + vir + "Virus_idle0.png"),
                     pygame.image.load(img + spr + idle + vir + "Virus_idle1.png"),
                     pygame.image.load(img + spr + idle + vir + "Virus_idle2.png"),
                     pygame.image.load(img + spr + idle + vir + "Virus_idle3.png"),
                     pygame.image.load(img + spr + idle + vir + "Virus_idle4.png")]

        class virusAttack:
            ani_2 = [pygame.image.load(img + spr + att + vir + "Virus_attack0.png"),
                     pygame.image.load(img + spr + att + vir + "Virus_attack1.png"),
                     pygame.image.load(img + spr + att + vir + "Virus_attack2.png"),
                     pygame.image.load(img + spr + att + vir + "Virus_attack3.png"),
                     pygame.image.load(img + spr + att + vir + "Virus_attack4.png")]

        class caballeroIdle:
            ani_l = [pygame.image.load(img + spr + idle + cab + "caballerito_idle0.png"),
                     pygame.image.load(img + spr + idle + cab + "caballerito_idle1.png"),
                     pygame.image.load(img + spr + idle + cab + "caballerito_idle2.png"),
                     pygame.image.load(img + spr + idle + cab + "caballerito_idle3.png"),
                     pygame.image.load(img + spr + idle + cab + "caballerito_idle4.png")]

        class caballeroAttack:
            ani_1 = [pygame.image.load(img + spr + att + cab + "caballerito_attack0.png"),
                     pygame.image.load(img + spr + att + cab + "caballerito_attack1.png"),
                     pygame.image.load(img + spr + att + cab + "caballerito_attack2.png"),
                     pygame.image.load(img + spr + att + cab + "caballerito_attack3.png"),
                     pygame.image.load(img + spr + att + cab + "caballerito_attack4.png"),
                     pygame.image.load(img + spr + att + cab + "caballerito_attack5.png"),
                     pygame.image.load(img + spr + att + cab + "caballerito_attack6.png"),
                     pygame.image.load(img + spr + att + cab + "caballerito_attack7.png"),
                     pygame.image.load(img + spr + att + cab + "caballerito_attack8.png")]

    # ========================================================================
    # ========  GENERAL SETTINGS  ============================================
    class generalSettings:
        screenWidth = 800
        screenHeight = 600
        screenTitle = "Requiem of the Fallen"
        generalFont = "Fonts/8bit.ttf"
    # ========================================================================
    # ========  COLORES  =====================================================
    class colors:
        trasparent = (0)
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        purple = (117,0,255)
        lightPurple = (186,127,255)
        cyan = (41,139,255)
