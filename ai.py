import pygame, sys

from entity import Ent

class Enemy(Ent):
    
    def __init__(self, name, kind, color, shape, v, a):
        super().__init__(name, kind, color, shape, v, a)

    def move(self, pos):
        
        old = self.shape

        paddle = self.shape[1] + 25

        if abs(paddle - pos) >= self.v.x:
            move = self.v.x
        else:
            move = abs((self.shape[1] + 25) - pos)

        if paddle < pos:
            self.shape = (old[0], old[1]+move, old[2], old[3])
        elif paddle + 25 > pos:
            self.shape = (old[0], old[1]-move, old[2], old[3])
