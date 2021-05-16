import pygame as pg
import pygame_gui


class Gui:
    """A class which is in charge of all of the gui elements in the game

    Attributes:
        res: the resolution of the window in a tuple (x,y)
        healthbar_list: a list containing pygame_gui healthbar objects for all enemies in a level
        player_health_bar: a pygame_gui healthbar object for the player
    """
    def __init__(self, res=(640, 360)):
        """The class constructor

        Args:
            res: the resolution of the window in a tuple (x,y)
        """
        self.manager = pygame_gui.UIManager(res)
        self.panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pg.Rect((10, 60), (100, 100)),
            manager=self.manager,
            starting_layer_height=10,
            visible=False
        )
        self.item_list = pygame_gui.elements.ui_selection_list.UISelectionList(
            relative_rect=pg.Rect((10, 60), (100, 100)),
            manager=self.manager,
            parent_element=self.panel,
            item_list=["Sword", "Shield", "Potion"],
            starting_height=11,
            visible=False
        )
        #self.item_list.disable()
        self.item_list.get_single_selection()
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

    def set_inventory_visible(self):
        """A method which enables the inventory panel
        """
        if self.panel.visible:
            self.panel.hide()
            self.item_list.hide()
        else:
            self.panel.show()
            self.item_list.show()