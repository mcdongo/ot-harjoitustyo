from random import randint
import pygame as pg
from player import Player
from wall import Wall
from floor import Floor
from stairs import Stairs
from slime import Slime
from ranger import Ranger


class Level:
    def __init__(self, level_map, cell_size):
        self.next_level = False
        self.cell_size = cell_size
        self.walls = pg.sprite.Group()
        self.floors = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.objects = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.level_map = level_map
        self.offset_x = 0
        self.offset_y = 0
        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for pos_y in range(height):
            for pos_x in range(width):
                cell = level_map[pos_y][pos_x]
                normalized_x = pos_x * self.cell_size
                normalized_y = pos_y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.player = Player(pos_x, pos_y, normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.level_map[pos_y][pos_x] = self.player
                elif cell == 3:
                    self.stairs = Stairs(normalized_x, normalized_y)
                elif cell == 4:
                    enemy = Slime(pos_x, pos_y, normalized_x, normalized_y)
                    self.enemies.add(enemy)
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.level_map[pos_y][pos_x] = enemy
                elif cell == 5:
                    enemy = Ranger(pos_x, pos_y, normalized_x, normalized_y)
                    self.enemies.add(enemy)
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.level_map[pos_y][pos_x] = enemy

        self.all_sprites.add(
            self.walls,
            self.floors,
            self.stairs,
            self.enemies,
            self.objects,
            self.player
        )

        self.refresh_enemy_queue()
        self.setup_camera()

    def setup_camera(self):
        while (self.player.rect.x < 300 or self.player.rect.x > 400):
            if self.player.rect.x < 300:
                self.scroll_camera(direction_x=-50, direction_y=0, player=True)
            else:
                self.scroll_camera(direction_x=50, direction_y=0, player=True)

        while (self.player.rect.y < 150 or self.player.rect.y > 250):
            if self.player.rect.y < 150:
                self.scroll_camera(direction_x=0, direction_y=50, player=True)
            else:
                self.scroll_camera(direction_x=0, direction_y=-50, player=True)

    def refresh_enemy_queue(self):
        for enemy in self.enemies:
            enemy.bfs(self.level_map, self.player)

    def update(self, current_time):
        for enemy in self.enemies:
            if enemy.should_move(current_time):
                self.start_entity_movement(enemy)
                enemy.previous_move_time = current_time
                if isinstance(enemy, Ranger):
                    arrow = enemy.shoot()
                    self.objects.add(arrow)
                    self.all_sprites.add(arrow)
            if enemy.is_moving:
                if abs(enemy.moved) == abs(enemy.move_limit):
                    self.end_animation(enemy)
                else:
                    self._move_enemy(enemy)
            enemy.update(current_time)

        for arrow in self.objects:
            if pg.sprite.spritecollide(arrow, self.walls, False):
                arrow.kill()
            if pg.sprite.collide_rect(self.player, arrow):
                arrow.kill()
                if not (self.player.shielded and abs(arrow.direction - self.player.direction) == 2):
                    self.player.current_health -= 1
                print(self.player.current_health)
            arrow.update()

        if self.player.is_moving:
            if abs(self.player.moved) == abs(self.player.move_limit):
                self.end_animation(self.player)
            else:
                self.player.update(current_time)
                self.move_player(self.player.direction_x/25, self.player.direction_y/25)
        if self.player.attack:
            self.player.update(current_time)

    def start_entity_movement(self, entity, direction_x=0, direction_y=0):
        entity.is_moving = True
        if isinstance(entity, Player):
            entity.move_limit = direction_x + direction_y
            entity.direction_x = direction_x
            entity.direction_y = direction_y
        entity.moved = 0

        if isinstance(entity, (Slime, Ranger)):
            entity.next_move()
            entity.move_limit = entity.direction_x + entity.direction_y
            entity.change_direction()
        if not self._entity_can_move(entity, entity.direction_x, entity.direction_y):
            self.end_animation(entity)
            return

        if isinstance(entity, Player):
            self.refresh_enemy_queue()
            self.move_entity_on_map(direction_x, direction_y, entity)
        else:
            self.move_entity_on_map(entity.direction_x, entity.direction_y, entity)

    def move_entity_on_map(self, direction_x, direction_y, entity):
        cur_pos = (entity.map_pos_y, entity.map_pos_x)
        next_pos = (cur_pos[0]+int(direction_y/50), cur_pos[1]+int(direction_x/50))
        self.level_map[cur_pos[0]][cur_pos[1]] = 0
        self.level_map[next_pos[0]][next_pos[1]] = entity
        entity.map_pos_y = next_pos[0]
        entity.map_pos_x = next_pos[1]

    def end_animation(self, entity):
        entity.is_moving = False
        entity.direction_x = 0
        entity.direction_y = 0
        if isinstance(entity, (Player, Ranger)):
            entity.image = entity.images[entity.direction][0]
        else:
            entity.image = entity.images[0]

    def move_player(self, direction_x=0, direction_y=0):
        if direction_x > 0:
            self.player.change_direction(1)
        if direction_x < 0:
            self.player.change_direction(3)
        if direction_y > 0:
            self.player.change_direction(2)
        if direction_y < 0:
            self.player.change_direction(0)
        if not self._entity_can_move(self.player, direction_x, direction_y):
            self.end_animation(self.player)
            return

        self.player.moved += direction_x + direction_y

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
            self.scroll_camera(direction_x, direction_y)
        else:
            self.player.rect.move_ip(direction_x, direction_y)

        if self._check_for_stairs():
            self.next_level = True

    def _entity_can_move(self, entity, direction_x=0, direction_y=0):
        entity.rect.move_ip(direction_x, direction_y)

        colliding_walls = pg.sprite.spritecollide(entity, self.walls, False)
        colliding_enemies = pg.sprite.spritecollide(entity, self.enemies, False)

        colliding_enemies = not colliding_enemies
        can_move = not colliding_walls

        entity.rect.move_ip(-direction_x, -direction_y)

        return can_move

    def _move_enemy(self, enemy):
        enemy.moved += enemy.direction_x/25 + enemy.direction_y/25
        enemy.rect.move_ip(enemy.direction_x/25, enemy.direction_y/25)

    def scroll_camera(self, direction_x, direction_y, player=False):
        self.offset_x -= direction_x
        self.offset_y -= direction_y
        for sprite in self.all_sprites:
            if not player:
                if sprite != self.player:
                    sprite.rect.move_ip(-direction_x, -direction_y)
            else:
                sprite.rect.move_ip(-direction_x, direction_y)

    def _check_for_stairs(self):
        on_stairs = pg.sprite.collide_rect(self.player, self.stairs)

        return on_stairs

    def get_next_level(self):
        return self.next_level

    def attack(self, entity):
        entity.attack = True
        direction_x, direction_y = 0, 0
        if entity.direction == 0:
            direction_y = -5
        if entity.direction == 1:
            direction_x = 5
        if entity.direction == 2:
            direction_y = 5
        if entity.direction == 3:
            direction_x = -5

        entity.rect.move_ip(direction_x, direction_y)
        for enemy in pg.sprite.spritecollide(entity, self.enemies, False):
            enemy.hurt()
        entity.rect.move_ip(-direction_x, -direction_y)

    def update_enemy_queue(self):
        for enemy in self.enemies:
            enemy.bfs(self.level_map, self.player)
