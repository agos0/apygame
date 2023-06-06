import pygame
import random
class enemy:
    def __init__(self, ex, ey, surface):
        self.ex = ex
        self.ey = ey
        self.surface = surface

    def e_display(self):
        pygame.draw.rect(self.surface, (0, 255, 0), (self.ex, self.ey, 45, 45))