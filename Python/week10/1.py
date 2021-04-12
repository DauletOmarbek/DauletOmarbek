import pygame
import os
import random
def music():
    pygame.mixer.music.load('000.mp3')
    pygame.mixer.music.play()
pygame.init()
screen = pygame.display.set_mode((768, 720))

_image_library = {}
road = pygame.image.load("road.jpg")
image = pygame.image.load('bmw.png')
x = 20
done = False
y=0
car_speed = 35
car1_x = random.randint(0,768-150)
car1_y = -300
car1 = pygame.image.load("car3.png")
accident = False
car1_speed = float(40)
level = int(0)
while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_r]:
        accident = False
        level = 0
        car1_speed = 40
    if x-car_speed>=0:
        if pressed[pygame.K_LEFT]:
            x-=car_speed
    if x+car_speed+130<=768:
        if pressed[pygame.K_RIGHT]:
            x+=car_speed
    if x+130<=768 and x>=0 and not accident:
        if y>=720:
            y=0
        
        y+=40
        screen.fill((98, 98, 98))
        
        pygame.draw.rect(screen,(229,229,229),(256,y+360,15,100))
        pygame.draw.rect(screen,(229,229,229),(256,y,15,100))
        pygame.draw.rect(screen,(229,229,229),(256,y-360,15,100))
        pygame.draw.rect(screen,(229,229,229),(256,y-720,15,100))
        pygame.draw.rect(screen,(229,229,229),(512,y+360,15,100))
        pygame.draw.rect(screen,(229,229,229),(512,y,15,100))
        pygame.draw.rect(screen,(229,229,229),(512,y-360,15,100))
        pygame.draw.rect(screen,(229,229,229),(512,y-720,15,100))
        if car1_y >=720:
            car1_x = random.randint(0,768-150)
            car1_y = -300
            car1_speed +=1
            level +=1
            car_speed +=1
        car1_y += car1_speed
        
        
        screen.blit(image, (x, 400))
        screen.blit(car1,(car1_x,car1_y))
    f3 = pygame.font.SysFont('serif', 50)
    text3 = f3.render(str(level),True,(255,0,0))    
    screen.blit(text3,(20,20))

    if 400<car1_y+300 and ((x>car1_x+10 and x<car1_x+120) or (x+120>car1_x and x+120<car1_x+120)) and not accident:
        accident = True
        music()
    if accident:
        f1 = pygame.font.SysFont('serif', 100)
        f2 = pygame.font.SysFont('serif', 25)
        text1 = f1.render("Game over", True, (255, 0, 0))
        text2 = f2.render("If you want to continue press R",True,(0,0,0))
        screen.blit(text1,(150,250))
        screen.blit(text2,(220,350))

    pygame.display.update()
    pygame.time.delay(60)
pygame.quit()