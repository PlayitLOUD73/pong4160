import pygame, sys

from entity import Ent
from circle import Circle

FRAMES = 60


class Model:
    
    # Hardcoded for 1 paddle and 1 ball for now
    def setupGame(self):

        rX = 50
        rY = 50
        rW = 10
        rH = 50
        list = []
    
        list.append(Ent("paddle", "rect", (0, 0, 255), (rX, rY, rW, rH), (0,0)))
        list.append(Ent("ball", "circ", (255, 255, 255), Circle(250, 250, 5), (25,20)))
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

    # bounds check
    def boundsCheck(self, b, x1, y1, x2, y2):
        if b.shape.x - b.shape.rad >= x1 and b.shape.x + b.shape.rad <= x2:
            if b.shape.y - b.shape.rad <= y1 and b.shape.y + b.shape.rad >= y2:
                return True
        if b.shape.x - b.shape.rad <= x1 and b.shape.x + b.shape.rad >= x2:
            if b.shape.y - b.shape.rad >= y1 and b.shape.y + b.shape.rad <= y2:
                return True
        return False


    def updateBall(self, b, p):
        b.shape.x +=(b.v[0] / FRAMES)
        b.shape.y += (b.v[1] / FRAMES)
        
        # checking for borders
        if self.boundsCheck(b, 0, 480, 640, 480):
            b.v = (b.v[0], b.v[1] * -1.0)
        if self.boundsCheck(b, 640, 0, 640, 480):
            b.v = (b.v[0] * -1.0, b.v[1])
        if self.boundsCheck(b, 0, 0, 640, 0):
            b.v = (b.v[0], b.v[1] * -1.0)
        
        # checking for paddle
        rect = pygame.Rect(p.shape)
        if self.boundsCheck(b, rect.topright[0], rect.topright[1], rect.bottomright[0], rect.bottomright[1]):
            b.v = (b.v[0] * -1.0, b.v[1])

    # updates state of the game
    def update(self, ents, events):
        for event in events:
            ents[0] = self.readInput(ents[0], event)
        self.updateBall(ents[1], ents[0])
        return ents
