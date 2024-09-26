import random


def generate_maze(width, height):
    """
    Generate a random maze using depth-first search algorithm.

    Args:
    width (int): The width of the maze.
    height (int): The height of the maze.

    Returns:
    list: A 2D list representing the maze where:
          0 = path, 1 = wall, 2 = start, 3 = end
    """
    # Initialize the maze with walls
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve_path(x, y):
        """Recursively carve paths in the maze."""
        maze[y][x] = 0  # Mark current cell as path
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)  # Randomize direction order
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0  # Carve path to next cell
                carve_path(nx, ny)  # Recursively carve from next cell

    # Start carving from (1, 1)
    carve_path(1, 1)

    # Ensure path to end
    maze[height - 2][width - 2] = 0
    if maze[height - 2][width - 3] == 1 and maze[height - 3][width - 2] == 1:
        maze[height - 2][width - 3] = 0  # Create a path to the end

    # Set start and end points
    maze[1][1] = 2  # Start
    maze[height - 2][width - 2] = 3  # End

    # Add bottom and right borders
    for x in range(width):
        maze[height - 1][x] = 1
    for y in range(height):
        maze[y][width - 1] = 1

    return maze
