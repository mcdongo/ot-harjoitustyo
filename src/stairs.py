import os
import pygame as pg
from floor import Floor

DIRNAME = os.path.dirname(__file__)


class Stairs(Floor):
    """An object which is required for the game to switch levels

    Attributes:
        image: a pygame image
    """
    def __init__(self, x, y):
        """Class constructor

        Args:
            x: spot on the x-axis on the screen
            y: spot on the y-axis on the screen
        """
        super().__init__(x, y)
        self.image = pg.image.load(
            os.path.join(DIRNAME, "assets", "stairs.png"))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
