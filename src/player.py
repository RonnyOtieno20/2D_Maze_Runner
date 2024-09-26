class Player:
    """Represents the player in the maze."""

    def __init__(self, x, y):
        """
        Initialize the player at the given coordinates.

        Args:
            x (int): Initial x-coordinate
            y (int): Initial y-coordinate
        """
        self.x = x
        self.y = y

    def move(self, direction, maze):
        """
        Move the player in the specified direction if possible.

        Args:
            direction (str): Movement direction ('h', 'j', 'k', or 'l')
            maze (list): 2D list representing the current maze state

        Returns:
            bool: True if the move was successful, False otherwise
        """
        dx, dy = 0, 0
        if direction == "h":
            dx = -1  # Move left
        elif direction == "l":
            dx = 1  # Move right
        elif direction == "k":
            dy = -1  # Move up
        elif direction == "j":
            dy = 1  # Move down

        new_x, new_y = self.x + dx, self.y + dy
        if (
            0 <= new_x < len(maze[0])
            and 0 <= new_y < len(maze)
            and maze[new_y][new_x] != 1
        ):
            self.x, self.y = new_x, new_y
            return True
        return False
