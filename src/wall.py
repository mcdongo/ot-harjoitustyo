import pygame as pg


class Wall(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pg.Surface([50, 50])
        self.image.fill((0, 0, 0))#211, 211, 211))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
