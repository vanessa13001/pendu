from unidecode import unidecode
import secrets

def add_word():
    new_word = input("Veuillez entrer un nouveau mot : ").strip().lower()

    secret_words = open("./words/words.txt", "r", encoding="UTF-8")
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
    with open("./words/words.txt",'r', encoding="UTF-8") as secret_words:
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
            case "_":
                user_word_format.append("_")
            case _:
                user_word_format.append(user_word)

    return user_word_format
