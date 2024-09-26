import unittest
import sys
import os
from maze_generator import generate_maze

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestMazeGenerator(unittest.TestCase):

    def test_maze_dimensions(self):
        width, height = 15, 20
        maze = generate_maze(width, height)
        self.assertEqual(len(maze), height)
        self.assertEqual(len(maze[0]), width)

    def test_maze_borders(self):
        maze = generate_maze(10, 10)
        for x in range(10):
            self.assertEqual(maze[0][x], 1)  # Top border
            self.assertEqual(maze[9][x], 1)  # Bottom border
        for y in range(10):
            self.assertEqual(maze[y][0], 1)  # Left border
            self.assertEqual(maze[y][9], 1)  # Right border

    def test_start_and_end_points(self):
        maze = generate_maze(10, 10)
        self.assertEqual(maze[1][1], 2)  # Start point
        self.assertEqual(maze[8][8], 3)  # End point

    def test_path_to_end(self):
        maze = generate_maze(10, 10)
        self.assertTrue(maze[7][8] == 0 or maze[8][7] == 0)  # Path to end exists

    def test_maze_connectivity(self):
        maze = generate_maze(10, 10)
        visited = set()

        def dfs(x, y):
            if (x, y) in visited or maze[y][x] == 1:
                return
            visited.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 10 and 0 <= ny < 10:
                    dfs(nx, ny)

        dfs(1, 1)  # Start from (1,1)
        self.assertIn((8, 8), visited)  # End point should be reachable


if __name__ == "__main__":
    unittest.main()
