import pygame, sys


SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screenColor = (0,0,0)
class View:
   
    
    #def __init__():
    #    pass
    def view_init(self):
        pygame.display.set_caption("Pong 4160")
        self.surface = pygame.display.set_mode(SCREEN_SIZE)

    def update_screen(self, ents):
        
        self.surface.fill(screenColor)

        # loops over all entities to display them
        for x in ents:
            if x.kind == "rect":
                pygame.draw.rect(self.surface, x.color, x.shape)
            elif x.kind == "circ":
                pygame.draw.circle(self.surface, x.color, (x.shape.pos.x, x.shape.pos.y), x.shape.rad)
        
        pygame.display.update()