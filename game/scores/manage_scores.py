import json
import os
from ..__settings__ import SCORE_PATH

"""
player_id : Checks if the player's ID exists in the scores dictionary. 
If not, initializes the player's record with default values and saves the scores.

Args:
 player (str): The player's name or identifier.
scores (dict): Dictionary containing all player records.
{
    "player": {
    "win_streak": int,
    "wins": int,
    "losses": int
    },...
}
"""


def player_id(player, scores):

    if player not in scores:
        # Initialize the player's record with default values
        scores[player] = {"win_streak": 0, "wins": 0, "losses": 0}
        save_scores(scores)


"""
Load_scores : Loads the scores from the JSON file. 
If the file does not exist, it creates an empty JSON file.

Returns:
dict: Dictionary containing all player records.
"""


def load_scores():

    if not os.path.exists(SCORE_PATH):
        # Create an empty JSON file if it doesn't exist
        with open(SCORE_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    # Read and load the scores from the file
    with open(SCORE_PATH, "r") as file:
        scores = json.load(file)
    return scores


"""
Save_scores : Saves the scores dictionary to the JSON file.

Args:
scores (dict): Dictionary containing all player records.
"""


def save_scores(scores):

    with open(SCORE_PATH, "w") as file:
        json.dump(scores, file, indent=4)


"""
Update_scores : Updates the scores for a player based on the game result.

Args:
life_count (int): The number of lives remaining (0 means the player lost).
user_word_format (list): The word format showing guessed letters and underscores.

player (str): The player's name or identifier.
"""


def update_scores(life_count, user_word_format, player):

    # Load the current scores
    scores = load_scores()
    player = str(player).lower()
    # Ensure the player's record exists
    player_id(player, scores)
    # Update scores based on the game outcome
    if life_count == 0:
        # Player lost the game
        scores[player]['losses'] += 1
        scores[player]['win_streak'] = 0
    elif '_' not in user_word_format:
        # Player won the game
        scores[player]['wins'] += 1
        scores[player]['win_streak'] += 1
    # Save the updated scores
    save_scores(scores)


"""
erase_all_record : Deletes the score file, erasing all records.
"""


def erase_all_record():

    os.remove(SCORE_PATH)
