import pygame as pg


class Floor(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.Surface([50, 50])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
