import secrets
from unidecode import unidecode
import json

def display_menu():
    menu_choice = input(" === MENU === \n"
          "1. Nouvelle partie \n"
          "2. Partie en cours \n"
          "3. Historique des scores \n"
          "4. Ajouter un mot \n"
          "5. Quitter le jeu \n").strip()
    return menu_choice

def player_id():
    user_name = input("Votre nom utilisateur : ").strip().lower()
    score = 0
    with open("scores.txt", "a", encoding="UTF-8") as score_file:
        score_file.write(f"{user_name} : {score}")

    # return user_name

def add_word():
    new_word = input("Veuillez entrer un nouveau mot : ").strip().lower()

    secret_words = open("words.txt", "r", encoding="UTF-8")
    secret_words_list = secret_words.readlines()
    secret_words.close()

    for index in range(len(secret_words_list)):
        secret_words_list[index] = secret_words_list[index].replace("\n", "")
 
    if new_word in secret_words_list:
        print("Ce mot existe déjà")       

    else:
        secret_words = open("words.txt", "a", encoding="UTF-8")
        secret_words.write("\n"+new_word)
        secret_words.close()

def game_loop(life_count, guess_word,user_word_format, score):
    letters = []

    while life_count >= 0 :
        guess_letter = unidecode(input("Veuillez entrer une lettre : ").lower()[0:1])
        letters.append(guess_letter.upper())

        for index in range(len(guess_word)):
            if guess_letter == guess_word[index]:
                user_word_format[index] = guess_word[index]

        print(f"\033[H\033[2J", end="")
        print(' '.join(user_word_format))
        print(f"lettre(s) déjà proposée(s) {' '.join(letters)}")

        if "_" not in user_word_format:
            print("vous avez gagné !! ")
            score += 1
            break
        elif guess_letter not in guess_word and life_count > 0:
            life_count -= 1
            print(f"il vous reste {life_count} vies")

        elif "_" in user_word_format and life_count == 0:    
            print(f"vous avez perdu ! Le mot à deviner était {''.join(guess_word)}")
            life_count -= 1
            score += 0
       
    return score
    
def get_guess_word():
     with open("words.txt",'r', encoding="UTF-8") as secret_words:
        secret_words_list = secret_words.readlines()
        guess_word = list(unidecode(secret_words_list[secrets.randbelow(len(secret_words_list))].strip().lower()))

        return guess_word
     
def display_user_word(guess_word):
    user_word = "_"
    user_word_format = []

    for index in range(len(guess_word)):
        match guess_word[index]:
            case " ":
                user_word_format.append(" ")
            case "'":
                user_word_format.append("'")
            case "-":
                user_word_format.append("-")
            case _:
                user_word_format.append(user_word)

    return user_word_format

def main():
    game_run = True
    while game_run:

        menu = display_menu()
        match menu:
            case "1":
                player_id()
                guess_word = get_guess_word()
                user_word_format = display_user_word(guess_word)
                '''Il y a 7 vies au jeu du pendu'''
                life_count = 7
                score = 0
                print(f"mot à deviner : {' '.join(user_word_format)}")
                game_loop(life_count, guess_word,user_word_format, score) 

            case "4":
                add_word()

            case "5":
                game_run = False


main()

