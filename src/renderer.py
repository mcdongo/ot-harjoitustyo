import os
import pygame as pg

DIRNAME = os.path.dirname(__file__)

class Renderer:
    def __init__(self, display, level, gui):
        self._display = display
        self._level = level
        self._gui = gui
        self.dark = pg.image.load(os.path.join(DIRNAME, "assets", "dark.png"))

    def render(self):
        self._display.fill((0, 0, 0))
        self._level.all_sprites.draw(self._display)
        self._gui.manager.draw_ui(self._display)
        #self._display.blit(self.dark, (0,0))

        pg.display.update()
