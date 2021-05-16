import os
from random import randint
from spritesheet import Spritesheet
from entity import Entity

DIRNAME = os.path.dirname(__file__)
SPRITE_SHEET = Spritesheet("slime-spritesheet.png")


class Slime(Entity):
    """A class for an Slime enemy type

    Attributes:
        previous_move_time: integer, last time moved in ticks
        move_queue: a list of moves in a queue
        images: a list of pygame surfaces
        direction: integer, which way this entity is facing (0-3)
        image: current displayed image
        rect: pygame rect object
        health_capacity: integer, maximum health
        current_health: integer, current health
        attack_time: integer, telling how many ticks is left in the animation
    """
    def __init__(self, map_pos_x, map_pos_y, pos_x, pos_y):
        """A class constructor

        Args:
            map_pos_x: spot on the map on the x-axis
            map_pos_y: sopt on the map on the y-axis
            pos_x: spot on the screen on the x-axis
            pos_y: spot on the screen on the y-axis
        """
        super().__init__(map_pos_x, map_pos_y)

        self.previous_move_time = 0
        self.move_queue = []

        self.images = SPRITE_SHEET.load_strip((0, 0, 50, 50), 4, -1)
        self.attack_images = SPRITE_SHEET.load_strip((0, 50, 50, 50), 4, -1)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.time_red = 0
        self.health_capacity = randint(3, 8)
        self.current_health = self.health_capacity
        self.attack_time = 0

    def should_move(self, current_time):
        """Determines if entity should move

        Returns:
            True if enough time has passed otherwise
        """
        if current_time:
            return current_time - self.previous_move_time >= randint(1200, 1800)
        return False

    def next_move(self):
        """A method which determines this entity's next move
        """
        if self.move_queue == [] or len(self.move_queue) > 10:
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


    def update(self, current_time):
        """A method which updates animations

        Args:
            current_time: how many ticks have passed since the game was booted
        """
        if current_time - self.last_updated >= 120:
            if self.is_moving:
                self.walking_animation()
                self.image = self.images[self.frame]
                self.last_updated = current_time

            if self.attack:
                if self.attack_time > 0:
                    self.attack_time -= 1
                    self.image = self.attack_images[self.direction]
                else:
                    self.attack = False
                    self.attack_time = 0
                    self.image = self.images[0]

    def start_attack(self):
        """A method which starts the attack animation of this entity
        """
        self.attack = True
        self.attack_time = 5
