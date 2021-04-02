import pygame as pg

 
sc = pg.display.set_mode((720, 360))
 
# здесь будут рисоваться фигуры
 
pg.display.update()
x=100
y=100
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(60)
    sc.fill((0,0,0))
    pi=3.14
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x-=10
    if keys[pg.K_RIGHT]:
        x+=10
    if keys[pg.K_UP]:
        y-=10
    if keys[pg.K_DOWN]:
        y+=10

    pg.draw.ellipse(sc,(255,0,0),(100,200,x,y))
    pg.display.update()
