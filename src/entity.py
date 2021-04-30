import pygame as pg

class Entity(pg.sprite.Sprite):
    def __init__(self, map_pos_x, map_pos_y):
        super().__init__()
        self.frame = 0
        self.last_updated = 0
        self.is_moving = False
        self.attack = False
        self.map_pos_x = map_pos_x
        self.map_pos_y = map_pos_y
        self.health = 0
        self.moved = 0
        self.direction_x = 0
        self.direction_y = 0

    def walking_animation(self):
        if self.frame == 3:
            self.frame = 0
        else:
            self.frame += 1

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

    def change_direction(self):
        if self.direction_x < 0:
            self.direction = 3
        if self.direction_x > 0:
            self.direction = 1
        if self.direction_y < 0:
            self.direction = 0
        if self.direction_y > 0:
            self.direction = 2