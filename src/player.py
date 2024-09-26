class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, maze):
        dx, dy = 0, 0
        if direction == "h":
            dx = -1
        elif direction == "l":
            dx = 1
        elif direction == "k":
            dy = -1
        elif direction == "j":
            dy = 1

        new_x, new_y = self.x + dx, self.y + dy
        if (
            0 <= new_x < len(maze[0])
            and 0 <= new_y < len(maze)
            and maze[new_y][new_x] != 1
        ):
            self.x, self.y = new_x, new_y
