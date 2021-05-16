import pygame as pg


class Wall(pg.sprite.Sprite):
    """A class for walls which surround and form obstacles in the level

    Attributes:
        image: pygame image
    """
    def __init__(self, pos_x, pos_y):
        """A class constructor

        Args:
            pos_x: position on the screen on the x-axis
            pos_y: position on the screen on the y-axis
        """
        super().__init__()

        self.image = pg.Surface([50, 50])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
