import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 5, 0, 0, 2, 1],
             [1, 0, 0, 3, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP, CELL_SIZE)

    def assert_enemy_facing_correctly(self, enemy, direction):
        self.assertEqual(enemy.direction, direction)

    def test_enemy_facing_correctly(self):
        for enemy in self.level_1.enemies:
            self.assert_enemy_facing_correctly(enemy, 2)

        for enemy in self.level_1.enemies:
            enemy.direction_x = -50
            enemy.change_direction()
            self.assert_enemy_facing_correctly(enemy, 3)

        for enemy in self.level_1.enemies:
            enemy.direction_x = 50
            enemy.change_direction()
            self.assert_enemy_facing_correctly(enemy, 1)

        for enemy in self.level_1.enemies:
            enemy.direction_x = 0
            enemy.direction_y = -50
            enemy.change_direction()
            self.assert_enemy_facing_correctly(enemy, 0)