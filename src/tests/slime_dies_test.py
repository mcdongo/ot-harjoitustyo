import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 4, 0, 0, 2, 1],
             [1, 0, 0, 3, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP, CELL_SIZE)

    def assert_enemy_is_dead(self, enemy):
        self.assertEqual(enemy.current_health, 0)
    
    def assert_enemy_takes_damage(self, enemy, hitpoints):
        self.assertEqual(enemy.current_health, hitpoints)

    def assert_should_move_working_properly(self, enemy, time, value):
        self.assertEqual(enemy.should_move(time), value)

    def test_enemy_takes_damage_and_dies(self):
        for enemy in self.level_1.enemies:
            enemy.current_health = 5
            self.assert_should_move_working_properly(enemy, None, False)
            self.assert_should_move_working_properly(enemy, 200, False)
            self.assert_should_move_working_properly(enemy, 1800, True)

            self.assert_enemy_takes_damage(enemy, 5)
            enemy.hurt()
            self.assert_enemy_takes_damage(enemy, 4)
            enemy.hurt()
            self.assert_enemy_takes_damage(enemy, 3)
            enemy.hurt()
            self.assert_enemy_takes_damage(enemy, 2)
            enemy.hurt()
            self.assert_enemy_takes_damage(enemy, 1)
            enemy.hurt()
            self.assert_enemy_is_dead(enemy)