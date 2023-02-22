import pygame, sys

class Ent:

    def __init__(self, name, kind, color, shape, v, a):
        self.name = name        # Name
        self.kind = kind        # Kind
        self.color = color      # Color
        self.shape = shape      # Shape
        self.v = v              # Velocity
        self.a = a              # Acceleration
