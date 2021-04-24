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

        self.is_moving = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 5
        self.damaged = False
        self.time_red = 0

    def should_move(self, current_time):
        if current_time:
            return current_time - self.previous_move_time >= 1200
        return False

    def hurt(self):
        self.health -= 1
        self.image.fill([255,0,0])
        self.damaged = True
        self.time_red = 10
        print(self.health)
        if self.health == 0:
            self.kill()

    def update(self):
        if self.damaged:
            if self.time_red > 0:
                self.time_red -= 1
            else:
                self.image.fill([50, 50, 50])
                self.damaged = False