import pygame, sys

from entity import Ent
from circle import Circle
from ai import Enemy

FRAMES = 60


class Model:
    
    def __init__(self):
        self.totalHits = 0

    # Hardcoded for 1 paddle and 1 ball for now
    def setupGame(self):

        rX = 50
        rY = 50
        eX = 590
        eY = 50
        rW = 10
        rH = 50
        list = []
    
        list.append(Ent("paddle", "rect", (0, 0, 255), (rX, rY, rW, rH), (0,0)))
        list.append(Ent("ball", "circ", (255, 255, 255), Circle(250, 250, 5), (25,20)))
        list.append(Enemy("enemy", "rect", (255, 0, 00), (eX, eY, rW, rH), (0,0)))
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

    # bounds check (might not be finished)
    def boundsCheck(self, b, x1, y1, x2, y2):
        if b.shape.x - b.shape.rad >= x1 and b.shape.x + b.shape.rad <= x2:
            if b.shape.y - b.shape.rad <= y1 and b.shape.y + b.shape.rad >= y2:
                return True
        if b.shape.x - b.shape.rad <= x1 and b.shape.x + b.shape.rad >= x2:
            if b.shape.y - b.shape.rad >= y1 and b.shape.y + b.shape.rad <= y2:
                return True
        return False

    def speedUp(self, b):
        self.totalHits += 1
        if self.totalHits % 4 == 0: 
            b.v = (b.v[0] * 1.2, b.v[1] * 1.2)

    def updateBall(self, b, p, e):
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
            self.speedUp(b)
        
        # checking for ai paddle
        enemyRect = pygame.Rect(e.shape)
        if self.boundsCheck(b, enemyRect.topleft[0], enemyRect.topleft[1], enemyRect.bottomleft[0], enemyRect.bottomleft[1]):
            b.v = (b.v[0] * -1.0, b.v[1])
            self.speedUp(b)

    # updates state of the game
    def update(self, ents, events):
        for event in events:
            ents[0] = self.readInput(ents[0], event)
        self.updateBall(ents[1], ents[0], ents[2])
        ents[2].move(ents[1].shape.y)

        

        return ents
