import os
import pygame as pg
from spritesheet import Spritesheet

ARROW_SPRITE_SHEET = Spritesheet("arrow-sheet.png")
DIRNAME = os.path.dirname(__file__)

class Arrow(pg.sprite.Sprite):
    """Class for arrows to be fired either by the player or by the npcs.

    Attributes:
        pos_y: starting y position on the map
        pos_x: starting x position on the map
        direction: the direction the arrow is facing (0-3, going clockwise, 0 being up)
        image: a pygame surface object (spritesheet image)
        rect: a pygame rect object
    """

    def __init__(self, pos_y, pos_x, direction):
        """Class constructor, which creates a new arrow

        Args:
            pos_y: starting y position on the map
            pos_x: starting x position on the map
            direction: the direction the arrow is facing (0-3, going clockwise, 0 being up)
        """
        super().__init__()
        self.image = ARROW_SPRITE_SHEET.image_at((direction*50, 0, 50, 50), -1)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.direction = direction
        self.direction_x, self.direction_y = 0, 0
        if direction == 0:
            self.direction_y = -5
        if direction == 1:
            self.direction_x = 5
        if direction == 2:
            self.direction_y = 5
        if direction == 3:
            self.direction_x = -5

    def update(self):
        """A method which moves the arrow in the intended direction

        """
        self.rect.move_ip(self.direction_x, self.direction_y)

class Item(pg.sprite.Sprite):
    """Class for item objects which can be picked up in the level

    Atrributes:
        image: pygame surface object
        rect: a pygame rect object
        map_pos_x: spot on the x-axis in the map
        map_pos_y: spot on the y-axis in the map
    """
    def __init__(self, map_pos_x, map_pos_y, pos_x, pos_y):
        """A class constructor. Loads wanted image into memory

        Args:
            map_pos_x: spot on x-axis in the map
            map_pos_y: spot on y-axis in the map
            pos_x: spot on the screen on the x-axis
            pos_y: spot on the screen on the y-axis
        """
        super().__init__()
        self.image = pg.image.load(os.path.join(DIRNAME, "assets", "health_potion.png"))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.map_pos_x = map_pos_x
        self.map_pos_y = map_pos_y
