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