#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
SCORE_COINS = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.image2 = pygame.image.load("brill.png")
        self.respawn()
    def move(self):
        self.rect.move_ip(0, SPEED // 2)  # коины падают медленнее врагов
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        if random.choice([True,False]): #здесь на рандом выбираем TRUE ИЛИ FALSE, нужно что бы наугад выбрать какой будет следующий коин
            self.current_image = self.image
            self.value = 1 # если монетка то +1 к скору
        else:
            self.current_image = self.image2
            self.value = 3 # если бриллиант то +3 к скору
        self.rect = self.current_image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), random.randint(-200, -50)))

 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() # родительский класс
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect() # даем рект для объекта чтобы могли использовать коллизию
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coins()
 
#Creating Sprites Groups
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(background, (0,0))
    #for score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    #for score_coins
    scores = font_small.render(str(SCORE_COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (350,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        if isinstance(entity, Coins):  # Если объект - коин
            DISPLAYSURF.blit(entity.current_image, entity.rect)
            entity.move()
        else:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
    # чекаем на то коснулись ли наши ректанглы между друг другом, если плэйер с коином, зарабатываем score 
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in coins:
            if P1.rect.colliderect(coin.rect):  # Проверяем конкретный коин
                SCORE_COINS += coin.value  # Добавляем нужное значение
                coin.respawn()  # Респавним коин
    # если достигли N или больше,  который дал нам юзер, увеличваем скорость врага
    if SCORE_COINS >= 5:
        ENEMY_SPEED = 13

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)