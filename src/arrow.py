import pygame as pg
from spritesheet import Spritesheet
SPRITE_SHEET = Spritesheet("arrow-sheet.png")

class Arrow(pg.sprite.Sprite):
    def __init__(self, pos_y, pos_x, direction):
        super().__init__()
        self.image = SPRITE_SHEET.image_at((direction*50, 0, 50, 50), -1)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.direction_x, self.direction_y = 0, 0
        if direction == 0:
            self.direction_y = -10
        if direction == 1:
            self.direction_x = 10
        if direction == 2:
            self.direction_y = 10
        if direction == 3:
            self.direction_x = -10

    def update(self):
        self.rect.move_ip(self.direction_x, self.direction_y)
