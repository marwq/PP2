from datetime import datetime

import pygame


pygame.init()
screen = pygame.display.set_mode((1400, 1050))
done = False

class Img:
    base_path = "lab7/clock/img/"
    clock = pygame.image.load(f"{base_path}mickeyclock.jpeg")
    left = pygame.image.load(f"{base_path}left.png")
    right = pygame.image.load(f"{base_path}right.png")
    
    left_rect = left.get_rect(center=(700, 525))
    right_rect = right.get_rect(center=(700, 525))
    
    
def get_minute_angle():
    now = datetime.now()
    minute = now.minute + 9
    return minute * -6

def get_second_angle():
    now = datetime.now()
    second = now.second - 9.5
    return second * -6

def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

def draw_all():
    screen.blit(Img.clock, (0, 0))
    
    left_rotated, left_rotated_rect = rot_center(Img.left, Img.left_rect, get_minute_angle())
    right_rotated, right_rotated_rect = rot_center(Img.right, Img.right_rect, get_second_angle())
    
    screen.blit(left_rotated, left_rotated_rect)
    screen.blit(right_rotated, right_rotated_rect)
    
    pygame.display.flip()
    
def events_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global done
            done = True

while not done:
    draw_all()
    events_handler()