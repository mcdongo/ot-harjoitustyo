import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1, 1],
             [1, 2, 0, 5, 1],
             [1, 0, 0, 3, 1],
             [1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP, CELL_SIZE)

    def assert_enemy_bfs_route_correct(self):
        for enemy in self.level_1.enemies:
            self.assertEqual(enemy.move_queue, [(2, 3), (2, 2), (2, 1)])

    def assert_next_move_correct(self, enemy, direction_x=0, direction_y=0):
        if direction_x != 0:
            self.assertEqual(enemy.direction_x, direction_x)
        if direction_y != 0:
            self.assertEqual(enemy.direction_y, direction_y)


    def test_enemy_bfs_route_correct(self):
        self.assert_enemy_bfs_route_correct()

        for enemy in self.level_1.enemies:
            enemy.next_move()
            self.assert_next_move_correct(enemy, direction_y=50)

            enemy.next_move()
            self.assert_next_move_correct(enemy, direction_x=-50)

            enemy.next_move()
            self.assert_next_move_correct(enemy, direction_x=-50)

