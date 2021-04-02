import pygame
size = (720, 360)
win = pygame.display.set_mode(size)
run = True
x = 100
y = 100
x_change = 0
y_change = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    x+=x_change
    y+=y_change
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        x_change=0
        y_change=1    
    if keys[pygame.K_UP]:
        x_change=0
        y_change=(-1)
    if keys[pygame.K_LEFT]:
        x_change=(-1)
        y_change=0
    if keys[pygame.K_RIGHT]:
        x_change=1
        y_change=0
    pygame.time.delay(5)
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,255,255), [x,y, 10,10])

    pygame.display.update()