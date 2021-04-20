import os
import pygame as pg


DIRNAME = os.path.dirname(__file__)


class Player(pg.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.direction = 2
        self.images = [
            pg.image.load(os.path.join(DIRNAME, "assets", "player1.png")),
            pg.image.load(os.path.join(DIRNAME, "assets", "player2.png")),
            pg.image.load(os.path.join(DIRNAME, "assets", "player3.png")),
            pg.image.load(os.path.join(DIRNAME, "assets", "player4.png"))
        ]
        self.image = self.images[self.direction]
        # self.image.fill((0,255,0))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def change_direction(self, direction):
        self.direction = direction
        self.image = self.images[direction]
