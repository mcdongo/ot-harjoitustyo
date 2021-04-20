import unittest
from level import Level

LEVEL_MAP = [[1, 1, 1, 1, 1],
             [1, 0, 2, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 3, 4, 0, 1],
             [1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP, CELL_SIZE)

    def assert_coordinates_equal(self, x, y):
        self.assertEqual(self.level_1.offset_x, x)
        self.assertEqual(self.level_1.offset_y, y)

    def test_can_move_in_floor(self):

        self.assert_coordinates_equal(0, 0)

        self.level_1.move_player(dy=CELL_SIZE)
        self.assert_coordinates_equal(0, -1 * CELL_SIZE)

        self.level_1.move_player(dx=-CELL_SIZE)
        self.assert_coordinates_equal(1 * CELL_SIZE, -1 * CELL_SIZE)
