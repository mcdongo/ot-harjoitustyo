import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1],
             [1, 0, 2, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 1]]

CELL_SIZE = 50

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP, CELL_SIZE)

    def assert_direction_facing_equal(self, sprite, direction):
        self.assertEqual(sprite.direction, direction)
        self.assertEqual(sprite.direction, direction)

    def test_player_facing_correct(self):
        
        self.assert_direction_facing_equal(self.level_1.player, 2)
        
        self.level_1.move_player(dx=-CELL_SIZE)
        self.assert_direction_facing_equal(self.level_1.player, 3)

        self.level_1.move_player(dx=CELL_SIZE)
        self.assert_direction_facing_equal(self.level_1.player, 1)