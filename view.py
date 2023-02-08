import pygame, sys


SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

class View:
   
    
    #def __init__():
    #    pass
    def view_init(self):
        pygame.display.set_caption("Pong 4160")
        surface = pygame.display.set_mode(SCREEN_SIZE)

    def update_screen(self):
        pygame.display.update()