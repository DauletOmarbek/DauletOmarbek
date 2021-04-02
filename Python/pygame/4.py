import pygame
import random
size=(720,360)
win = pygame.display.set_mode(size)
done = True
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
x=100
y=100
speed_x = 1
speed_y = 1
a=list()
b=list()
c=list()
d=list()
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        a.append(random.randint(0+25,720-25))
        b.append(random.randint(0+25,360-25))
        c.append(pow((-1),random.randint(0,1)))
        d.append(pow((-1),random.randint(0,1)))
    for k in range(len(a)):
        a[k]+=c[k]
        b[k]+=d[k]
        if a[k]+25>720:
            c[k]*=(-1)
        if a[k]-25<0:
            c[k]*=(-1)
        if b[k]+25>360:
            d[k]*=(-1)
        if b[k]-25<0:
            d[k]*=(-1) 
    pygame.time.delay(1)
    win.fill(BLACK)
    for k in range(len(a)):
        pygame.draw.circle(win,RED,(a[k],b[k]),25)
    
    pygame.display.update()