import os
import pygame as pg

DIRNAME = os.path.dirname(__file__)

class Spritesheet():
    def __init__(self, filename):
        try:
            self.sheet = pg.image.load(os.path.join(DIRNAME, "assets", filename))
        except Exception as message:
            print("Unable to load spritesheet image: {0}".format(filename))
            raise SystemExit(message)

    def image_at(self, rectangle, colorkey=None):
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size)
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image

    def images_at(self, rects, colorkey=None):
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey=None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
