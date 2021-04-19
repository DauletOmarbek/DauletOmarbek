import pygame
import random
height = 400
length = 400
size = (length, height)
size_snake = 10

length_snake = []
x, y = random.randint(0,height-size_snake), random.randint(0,height-size_snake)
length_snake.append((x,y))
x_speed = 10
y_speed = 0
speed = 10

win = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y_speed!=speed: 
        x_speed=0
        y_speed=(-1)*speed
    if pressed[pygame.K_DOWN] and y_speed!=(-1)*speed:
        x_speed=0 
        y_speed=(1)*speed
    if pressed[pygame.K_LEFT] and x_speed!=speed:
        x_speed=(-1)*speed 
        y_speed=0
    if pressed[pygame.K_RIGHT] and x_speed!=(-1)*speed:
        x_speed=(1)*speed 
        y_speed=0
    pygame.time.delay(60)
    win.fill((0,0,0))
    pygame.display.update()
    


