import pygame, sys, random

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

        # random direction and velocity
        random.seed()
        vX = random.randint(250, 350) / 100.0
        vY = random.randint(250, 350) / 100.0
        vD = random.randint(0,1)

        if vD == 1:
            vY *= -1.0

        # player paddle
        list.append(Ent("paddle", "rect", (0, 0, 255), (rX, rY, rW, rH), pygame.math.Vector2(0,0), (0, 0)))

        # ball
        list.append(Ent("ball", "circ", (255, 255, 255), Circle(pygame.math.Vector2(250, 250), 5), pygame.math.Vector2(vX,vY), (0, 0)))

        # ai paddle
        list.append(Enemy("enemy", "rect", (255, 0, 0), (eX, eY, rW, rH), pygame.math.Vector2(0,0), (0, 0)))
        return list
    
    # reads list of events
    def readInput(self, ent, event):
        if event == pygame.K_UP:
            old = ent.shape
            ent.shape = (old[0], old[1]-6, old[2], old[3])
        elif event == pygame.K_DOWN:
            old = ent.shape
            ent.shape = (old[0], old[1]+6, old[2], old[3])
        return ent

    # bounds check (might not be finished)
    def boundsCheck(self, b, x1, y1, x2, y2):
        if b.shape.pos.x - b.shape.rad >= x1 and b.shape.pos.x + b.shape.rad <= x2:
            if b.shape.pos.y - b.shape.rad <= y1 and b.shape.pos.y + b.shape.rad >= y2:
                return True
        if b.shape.pos.x - b.shape.rad <= x1 and b.shape.pos.x + b.shape.rad >= x2:
            if b.shape.pos.y - b.shape.rad >= y1 and b.shape.pos.y + b.shape.rad <= y2:
                return True
        return False

    # Will be replaced with dynamic acceleration
    def speedUp(self, b):
        self.totalHits += 1
        if self.totalHits % 4 == 0: 
            b.v = pygame.math.Vector2(b.v.x * 1.2, b.v.y * 1.2)

    # need to add acceleration and a proper angle detection function
    def updateBall(self, b, p, e):
        b.shape.pos.x += (b.v.x)
        b.shape.pos.y += (b.v.y)
        # b.shape.pos += b.v
        
        # checking for borders
        if self.boundsCheck(b, 0, 480, 640, 480):
            # b.v = (b.v[0], b.v[1] * -1.0)
            b.v = b.v.reflect(pygame.math.Vector2(0, 1))
        if self.boundsCheck(b, 640, 0, 640, 480):
            # b.v = (b.v[0] * -1.0, b.v[1])
            b.v = b.v.reflect(pygame.math.Vector2(1,0))
        if self.boundsCheck(b, 0, 0, 640, 0):
            # b.v = (b.v[0], b.v[1] * 1.0)
            b.v = b.v.reflect(pygame.math.Vector2(0,1))
        
        # checking for paddle
        rect = pygame.Rect(p.shape)
        if self.boundsCheck(b, rect.topright[0], rect.topright[1], rect.bottomright[0], rect.bottomright[1]):
            # b.v = (b.v.x * -1.0, b.v[1])
            b.v = b.v.reflect(pygame.math.Vector2(1,0))
            self.speedUp(b)
        
        # checking for ai paddle
        enemyRect = pygame.Rect(e.shape)
        if self.boundsCheck(b, enemyRect.topleft[0], enemyRect.topleft[1], enemyRect.bottomleft[0], enemyRect.bottomleft[1]):
            # b.v = (b.v[0] * -1.0, b.v[1])
            b.v = b.v.reflect(pygame.math.Vector2(1,0))
            self.speedUp(b)

    # updates state of the game
    def update(self, ents, events):
        for event in events:
            ents[0] = self.readInput(ents[0], event)
        self.updateBall(ents[1], ents[0], ents[2])
        # ents[2].traceBall(ents[1])
        ents[2].move(ents[1].shape.pos.y)

        

        return ents
