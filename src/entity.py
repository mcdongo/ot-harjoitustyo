import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, map_pos_x, map_pos_y):
        super().__init__()
        self.frame = 0
        self.last_updated = 0
        self.is_moving = False
        self.attack = False
        self.map_pos_x = map_pos_x
        self.map_pos_y = map_pos_y
        self.health = 0
        self.moved = 0
