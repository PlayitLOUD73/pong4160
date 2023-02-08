import pygame, sys

from view import View
from controller import Controller
from model import Model
    
view = View()
controller = Controller()
model = Model()

pygame.init()

view.view_init()

while True:
    controller.get_events()
    view.update_screen()