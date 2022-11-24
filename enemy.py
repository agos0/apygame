import pygame
import random
class enemy:
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy

    def display(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), (self.cx, self.cy, 45, 45))

           