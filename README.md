# MazeRunner

MazeRunner is a command-line adventure game where players navigate through procedurally generated mazes. This project was developed as part of my portfolio for Holberton School, showcasing skills in algorithmic thinking, data structures, and command-line interface design.

![MazeRunner Demo](maze-demo.gif)

[View Project Landing Page](https://ronnyotieno20.github.io/2D_Maze_Runner/)

## Features

- **Procedural Maze Generation**: Every game presents a unique maze challenge.
- **ASCII Rendering**: Experience the maze in beautifully crafted ASCII art.
- **Vim-style Navigation**: Use h, j, k, l keys for efficient movement through the maze.
- **Save and Load**: Pause your adventure and resume it later!
- **Scoring System**: Challenge yourself to reach the exit in the fewest moves and shortest time.
- **Colorful Interface**: Enjoy a visually appealing command-line experience with colored elements.

## Installation

To run MazeRunner, you'll need Python 3.7 or higher installed on your system.

1. Clone this repository:
   ```bash
   git clone https://github.com/RonnyOtieno20/2D_Maze_Runner.git
   Navigate to the project directory:
   ```

```bash
cd 2D_Maze_Runner
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To start a new game, from the root directory run:

```bash
python src/maze_runner.py
```

### Commands:

```code
h: Move left
j: Move down
k: Move up
l: Move right
s: Save current game
o: Load a saved game
q: Quit game
```

## Project Structure

```code
2D_Maze_Runner/
│
├── maze_runner.py # Main game file
├── maze_generator.py # Maze generation algorithm
├── renderer.py # ASCII rendering functions
├── player.py # Player class and movement logic
├── save_load.py # Save and load game functionality
├── input_handler.py # Handle user input
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

## Development

This project is developed using Python 3.7+. The main components are:

- Maze generation using Depth-First Search algorithm with recursive backtracking
- ASCII rendering for visualizing the maze using the colorama library
- Player movement with collision detection
- Save/Load functionality using JSON serialization
- Input handling for smooth, non-blocking user interaction

## Testing

To run the tests for MazeRunner, use the following command:

```bash
python -m unittest discover -v
```

This will run all the test files in the tests directory.

## Contributing

Contributions to MazeRunner are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://opensource.org/license/mit).

## Contact

Ronny Owuor

- GitHub: [@RonnyOtieno20](https://github.com/RonnyOtieno20)
- Twitter: [@ronny_optimist](https://twitter.com/ronny_optimist)
- LinkedIn: [Ronny Owuor](https://www.linkedin.com/in/ronnyotieno)

## Acknowledgements

- Holberton School for the project inspiration and guidance
- The Python community for excellent libraries and resources

## Future Enhancements

- Multiple difficulty levels
- Leaderboard system
- Sound effects (for compatible terminals)
- AI-powered maze solver for demonstrations

