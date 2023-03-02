import pygame, sys


SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screenColor = (0,0,0)
white = (255, 255, 255)
class View:
   
    def view_init(self):
        pygame.display.set_caption("Pong 4160")
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        self.largeFont = pygame.font.SysFont('droidsans.ttf', 48)
        self.smallFont = pygame.font.SysFont('droidsans.ttf', 36)

    def update_screen(self, ents, state):
        
        self.surface.fill(screenColor)

        # loops over all entities to display them
        for x in ents:
            if x.kind == "rect":
                pygame.draw.rect(self.surface, x.color, x.shape)
            elif x.kind == "circ":
                pygame.draw.circle(self.surface, x.color, (x.shape.pos.x, x.shape.pos.y), x.shape.rad)
        
        # manages game over text
        if state != 0:
            if state == 1:
                text = "YOU WIN!"
            else:
                text = "COM WINS"
            
            textObject = self.largeFont.render(text, True, white, screenColor)
            textRect = textObject.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) - 24)
            
            littleText = self.smallFont.render("PRESS ENTER TO RESTART", True, white, screenColor)
            littleTextRect = littleText.get_rect()
            littleTextRect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 24)
            
            self.surface.blit(textObject, textRect)
            self.surface.blit(littleText, littleTextRect)
        
        pygame.display.update()