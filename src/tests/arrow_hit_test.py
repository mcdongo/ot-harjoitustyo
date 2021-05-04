import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1, 1],
             [1, 2, 0, 5, 1],
             [1, 0, 0, 3, 1],
             [1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestArrow(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP, CELL_SIZE)
        for enemy in self.level_1.enemies:
            enemy.direction = 3

    def assert_player_hp_correct_after_arrow_hit(self):
        self.assertEqual(self.level_1.player.current_health, 9)

    def assert_arrow_facing_correctly_when_spawning(self, arrow, direction):
        self.assertEqual(arrow.direction, direction)
    
    def assert_player_blocks_arrow_when_shielded(self):
        self.assertEqual(self.level_1.player.current_health, 9)

    def test_arrow(self):
        for enemy in self.level_1.enemies:
            enemy.direction = 0
            arrow = enemy.shoot()
            
            self.assert_arrow_facing_correctly_when_spawning(arrow, 0)
            enemy.direction = 1
            arrow = enemy.shoot()
            self.assert_arrow_facing_correctly_when_spawning(arrow, 1)
            
            enemy.direction = 2
            arrow = enemy.shoot()
            self.assert_arrow_facing_correctly_when_spawning(arrow, 2)

            enemy.direction = 3
            arrow = enemy.shoot()
            self.assert_arrow_facing_correctly_when_spawning(arrow, 3)


            arrow = enemy.shoot()
            self.level_1.objects.add(arrow)
        for i in range(15):
            self.level_1.update_objects()
        self.assert_player_hp_correct_after_arrow_hit()

        self.level_1.player.shielded = True
        self.level_1.player.direction = 1

        for enemy in self.level_1.enemies:
            arrow = enemy.shoot()
            self.level_1.objects.add(arrow)
        for i in range(15):
            self.level_1.update_objects()
        self.assert_player_blocks_arrow_when_shielded()

