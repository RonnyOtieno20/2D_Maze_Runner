import unittest
import os
from save_load import save_game, load_game
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestSaveLoad(unittest.TestCase):

    def setUp(self):
        self.test_filename = "test_save.json"
        self.test_game_state = {
            "maze": [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            "player_x": 1,
            "player_y": 1,
            "score": 100,
            "moves": 10,
            "start_time": 1630000000,
        }

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save_game(self):
        result = save_game(self.test_game_state, self.test_filename)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.test_filename))

    def test_load_game(self):
        save_game(self.test_game_state, self.test_filename)
        loaded_state = load_game(self.test_filename)
        self.assertEqual(loaded_state, self.test_game_state)

    def test_load_nonexistent_game(self):
        loaded_state = load_game("nonexistent_file.json")
        self.assertIsNone(loaded_state)


if __name__ == "__main__":
    unittest.main()
