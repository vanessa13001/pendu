from game_loop import game_loop
from scores.manage_scores import player_id, display_entire_record, display_user_record, erase_all_record, reset_user_record
from words.manage_words import get_guess_word, display_user_word, add_word

def display_menu():
    menu_choice = input(" === MENU === \n"
          "1. Nouvelle partie \n"
          "2. Partie en cours \n"
          "3. Historique des scores \n"
          "4. Ajouter un mot \n"
          "5. Quitter le jeu \n").strip()
    return menu_choice
 
def main():
    scores_file = './scores/scores_file.json'

    game_run = True
    while game_run:

        # print(f"\033[H\033[2J", end="")
        menu = display_menu()
        match menu:
            case "1":
                player = player_id()
                guess_word = get_guess_word()
                user_word_format = display_user_word(guess_word)
                scores_file = './scores/scores_file.json'

                '''Il y a 7 vies au jeu du pendu'''
                life_count = 7
                print(f"mot à deviner : {' '.join(user_word_format)}")
                game_loop(life_count, guess_word, user_word_format, scores_file, player) 
            case "3":
                sub_menu = input(" === HISTORIQUE === \n"
                                "1. Tout l'historique \n"
                                "2. L'historique d'un joueur \n"
                                "3. Supprimer tout l'historique \n"
                                "4. Supprimer l'historique d'un joueur \n"
                                "5. Retour \n")
                match sub_menu:
                    case "1":
                        display_entire_record(scores_file)
                    case "2":
                        player = input("L'historique de quel joueur voulez-vous voir ?").lower().strip()
                        display_user_record(scores_file, player)
                    case "3":
                        choice = input("Êtes-vous sûr de vouloir supprimer tout l'historique ? o/n").lower()
                        if choice == "o":
                            erase_all_record(scores_file)
                        else:
                            continue
                    case "4":
                        player = input("L'historique de quel joueur voulez-vous voir ?").lower().strip()
                        reset_user_record(scores_file, player)
                    case "5":
                        continue
                    case _:
                        print("cette commande n'est pas reconnue")
            case "4":
                add_word()

            case "5":
                print("Vous allez quitter le jeu !")
                game_run = False
            case _:
                print("La commande n'a pas été reconnue")

main()

