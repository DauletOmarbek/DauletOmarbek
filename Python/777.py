import pygame

pygame.init()
a = pygame.mixer.music.load("muz.mp3")
b = pygame.mixer.music.load("000.mp3")
pygame.cdrom.play(a)
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Snake game")
while True:    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.mixer.music.stop()
                if event.key == pygame.K_e:
                    pygame.mixer.music.play()
        