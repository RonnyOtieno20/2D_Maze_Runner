#!/usr/bin/env python3
"""
Input Handler Module for MazeRunner

This module provides a cross-platform solution for reading single keystrokes
without requiring the Enter key to be pressed.

Author: Ronny Owuor
Date: September 2024
"""

import sys
import termios
import tty
import select


def getch():
    """
    Read a single keystroke from stdin without echo.

    Returns:
        str: The character read from stdin
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            ch = sys.stdin.read(1)
        else:
            ch = ""
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == "__main__":
    print("Press any key (press 'q' to quit):")
    while True:
        char = getch()
        if char == "q":
            break
        print(f"You pressed: {char}")
