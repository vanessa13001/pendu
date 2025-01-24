import json
import os

''' Florence functions '''

def player_id():
    player_name = input("Votre nom utilisateur : ").strip().lower()
    scores = load_scores('./scores/scores_file.json')

    if player_name not in scores:
        scores[player_name] = {"points": 0, "victoires": 0, "defaites": 0}
        save_scores('./scores/scores_file.json', scores)
    return player_name

def load_scores(scores_file):
    scores_file = './scores/scores_file.json'
    if not os.path.exists(scores_file):
        with open(scores_file, "w", encoding="UTF-8") as file:
            json.dump({}, file)  # create json file if it doesn't exist and put an empty dictionary
    with open(scores_file, "r") as file:
        scores = json.load(file)
    return scores

# Save scores inside JSON file
def save_scores(scores_file, scores):
    with open(scores_file, "w") as file:
        json.dump(scores, file, indent=4)
    print(f"Scores sauvegardés avec succès dans {scores_file}.")  # Add print to check if save worked


'''End Florence function'''


def display_entire_record(scores_file):
    with open(scores_file, "r", encoding="UTF-8") as file:
        record = json.load(file)
    
    for player in record:
        points = record[player]['points']
        victory = record[player]['victoires']
        defeat = record[player]['defaites']
        player_record= f"{player.upper()} \n   VICTOIRES : {victory} \n   DEFAITES : {defeat} \n   POINTS : {points}"  
        print(player_record)
        print("- - - - - - - - -")

def display_user_record(scores_file, player):
    with open(scores_file, "r", encoding="UTF-8") as file:
        record = json.load(file)
    
    if player in record:
        points = record[player]['points']
        victory = record[player]['victoires']
        defeat = record[player]['defaites']
        player_record= f"{player.upper()} \n   VICTOIRES : {victory} \n   DEFAITES : {defeat} \n   POINTS : {points}"  
        print(player_record)

    else:
        print(f"Le joueur {player} n'existe pas")

def erase_all_record(scores_file):
    os.remove(scores_file)

def reset_user_record(scores_file, player):
    with open(scores_file, "r", encoding="UTF-8") as file:
        record = json.load(file)

    if player in record:
        del record[player]
        with open(scores_file, "w") as file:
            json.dump(record, file, indent=4)
            print(f"l'historique de {player} a été supprimé avec succès")
            
    else:
        print(f"Il n'est pas possible de supprimer l'historique de {player} car ce joueur n'existe pas")

    

# def restore_record(scores_file):
