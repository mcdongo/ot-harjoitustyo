import pygame as pg


class EventQueue:
    """A class which returns a list of pygame events
    """
    def get(self):
        """A function which returns a list of pygame events

        Returns:
            pygame event list
        """
        return pg.event.get()
