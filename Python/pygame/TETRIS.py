import pygame
import sys
pygame.font.init()
size = (720, 360)
win = pygame.display.set_mode(size)
run = True
x=320
circle_x = 100
circle_y = 100
x_speed = 5
y_speed = 5

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if 0<=x-10 and x-10<=720-80:
            x-=10
    if keys[pygame.K_RIGHT]:
        if 0<=x+10 and x+10<=720-80:
            x+=10
    win.fill((0,0,0))
    pygame.time.delay(20)
    circle_x+=x_speed
    circle_y+=y_speed
    if circle_x+10>720:
        x_speed=(-1)
    if circle_x-10<0:
        x_speed*=(-1)
    if circle_y<340 and circle_y+10>340 and (x<circle_x and circle_x<x+80):
        y_speed*=(-1)
    if circle_y>335:
        f1 = pygame.font.Font(None, 60)
        text1 = f1.render('Game Over', True,(180, 0, 0))
        win.blit(text1, (250, 140))
    if circle_y-10<0:
        y_speed*=(-1) 

    #
    pygame.draw.circle(win, (255,0,0),(circle_x,circle_y),10)


    # [______]
    pygame.draw.rect(win, (255,255,255), [x,350 , 80,10])
    pygame.display.update()    