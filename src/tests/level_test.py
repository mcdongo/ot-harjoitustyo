import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1],
             [1, 0, 2, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 1]]

CELL_SIZE = 50

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP, CELL_SIZE)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move_in_floor(self):
        player = self.level_1.player
        
        self.assert_coordinates_equal(player, 2 * CELL_SIZE, 1 * CELL_SIZE)
        
        self.level_1.move_player(dy=CELL_SIZE)
        self.assert_coordinates_equal(player, 2 * CELL_SIZE, 2 * CELL_SIZE)

        self.level_1.move_player(dx=-CELL_SIZE)
        self.assert_coordinates_equal(player, 1 * CELL_SIZE, 2 * CELL_SIZE)