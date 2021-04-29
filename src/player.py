import pygame as pg
from entity import Entity
from spritesheet import Spritesheet

SPRITE_SHEET = Spritesheet("player-spritesheet.png")
STAB_SPRITE_SHEET = Spritesheet("playerstab.png")
PLAYER_SHIELDED_SHEET = Spritesheet("playershielded-sheet.png")

class Player(Entity):
    def __init__(self, map_pos_x, map_pos_y, pos_x=0, pos_y=0):
        super().__init__(map_pos_x, map_pos_y)
        self.images = [SPRITE_SHEET.load_strip((0, i*50, 50, 50), 4, -1)
                       for i in range(4)]

        self.direction = 2
        self.stab_images = STAB_SPRITE_SHEET.load_strip((0, 0, 50, 50), 4, -1)
        self.shielded_images = PLAYER_SHIELDED_SHEET.load_strip((0, 0, 50, 50), 4, -1)
        self.image = self.images[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.health = 5
        self.shielded = False

    def change_direction(self, direction):
        self.direction = direction
        self.image = self.images[self.direction][self.frame]

    def update(self, current_time):
        if self.shielded:
            return

        if current_time - self.last_updated >= 120:
            if self.attack:
                self.attack_animation()
            else:
                self.walking_animation()
                self.image = self.images[self.direction][self.frame]
            self.last_updated = current_time

    def attack_animation(self):
        if self.image in self.stab_images:
            self.attack = False
            self.image = self.images[self.direction][0]
        else:
            self.image = self.stab_images[self.direction]

    def apply_shield(self):
        if self.shielded:
            self.shielded = False
            self.image = self.images[self.direction][self.frame]
        else:
            self.shielded = True
            self.image = self.shielded_images[self.direction]
            