from colorama import Fore, Back, Style, init
import os

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def render_maze(maze, player):
    clear_screen()
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if player.x == x and player.y == y:
                print(Fore.YELLOW + "☺", end="")  # Yellow smiley face for player
            elif cell == 1:  # Wall
                print(Fore.WHITE + Back.BLACK + "█", end="")
            elif cell == 2:  # Start
                print(Fore.GREEN + "⌂", end="")  # Green house for start
            elif cell == 3:  # End
                print(Fore.RED + "◎", end="")  # Red target for end
            else:  # Path
                print(" ", end="")
        print(Style.RESET_ALL)  # Reset color at the end of each line
    print(
        "\n"
        + Fore.YELLOW
        + "☺: Player, "
        + Fore.GREEN
        + "⌂: Start, "
        + Fore.RED
        + "◎: End, "
        + Fore.WHITE
        + "█: Wall"
    )

