import pygame as pg
import pygame_gui

class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size, gui):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._gui = gui

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            current_time = self._clock.get_ticks()
            time_delta = current_time / 1000.0
            self._level.update(current_time)

            if self._level.get_next_level():
                return True

            self._gui.manager.update(time_delta)
            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for e in self._event_queue.get():
            if e.type == pg.KEYDOWN:
                if not self._level.player.is_moving:
                    if e.key == pg.K_LEFT:
                        self._level.start_player_movement(dx=-self._cell_size)
                    if e.key == pg.K_RIGHT:
                        self._level.start_player_movement(dx=self._cell_size)
                    if e.key == pg.K_UP:
                        self._level.start_player_movement(dy=-self._cell_size)
                    if e.key == pg.K_DOWN:
                        self._level.start_player_movement(dy=self._cell_size)
                    if e.key == pg.K_SPACE:
                        self._level.attack(self._level.player)
                if e.key == pg.K_ESCAPE:
                    return False
            
            if e.type == pg.USEREVENT:
                if e.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if e.ui_element == self._gui.hello_button:
                        print("hello world")

            elif e.type == pg.QUIT:
                return False

            self._gui.manager.process_events(e)

    def _render(self):
        self._renderer.render()

        pg.display.update()

    def next_level(self, level):
        self._level = level
