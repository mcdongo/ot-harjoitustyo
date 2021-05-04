import pygame as pg
import pygame_gui


class Gui:
    def __init__(self, res=(640, 360)):
        self.manager = pygame_gui.UIManager(res)
        self.hello_button = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect((350, 275), (100, 50)),
            text='Say Hello',
            manager=self.manager)
        self.healthbar_list = []
        self.player_health_bar = None

    def set_health_bar(self, sprite):
        self.healthbar_list.append(pygame_gui.elements.UIWorldSpaceHealthBar(
            relative_rect=pg.Rect((10, 10), (50, 10)),
            sprite_to_monitor=sprite,
            manager=self.manager
            ))

    def update(self):
        for healthbar in self.healthbar_list:
            if healthbar.current_health == 0:
                healthbar.kill()

    def set_player_health_bar(self, player):
        self.player_health_bar = pygame_gui.elements.UIScreenSpaceHealthBar(
            relative_rect=pg.Rect((10, 10), (100, 50)),
            sprite_to_monitor=player,
            manager=self.manager
        )
