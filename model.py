import pygame, sys

from entity import Ent
from circle import Circle


class Model:
    
    # Hardcoded for 1 paddle and 1 ball for now
    def setupGame(self):

        rX = 50
        rY = 50
        rW = 10
        rH = 50
        list = []
    
        list.append(Ent("paddle", "rect", (0, 0, 255), (rX, rY, rW, rH)))
        list.append(Ent("ball", "circ", (255, 255, 255), Circle(250, 250, 5)))
        return list
    
    # reads list of events
    def readInput(self, ent, event):
        if event == pygame.K_UP:
            old = ent.shape
            ent.shape = (old[0], old[1]-1, old[2], old[3])
        elif event == pygame.K_DOWN:
            old = ent.shape
            ent.shape = (old[0], old[1]+1, old[2], old[3])
        return ent

    # updates state of the game
    def update(self, ents, events):
        for event in events:
            ents[0] = self.readInput(ents[0], event)
        return ents
