import pygame as pg
import pygame_gui

class GameLoop:
    """Class which is in charge of updating the game and handling events
    
    Attributes:
        level: a Level object
        renderer: a Renderer object
        event_queue: an EventQueue object
        clock: a Clock object
        cell_size: value of how many pixels wide and tall each cell is in the game
        gui: a gui object
        shift: boolean value telling if left shift is pressed at the moment
    """
    def __init__(self, level, renderer, event_queue, clock, cell_size, gui):
        """Constructs the class.

        Args:
            level: a Level object
            renderer: a Renderer object
            event_queue: an EventQueue object
            clock: a Clock object
            cell_size: value of how many pixels wide and tall each cell is in the game
            gui: a gui object
            menu: boolean, True if game is in menu
        """
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self._gui = gui
        self.shift = False
        self.menu = True

    def start(self):
        """The main game loop. Updates everything
        """
        self.start_menu()
    
    def start_game(self):
        """Actual in game loop function
        """
        while True:
            if self._handle_events() is False:
                break

            current_time = self._clock.get_ticks()
            time_delta = current_time / 1000.0
            self._level.update(current_time)

            if self._level.get_next_level():
                return True

            self._gui.manager.update(time_delta)
            self._render()

            self._clock.tick(60)

    def start_menu(self):
        """A function for handling events in the primary menu
        """
        while True:
            if self._handle_menu_events() is False:
                break

            self._render()
            self._clock.tick(60)
                
    def _handle_menu_events(self):
        for event in self._event_queue.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return False
                if event.key == pg.K_DOWN:
                    self._renderer.menu_list(1)
                if event.key == pg.K_UP:
                    self._renderer.menu_list(-1)
                if event.key == pg.K_SPACE:
                    self.menu = False
                    self.start_game()

    def _handle_events(self):
        """A method for handling user inputted events eg. button presses
        """

        for event in self._event_queue.get():
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_LSHIFT:
                    self.shift = True
                if event.key == pg.K_LCTRL:
                    self._level.player.apply_shield()

                if not self._level.player.is_moving and not self._level.player.shielded:
                    if event.key == pg.K_LEFT:
                        if not self.shift:
                            self._level.start_entity_movement(self._level.player, direction_x=-self._cell_size)
                        else:
                            self.shift_function(direction_x=-self._cell_size)

                    if event.key == pg.K_RIGHT:
                        if not self.shift:
                            self._level.start_entity_movement(self._level.player, direction_x=self._cell_size)
                        else:
                            self.shift_function(direction_x=self._cell_size)

                    if event.key == pg.K_UP:
                        if not self.shift:
                            self._level.start_entity_movement(self._level.player, direction_y=-self._cell_size)
                        else:
                            self.shift_function(direction_y=-self._cell_size)

                    if event.key == pg.K_DOWN:
                        if not self.shift:
                            self._level.start_entity_movement(self._level.player, direction_y=self._cell_size)
                        else:
                            self.shift_function(direction_y=self._cell_size)

                    if event.key == pg.K_e:
                        self._gui.set_inventory_visible()

                    if event.key == pg.K_SPACE:
                        if not self._level.player.shielded:
                            self._level.attack(self._level.player)
                if event.key == pg.K_ESCAPE:
                    self.menu = True
                    return False

            if event.type == pg.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self._gui.hello_button:
                        print("hello world")

            elif event.type == pg.QUIT:
                return False

            self._gui.manager.process_events(event)
            self._gui.update()

            if event.type == pg.KEYUP:
                if event.key == pg.K_LSHIFT:
                    self.shift = False
                if event.key == pg.K_LCTRL:
                    self._level.player.apply_shield()

    def _render(self):
        """A method which renders everything on the screen
        """
        if not self.menu:
            self._renderer.render()
        else:
            self._renderer.render_menu()

        pg.display.update()

    def next_level(self, level):
        """A function which loads the next level into memory
        """
        self._level = level

    def shift_function(self, direction_x=0, direction_y=0):
        """This method is used to change the direction the player is facing if the left shift key is pressed
        alongside with an arrow key
        """
        if self.shift:
            if direction_y < 0:
                self._level.player.change_direction(0)
            if direction_x > 0:
                self._level.player.change_direction(1)
            if direction_y > 0:
                self._level.player.change_direction(2)
            if direction_x < 0:
                self._level.player.change_direction(3)
