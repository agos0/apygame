from turtle import delay
import pygame as pg, sys
from pygame.locals import *
from pygame.math import Vector2
from pygame.time import delay

def main():
    pg.init()
    
    size = width, height = 1000, 800
    x_buffer = 535
    y_buffer = 435
    window = pg.display.set_mode(size)

    black = 0, 0, 0
    white = 255, 255, 255
    blue = 0, 0, 255

    pg.display.set_caption("game test")

    cx = 100
    cy = 200

    velocity = pg.Vector2()
    velocity.x = 3
    velocity.y = 0

    acceleration = 0.1

    while True:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        window.fill(black)

        rect1 = pg.draw.rect(window, blue, (cx, cy, 75, 75))
        
        cx += velocity.x
        if cx + x_buffer > width:
            velocity.x = -3
        if cx < 0:
            velocity.x = 3

        cy += velocity.y
        velocity.y += acceleration
        if keys[pg.K_w]:
            velocity.y = -3
        if cy + y_buffer > height:
            velocity.y = -3
        if cy < 0:
            velocity.y = 3    

        window.blit(window, rect1)
        pg.display.update()
        pg.display.flip()
        pg.time.delay(10)

if __name__ == "__main__":
    main()