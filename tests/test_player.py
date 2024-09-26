import unittest
import sys
import os
from player import Player

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(1, 1)
        self.maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

    def test_initialization(self):
        self.assertEqual(self.player.x, 1)
        self.assertEqual(self.player.y, 1)

    def test_move_right(self):
        self.assertTrue(self.player.move("l", self.maze))
        self.assertEqual(self.player.x, 2)
        self.assertEqual(self.player.y, 1)

    def test_move_down(self):
        self.assertTrue(self.player.move("j", self.maze))
        self.assertEqual(self.player.x, 1)
        self.assertEqual(self.player.y, 2)

    def test_move_into_wall(self):
        self.assertFalse(self.player.move("k", self.maze))
        self.assertEqual(self.player.x, 1)
        self.assertEqual(self.player.y, 1)

    def test_move_out_of_bounds(self):
        self.player.x = 3
        self.player.y = 3
        self.assertFalse(self.player.move("l", self.maze))
        self.assertEqual(self.player.x, 3)
        self.assertEqual(self.player.y, 3)

    def test_invalid_direction(self):
        original_x, original_y = self.player.x, self.player.y
        self.assertFalse(self.player.move("x", self.maze))
        self.assertEqual(self.player.x, original_x)
        self.assertEqual(self.player.y, original_y)

    def test_move_sequence(self):
        moves = ["l", "j", "l", "k"]
        for move in moves:
            self.player.move(move, self.maze)
        self.assertEqual(self.player.x, 3)
        self.assertEqual(self.player.y, 1)


if __name__ == "__main__":
    unittest.main()
