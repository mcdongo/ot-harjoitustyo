import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1, 1],
             [1, 2, 0, 4, 1],
             [1, 0, 0, 3, 1],
             [1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP, CELL_SIZE)

    def assert_enemy_bfs_route_correct(self):
        for enemy in self.level_1.enemies:
            self.assertEqual(enemy.move_queue, [(2, 3), (2, 2), (2, 1)])

    def test_enemy_bfs_route_correct(self):
        self.assert_enemy_bfs_route_correct()

