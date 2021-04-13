import pygame as pg
from level import Level
from gameloop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50

def main():
    display = pg.display.set_mode((640, 360))

    pg.display.set_caption("Crawler")
    level = Level(LEVEL_MAP, CELL_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    pg.init()
    game_loop.start()

if __name__ == "__main__":
    main()