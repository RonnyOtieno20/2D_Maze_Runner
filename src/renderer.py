from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)


def render_maze(maze, player):
    """
    Render the maze and player position using ASCII characters and colors.

    Args:
    maze (list): 2D list representing the maze
    player (Player): Player object containing current position
    """
    # Create a buffer to hold the entire screen
    buffer = []

    for y, row in enumerate(maze):
        line = []
        for x, cell in enumerate(row):
            if player.x == x and player.y == y:
                line.append(Fore.YELLOW + "☺")  # Yellow smiley face for player
            elif cell == 1:  # Wall
                line.append(Fore.WHITE + Back.BLACK + "█")
            elif cell == 2:  # Start
                line.append(Fore.GREEN + "⌂")  # Green house for start
            elif cell == 3:  # End
                line.append(Fore.RED + "◎")  # Red target for end
            else:  # Path
                line.append(" ")
        buffer.append("".join(line))

    # Add legend to buffer
    buffer.append(
        "\n"
        + Fore.YELLOW
        + "☺: Player, "
        + Fore.GREEN
        + "⌂: Start, "
        + Fore.RED
        + "◎: End, "
        + Fore.WHITE
        + "█: Wall, "
        + Fore.BLUE
        + "💾: Save, "
        + Fore.MAGENTA
        + "📂: Load"
    )

    # Clear the screen (use ANSI escape code for better cross-platform support)
    print("\033[H\033[J", end="")

    # Print the entire buffer at once
    print("\n".join(buffer))

    # Print controls
    print("\nControls: h/j/k/l to move, s to save, o to load, q to quit")
