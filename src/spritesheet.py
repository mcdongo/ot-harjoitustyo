import os
import pygame as pg

DIRNAME = os.path.dirname(__file__)

class Spritesheet():
    """Takes full spritesheet images and turns them into pygame.surface objects with wanted
    width and height

    Attributes:
        sheet: A complete spritesheet image
    """
    def __init__(self, filename):
        """A class constructor

        Args:
            filename: str, name of the file
        """
        try:
            self.sheet = pg.image.load(os.path.join(DIRNAME, "assets", filename))
        except Exception as message:
            print("Unable to load spritesheet image: {0}".format(filename))
            raise SystemExit(message)

    def image_at(self, rectangle, colorkey=None):
        """Function which gets a specific sprite out of a spritesheet

        Args:
            rectangle: a pygame rectangle object
            colorkey: the color which the user wants to get filtered out
        Returns:
            image: a pygame surface object
        """
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size)
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image

    def images_at(self, rects, colorkey=None):
        """Function which gets several sprites from a spritesheet image

        Args:
            rects: a list of pygame rect objects
            colorkey: the color which the user wants to get filtered out
        Returns:
            a list of pygame surface objects
        """
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey=None):
        """A function which gets several sprites which are next to each other

        Args:
            rect: a pygame rect object
            image_count: how many images on the x-axis
            colorkey: the color which the user wants to get filtered out
        Returns:
            A list of pygame surface objects
        """
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
