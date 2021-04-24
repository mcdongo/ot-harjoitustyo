import pygame as pg
import pygame_gui


class Gui:
    def __init__(self, res=(640, 360)):
        self.manager = pygame_gui.UIManager(res)
        '''self.hello_button = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect((350, 275), (100, 50)),
            text='Say Hello',
            manager=self.manager)'''