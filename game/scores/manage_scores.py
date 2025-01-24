import json
import os
from ..__settings__ import SCORE_PATH

def player_id(player, scores):
    if player not in scores:
        scores[player] = {"win_streak": 0, "wins": 0, "losses": 0}
        save_scores(scores)

def load_scores():
    if not os.path.exists(SCORE_PATH):
        with open(SCORE_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)  # create json file if it doesn't exist and put an empty dictionary
    with open(SCORE_PATH, "r") as file:
        scores = json.load(file)
    return scores

def save_scores(scores):
    with open(SCORE_PATH, "w") as file:
        json.dump(scores, file, indent=4)

def update_scores(life_count, user_word_format, player):
    scores = load_scores()
    player = str(player).lower()
    player_id(player, scores)
    if life_count == 0:
        scores[player]['losses'] +=1
        scores[player]['win_streak'] = 0
    elif '_' not in user_word_format:
        scores[player]['wins'] +=1
        scores[player]['win_streak'] +=1
    save_scores(scores)

def erase_all_record():
    os.remove(SCORE_PATH)


