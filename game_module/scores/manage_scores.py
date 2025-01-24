import json
import os
'''
    Florence functions
'''
def player_id(player, scores):
    if player not in scores:
        scores[player] = {"win_streak": 0, "wins": 0, "losses": 0}
        save_scores(scores,'game_module/scores/scores_file.json')

def load_scores(scores_file='game_module/scores/scores_file.json'):
    if not os.path.exists(scores_file):
        with open(scores_file, "w", encoding="UTF-8") as file:
            json.dump({}, file)  # create json file if it doesn't exist and put an empty dictionary
    with open(scores_file, "r") as file:
        scores = json.load(file)
    return scores

def save_scores(scores, scores_file='game_module/scores/scores_file.json'):
    with open(scores_file, "w") as file:
        json.dump(scores, file, indent=4)

'''End Florence function'''


def display_entire_record(scores_file):
    with open(scores_file, "r", encoding="UTF-8") as file:
        record = json.load(file)
    
    for player in record:
        win_streak = record[player]['win_streak']
        victory = record[player]['wins']
        defeat = record[player]['losses']
        player_record= f"{player.upper()} \n   Wins : {victory} \n   Losses : {defeat} \n   Win streak : {win_streak}"  
        print(player_record)
        print("- - - - - - - - -")

def display_user_record(scores_file, player):
    with open(scores_file, "r", encoding="UTF-8") as file:
        record = json.load(file)
    
    if player in record:
        win_streak = record[player]['win_streak']
        victory = record[player]['wins']
        defeat = record[player]['losses']
        player_record= f"{player.upper()} \n   Wins : {victory} \n   Losses : {defeat} \n   Win streak : {win_streak}"  
        print(player_record)

    else:
        print(f"Le joueur {player} n'existe pas")

def erase_all_record(scores_file='game_module/scores/scores_file.json'):
    os.remove(scores_file)

def reset_user_record(scores_file, player):
    with open(scores_file, "r", encoding="UTF-8") as file:
        record = json.load(file)

    if player in record:
        del record[player]
    else:
        print(f"Il n'est pas possible de supprimer l'historique de {player} car ce joueur n'existe pas")

    with open(scores_file, "w") as file:
        json.dump(record, file, indent=4)
        print(f"l'historique de {player} a été supprimé avec succès")

# def restore_record(scores_file):
