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
        for y in range(len(self.level_1.level_map)):
            for x in range(len(self.level_1.level_map[0])):
                if self.level_1.level_map[y][x] == self.level_1.player:
                    final_y = y
                    final_x = x
        
        self.assertEqual(final_y, self.level_1.player.map_pos_y)
        self.assertEqual(final_x, self.level_1.player.map_pos_x)

    def test_can_move_in_floor(self):

        self.assert_coordinates_equal(0, 0)

        self.level_1.move_player(direction_y=CELL_SIZE)
        self.assert_coordinates_equal(0, -1 * CELL_SIZE)

        self.level_1.move_player(direction_x=-CELL_SIZE)
        self.assert_coordinates_equal(1 * CELL_SIZE, -1 * CELL_SIZE)
