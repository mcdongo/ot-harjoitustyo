import pygame as pg

class Clock:
    def __init__(self):
        self._clock = pg.time.Clock()

    def tick(self, fps):
        self._clock.tick(fps)

    def get_ticks(self):
        pg.time.get_ticks()