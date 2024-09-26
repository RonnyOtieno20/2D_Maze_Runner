import time
from maze_generator import generate_maze
from renderer import render_maze
from player import Player
from input_handler import getch


class MazeRunner:
    def __init__(self):
        self.width, self.height = 40, 20  # Smaller maze for better visibility
        self.maze = generate_maze(self.width, self.height)
        self.player = Player(1, 1)
        self.running = True
        self.score = 0
        self.moves = 0
        self.start_time = time.time()

    def play(self):
        while self.running:
            render_maze(self.maze, self.player)
            print(
                f"Score: {self.score} | Moves: {self.moves} | Time: {int(time.time() - self.start_time)}s"
            )
            print("Use h/j/k/l to move, q to quit")
            key = getch().lower()
            if key in ["h", "j", "k", "l"]:
                self.moves += 1
                old_x, old_y = self.player.x, self.player.y
                self.player.move(key, self.maze)
            elif key == "q":
                self.running = False
            if self.player.x == self.width - 2 and self.player.y == self.height - 2:
                render_maze(self.maze, self.player)
                final_time = int(time.time() - self.start_time)
                self.score = 1000 - self.moves - final_time
                print(f"Congratulations! You've reached the exit!")
                print(
                    f"Final Score: {self.score} | Moves: {self.moves} | Time: {final_time}s"
                )
                self.running = False
                break
        print("Thanks for playing MazeRunner!")


if __name__ == "__main__":
    game = MazeRunner()
    game.play()
