import pygame as pg
import pygame_gui


class Gui:
    """A class which is in charge of all of the gui elements in the game

    Attributes:
        res: the resolution of the window in a tuple (x,y)
    """
    def __init__(self, res=(640, 360)):
        """The class constructor

        Args:
            res: the resolution of the window in a tuple (x,y)
        """
        self.manager = pygame_gui.UIManager(res)
        self.hello_button = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect((350, 275), (100, 50)),
            text='Say Hello',
            manager=self.manager)
        self.healthbar_list = []
        self.player_health_bar = None

    def set_health_bar(self, sprite):
        """Creates a health bar for a sprite

        Args:
            sprite: the sprite in question which gets a health bar
        """
        self.healthbar_list.append(pygame_gui.elements.UIWorldSpaceHealthBar(
            relative_rect=pg.Rect((10, 10), (50, 10)),
            sprite_to_monitor=sprite,
            manager=self.manager
            ))

    def update(self):
        """Method which checks if a healthbar object should be killed
        """
        for healthbar in self.healthbar_list:
            if healthbar.current_health == 0:
                healthbar.kill()

    def set_player_health_bar(self, player):
        """Creates a health bar for the player

        Args:
            player: a player object
        """
        self.player_health_bar = pygame_gui.elements.UIScreenSpaceHealthBar(
            relative_rect=pg.Rect((10, 10), (100, 50)),
            sprite_to_monitor=player,
            manager=self.manager
        )
