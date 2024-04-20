#imports
import pygame as pg
import random
import time
import psycopg2

#connection to server
conn = psycopg2.connect(
    host='localhost',
    database='snake_game',
    user='postgres',
    password='password'
    )
# create a Cursor
cur = conn.cursor()

#create table
cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                user_name VARCHAR(20) PRIMARY KEY,
                user_score INT,
                user_level INT
            )
            """)

# get user name
user_name = input("Enter your username : ")
user_score = 0 
user_level = 1
# checking if it's new user 
cur.execute("""
            SELECT * FROM users
            WHERE user_name ='{}'
            """.format(user_name))

user = cur.fetchone()
if user==None:
    cur.execute("""
                INSERT INTO users (user_name,user_score,user_level)
                VALUES ('{}','{}','{}')
                """.format(user_name,user_score,user_level)
                )
    conn.commit()
else :
    user_name,user_score,user_level = user

clock = pg.time.Clock()
score = 0
score_level = 0
level = user_level
snake_speed = 10

#initializing
pg.init()

#screen sets
width = 800
height= 600
screen = pg.display.set_mode((width, height))

#for checking is our snake eat food
snake_pos = [100,60]

#snake body parts(by default the starting  4 blocks) 
snake_body = [
    [100,60], 
    [80,60],
    [60,60],
    [40,60],
]

#for checking if snake eat
food_eaten = False

#food's pos
food_pos = [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]

# current direction for checking to (by default to right)
direction = 'RIGHT'
#changing direction 
change_to = direction


def game_over():
    font = pg.font.Font("lab10/BebasNeue-Regular.ttf", 50)
    game_over_surface = font.render("Game Over", True, (0, 255, 0))
    screen.fill('red')
    score_surface = font.render("SCORES:"+str(score), True, (0, 255, 0))
    screen.blit(score_surface, score_surface.get_rect(center = (width//2+100,height//2+100)) )
    screen.blit(game_over_surface, game_over_surface.get_rect(center= (width//2,height//2)) )
    pg.display.flip()
    time.sleep(2)
    pg.quit()
    quit()

def score_to_screen():
    font = pg.font.Font("lab10/BebasNeue-Regular.ttf", 20)
    score_surface = font.render("SCORES:"+str(score), True, (0, 255, 0))
    screen.blit(score_surface, score_surface.get_rect(center = (150,10)) )

def level_to_screen():
    font = pg.font.Font("lab10/BebasNeue-Regular.ttf", 20)
    level_surface = font.render("level:"+str(level), True, (0, 255, 0))
    screen.blit(level_surface, level_surface.get_rect(center= (50,10)) )

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            cur.execute("""
                        UPDATE users 
                        SET user_score = '{}', user_level = '{}'
                        WHERE user_name = '{}'
                        """.format(score,level,user_name))
            conn.commit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pg.K_LEFT:
                change_to = "LEFT"
            if event.key == pg.K_UP:
                change_to = "UP"
            if event.key == pg.K_DOWN:
                change_to = "DOWN"
    
    # CHECKING  TO NOT GO ON ITSELF
    if change_to=="RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to=="LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to=="UP" and direction != "DOWN":
        direction = "UP"
    if change_to=="DOWN" and direction != "UP":
        direction = "DOWN"

    if direction == "RIGHT":
        snake_pos[0] += 20
    if direction == "LEFT":
        snake_pos[0] -= 20
    if direction == "UP":
        snake_pos[1] -= 20
    if direction == "DOWN":
        snake_pos[1] += 20

    snake_body.insert(0, list(snake_pos) )
    if snake_pos[0]==food_pos[0] and snake_pos[1]==food_pos[1]:
        score += 10
        score_level+=10
        food_eaten = True
        if score_level > 50 :
            level+=1
            score_level =0 
            snake_speed +=1
            print(snake_speed)
    else:
        snake_body.pop()
    
    if food_eaten:
        cant_choose = False 
        food_pos =  [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]
        for i in snake_body:
                if i==food_pos:
                    cant_choose = True
                    break
        while cant_choose:
            cant_choose = False
            food_pos =  [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]
            for i in snake_body:
                if i==food_pos:
                    cant_choose = True
                    break

    for i in snake_body:
        if food_eaten :
            food_pos =  [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]
        if i==food_pos:
            food_pos =  [random.randint(2,width//20-1)*20 ,random.randint(2,height//20-1)*20 ]

        
    
    food_eaten= False
    screen.fill('black')
    pg.draw.line(screen ,(0,255,0), (0,20), (800, 20) )
    pg .draw.rect(screen,(0,0,0),(780,1,19,19))

    pg.draw.rect(screen, 'red',(snake_body[0][0],snake_body[0][1], 20,20))
    for pos in snake_body[1:]:
        pg.draw.rect(screen, 'yellow',(pos[0],pos[1], 20,20))

    pg.draw.rect(screen, 'white', (food_pos[0], food_pos[1], 20, 20))

    # Touching corners
    if snake_pos[0]>width-20 or snake_pos[0]<0 or snake_pos[1]<20 or snake_pos[1]>height-20 :
        cur.execute("""
                        UPDATE users 
                        SET user_score = '{}', user_level = '{}'
                        WHERE user_name = '{}'
                        """.format(score,level,user_name))
        conn.commit()
        game_over()
    
    # Touching own body
    for part in snake_body[1:]:
        if snake_pos == part:
            cur.execute("""
                        UPDATE users 
                        SET user_score = '{}', user_level = '{}'
                        WHERE user_name = '{}'
                        """.format(score,level,user_name))
            conn.commit()
            game_over()
    
    score_to_screen()
    level_to_screen()

    pg.display.update()
    clock.tick(snake_speed)