import pygame
import math
import sys

pygame.init()
size = (600, 420)
win = pygame.display.set_mode(size)
pygame.display.set_caption("Sin(), Cos()")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((255,255,255))
    pygame.draw.rect(win, (0,0,0), (40,20,520,360),1)

    pygame.draw.line(win, (0,0,0), [40,40],[559,40],1)
    pygame.draw.line(win, (0,0,0), [40,80],[559,80],1)
    pygame.draw.line(win, (0,0,0), [40,120],[559,120],1)
    pygame.draw.line(win, (0,0,0), [40,160],[559,160],1)
    pygame.draw.line(win, (0,0,0), [40,200],[559,200],2)
    pygame.draw.line(win, (0,0,0), [40,240],[559,240],1)
    pygame.draw.line(win, (0,0,0), [40,280],[559,280],1)
    pygame.draw.line(win, (0,0,0), [40,320],[559,320],1)
    pygame.draw.line(win, (0,0,0), [40,360],[559,360],1)

    pygame.draw.line(win, (0,0,0), [60,20],[60,379],1)
    pygame.draw.line(win, (0,0,0), [140,20],[140,379],1)
    pygame.draw.line(win, (0,0,0), [220,20],[220,379],1)
    pygame.draw.line(win, (0,0,0), [300,20],[300,379],2)
    pygame.draw.line(win, (0,0,0), [380,20],[380,379],1)
    pygame.draw.line(win, (0,0,0), [460,20],[460,379],1)
    pygame.draw.line(win, (0,0,0), [540,20],[540,379],1)
    
    for x in range(60,540,10):
        if ((x/10)-2)%4==0:
            pygame.draw.line(win, (0,0,0),[x,20],[x,35])
        if (x/10)%2==0:
            pygame.draw.line(win,(0,0,0),[x,20],[x,29])
        else:
            pygame.draw.line(win, (0,0,0), [x,20], [x,24])
    
    for x in range(60,540,10):
        if ((x/10)-2)%4==0:
            pygame.draw.line(win, (0,0,0),[x,379],[x,364])
        if (x/10)%2==0:
            pygame.draw.line(win,(0,0,0),[x,379],[x,370])
        else:
            pygame.draw.line(win, (0,0,0), [x,379], [x,375])

    for x in range(40,360,10):
        if (x/10)%2==0:
            pygame.draw.line(win,(0,0,0),[40,x],[49,x])
        else:
            pygame.draw.line(win, (0,0,0), [40,x], [44,x])

    for x in range(40,360,10):
        if (x/10)%2==0:
            pygame.draw.line(win,(0,0,0),[559,x],[550,x])
        else:
            pygame.draw.line(win, (0,0,0), [559,x], [555,x])
    PI =3.14
    for x in range(60, 540,3):

        cos_y1 = 160*math.cos(((x-60)/80)*PI)
        cos_y2 = 160*math.cos(((x+1-60)/80)*PI)
        pygame.draw.aalines(win, (0,0,255), False, [(x, 200 + cos_y1), ((x + 1), 200 + cos_y2)])
    
    for x in range(60, 540):
        sin_y1 = 160*math.sin(((x-60)/80)*PI)
        sin_y2 = 160*math.sin(((x+1-60)/80)*PI)
        pygame.draw.aalines(win, (255,0,0), False, [(x, 200 + sin_y1), ((x + 1), 200 + sin_y2)])

    a=[' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
    for x in range(9):
        f1 = pygame.font.SysFont('serif', 15)
        text1 = f1.render(a[x], True, (0, 0, 0))
        win.blit(text1, (5, 32+(x*40)))
    b=['-3π', '5π', '-2π', '3π', ' -π', ' π', '  0', ' π', '  π','3π', ' 2π', '5π', ' 3π']
    place = 48
    for x in range(13):
        if x<7:
            if x%2==0:
                f1 = pygame.font.SysFont('serif', 15)
                text1 = f1.render(b[x], True, (0, 0, 0))
                win.blit(text1, (place,385))
                place+=40
            else:
                f1 = pygame.font.SysFont('serif', 15)
                text1 = f1.render(b[x], True, (0, 0, 0))
                win.blit(text1, (place+5,380))
                pygame.draw.line(win, (0,0,0),[place,396], [place+3,396])
                pygame.draw.line(win, (0,0,0),[place+7,396], [place+19,396])
                f2 = pygame.font.SysFont('serif', 15)
                text2 = f2.render('2', True, (0, 0, 0))
                win.blit(text2, (place+9,395))
                place+=40
        else:
            if x%2==0:
                f1 = pygame.font.SysFont('serif', 15)
                text1 = f1.render(b[x], True, (0, 0, 0))
                win.blit(text1, (place,385))
                place+=40
            else:
                f1 = pygame.font.SysFont('serif', 15)
                text1 = f1.render(b[x], True, (0, 0, 0))
                win.blit(text1, (place+5,380))
                pygame.draw.line(win, (0,0,0),[place+7,396], [place+19,396])
                f2 = pygame.font.SysFont('serif', 15)
                text2 = f2.render('2', True, (0, 0, 0))
                win.blit(text2, (place+9,395))
                place+=40
    pygame.draw.line(win,(255,255,255),[380,41],[380,79])
    f1 = pygame.font.SysFont('serif', 20)
    text1 = f1.render('sin', True, (0, 0, 0))
    win.blit(text1, (365,40))
    f2 = pygame.font.SysFont('serif', 20)
    text2 = f2.render('cos', True, (0, 0, 0))
    win.blit(text2, (365,58))
    pygame.draw.line(win,(255, 0, 0),[400,53],[440,53],2)
    for x in range(400,440,10):
        pygame.draw.line(win,(0, 0, 255),[x,70],[x+5,70],2)



    pygame.display.update()
