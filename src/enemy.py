import os
import pygame as pg

DIRNAME = os.path.dirname(__file__)


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.previous_move_time = 0

        '''self.image = pg.image.load(
            os.path.join(dirname, "assets", "enemy.png")
        )'''

        self.image = pg.Surface([50, 50])
        self.image.fill([50, 50, 50])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def should_move(self, current_time):
        if current_time:
            return current_time - self.previous_move_time >= 500
        return False
