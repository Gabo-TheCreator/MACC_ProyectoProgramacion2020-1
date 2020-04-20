import pygame
from pygame.locals import *
import Common
from Constantes import Constants


class mainMenu:

    screen: pygame.surface = None
    common = Common
    cons = Constants

    def __init__(self, screen):
        # Initialize Screen
        self.screen = screen

        # Initialize
        self.screen.blit(self.common.bg_tit, (0, 0))
        self.screen.blit(self.common.title, ((self.cons.generalSettings.screenWidth / 2) - 216, 100))
        self.screen.blit(self.common.PLAY_n, (125, 412.5))
        self.screen.blit(self.common.ABOUT_n, (325, 412.5))
        self.screen.blit(self.common.EXIT_n, (525, 412.5))

        event = pygame.event.wait()
        if event.type == KEYDOWN:
            key = event.key
            if key == K_LEFT:
                print("Key left")
            elif key == K_RIGHT:
                print("Key Right")

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         self.common.EndLine.play()
        #         if event.type == pygame.K_RIGHT:
        #             print("Right")
        #         elif event.type == pygame.K_LEFT:
        #             print("Left")
        #     elif event.type == pygame.KEYUP:
        #         print("Alguna tecla se ha dejado de precionar")


