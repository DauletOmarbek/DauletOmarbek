import pygame
import os

def choise(pos):
    global pencil,erasel,rectangle,circle,color
    if (15 <= pos[0] <= 40) and (10 <= pos[1] <= 35):
        pencil = True
        erasel = False
        rectangle = False
        circle = False
    if (55 <= pos[0] <= 80) and (10 <= pos[1] <= 35):
        pencil = False
        erasel = True
        rectangle = False
        circle = False
    if (15 <= pos[0] <= 40) and (50 <= pos[1] <= 75):
        pencil = False
        erasel = False
        rectangle = True
        circle = False
    if (55 <= pos[0] <= 80) and (50 <= pos[1] <= 75):
        pencil = False
        erasel = False
        rectangle = False
        circle = True
    
    
    
    if(18 <= pos[0] <= 36) and (90 <= pos[1] <= 112):
        color=(128,64,64)
    if(41 <= pos[0] <= 58) and (90 <= pos[1] <= 112):
        color=(255,0,0)
    if(64 <= pos[0] <= 81) and (90 <= pos[1] <= 112):
        color=(255,128,128)
    if(18 <= pos[0] <= 36) and (120 <= pos[1] <= 143):
        color=(255,128,64)
    if(41 <= pos[0] <= 58) and (120 <= pos[1] <= 143):
        color=(255,255,0)
    if(64 <= pos[0] <= 81) and (120 <= pos[1] <= 143):
        color=(255,255,128)
    if(18 <= pos[0] <= 36) and (150 <= pos[1] <= 173):
        color=(0,255,0)
    if(41 <= pos[0] <= 58) and (150 <= pos[1] <= 173):
        color=(128,255,0)
    if(64 <= pos[0] <= 81) and (150 <= pos[1] <= 173):
        color=(128,255,128)
    if(18 <= pos[0] <= 36) and (180 <= pos[1] <= 203):
        color=(0,128,128)
    if(41 <= pos[0] <= 58) and (180 <= pos[1] <= 203):
        color=(0,255,64)
    if(64 <= pos[0] <= 81) and (180 <= pos[1] <= 203):
        color=(0,255,128)
    if(18 <= pos[0] <= 36) and (210 <= pos[1] <= 233):
        color=(0,64,128)
    if(41 <= pos[0] <= 58) and (210 <= pos[1] <= 233):
        color=(0,255,255)
    if(64 <= pos[0] <= 81) and (210 <= pos[1] <= 233):
        color=(128,255,255)
    if(18 <= pos[0] <= 36) and (242 <= pos[1] <= 265):
        color=(128,128,255)
    if(41 <= pos[0] <= 58) and (242 <= pos[1] <= 265):
        color=(0,128,192)
    if(64 <= pos[0] <= 81) and (242 <= pos[1] <= 265):
        color=(0,128,255)
    if(18 <= pos[0] <= 36) and (272 <= pos[1] <= 295):
        color=(128,0,64)
    if(41 <= pos[0] <= 58) and (272 <= pos[1] <= 295):
        color=(128,128,192)
    if(64 <= pos[0] <= 81) and (272 <= pos[1] <= 295):
        color=(255,128,192)
    if(18 <= pos[0] <= 36) and (303 <= pos[1] <= 326):
        color=(255,0,128)
    if(41 <= pos[0] <= 58) and (303 <= pos[1] <= 326):
        color=(255,0,255)
    if(64 <= pos[0] <= 81) and (303 <= pos[1] <= 326):
        color=(255,128,255)
    if(18 <= pos[0] <= 36) and (330 <= pos[1] <= 353):
        color=(255,255,255)
    if(41 <= pos[0] <= 58) and (330 <= pos[1] <= 353):
        color=(64,0,128)
    if(64 <= pos[0] <= 81) and (330 <= pos[1] <= 353):
        color=(128,0,255)
    
def draw_pencil(start, end, width, color):
    x1 = start[0]-100
    y1 = start[1]
    x2 = end[0]-100
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(paint, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(paint, color, (x, y), width)
def draw_erasel(start, end, width, color):
    x1 = start[0]-100
    y1 = start[1]
    x2 = end[0]-100
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(paint, (255,255,255), (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(paint, (255,255,255), (x, y), width)
def draw_rectangle(start, end, width, color):
    pygame.draw.rect(paint, color, (start[0]-100,start[1], abs(start[0]-end[0]), abs(start[1]-end[1])),width)
def draw_circle(start, end, width, color):
    pygame.draw.circle(paint, color, (start[0]-width-100,start[1]-width), pow(pow((start[0]-end[0]),2)+pow((start[1]-end[1]),2),1/2) ,width)


win = pygame.display.set_mode((900,600))
paint = pygame.Surface((800,600))
paint.fill((255,255,255))
pygame.display.set_caption("Paint")
pencil_image = pygame.image.load("pencil.png")
erasel_image = pygame.image.load("erasel.png")
rectangle_image = pygame.image.load("rectangle.png")
circle_image = pygame.image.load("circle.png")
color_image = pygame.image.load("color.png")
pencil = False
erasel = False
rectangle = False
circle = False
radius = 10
color = (0,0,0)
draw_on = False
last_pos = (0, 0)
draw_rec = (0,0)




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                radius += 2
            if event.key == pygame.K_DOWN:
                radius -= 2
            if event.key == pygame.K_s:
                pygame.image.save(paint,"paint_pygame.png")
        if event.type == pygame.MOUSEBUTTONDOWN:
            choise(event.pos)
            draw_rec = event.pos
            draw_on = True
            if pencil:
                pygame.draw.circle(paint,color,(event.pos[0]-100,event.pos[1]), radius)
            if erasel:
                pygame.draw.circle(paint,(255,255,255),(event.pos[0]-100,event.pos[1]), radius)
            
        if event.type == pygame.MOUSEBUTTONUP:
            draw_on = False
            if rectangle:
                    draw_rectangle(draw_rec, event.pos, radius,color)
            if circle:
                draw_circle(draw_rec, event.pos, radius,color)
        if event.type == pygame.MOUSEMOTION:
            if draw_on:
                if pencil:
                    draw_pencil(last_pos, event.pos, radius, color)
                if erasel:
                    draw_erasel(last_pos, event.pos, radius, color)
                
                
            last_pos = event.pos


        win.fill((200,215,221))
        win.blit(paint, (100,0))
        win.blit(pencil_image, (15,10))
        win.blit(erasel_image, (55,10))
        win.blit(rectangle_image, (15, 50))
        win.blit(circle_image, (55, 50))
        win.blit(color_image,(15,85))
        if pencil:
            win.blit(pencil_image, (15,550))
        if erasel:
            win.blit(erasel_image, (15,550))
        if rectangle:
            win.blit(rectangle_image, (15, 550))
        if circle:
            win.blit(circle_image, (15, 550))
        pygame.draw.rect(win,color,(55,550,25,25))



    pygame.display.update()
    

pygame.quit()