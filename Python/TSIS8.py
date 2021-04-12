import pygame
import random
pygame.init()

def coin_random(car2_x):
    y = int(random.randint(25,975))
    if (25<=y and y<car2_x-30)  or (car2_x+130 < y and y <=975):
        return y
    else:
        return coin_random(car2_x)
def music():
    pygame.mixer.music.load('000.mp3')
    pygame.mixer.music.play()
#screen
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game")
#main car1
car1_x = 200
car1_y = 520
car1_speed = 10
car1_speed_turn = 10 
car1_image = pygame.image.load("car1.png")

#car2
car2_x = random.randint(0,900)
car2_y = -300
car2_speed = 15 
car2_image = pygame.image.load("car2.png")

#coin
coin_size = 25
coin_x = coin_random(car2_x)
coin_y = -50
coin_image = pygame.image.load("coin.png")
level = 0

#accident
accident = False
run = True
y_lines = 800

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            run = False
    
    #move main car1
    pressed = pygame.key.get_pressed()
    if car1_x-car1_speed_turn>=0:
        if pressed[pygame.K_LEFT] and not accident:
            car1_x -=car1_speed_turn
    if car1_x+car1_speed_turn+100<1000:
        if pressed[pygame.K_RIGHT] and not accident:
            car1_x +=car1_speed_turn
    if pressed[pygame.K_r]:
        #car1
        car1_speed = 10
        car1_speed_turn = 10
        #car2
        car2_x = random.randint(0,900)
        car2_y = -300
        car2_speed = random.randint(13,20)  
        #coin
        coin_x = coin_random(car2_x)
        coin_y = -50
        #accident
        accident = False
        #level
        level = 0
        
    screen.fill((98,98,98))
    
    
    #lines
    for y in range(0,5):
        k = y_lines-y*(400)
        for x in range(190,800,200):
            pygame.draw.rect(screen,(255,255,255),(x, k, 20, 100))
    y_lines+=car2_speed
    if y_lines-4*400>0:
        y_lines = 800
   
    #car2
    screen.blit(car2_image,(car2_x,car2_y))
    #pygame.draw.rect(screen,(255,0,0),(car2_x,car2_y, 100, 200))
    car2_y +=car2_speed
    if car2_y>800:
        car2_x = random.randint(0,900)
        car2_y = -300
       

    #coin
    screen.blit(coin_image,(coin_x,coin_y))
    coin_y+=car2_speed
    if coin_y>=800:
        coin_x = coin_random(car2_x)
        coin_y = -50
    #level
    if ((coin_x-25 < car1_x+90 and car1_x+90 < coin_x+25) or (coin_x-25 < car1_x+20 and car1_x+20 < coin_x+25)) and ((coin_y-25 < car1_y and car1_y < coin_y+25) or (coin_y-25 < car1_y+190 and car1_y+190 < coin_y+25)):
        coin_x = coin_random(car2_x)
        coin_y = -50
        level+=1
        if level%3==0:
            car2_speed+=1
            car1_speed+=1
            car1_speed_turn+=1
        
    #accident
    if ((car2_x < car1_x+90 and car1_x+90 < car2_x+90) or (car2_x < car1_x+20 and car1_x+20 < car2_x+90)) and not accident and ((car2_y < car1_y and car1_y < car2_y+190) or (car2_y < car1_y+190 and car1_y+190 < car2_y+190)):
        accident = True
        music()
        
    if accident:
        f1 = pygame.font.SysFont('serif', 100)
        f2 = pygame.font.SysFont('serif', 25)
        text1 = f1.render("Game over", True, (255, 0, 0))
        text2 = f2.render("If you want to continue press R",True,(0,0,0))
        screen.blit(text1,(250,250))
        screen.blit(text2,(320,350))
        car1_speed = 0
        car2_speed = 0
    
    f3 = pygame.font.SysFont('serif', 50)
    text3 = f3.render(str(level),True,(255,0,0))    
    screen.blit(text3,(20,20))
    #screen
    screen.blit(car1_image, (car1_x,car1_y))
    #pygame.draw.rect(screen,(255,0,0),(car1_x,car1_y, 100, 200))
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()    
    
