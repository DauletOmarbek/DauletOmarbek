import time
import pygame
import math

width = 640 
hight = 480

color = pygame.Color(255,255,0,0)
background_color = pygame.Color(0,0,0,0)

pygame.init()
pygame.display.set_caption("SINE WAVE")
win = pygame.display.set_mode((width, hight))
win.fill(background_color)

surface = pygame.Surface((width,hight))
surface.fill(background_color)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    surface.fill(background_color)
    speed = 2
    freq = 3
    amp = 40
    for x in range(width):
        y = int((hight / 2) + amp * math.sin(freq * ((float(x)/width) * (2 * math.pi ) + (speed * time.time()))))
        surface.set_at((x, y), color)
    win.blit(surface, (0, 0))
    pygame.display.flip()