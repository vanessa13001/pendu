from unidecode import unidecode
import secrets

def add_word(new_word, game_mode):
    new_word = str(new_word).strip().lower()

    special_caracter = ["'", "-", " "]

    is_valid = True
    for caracter in special_caracter:
        if caracter in new_word:
            get_index_caracter = new_word.index(caracter)
            if new_word[(get_index_caracter)+1] in special_caracter:
                is_valid = False
                return "invalid"
    
    if is_valid:
        if game_mode == 0:
            secret_words = open("game_module/words/words_easy.txt", "r", encoding="UTF-8")
        else :
            secret_words = open("game_module/words/words_hard.txt", "r", encoding="UTF-8")
        
        secret_words_list = secret_words.readlines()
        secret_words.close()

        for index in range(len(secret_words_list)):
            secret_words_list[index] = secret_words_list[index].replace("\n", "")
        if new_word in secret_words_list:
            return False
        
        else:
            if game_mode == 0:
                secret_words = open("game_module/words/words_easy.txt", "a", encoding="UTF-8")
            else:
                secret_words = open("game_module/words/words_hard.txt", "a", encoding="UTF-8")

            secret_words.write("\n"+new_word)
            secret_words.close()
            return True    

def get_guess_word(game_mode):
    if game_mode == 0:
        with open("game_module/words/words_easy.txt",'r', encoding="UTF-8") as secret_words:
            secret_words_list = secret_words.readlines()
            guess_word = list(unidecode(secret_words_list[secrets.randbelow(len(secret_words_list))].strip().upper()))
    else:
        with open("game_module/words/words_hard.txt",'r', encoding="UTF-8") as secret_words:
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