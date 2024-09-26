import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
from renderer import render_maze
from player import Player

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestRenderer(unittest.TestCase):

    def setUp(self):
        self.maze = [
            [1, 1, 1, 1, 1],
            [1, 2, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 3, 1],
            [1, 1, 1, 1, 1],
        ]
        self.player = Player(1, 1)

    @patch("sys.stdout", new_callable=StringIO)
    def test_render_maze(self, mock_stdout):
        render_maze(self.maze, self.player)
        output = mock_stdout.getvalue()

        self.assertIn("█████", output)  # Wall
        self.assertIn("☺", output)  # Player
        self.assertIn("⌂", output)  # Start
        self.assertIn("◎", output)  # End

        # Check legend
        self.assertIn("☺: Player", output)
        self.assertIn("⌂: Start", output)
        self.assertIn("◎: End", output)
        self.assertIn("█: Wall", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_player_movement(self, mock_stdout):
        self.player.x = 2
        self.player.y = 1
        render_maze(self.maze, self.player)
        output = mock_stdout.getvalue()
        self.assertIn("█☺", output)  # Player next to wall

    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_path(self, mock_stdout):
        self.player.x = 3
        self.player.y = 1
        render_maze(self.maze, self.player)
        output = mock_stdout.getvalue()
        self.assertIn(" ", output)  # Empty path


if __name__ == "__main__":
    unittest.main()
