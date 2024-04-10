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
SPEED = 5
SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("img/AnimatedStreet.png")
bg_rect = background.get_rect()

background_2 = pygame.image.load("img/AnimatedStreet.png")
bg_rect_2 = background.get_rect()
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


def draw_road():
    bg_rect.move_ip(0, SPEED)
    bg_rect_2.y = bg_rect.y - bg_rect.height
    DISPLAYSURF.blit(background, bg_rect)
    DISPLAYSURF.blit(background_2, bg_rect_2)
    if bg_rect.y > SCREEN_HEIGHT:
        bg_rect.y = 0
        bg_rect_2.y = -bg_rect.height
    

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("img/Enemy.png")
        self.rect = self.image.get_rect()
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
        self.image_straight = pygame.image.load("img/Player.png")
        self.image_left = pygame.image.load("img/Player.png")
        self.image_right = pygame.image.load("img/Player.png")
        
        # rotate left and right
        self.image_left = pygame.transform.rotate(self.image_left, 7)
        self.image_right = pygame.transform.rotate(self.image_right, -7)
        
        self.image = self.image_straight
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
                self.image = self.image_left
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                self.image = self.image_right
        
        if (not pressed_keys[K_LEFT]) and (not pressed_keys[K_RIGHT]):
            self.image = self.image_straight
            
        
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin(random.randint(40, SCREEN_WIDTH - 40), 0)
C2 = Coin(random.randint(40, SCREEN_WIDTH - 40), -150)
C3 = Coin(random.randint(40, SCREEN_WIDTH - 40), -300)
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

coins = [C1, C2, C3]
coins_group = pygame.sprite.Group()
for i in coins:
    all_sprites.add(i)
    coins_group.add(i)

 
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
 
    draw_road()
    
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        #   pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()       
        
    if pygame.sprite.spritecollideany(P1, coins_group):
        for coin in coins:
            if pygame.sprite.collide_rect(P1, coin):
                coin.rect.top = 0
                coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), coin.rect.y-300)
                SCORE += 1
                break 
         
    pygame.display.update()
    FramePerSec.tick(FPS)