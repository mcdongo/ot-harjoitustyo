import pygame as pg


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

    def start(self):
        while True:
            if self._handle_events() == False:
                break
            
            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for e in self._event_queue.get():
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self._level.move_player(dx=-self._cell_size)
                if e.key == pg.K_RIGHT:
                    self._level.move_player(dx=self._cell_size)
                if e.key == pg.K_UP:
                    self._level.move_player(dy=-self._cell_size)
                if e.key == pg.K_DOWN:
                    self._level.move_player(dy=self._cell_size)

            elif e.type == pg.QUIT:
                return False

    def _render(self):
        self._renderer.render()

        pg.display.update()