import pygame as pg


class EventQueue:
    def get(self):
        return pg.event.get()
