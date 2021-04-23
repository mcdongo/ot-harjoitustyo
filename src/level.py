from random import randint
import pygame as pg
from player import Player
from wall import Wall
from floor import Floor
from stairs import Stairs
from enemy import Enemy


class Level:
    def __init__(self, level_map, cell_size):
        self.next_level = False
        self.cell_size = cell_size
        self.walls = pg.sprite.Group()
        self.floors = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
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
                elif cell == 3:
                    self.stairs = Stairs(normalized_x, normalized_y)
                elif cell == 4:
                    self.enemies.add(Enemy(normalized_x, normalized_y))

        self.all_sprites.add(
            self.walls,
            self.floors,
            self.stairs,
            self.enemies,
            self.player
        )

    def update(self, current_time):
        for enemy in self.enemies:
            if enemy.should_move(current_time):
                self._move_enemy(enemy)
                enemy.previous_move_time = current_time
        self.player.update(current_time)

    def move_player(self, dx=0, dy=0):
        if dx > 0:
            self.player.change_direction(1)
        if dx < 0:
            self.player.change_direction(3)
        if dy > 0:
            self.player.change_direction(2)
        if dy < 0:
            self.player.change_direction(0)
        if not self._entity_can_move(self.player, dx, dy):
            return

        scroll_camera = False

        if self.player.rect.right >= 350:
            scroll_camera = True
        if self.player.rect.left <= 100 and self.offset_x <= 0:
            scroll_camera = True
        if self.player.rect.top <= 100:
            scroll_camera = True
        if self.player.rect.bottom >= 250 and self.offset_y > 0:
            scroll_camera = True

        if scroll_camera:
            self.scroll_camera(dx, dy)
        else:
            self.player.rect.move_ip(dx, dy)

        if self._check_for_stairs():
            self.next_level = True

    def _entity_can_move(self, entity, dx=0, dy=0):
        entity.rect.move_ip(dx, dy)

        colliding_walls = pg.sprite.spritecollide(entity, self.walls, False)

        can_move = not colliding_walls

        entity.rect.move_ip(-dx, -dy)

        return can_move

    def _move_enemy(self, enemy):
        dx, dy = 0, 0
        direction = randint(0, 3)
        if direction == 0:
            dy = -50
        if direction == 1:
            dx = 50
        if direction == 2:
            dy = 50
        if direction == 3:
            dx = -50

        if not self._entity_can_move(enemy, dx, dy):
            return

        enemy.rect.move_ip(dx, dy)

    def scroll_camera(self, dx, dy):
        self.offset_x -= dx
        self.offset_y -= dy
        for sprite in self.all_sprites:
            if sprite != self.player:
                sprite.rect.move_ip(-dx, -dy)

    def _check_for_stairs(self):
        on_stairs = pg.sprite.collide_rect(self.player, self.stairs)

        return on_stairs

    def get_next_level(self):
        return self.next_level
