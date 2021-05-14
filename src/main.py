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

CELL_SIZE = 50
DB_CONNECTION = Connection("state.db")

class Main:
    def __init__(self):
        self.display = pg.display.set_mode((640, 360))
        pg.display.set_caption("Crawler")
        pg.init()
        self.level_list = None
        self.gui = Gui((640, 360))
        self.level_id = 0
        self.level = None
        self.event_queue = EventQueue()
        self.clock = Clock()
        self.renderer = Renderer(self.display, self.level, self.gui)
        self.game_loop = None
        self.menu_loop = MenuLoop(self.renderer, self.event_queue, self.clock)

        self.start_menu()

    def load_level_list(self):
        self.level_list = DB_CONNECTION.get_map_data()

    def build_essentials(self):
        self.load_level_list()
        self.load_level()
        self.gui = Gui((640, 360))
        self.add_healthbars()
        self.renderer = Renderer(self.display, self.level, self.gui)
        self.game_loop = GameLoop(self.level, self.renderer,
                                  self.event_queue, self.clock, CELL_SIZE, self.gui)


    def load_level(self):
        self.level = Level(self.level_list[self.level_id], CELL_SIZE)
    
    def add_healthbars(self):
        for enemy in self.level.enemies:
            self.gui.set_health_bar(enemy)
        self.gui.set_player_health_bar(self.level.player)

    def load_level_id(self):
        data = DB_CONNECTION.get_player_data()
        if data:
            self.level_id = data[2]

    def load_player_data(self):
        data = DB_CONNECTION.get_player_data()
        if data:
            self.level.player.current_health = data[0]
            self.level.player.inventory = data[1]
        self.gui.set_player_health_bar(self.level.player)

    def store_player_data(self):
        DB_CONNECTION.store_player_data(self.level.player, self.level_id)

    def start_menu(self):
        state = self.menu_loop.start()
        if state != -1:
            if state == 0:
                DB_CONNECTION.reset_player_data()
                self.level_id = 0
                self.build_essentials()
            if state == 1 and not self.level:
                self.load_level_id()
                self.build_essentials()
                self.load_player_data()
            self.run()

    def run(self):
        state = self.game_loop.start()
        if state == 1:
            self.start_menu()
        if state == 3:
            self.level_id += 1
            self.store_player_data()
            self.build_essentials()
            self.load_player_data()
            self.run()
        if state == 4:
            self.__init__()

"""class Main():
    def __init__(self, LEVEL_MAP):
        self.display = pg.display.set_mode((640, 360))
        pg.display.set_caption("Crawler")
        pg.init()
        self.gui = Gui((640, 360))
        self.level_id = 0

        self.load_level_list_from_db()
        self.event_queue = EventQueue()
        self.clock = Clock()
        self.load_level()
        self.gui.set_player_health_bar(self.level.player)
        self.load_renderer(self.display, self.level, self.gui)
        self.menu_loop = MenuLoop(self.renderer, self.event_queue, self.clock)
        self.load_gameloop(self.level, self.renderer,
                           self.event_queue, self.clock, CELL_SIZE, self.gui)

        self.start_menu()

    def load_level_list_from_db(self):
        self.level_list = DB_CONNECTION.get_map_data()

    def save_player_data(self):
        DB_CONNECTION.store_player_data(self.level.player, self.level_id)

    def get_player_data(self):
        return DB_CONNECTION.get_player_data()

    def update_player_data(self, data):
        if data:
            self.level.player.current_health = data[0]
            self.level.player.inventory = data[1]

    def load_level(self):
        player_data = self.get_player_data()
        print(player_data)
        if player_data:
            self.level_id = player_data[2]
        self.gui = Gui((640, 360))
        self.level = Level(self.level_list[self.level_id], CELL_SIZE)
        self.load_renderer(self.display, self.level, self.gui)
        self.load_gameloop(self.level, self.renderer,
                           self.event_queue, self.clock, CELL_SIZE, self.gui)
        self.update_player_data(player_data)
        self.gui.set_player_health_bar(self.level.player)
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
            if state == 0:
                DB_CONNECTION.reset_player_data()
            if state == 1:
                player_data = self.get_player_data()
                self.update_player_data(player_data)
                self.load_level()

            self.run()

    def run(self):
        state = self.game_loop.start()
        if state == 1:
            self.start_menu()
        if state == 3:
            self.level_id += 1
            self.load_level_list_from_db()
            self.save_player_data()
            self.load_level()
            self.run()
        if state == 4:
            self.__init__(None)
"""


if __name__ == "__main__":
    GAME = Main()
