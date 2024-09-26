import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from input_handler import getch


class TestInputHandler(unittest.TestCase):

    @patch("sys.stdin.fileno")
    @patch("termios.tcgetattr")
    @patch("tty.setraw")
    @patch("select.select")
    @patch("sys.stdin.read")
    @patch("termios.tcsetattr")
    def test_getch(
        self,
        mock_tcsetattr,
        mock_read,
        mock_select,
        mock_setraw,
        mock_tcgetattr,
        mock_fileno,
    ):
        mock_fileno.return_value = 0
        mock_tcgetattr.return_value = "old_settings"
        mock_select.return_value = ([sys.stdin], [], [])
        mock_read.return_value = "a"

        result = getch()
        self.assertEqual(result, "a")

        mock_fileno.assert_called_once()
        mock_tcgetattr.assert_called_once_with(0)
        mock_setraw.assert_called_once_with(0)
        mock_select.assert_called_once()
        mock_read.assert_called_once_with(1)
        mock_tcsetattr.assert_called_once_with(0, termios.TCSADRAIN, "old_settings")

    @patch("sys.stdin.fileno")
    @patch("termios.tcgetattr")
    @patch("tty.setraw")
    @patch("select.select")
    @patch("termios.tcsetattr")
    def test_getch_no_input(
        self, mock_tcsetattr, mock_select, mock_setraw, mock_tcgetattr, mock_fileno
    ):
        mock_fileno.return_value = 0
        mock_tcgetattr.return_value = "old_settings"
        mock_select.return_value = ([], [], [])

        result = getch()
        self.assertEqual(result, "")

        mock_fileno.assert_called_once()
        mock_tcgetattr.assert_called_once_with(0)
        mock_setraw.assert_called_once_with(0)
        mock_select.assert_called_once()
        mock_tcsetattr.assert_called_once_with(0, termios.TCSADRAIN, "old_settings")


if __name__ == "__main__":
    unittest.main()
