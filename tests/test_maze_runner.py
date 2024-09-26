import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
from maze_runner import MazeRunner

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestMazeRunner(unittest.TestCase):
    def setUp(self):
        self.game = MazeRunner()  # Remove width and height parameters

    def test_initialization(self):
        self.assertEqual(self.game.width, 10)
        self.assertEqual(self.game.height, 10)
        self.assertIsNotNone(self.game.maze)
        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 1)
        self.assertTrue(self.game.running)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.moves, 0)

    @patch("maze_runner.getch")
    @patch("maze_runner.render_maze")
    def test_play_quit(self, mock_render, mock_getch):
        mock_getch.return_value = "q"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.game.play()
        self.assertFalse(self.game.running)
        self.assertIn("Thanks for playing MazeRunner!", fake_out.getvalue())

    @patch("maze_runner.getch")
    @patch("maze_runner.render_maze")
    def test_play_move(self, mock_render, mock_getch):
        mock_getch.side_effect = ["l", "q"]
        self.game.play()
        self.assertEqual(self.game.moves, 1)

    def test_check_win_condition(self):
        self.game.player.x = self.game.width - 2
        self.game.player.y = self.game.height - 2
        self.assertTrue(self.game._check_win_condition())

    @patch("maze_runner.render_maze")
    def test_end_game(self, mock_render):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.game._end_game()
        self.assertIn("Congratulations!", fake_out.getvalue())
        self.assertIn("Final Score:", fake_out.getvalue())


if __name__ == "__main__":
    unittest.main()
