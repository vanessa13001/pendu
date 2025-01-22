import secrets
from unidecode import unidecode
import json
import os

"""
json for score
"""

# Fonction pour charger les scores depuis un fichier JSON
def charger_scores(fichier_scores):
    if not os.path.exists(fichier_scores):
        with open(fichier_scores, "w") as file:
            json.dump({}, file)  # Crée un fichier JSON vide avec un dictionnaire
    with open(fichier_scores, "r") as file:
        scores = json.load(file)
    return scores

# Fonction pour sauvegarder les scores dans un fichier JSON
def sauvegarder_scores(fichier_scores, scores):
    with open(fichier_scores, "w") as file:
        json.dump(scores, file, indent=4)
    print(f"Scores sauvegardés avec succès dans {fichier_scores}.")  # Ajout pour vérifier la sauvegarde

# Fonction pour mettre à jour le score d'un joueur après une défaite
def mettre_a_jour_score_defaite(fichier_scores, joueur):
    scores = charger_scores(fichier_scores)
    joueur = joueur.lower()

    if joueur not in scores:
        scores[joueur] = {"points": 0, "victoires": 0, "defaites": 1, "defaites_consecutives": 1}
    else:
        scores[joueur]["defaites"] += 1  # Incrémenter le nombre de défaites
        scores[joueur]["defaites_consecutives"] += 1  # Incrémenter le nombre de défaites consécutives

        # Réduire les points en fonction des défaites consécutives
        if scores[joueur]["defaites_consecutives"] == 2:
            scores[joueur]["points"] -= 3  # Réduire de 3 points pour 2 défaites consécutives
        else:
            scores[joueur]["points"] -= 1  # Réduire de 1 point pour chaque défaite

    sauvegarder_scores(fichier_scores, scores)

"""
function menu
"""    

def display_menu():
    menu_choice = input(" === MENU === \n"
                        "1. Nouvelle partie \n"
                        "2. Partie en cours \n"
                        "3. Historique des scores \n"
                        "4. Ajouter un mot \n"
                        "5. Quitter le jeu \n").strip()
    return menu_choice

# Fonction pour gérer l'identité du joueur
def player_id(fichier_scores):
    user_name = input("Votre nom utilisateur : ").strip().lower()
    scores = charger_scores(fichier_scores)

    if user_name not in scores:
        scores[user_name] = {"points": 0, "victoires": 0, "defaites": 0, "defaites_consecutives": 0}
        sauvegarder_scores(fichier_scores, scores)

    return user_name

"""
function word files
"""

def add_word():  # TODO check if word already exists or not
    new_word = input("Veuillez entrer un nouveau mot : ").strip().lower()

    # Ouverture du fichier words.txt pour vérifier si le mot existe déjà
    with open("words.txt", "r", encoding="UTF-8") as secret_words:
        secret_words_list = secret_words.readlines()

    secret_words_list = [word.strip().lower() for word in secret_words_list]

    if new_word in secret_words_list:
        print("Ce mot existe déjà")
    else:
        # Ajout du mot au fichier words.txt
        with open("words.txt", "a", encoding="UTF-8") as secret_words:
            secret_words.write("\n" + new_word)
        print("Mot ajouté avec succès.")


"""
function for score historic
"""

# Fonction pour afficher l'historique des scores
def afficher_scores(fichier_scores):
    scores = charger_scores(fichier_scores)
    if scores:
        print("\nHistorique des scores :")
        for joueur, data in scores.items():
            print(f"{joueur.capitalize()} - Points : {data['points']}, Victoires : {data['victoires']}, Défaites : {data['defaites']}")
    else:
        print("Aucun score enregistré.")

"""
Main function for the game loop
"""
# Fonction principale de la boucle du jeu
def game_loop(fichier_scores, joueur, life_count, guess_word, user_word_format):
    letters = []
    scores = charger_scores(fichier_scores)

    while life_count >= 0:
        guess_letter = unidecode(input("Veuillez entrer une lettre : ").lower()[0:1])

        # Vérification que l'utilisateur entre bien une lettre
        if not guess_letter.isalpha() or len(guess_letter) != 1:
            print("Veuillez entrer une seule lettre valide.")
            continue

        letters.append(guess_letter.upper())

        for index in range(len(guess_word)):
            if guess_letter == guess_word[index]:
                user_word_format[index] = guess_word[index]

        print(f"\033[H\033[2J", end="")  # Clear screen (fonction spécifique à certains systèmes)
        print(' '.join(user_word_format))
        print(f"lettre(s) déjà proposée(s) {' '.join(letters)}")

        if "_" not in user_word_format:
            print("Vous avez gagné !!")
            
            # Normalisation du nom du joueur (en minuscules) pour éviter les problèmes de casse
            joueur_normalise = joueur.lower()
            
            # Vérification si le joueur existe dans les scores
            if joueur_normalise not in scores:
                print(f"Erreur: Le joueur {joueur} n'existe pas dans les scores. Création de son profil.")
                scores[joueur_normalise] = {"points": 0, "victoires": 0, "defaites": 0, "defaites_consecutives": 0}  # Création d'un profil joueur si nécessaire

            # Incrémente les points et les victoires
            scores[joueur_normalise]["points"] += 1  # Ajouter un point au joueur existant
            scores[joueur_normalise]["victoires"] += 1  # Incrémenter les victoires
            scores[joueur_normalise]["defaites_consecutives"] = 0  # Réinitialiser les défaites consécutives

            # Affichage des scores après mise à jour pour vérifier l'incrémentation
            print(f"Scores mis à jour pour {joueur.capitalize()}: Points = {scores[joueur_normalise]['points']}, Victoires = {scores[joueur_normalise]['victoires']}, Défaites = {scores[joueur_normalise]['defaites']}")

            # Sauvegarde des scores
            sauvegarder_scores(fichier_scores, scores)
            
            break
        elif guess_letter not in guess_word and life_count > 0:
            life_count -= 1
            print(f"Il vous reste {life_count} vies")
        elif "_" in user_word_format and life_count == 0:
            print(f"Vous avez perdu ! Le mot à deviner était {''.join(guess_word)}")
            mettre_a_jour_score_defaite(fichier_scores, joueur)
            break

def get_guess_word():
    with open("words.txt", 'r', encoding="UTF-8") as secret_words:
        secret_words_list = secret_words.readlines()
        guess_word = list(unidecode(secret_words_list[secrets.randbelow(len(secret_words_list))].strip().lower()))
        return guess_word

def display_user_word(guess_word):
    user_word = "_"
    user_word_format = []

    for index in range(len(guess_word)):
        if guess_word[index] != " ":
            user_word_format.append(user_word)
        else:
            user_word_format.append(" ")

    return user_word_format

def main():
    scores_file = "scores.json"  # Fichier contenant les scores
    game_run = True
    while game_run:
        menu = display_menu()

        if menu == "1":
            joueur = player_id(scores_file)
            guess_word = get_guess_word()
            user_word_format = display_user_word(guess_word)
            life_count = 7
            print("Il y a 7 vies au jeu du pendu.")  
            print(f"Mot à deviner : {' '.join(user_word_format)}")
            game_loop(scores_file, joueur, life_count, guess_word, user_word_format)

        elif menu == "2":
            print("Partie en cours : Cette fonctionnalité n'est pas encore implémentée.")
            continue

        elif menu == "3":
            afficher_scores(scores_file)

        elif menu == "4":
            add_word()

        elif menu == "5":
            game_run = False
            exit()

if __name__ == "__main__":
    main()
