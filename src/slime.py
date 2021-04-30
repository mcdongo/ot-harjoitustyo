import os
from random import randint
import pygame as pg
from spritesheet import Spritesheet
from entity import Entity

DIRNAME = os.path.dirname(__file__)
SPRITE_SHEET = Spritesheet("slime-spritesheet.png")


class Slime(Entity):
    def __init__(self, map_pos_x, map_pos_y, pos_x, pos_y):
        super().__init__(map_pos_x, map_pos_y)

        self.previous_move_time = 0
        self.move_queue = []

        self.images = SPRITE_SHEET.load_strip((0, 0, 50, 50), 4, -1)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damaged = False
        self.time_red = 0
        self.health = 5

    def should_move(self, current_time):
        if current_time:
            return current_time - self.previous_move_time >= 1800
        return False

    def next_move(self):
        if self.move_queue == []:
            direction = randint(0, 3)
            if direction == 0:
                self.direction_y = -50
            if direction == 1:
                self.direction_x = 50
            if direction == 2:
                self.direction_y = 50
            if direction == 3:
                self.direction_x = -50
        else:
            next_move = self.move_queue.pop(0)
            if self.map_pos_y > next_move[0]:
                self.direction_y = -50
            if self.map_pos_y < next_move[0]:
                self.direction_y = 50
            if self.map_pos_x > next_move[1]:
                self.direction_x = -50
            if self.map_pos_x < next_move[1]:
                self.direction_x = 50


    def hurt(self):
        self.health -= 1
        self.image.fill([255, 0, 0])
        self.damaged = True
        self.time_red = 10
        if self.health == 0:
            self.kill()

    def update(self, current_time):
        if current_time - self.last_updated >= 120:
            if self.is_moving:
                self.walking_animation()
                self.image = self.images[self.frame]
                self.last_updated = current_time

        if self.damaged:
            if self.time_red > 0:
                self.time_red -= 1
            else:
                self.image.fill([50, 50, 50])
                self.damaged = False

    '''def walking_animation(self):
        if self.frame == 3:
            self.frame = 0
        else:
            self.frame += 1
        self.image = self.images[self.frame]'''
