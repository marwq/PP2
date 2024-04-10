from __future__ import annotations

import sys
import random
import pygame as pg
from pygame.locals import *



pg.init()


def load_images() -> list[list[pg.Surface]]:
    graphics = pg.image.load("img/snake-graphics.png")
    images = [[None for _ in range(4)] for _ in range(5)]
    
    for i in range(5):
        for j in range(4):
            images[i][j] = graphics.subsurface((i*64, j*64, 64, 64))
    
    return images

class Graphics:
    BACKGROUND_COLOR = (244, 202, 22)
    
    images = load_images()
    images_head: dict[tuple[int, int], pg.Surface] = {
        (1, 0): images[4][0],
        (0, 1): images[4][1],
        (-1, 0): images[3][1],
        (0, -1): images[3][0]
    }
    images_tail: dict[tuple[int, int], pg.Surface] = {
        (1, 0): images[4][2],
        (0, 1): images[4][3],
        (-1, 0): images[3][3],
        (0, -1): images[3][2]
    }
    images_body: dict[tuple[int, int], pg.Surface] = {
        (1, 0): images[1][0],
        (0, 1): images[2][1]
    }
    images_bend: dict[tuple[tuple[int, int], tuple[int, int]], pg.Surface] = {
        ((1, 0), (0, 1)): images[2][0],
        ((0, 1), (-1, 0)): images[2][2],
        ((-1, 0), (0, -1)): images[0][1],
        ((0, -1), (1, 0)): images[0][0],
        ((1, 0), (0, -1)): images[2][2],
        ((0, -1), (-1, 0)): images[2][0],
        ((-1, 0), (0, 1)): images[0][0],
        ((0, 1), (1, 0)): images[0][1]
    }
    image_apple = images[0][3]
    font_small = pg.font.SysFont("Verdana", 20)

class Snake:
    def __init__(self, apples_count: int  = 1) -> None:
        self.alive = True
        self.world: list[list[tuple[int, int] | None]] = [[None for _ in range(13)] for _ in range(13)]
        self.head = (3, 4)
        self.tail = (1, 4)
        for i in range(1, 4):
            self.world[i][4] = (i+1, 4)
        self.direction = (1, 0)
        self.apples: set[tuple[int, int]] = set()
        self.apples = {self._generate_apple_position() for _ in range(apples_count)}
        self.score = 0
        
    @staticmethod
    def _coordinates_to_rect(x: int, y: int) -> pg.Rect:
        return pg.Rect(x*64, y*64, 64, 64)
    
    def _generate_apple_position(self) -> tuple[int, int]:
        self.all_positions = set((i, j) if not self.world[i][j] else None for j in range(12) for i in range(12))
        self.all_positions -= self.apples
        self.all_positions -= {None}
        return random.choice(list(self.all_positions))
        
    def die(self):
        self.alive = False
        print('die')
            
    def update(self):
        self.controls()
        
        # move head
        hx, hy = self.head
        dx, dy = self.direction
        new_hx, new_hy = hx + dx, hy + dy
        
        # Проверяем, не врезалась ли голова в стену или в тело, перед обновлением world
        if new_hx < 0 or new_hx >= 12 or new_hy < 0 or new_hy >= 12 or self.world[new_hx][new_hy] is not None:
            self.die()
            return
        
        # Обновляем голову в world
        self.head = new_hx, new_hy
        self.world[hx][hy] = self.head
        self.world[new_hx][new_hy] = (new_hx + dx, new_hy + dy)
        
        # collect apple
        collected = False
        if self.head in self.apples:
            self.apples.remove(self.head)
            self.apples.add(self._generate_apple_position())
            collected = True
            self.score += 1
        
        # move tail
        if not collected:
            tx, ty = self.tail
            next_tx, next_ty = self.world[tx][ty]
            self.world[tx][ty] = None
            self.tail = next_tx, next_ty
        
        # check if head is on wall
        if new_hx < 0 or new_hx >= 12 or new_hy < 0 or new_hy >= 12:
            self.die()
        
    def controls(self):
        pressed = pg.key.get_pressed()
        controls: dict[int, tuple[int, int]] = {
            pg.K_UP: (0, -1),
            pg.K_DOWN: (0, 1),
            pg.K_LEFT: (-1, 0),
            pg.K_RIGHT: (1, 0)
        }
        current_direction = self.direction
        for key, new_direction in controls.items():
            if pressed[key]:
                if current_direction != (-new_direction[0], -new_direction[1]):
                    self.direction = new_direction
                    break
            
                
    def draw(self, screen: pg.Surface) -> None:
        screen.fill(Graphics.BACKGROUND_COLOR)
        for x, y in self.apples:
            screen.blit(Graphics.image_apple, self._coordinates_to_rect(x, y))
        
        # Начинаем с хвоста
        tx, ty = self.tail
        next_ = self.world[tx][ty]
        
        if next_ is not None:  # Убедимся, что следующий сегмент существует
            tail_direction = (next_[0] - tx, next_[1] - ty)
            screen.blit(Graphics.images_tail[tail_direction], self._coordinates_to_rect(tx, ty))
        else:  # Если змея состоит только из головы, просто нарисуем голову
            screen.blit(Graphics.images_head[self.direction], self._coordinates_to_rect(tx, ty))
            return  # Завершаем функцию, если змея слишком мала
        
        cur_ = (tx, ty)
        while next_:
            prev_ = cur_
            cur_ = next_
            next_ = self.world[cur_[0]][cur_[1]] if cur_ else None
            
            if next_:  # Для тела змеи
                dx1, dy1 = cur_[0] - prev_[0], cur_[1] - prev_[1]
                if next_:
                    dx2, dy2 = next_[0] - cur_[0], next_[1] - cur_[1]
                # Для изгибов
                if dx1 != dx2 or dy1 != dy2:
                    screen.blit(Graphics.images_bend[((dx1, dy1), (dx2, dy2))], self._coordinates_to_rect(cur_[0], cur_[1]))
                else:  # Для прямого участка тела
                    screen.blit(Graphics.images_body[(abs(dx1), abs(dy1))], self._coordinates_to_rect(cur_[0], cur_[1]))
            else:  # Для головы змеи
                screen.fill(Graphics.BACKGROUND_COLOR, self._coordinates_to_rect(prev_[0], prev_[1]))
                screen.blit(Graphics.images_head[self.direction], self._coordinates_to_rect(prev_[0], prev_[1]))
    
        scores = Graphics.font_small.render(f'Level {self.score}', True, (0, 0, 0))
        screen.blit(scores, (10,10))

                
                
def main():
    snake = Snake()
    screen = pg.display.set_mode((12*64, 12*64))
    clock = pg.time.Clock()
    while snake.alive:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                snake.alive = False
        snake.update()
        snake.draw(screen)
        pg.display.flip()
        clock.tick(5+snake.score)
    
    
if __name__ == '__main__':
    main()