import pygame, sys

class Ent:

    def __init__(self, name, kind, color, shape, v):
        self.name = name
        self.kind = kind
        self.color = color
        self.shape = shape
        self.v = v