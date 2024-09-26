import time
from maze_generator import generate_maze
from renderer import render_maze
from player import Player
from input_handler import getch
from save_load import save_game, load_game


class MazeRunner:
    """Main game class that handles the game loop and player interactions."""

    def __init__(self, width=40, height=20):
        """Initialize the game with default settings."""
        self.width = width
        self.height = height
        self.maze = generate_maze(self.width, self.height)
        self.player = Player(1, 1)  # Start player at (1,1)
        self.running = True
        self.score = 0
        self.moves = 0
        self.start_time = time.time()

    def save_game_state(self):
        """Save the current game state."""
        game_state = {
            "maze": self.maze,
            "player_x": self.player.x,
            "player_y": self.player.y,
            "score": self.score,
            "moves": self.moves,
            "start_time": self.start_time,
        }
        if save_game(game_state):
            print("Game saved successfully!")
        else:
            print("Failed to save game.")

    def load_game_state(self):
        """Load a saved game state."""
        game_state = load_game()
        if game_state:
            self.maze = game_state["maze"]
            self.player.x = game_state["player_x"]
            self.player.y = game_state["player_y"]
            self.score = game_state["score"]
            self.moves = game_state["moves"]
            self.start_time = game_state["start_time"]
            print("Game loaded successfully!")
        else:
            print("Failed to load game.")

    def play(self):
        """Main game loop."""
        while self.running:
            # Render the current state of the maze
            render_maze(self.maze, self.player)

            # Display game information
            print(
                f"Score: {self.score} | Moves: {self.moves} | Time: {int(time.time() - self.start_time)}s"
            )
            print("Use h/j/k/l to move, q to quit")

            # Get player input
            key = getch().lower()

            if key in ["h", "j", "k", "l"]:
                # Handle movement
                self.moves += 1
                old_x, old_y = self.player.x, self.player.y
                self.player.move(key, self.maze)
            elif key == "q":
                # Quit the game
                self.running = False
            elif key == "s":
                # Save the game
                self.save_game_state()
            elif key == "l":
                # Load the game
                self.load_game_state()

            # Check if player has reached the exit
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
