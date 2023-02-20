import pygame, sys

from view import View
from controller import Controller
from model import Model
    
view = View()
controller = Controller()
model = Model()

pygame.init()

view.view_init()

ents = model.setupGame()

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    events = controller.get_events()
    model.update(ents, events)
    view.update_screen(ents)
