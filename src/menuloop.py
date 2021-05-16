import pygame as pg

class MenuLoop:
    """Class for handling events in the menu and rendering it

    Attributes:
        renderer: A Renderer object
        event_queue: An EventQueue object
        clock: A Pygame.clock object
    """
    def __init__(self, renderer, event_queue, clock):
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        """The main loop, in charge of handling events
        
        Returns:
            -1 if user wants to quit
            0 if user wants to start a new game
            1 if user wants to continue an earlier save
        """
        while True:
            events = self._handle_events()
            if events in (-1, 0, 1):
                return events

            self._render()
            self._clock.tick(60)

    def _handle_events(self):
        """A method handling user inputted events eg. button presses
        
        Returns:
            -1 if user wants to quit the program
            0 if user wants to start a new game
            1 if user wants to continue an earlier save
        """
        for event in self._event_queue.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return -1
                if event.key == pg.K_DOWN:
                    self._renderer.menu_list(1)
                if event.key == pg.K_UP:
                    self._renderer.menu_list(-1)
                if event.key == pg.K_SPACE:
                    return self._renderer.menu_number
            elif event.type == pg.QUIT:
                return -1

    def _render(self):
        """A method which renders the menu on the screen
        """
        self._renderer.render_menu()
        pg.display.update()

