import pygame as pg


class Renderer:
    def __init__(self, display, level, gui):
        self._display = display
        self._level = level
        self._gui = gui

    def render(self):
        self._display.fill((0, 0, 0))
        self._level.all_sprites.draw(self._display)
        self._gui.manager.draw_ui(self._display)

        pg.display.update()
