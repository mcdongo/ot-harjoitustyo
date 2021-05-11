import os
import pygame as pg

DIRNAME = os.path.dirname(__file__)

class Renderer:
    def __init__(self, display, level, gui):
        self._display = display
        self._level = level
        self._gui = gui
        self.dark = pg.image.load(os.path.join(DIRNAME, "assets", "dark.png"))
        self.menu_image = pg.image.load(os.path.join(DIRNAME, "assets", "menu.png"))
        self.new_game_button = pg.image.load(os.path.join(DIRNAME, "assets", "new_game.png"))
        self.continue_button = pg.image.load(os.path.join(DIRNAME, "assets", "continue.png"))
        self.menu_number = 0

    def render(self):
        self._display.fill((0, 0, 0))
        self._level.all_sprites.draw(self._display)
        self._gui.manager.draw_ui(self._display)
        #self._display.blit(self.dark, (0,0))

        pg.display.update()

    def render_menu(self):
        self._display.blit(self.menu_image, (0, 0))
        pg.draw.rect(self._display, (255, 255, 255), (193, 115+(self.menu_number*74), 250, 50))
        self._display.blit(self.new_game_button, (163, 95))
        self._display.blit(self.continue_button, (159, 169))

    def menu_list(self, val):
        if val > 0:
            if self.menu_number == 1:
                self.menu_number = 0
            else:
                self.menu_number += 1
        
        if val < 0:
            if self.menu_number == 0:
                self.menu_number = 1
            else:
                self.menu_number -= 1
