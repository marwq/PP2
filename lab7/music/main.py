from __future__ import annotations

import os
import pygame


class App:
    def __init__(self, songs_folder: str):
        self.done = False
        self.songs_folder = songs_folder
        self.screen = pygame.display.set_mode((400, 400))
        files = os.listdir(songs_folder)
        self.songs = [f for f in files if f.endswith('.mp3')]
        self.count = len(self.songs)
        self.curr_id = 0
        self.is_playing = False
        self.set_buttons()
        
    def set_buttons(self):
        self.buttons = [
            [self.prev_song, (28, 300, 110, 100)],
            [self.play_pause, (145, 300, 110, 100)],
            [self.next_song, (262, 300, 110, 100)]
        ]
        
    def start(self):
        pygame.mixer.init()
        pygame.init()
        
        pygame.mixer.music.load(
            os.path.join(self.songs_folder, self.songs[self.curr_id])
        )
        pygame.mixer.music.play()
        self.is_playing = True
        
        while not self.done:
            self.handle_events()
            self.draw_all()
            pygame.display.flip()
    
    class Img:
        base_path = "lab7/music/img/"
        ui = pygame.image.load(f"{base_path}ui.png")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.next_song()
                if event.key == pygame.K_LEFT:
                    self.prev_song()
                if event.key == pygame.K_SPACE:
                    self.play_pause()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0], event.pos[1]
                for button in self.buttons:
                    x0, y0, x1, y1 = button[1]
                    x1 += x0
                    y1 += y0
                    if x0 <= x <= x1 and y0 <= y <= y1:
                        button[0]()
                
    def next_song(self):
        self.curr_id = (self.curr_id + 1) % self.count
        print(f'> NEXT | Playing {self.songs[self.curr_id]}')
        pygame.mixer.music.load(
            os.path.join(self.songs_folder, self.songs[self.curr_id])
        )
        pygame.mixer.music.play()
        self.is_playing = True
        
    def prev_song(self):
        self.curr_id = (self.curr_id - 1) % self.count
        print(f'> PREV | Playing {self.songs[self.curr_id]}')
        pygame.mixer.music.load(
            os.path.join(self.songs_folder, self.songs[self.curr_id])
        )
        pygame.mixer.music.play()
        self.is_playing = True
        
    def play_pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.is_playing = not self.is_playing
        print('> RESUME' if self.is_playing else '> PAUSE')

    def draw_all(self):
        self.screen.blit(App.Img.ui, (0, 0))
        text = self.songs[self.curr_id]
        if len(text) > 25:
            text = text[:25] + '...'
        self.screen.blit(
            pygame.font.SysFont('arial', 20).render(
                text, True, (255, 255, 255)
            ), (45, 206)
        )
        pos = pygame.mixer.music.get_pos()
        pos = f'{pos // 60000:0>2}:{(pos // 1000) % 60:0>2}'
        self.screen.blit(
            pygame.font.SysFont('arial', 14).render(
                pos, True, (255, 255, 255)
            ), (45, 230)
        )


if __name__ == "__main__":
    app = App(
        songs_folder='lab7/music/songs/'
    )
    app.start()