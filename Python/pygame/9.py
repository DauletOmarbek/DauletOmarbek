import pygame
#pylint: disable=no-member
import sys
import math
pygame.init()
win = pygame.display.set_mode([840, 840])

points = []
win.fill([0,0,0])
run = True
n=10
A=200
for x in range(840):
    y= int(math.sin(x/840. * n * math.pi)*A+240)
    points.append([x,y])
pygame.draw.lines(win, [255,255,255], False, points, 3)
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            RUN = False
    