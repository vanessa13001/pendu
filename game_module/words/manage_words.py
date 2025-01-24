from unidecode import unidecode
import secrets

def add_word():
    new_word = input("Veuillez entrer un nouveau mot : ").strip().lower()
    secret_words = open("game_module/words/words.txt", "r", encoding="UTF-8")
    secret_words_list = secret_words.readlines()
    secret_words.close()
    for index in range(len(secret_words_list)):
        secret_words_list[index] = secret_words_list[index].replace("\n", "")
    if new_word in secret_words_list:
        print("Ce mot existe déjà")       
    else:
        secret_words = open("./words/words.txt", "a", encoding="UTF-8")
        secret_words.write("\n"+new_word)
        secret_words.close()

def get_guess_word():
    with open("game_module/words/words.txt",'r', encoding="UTF-8") as secret_words:
        secret_words_list = secret_words.readlines()
        guess_word = list(unidecode(secret_words_list[secrets.randbelow(len(secret_words_list))].strip().upper()))
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
            case "_":
                user_word_format.append("_")
            case _:
                user_word_format.append(user_word)
    return user_word_format

def input_guess_letter(letters, user_word_format, life_count):
    guess_letter = unidecode(input("Veuillez entrer une lettre : ").upper()[0:1])
    if guess_letter in letters:
        print(f"\033[H\033[2J", end="")
        print(' '.join(user_word_format))
        print(f"lettre(s) déjà proposée(s) {' '.join(letters)}")
        print(f"Vous avez déjà essayé {guess_letter}")
        print(f"il vous reste {life_count} vies")
        return input_guess_letter(letters, user_word_format, life_count)
    return guess_letter