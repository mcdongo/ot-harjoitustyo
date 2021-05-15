import pygame as pg

class Entity(pg.sprite.Sprite):
    """An entity class. It is inherited by all long-time characters in a level

    Attributes:
        map_pos_x: x position in the level
        map_pos_y: y position in the level
        frame: animation related. Declares which frame of a certain animation is shown (usually 0-3)
        is_moving: a boolean value True if the entity is moving, False otherwise
        attack: a boolean value telling if the entity is attacking at the moment
        health_capacity: Integer; the maximum health of said entity
        current_health: Integer; current health of said entity
        moved: animation related; keeps track of how much said entity has moved during an animation
        direction_x: Integer; current speed on the x-axis
        direction_y Integer; current speed on the y-axis
    """
    def __init__(self, map_pos_x, map_pos_y):
        """A constructor of the class. Creates a new entity.

        Args:
            map_pos_x: x position in the level
            map_pos_y: y position in the level
        """
        super().__init__()
        self.frame = 0
        self.last_updated = 0
        self.is_moving = False
        self.attack = False
        self.map_pos_x = map_pos_x
        self.map_pos_y = map_pos_y
        self.health_capacity = 10
        self.current_health = self.health_capacity
        self.moved = 0
        self.direction_x = 0
        self.direction_y = 0

    def walking_animation(self):
        """A method which updates which image is showed as this entity.
        """
        if self.frame == 3:
            self.frame = 0
        else:
            self.frame += 1

    def bfs(self, level_map, player):
        """A method which updates the movement queue for this entity using
        a breadth-first search.

        Args:
            level_map: a two dimensional list containing the current info of the level
            player: the player object which is in use of the current level
        """
        visited = [[False]*len(level_map[0]) for i in range(len(level_map))]

        goal = (player.map_pos_y, player.map_pos_x)

        queue = []
        cur_pos = (self.map_pos_y, self.map_pos_x)
        queue.append([cur_pos])
        visited[cur_pos[0]][cur_pos[1]] = True

        while queue:
            path = queue.pop(0)
            cur_pos = path[-1]

            """for test_pos in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if level_map[cur_pos[0]+test_pos[0]][cur_pos[1]+test_pos[1]] != 1:
                    if not visited[cur_pos[0]+test_pos[0]][cur_pos[1]+test_pos[1]]:
                        new_path = list(path)
                        new_path.append((cur_pos[0]+test_pos[0], cur_pos[1]+test_pos[1]))
                        queue.append(new_path)
                        visited[cur_pos[0]+test_pos[0]][cur_pos[1]+test_pos[1]] = True"""

            if level_map[cur_pos[0]-1][cur_pos[1]] != 1:
                if not visited[cur_pos[0]-1][cur_pos[1]]:
                    new_path = list(path)
                    new_path.append((cur_pos[0]-1, cur_pos[1]))
                    queue.append(new_path)
                    visited[cur_pos[0]-1][cur_pos[1]] = True
            
            if level_map[cur_pos[0]+1][cur_pos[1]] != 1:
                if not visited[cur_pos[0]+1][cur_pos[1]]:
                    new_path = list(path)
                    new_path.append((cur_pos[0]+1, cur_pos[1]))
                    queue.append(new_path)
                    visited[cur_pos[0]+1][cur_pos[1]] = True

            if level_map[cur_pos[0]][cur_pos[1]-1] != 1:
                if not visited[cur_pos[0]][cur_pos[1]-1]:
                    new_path = list(path)
                    new_path.append((cur_pos[0], cur_pos[1]-1))
                    queue.append(new_path)
                    visited[cur_pos[0]][cur_pos[1]-1] = True

            if level_map[cur_pos[0]][cur_pos[1]+1] != 1:
                if not visited[cur_pos[0]][cur_pos[1]+1]:
                    new_path = list(path)
                    new_path.append((cur_pos[0], cur_pos[1]+1))
                    queue.append(new_path)
                    visited[cur_pos[0]][cur_pos[1]+1] = True

            if cur_pos == goal:
                new_path.pop(0)
                #new_path.pop()
                self.move_queue = new_path
                break

    def change_direction(self):
        """A method which checks which way this entity should be facing
        """
        if self.direction_x < 0:
            self.direction = 3
        if self.direction_x > 0:
            self.direction = 1
        if self.direction_y < 0:
            self.direction = 0
        if self.direction_y > 0:
            self.direction = 2

    def hurt(self):
        """A function which decreases entitys hp

        Returns:
            True if entity's hp has fallen to 0
            False otherwise
        """
        self.current_health -= 1
        if self.current_health == 0:
            return True
        return False