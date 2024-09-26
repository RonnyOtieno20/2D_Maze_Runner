import json
import os


def save_game(game_state, filename="maze_game_save.json"):
    """
    Save the current game state to a file.

    Args:
    game_state (dict): A dictionary containing the current game state
    filename (str): The name of the file to save the game state (default: "maze_game_save.json")

    Returns:
    bool: True if save was successful, False otherwise
    """
    try:
        with open(filename, "w") as f:
            json.dump(game_state, f)
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False


def load_game(filename="maze_game_save.json"):
    """
    Load a saved game state from a file.

    Args:
    filename (str): The name of the file to load the game state from (default: "maze_game_save.json")

    Returns:
    dict: The loaded game state if successful, None otherwise
    """
    if not os.path.exists(filename):
        print("No saved game found.")
        return None

    try:
        with open(filename, "r") as f:
            game_state = json.load(f)
        return game_state
    except Exception as e:
        print(f"Error loading game: {e}")
        return None
