import pygame as pg
from spritesheet import Spritesheet

class Player(pg.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.direction = 2
        self.frame = 0
        self.last_updated = 0
        self.sprite_sheet = Spritesheet("player-spritesheet.png")
        self.images = [self.sprite_sheet.load_strip((0, i*50, 50, 50), 4, -1)
                       for i in range(4)]
        self.image = self.images[self.direction][self.frame]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def change_direction(self, direction):
        self.direction = direction
        self.image = self.images[self.direction][self.frame]

    def update(self, current_time):
        if current_time - self.last_updated >= 160:
            if self.frame == 3:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.direction][self.frame]
            self.last_updated = current_time
