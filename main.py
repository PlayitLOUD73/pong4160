import pygame, sys

from view import View
from controller import Controller
    
view = View()
controller = Controller()

pygame.init()

view.view_init()

while True:
    controller.get_events()
    view.update_screen()