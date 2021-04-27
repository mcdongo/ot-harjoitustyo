import pygame as pg
from spritesheet import Spritesheet

SPRITE_SHEET = Spritesheet("player-spritesheet.png")
STAB_SPRITE_SHEET = Spritesheet("playerstab.png")

class Player(pg.sprite.Sprite):
    def __init__(self, map_pos_x, map_pos_y, pos_x=0, pos_y=0):
        super().__init__()
        self.direction = 2
        self.frame = 0
        self.last_updated = 0
        self.images = [SPRITE_SHEET.load_strip((0, i*50, 50, 50), 4, -1)
                       for i in range(4)]

        self.stab_images = STAB_SPRITE_SHEET.load_strip((0, 0, 50, 50), 4, -1)
        self.image = self.images[self.direction][self.frame]
        self.rect = self.image.get_rect()

        self.is_moving = False
        self.attack = False
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.map_pos_x = map_pos_x
        self.map_pos_y = map_pos_y
        self.health = 10
        self.moved = 0

    def change_direction(self, direction):
        self.direction = direction
        self.image = self.images[self.direction][self.frame]

    def update(self, current_time):
        if current_time - self.last_updated >= 120:
            if self.attack:
                self.attack_animation()
            else:
                self.walking_animation()
            self.last_updated = current_time

    def walking_animation(self):
        if self.frame == 3:
            self.frame = 0
        else:
            self.frame += 1
        self.image = self.images[self.direction][self.frame]

    def attack_animation(self):
        if self.image in self.stab_images:
            self.attack = False
            self.image = self.images[self.direction][0]
        else:
            self.image = self.stab_images[self.direction]
            