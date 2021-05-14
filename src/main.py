import pygame as pg
import pygame_gui
from level import Level
from gameloop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock
from gui import Gui
from db_connection import Connection
from menuloop import MenuLoop

LEVEL_MAPS = [
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 5, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4, 0, 1],
     [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 4, 1, 0, 0, 3, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 2, 0, 0, 0, 0, 1, 5, 0, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
     [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 4, 1],
     [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
     [1, 0, 0, 0, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 3, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
     ]

CELL_SIZE = 50


class Main():
    def __init__(self, LEVEL_MAP):
        self.display = pg.display.set_mode((640, 360))
        pg.display.set_caption("Crawler")
        pg.init()
        self.gui = Gui((640, 360))
        self.db_connection = Connection("state.db")
        self.level_id = 2

        self.load_level_from_db()
        #self.load_level(LEVEL_MAP)
        self.gui.set_player_health_bar(self.level.player)
        self.event_queue = EventQueue()
        self.load_renderer(self.display, self.level, self.gui)
        self.clock = Clock()
        self.menu_loop = MenuLoop(self.renderer, self.event_queue, self.clock)
        self.load_gameloop(self.level, self.renderer,
                           self.event_queue, self.clock, CELL_SIZE, self.gui)

        self.start_menu()

    def load_level_from_db(self):
        temp = self.db_connection.get_data()
        if temp:
            self.level = temp
        else:
            self.load_level(LEVEL_MAPS[self.level_id])

    def save_level_to_db(self):
        self.db_connection.store_data(self.level)


    def load_level(self, level_map):
        self.level = Level(level_map, CELL_SIZE)
        for enemy in self.level.enemies:
            self.gui.set_health_bar(enemy)

    def load_renderer(self, display, level, gui):
        self.renderer = Renderer(display, level, gui)

    def load_gameloop(self, level, renderer, event_queue, clock, cell_size, gui):
        self.game_loop = GameLoop(
            level, renderer, event_queue, clock, cell_size, gui)

    def start_menu(self):
        state = self.menu_loop.start()
        if state != -1:
            self.run()

    def run(self):
        state = self.game_loop.start()
        if state == 1:
            self.start_menu()
        if state == 3:
            self.level_id += 1
            self.gui = Gui((640, 360))
            self.load_level(LEVEL_MAPS[self.level_id])
            self.gui.set_player_health_bar(self.level.player)
            self.load_renderer(self.display, self.level, self.gui)
            self.load_gameloop(self.level, self.renderer,
                               self.event_queue, self.clock, CELL_SIZE, self.gui)
            self.run()



if __name__ == "__main__":
    GAME = Main(None)
