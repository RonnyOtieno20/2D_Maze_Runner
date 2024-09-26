# MazeRunner

MazeRunner is a command-line adventure game where players navigate through procedurally generated mazes. This project was developed as part of my portfolio for Holberton School, showcasing skills in algorithmic thinking, data structures, and command-line interface design.

![MazeRunner Demo](maze-demo.gif)


[View Project Landing Page](https://ronnyotieno20.github.io/2D_Maze_Runner/)
## Features

-  **Procedural Maze Generation**: Every game presents a unique maze challenge.
-  **ASCII Rendering**: Experience the maze in beautifully crafted ASCII art.
-  **Player Movement**: Navigate through the maze using simple commands.
-  **Save and Load**: Pause your adventure and resume it later!
-  **Win Condition**: Race against time or count your moves to reach the exit.

## Installation

To run MazeRunner, you'll need Python 3.7 or higher installed on your system.

1. Clone this repository:

```bash
git clone https://github.com/RonnyOtieno20/2D_Maze_Runner.git
```

2. Navigate to the project directory:
```bash
cd 2D_Maze_Runner
```

3. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

4. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To start a new game, run:

```bash
python maze_runner.py
```

### Commands:

```bash
-  `w`: Move up
-  `s`: Move down
-  `a`: Move left
-  `d`: Move right
-  `save`: Save current game
-  `load`: Load a saved game
-  `quit`: Exit the game
```

## Project Structure

```code
2D_Maze_Runner/
│
├── maze_runner.py         # Main game file
├── maze_generator.py      # Maze generation algorithm
├── renderer.py            # ASCII rendering functions
├── player.py              # Player class and movement logic
├── save_load.py           # Save and load game functionality
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```


## Development

This project is developed using Python 3.7+. The main components are:

-  Maze generation using [algorithm name, e.g., Depth-First Search]
-  ASCII rendering for visualizing the maze
-  Player movement and collision detection
-  Save/Load functionality using JSON serialization


## Contributing

Contributions to MazeRunner are welcome! Please feel free to submit a Pull Request.


## License

This project is open source and available under the [MIT License](https://opensource.org/license/mit).


## Contact

Ronny Owuor
-  GitHub: [@RonnyOtieno20](https://github.com/RonnyOtieno20)
-  Twitter: [@ronny_optimist](https://twitter.com/ronny_optimist)
-  LinkedIn: [Ronny Owuor](https://www.linkedin.com/in/ronnyotieno)


## Acknowledgements

-  Holberton School for the project inspiration and guidance
