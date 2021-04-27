import os
import pygame as pg

DIRNAME = os.path.dirname(__file__)


class Enemy(pg.sprite.Sprite):
    def __init__(self, map_pos_x, map_pos_y, pos_x, pos_y):
        super().__init__()

        self.previous_move_time = 0
        self.move_queue = []

        '''self.image = pg.image.load(
            os.path.join(dirname, "assets", "enemy.png")
        )'''

        self.image = pg.Surface([50, 50])
        self.image.fill([50, 50, 50])

        self.map_pos_x = map_pos_x
        self.map_pos_y = map_pos_y

        self.is_moving = False
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.health = 5
        self.damaged = False
        self.time_red = 0

    def should_move(self, current_time):
        if current_time:
            return current_time - self.previous_move_time >= 1200
        return False

    def hurt(self):
        self.health -= 1
        self.image.fill([255, 0, 0])
        self.damaged = True
        self.time_red = 10
        if self.health == 0:
            self.kill()

    def update(self):
        if self.damaged:
            if self.time_red > 0:
                self.time_red -= 1
            else:
                self.image.fill([50, 50, 50])
                self.damaged = False

    def bfs(self, level_map, player):
        visited = [[False]*len(level_map[0]) for i in range(len(level_map))]

        goal = (player.map_pos_y, player.map_pos_x)

        queue = []
        cur_pos = (self.map_pos_y, self.map_pos_x)
        #print("{0}, player pos: {1}".format(cur_pos, goal))
        queue.append([cur_pos])
        visited[cur_pos[0]][cur_pos[1]] = True

        while queue:
            path = queue.pop(0)
            cur_pos = path[-1]
            #print(cur_pos)

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
                #print("Shortest:")
                #print(new_path)
                new_path.pop(0)
                self.move_queue = new_path
                break