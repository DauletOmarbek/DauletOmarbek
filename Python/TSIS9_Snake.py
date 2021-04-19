import pygame
import random

pygame.init()
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Snake game")

apple = pygame.image.load("apple.png")
background_game = pygame.image.load("123.png")
pygame.mixer.music.load("muz.mp3")
pygame.mixer.music.play()





class Food:
    def __init__(self):
        self.size_food = 10
        self.food_x = 100
        self.food_y = 100
    
    def random_food(self):
        self.food_x = random.randint(self.size_food,800-self.size_food)
        self.food_y = random.randint(self.size_food,800-self.size_food)
        if level_2:
            while ((200-self.size_food < self.food_x < 250+self.size_food) and (200-self.size_food < self.food_y < 600+self.size_food)) or ((550-self.size_food < self.food_x < 600+self.size_food) and (200-self.size_food < self.food_y < 600+self.size_food)) or ((250-self.size_food < self.food_x < 600+self.size_food) and (375-self.size_food < self.food_y < 425+self.size_food)):
                self.food_x = random.randint(self.size_food,800-self.size_food)
                self.food_y = random.randint(self.size_food,800-self.size_food)
        if level_3:
            while ((200-self.size_food < self.food_x < 250+self.size_food) and (200-self.size_food < self.food_y < 600+self.size_food)) or ((550-self.size_food < self.food_x < 600+self.size_food) and (200-self.size_food < self.food_y < 600+self.size_food)) or ((250-self.size_food < self.food_x < 600+self.size_food) and (375-self.size_food < self.food_y < 425+self.size_food)) or (25+self.size_food>self.food_x) or (self.food_x>775-self.size_food) or (25+self.size_food>self.food_y) or (self.food_y>775-self.size_food):
                self.food_x = random.randint(self.size_food,800-self.size_food)
                self.food_y = random.randint(self.size_food,800-self.size_food)
            

    
    def draw_food(self):
        win.blit(apple,(self.food_x-20,self.food_y-20))
        


