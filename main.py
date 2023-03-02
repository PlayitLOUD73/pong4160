import pygame, sys

from view import View
from controller import Controller
from model import Model

# State meanings
# -2 - game setup (includes restart)
# -1 - computer won game
#  0 - normal play
#  1 - player won game

state = -2

while True:
    
    # setup game
    if state == -2:

        view = View()
        controller = Controller()
        model = Model()

        pygame.init()

        view.view_init()

        ents = model.setupGame()
        clock = pygame.time.Clock()
        state = 0

    # Main Game loop
    events, state = controller.get_events(state)    
    if state == 0:
        clock.tick(60)
        ents, state = model.update(ents, events)
    view.update_screen(ents, state)
