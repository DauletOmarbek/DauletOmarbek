import pygame
pygame.init()
size = (720, 360)
win = pygame.display.set_mode(size)
pygame.display.set_caption("My game")
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    win.fill((255,255,255))
    pygame.draw.line(win, [200, 200, 200],[100, 100],[200, 200],10)
pygame.quit

