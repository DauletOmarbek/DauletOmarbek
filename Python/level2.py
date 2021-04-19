import pygame
win = pygame.display.set_mode((800,800))
def level1():
    pygame.draw.rect(win,(0,0,255),(200,200,50,400))
    pygame.draw.rect(win,(0,0,255),(550,200,50,400))
    pygame.draw.rect(win,(0,0,255),(250,375,350,50))

    if (200 < snake1.elements[0][0] + snake1. )




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((0,0,0))
    pygame.draw.rect(win,(0,0,255),(200,200,50,400))
    pygame.draw.rect(win,(0,0,255),(550,200,50,400))
    pygame.draw.rect(win,(0,0,255),(250,375,350,50))
    pygame.display.update()
pygame.quit()