class Snake:
    def __init__(self,x,y,color):
        self.size = 1
        self.elements = [[x,y]]
        self.radius = 10
        self.speed = 5
        self.dx = 0
        self.dy = 5
        self.size_add = False
        self.color = color
        self.level_snake = 0

    def is_add(self):
        self.size +=1
        self.elements.append([0,0])
        self.size_add = False

    def move(self):
        if self.size_add:
            self.is_add()
            
        for i in range(self.size-1, 0 ,-1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

        if self.elements[0][0] < 0:
            self.elements[0][0] = 800      
        if self.elements[0][0] > 800:
            self.elements[0][0] = 0
        if self.elements[0][1] < 0:
            self.elements[0][1] = 800      
        if self.elements[0][1] > 800:
            self.elements[0][1] = 0


    def eat_food(self,Foodx,Foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if (x-self.radius-10 <= Foodx <= x+self.radius+10) and (y-self.radius-10 <= Foody <= y+self.radius+10):
            self.is_add()
            food.random_food()
            self.level_snake+=1
            if self.level_snake%5==0:
                self.speed+=1
        

    def draw(self):
        for x in self.elements:
            pygame.draw.circle(win, self.color,x,self.radius)

def game_over():
    f1 = pygame.font.SysFont('serif', 100)
    f2 = pygame.font.SysFont('serif', 25)
    text1 = f1.render("Game over", True, (255, 0, 0))
    text2 = f2.render("If you want to continue press R",True,(255,0,0))
    win.blit(text1,(170,250))
    win.blit(text2,(220,350))
    snake1.dx = 0
    snake1.dy = 0
    snake2.dx = 0
    snake2.dy = 0
def draw_level_2():
    pygame.draw.rect(win,(0,0,255),(200,200,50,400))
    pygame.draw.rect(win,(0,0,255),(550,200,50,400))
    pygame.draw.rect(win,(0,0,255),(250,375,350,50))

def level2():
    global game_overr
    if ((200-snake1.radius < snake1.elements[0][0] < 250+snake1.radius) and (200-snake1.radius < snake1.elements[0][1] < 600+snake1.radius)) or ((550-snake1.radius < snake1.elements[0][0] < 600+snake1.radius) and (200-snake1.radius < snake1.elements[0][1] < 600+snake1.radius)) or ((250-snake1.radius < snake1.elements[0][0] < 600+snake1.radius) and (375-snake1.radius < snake1.elements[0][1] < 425+snake1.radius)):
        game_overr = True
        pygame.mixer.music.stop()
        pygame.mixer.music.load("game_over.mp3")
        pygame.mixer.music.play()
    if snake2_play:
        if ((200-snake2.radius < snake2.elements[0][0] < 250+snake2.radius) and (200-snake2.radius < snake2.elements[0][1] < 600+snake2.radius)) or ((550-snake2.radius < snake2.elements[0][0] < 600+snake2.radius) and (200-snake2.radius < snake2.elements[0][1] < 600+snake2.radius)) or ((250-snake2.radius < snake2.elements[0][0] < 600+snake2.radius) and (375-snake2.radius < snake2.elements[0][1] < 425+snake2.radius)):
            game_overr = True
            pygame.mixer.music.stop()
            pygame.mixer.music.load("game_over.mp3")
            pygame.mixer.music.play()

def draw_level_3():
    pygame.draw.rect(win,(0,0,255),(0,0,800,25))
    pygame.draw.rect(win,(0,0,255),(0,0,25,800))
    pygame.draw.rect(win,(0,0,255),(0,775,800,25))
    pygame.draw.rect(win,(0,0,255),(775,0,25,800))
    pygame.draw.rect(win,(0,0,255),(200,200,50,400))
    pygame.draw.rect(win,(0,0,255),(550,200,50,400))
    pygame.draw.rect(win,(0,0,255),(250,375,350,50))

def level3():
    global game_overr
    if ((200-snake1.radius < snake1.elements[0][0] < 250+snake1.radius) and (200-snake1.radius < snake1.elements[0][1] < 600+snake1.radius)) or ((550-snake1.radius < snake1.elements[0][0] < 600+snake1.radius) and (200-snake1.radius < snake1.elements[0][1] < 600+snake1.radius)) or ((250-snake1.radius < snake1.elements[0][0] < 600+snake1.radius) and (375-snake1.radius < snake1.elements[0][1] < 425+snake1.radius)) or (25+snake1.radius>snake1.elements[0][0]) or (snake1.elements[0][0]>775-snake1.radius) or (25+snake1.radius>snake1.elements[0][1]) or (snake1.elements[0][1]>775-snake1.radius):
        game_overr = True
        pygame.mixer.music.stop()
        pygame.mixer.music.load("game_over.mp3")
        pygame.mixer.music.play()
    if snake2_play:
        if ((200-snake2.radius < snake2.elements[0][0] < 250+snake2.radius) and (200-snake2.radius < snake2.elements[0][1] < 600+snake2.radius)) or ((550-snake2.radius < snake2.elements[0][0] < 600+snake2.radius) and (200-snake2.radius < snake2.elements[0][1] < 600+snake2.radius)) or ((250-snake2.radius < snake2.elements[0][0] < 600+snake2.radius) and (375-snake2.radius < snake2.elements[0][1] < 425+snake2.radius)) or (25+snake2.radius>snake2.elements[0][0]) or (snake2.elements[0][0]>775-snake2.radius) or (25+snake2.radius>snake2.elements[0][1]) or (snake2.elements[0][1]>775-snake2.radius):
            game_overr = True
            pygame.mixer.music.stop()
            pygame.mixer.music.load("game_over.mp3")
            pygame.mixer.music.play()

def draw_menu():
    background = pygame.image.load("background.png")
    player_1 = pygame.image.load("1.png")
    player_2 = pygame.image.load("2.png")
    game_exit = pygame.image.load("Exit.png")
    save = pygame.image.load("save.png")
    win.blit(background, (0,0))
    win.blit(player_1 ,(300,200))
    win.blit(player_2 ,(300,300))
    win.blit(save ,(300,400))
    win.blit(game_exit,(300,500))

def choice_menu(pos):
    global MENU
    global Level
    global snake2
    global snake2_play
    if (300 <= pos[0] <= 300+200) and (200 <= pos[1] <= 250):
        MENU = False
        Level = True
        snake2_play = False
    if (300 <= pos[0] <= 300+200) and (300 <= pos[1] <= 350):
        MENU = False
        Level = True
        snake2_play = True
    if (300 <= pos[0] <= 300+200) and (400 <= pos[1] <= 450):
        pass
    if (300 <= pos[0] <= 300+200) and (500 <= pos[1] <= 550):
        exit()

def draw_level():
    level1 = pygame.image.load("1level.png")
    level2 = pygame.image.load("2level.png")
    level3 = pygame.image.load("3level.png")
    win.blit(level1,(50,300))
    win.blit(level2,(300,300))
    win.blit(level3,(550,300))
    
def choice_level(pos):
    global Level
    global run
    global level_2
    global level_3
    global snake2, snake1
    if (50 <= pos[0] <= 250) and (300 <= pos[1] <= 500):
        Level = False
        run = True   
        level_2 = False 
        level_3 = False   
        snake1.elements = [[50,50]]
        snake2.elements = [[100,200]]
        snake1 = Snake(50,50,(0,0,255))
        snake2 = Snake(100,200,(0,255,0))
    if (300 <= pos[0] <= 500) and (300 <= pos[1] <= 500):
        level_2 = True
        level_3 = False
        Level = False
        run = True
        snake1.elements = [[50,50]]
        snake2.elements = [[100,200]]
        snake1 = Snake(50,50,(0,0,255))
        snake2 = Snake(100,200,(0,255,0))
    if (550 <= pos[0] <= 750) and (300 <= pos[1] <= 500):
        level_3 = True
        level_2 = False
        Level = False
        run = True
        snake1.elements = [[50,50]]
        snake2.elements = [[100,200]]
        snake1 = Snake(50,50,(0,0,255))
        snake2 = Snake(100,200,(0,255,0))





snake1 = Snake(50,50,(0,0,255))
snake2 = Snake(100,200,(0,255,0))
snake2_play = False
food = Food()
play_game = True
run = False
MENU = True
Level = False
level_1 = True
level_2 = False
level_3 = False
game_overr = False


while play_game:
    while MENU:    
        win.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                choice_menu(event.pos)
        draw_menu()
        pygame.display.update()
    
    while Level:    
        win.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                choice_level(event.pos)
        draw_level()
        pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MENU = True
                    run = False
                if event.key == pygame.K_r:
                    snake1.elements = [[50,50]]
                    snake2.elements = [[100,200]]
                    snake1 = Snake(50,50,(0,0,255))
                    snake2 = Snake(100,200,(0,255,0))
                    game_overr = False
                    pygame.mixer.music.load("muz.mp3")
                    pygame.mixer.music.play()
                    food.random_food()
                    
    
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and snake1.dy==0:
            snake1.dx = 0
            snake1.dy = -snake1.speed
        if pressed[pygame.K_DOWN] and snake1.dy==0:
            snake1.dx = 0
            snake1.dy = snake1.speed
        if pressed[pygame.K_RIGHT] and snake1.dx==0:
            snake1.dx = snake1.speed
            snake1.dy = 0
        if pressed[pygame.K_LEFT] and snake1.dx==0:
            snake1.dx = -snake1.speed
            snake1.dy = 0
        
        if snake2_play:
            if pressed[pygame.K_w] and snake2.dy==0:
                snake2.dx = 0
                snake2.dy = -snake2.speed
            if pressed[pygame.K_s] and snake2.dy==0:
                snake2.dx = 0
                snake2.dy = snake2.speed
            if pressed[pygame.K_d] and snake2.dx==0:
                snake2.dx = snake2.speed
                snake2.dy = 0
            if pressed[pygame.K_a] and snake2.dx==0:
                snake2.dx = -snake2.speed
                snake2.dy = 0

        win.fill((0,0,0))
        if not game_overr:
            if level_2:
                level2()
            if level_3:
                level3()
        if level_2:
                draw_level_2()
        if level_3:
                draw_level_3()
        if game_overr:
            game_over()
        food.draw_food()
        snake1.draw()
        snake1.eat_food(food.food_x,food.food_y)
        snake1.move()
        
        if snake2_play:
            snake2.draw()
            snake2.eat_food(food.food_x,food.food_y)
            snake2.move()
        
        
        pygame.display.flip()
        pygame.time.delay(30)

pygame.quit()
            
