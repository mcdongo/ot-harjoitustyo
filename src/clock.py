import pygame as pg


class Clock:
    """Class for handling time inside the game

    Attributes:
        _clock: a pygame clock object
    """
    def __init__(self):
        """Class constructor, creates a new clock
        """
        self._clock = pg.time.Clock()

    def tick(self, fps):
        """This method allows time to pass

        Args:
            fps: Frames per second (How many time the game is updated in a second)
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """This function tells how much time has passed since the game has been booted

        Returns:
            ticks, integer. How many times the game has been updated since boot
        """
        return pg.time.get_ticks()
