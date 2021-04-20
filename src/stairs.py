import os
import pygame as pg
from floor import Floor

DIRNAME = os.path.dirname(__file__)


class Stairs(Floor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pg.image.load(
            os.path.join(DIRNAME, "assets", "stairs.png"))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
