from random import randint
import pygame as pg
from spritesheet import Spritesheet
from entity import Entity
from objects import Arrow

SPRITE_SHEET = Spritesheet("ranger-sheet.png")

class Ranger(Entity):
    def __init__(self, map_pos_x, map_pos_y, pos_x, pos_y):
        super().__init__(map_pos_x, map_pos_y)
        
        self.previous_move_time = 0
        self.move_queue = []

        self.images = [SPRITE_SHEET.load_strip((0, i*50, 50, 50), 4, -1) 
                       for i in range(4)]
        self.direction = 2
        self.image = self.images[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damaged = False
        self.health = 5
        self.arrow = None

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
            return

        next_move = self.move_queue.pop(0)
        if self.map_pos_y > next_move[0]:
            self.direction_y = -50
        if self.map_pos_y < next_move[0]:
            self.direction_y = 50
        if self.map_pos_x > next_move[1]:
            self.direction_x = -50
        if self.map_pos_x < next_move[1]:
            self.direction_x = 50

    def update(self, current_time):
        if current_time - self.last_updated >= 120:
            if self.is_moving:
                self.walking_animation()
                self.image = self.images[self.direction][self.frame]
            self.last_updated = current_time

    def shoot(self):
        self.arrow = Arrow(self.rect.y, self.rect.x, self.direction)
        return self.arrow

    def hurt(self):
        self.current_health -= 1
        if self.current_health == 0:
            self.kill()
