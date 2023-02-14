import pygame, sys

from entity import Ent

class Enemy(Ent):
    
    def __init__(self, name, kind, color, shape, v):
        super().__init__(name, kind, color, shape, v)

    def traceBall(self, b):
        pass

    def move(self, pos):
        old = self.shape
        if self.shape[1] + 25 < pos:
            self.shape = (old[0], old[1]+1, old[2], old[3])
        elif self.shape[1] + 25 > pos:
            self.shape = (old[0], old[1]-1, old[2], old[3])
        