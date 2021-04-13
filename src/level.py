import pygame as pg
from player import Player
from wall import Wall
from floor import Floor

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.walls = pg.sprite.Group()
        self.floors = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self._initialize_sprites(level_map)

        self.offset_x = 0
        self.offset_y = 0

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])
        
        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.player = Player(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(
            self.walls,
            self.floors,
            self.player
        )

    def move_player(self, dx=0, dy=0):
        if dx > 0:
            self.player.change_direction(1)
        if dx < 0:
            self.player.change_direction(3)
        if dy > 0:
            self.player.change_direction(2)
        if dy < 0:
            self.player.change_direction(0)
        if not self._player_can_move(dx, dy):
            return

        scroll_camera = False

        '''if self.player.rect.right >= 360:
            scroll_camera = True
        if self.player.rect.left <= 120 and self.offset_x <= 0:
            scroll_camera = True
        if self.player.rect.top <= 120:
            scroll_camera = True
        if self.player.rect.bottom >= 250 and self.offset_y > 0:
            scroll_camera = True

        if scroll_camera:
            self.scroll_camera(dx, dy)
        else:'''
        self.player.rect.move_ip(dx, dy)

    def _player_can_move(self, dx=0, dy=0):
        self.player.rect.move_ip(dx, dy)

        colliding_walls = pg.sprite.spritecollide(self.player, self.walls, False)

        can_move = not colliding_walls

        self.player.rect.move_ip(-dx, -dy)

        return can_move

    def scroll_camera(self, dx, dy):
        print(self.player.rect.x, self.player.rect.y, self.offset_x, self.offset_y)
        self.offset_x -= dx
        self.offset_y -= dy
        for sprite in self.all_sprites:
            if sprite != self.player:
                sprite.rect.move_ip(-dx, -dy)