from random import choice
import pygame as pg
from spritesheet import Spritesheet

class Floor(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.sprite_sheet = Spritesheet("floor.png")
        self.image = choice(self.sprite_sheet.load_strip((0, 0, 50, 50), 4))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
