import pygame as pg
from level import Level
from gameloop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

LEVEL_MAP_1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
               [1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4, 0, 1],
               [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 3, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50

LEVEL_MAP_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Main():
    def __init__(self, LEVEL_MAP):
        self.display = pg.display.set_mode((640, 360))

        pg.display.set_caption("Crawler")
        self.load_level(LEVEL_MAP)
        self.event_queue = EventQueue()
        self.load_renderer(self.display, self.level)
        self.clock = Clock()
        self.load_gameloop(self.level, self.renderer,
                           self.event_queue, self.clock, CELL_SIZE)

        pg.init()
        self.run()

    def load_level(self, level_map):
        self.level = Level(level_map, CELL_SIZE)

    def load_renderer(self, display, level):
        self.renderer = Renderer(display, level)

    def load_gameloop(self, level, renderer, event_queue, clock, cell_size):
        self.game_loop = GameLoop(
            level, renderer, event_queue, clock, cell_size)

    def run(self):
        next_level = self.game_loop.start()

        if next_level:
            self.load_level(LEVEL_MAP_2)
            self.load_renderer(self.display, self.level)
            self.load_gameloop(self.level, self.renderer,
                               self.event_queue, self.clock, CELL_SIZE)
            self.run()


'''def main(LEVEL_MAP):
    display = pg.display.set_mode((640, 360))

    pg.display.set_caption("Crawler")
    level = Level(LEVEL_MAP, CELL_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    pg.init()
    next_level = game_loop.start()

    if next_level:
        main(LEVEL_MAP_2)'''


if __name__ == "__main__":
    GAME = Main(LEVEL_MAP_1)
