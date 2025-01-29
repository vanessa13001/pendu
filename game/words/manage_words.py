from unidecode import unidecode
import secrets
from ..__settings__ import EASY_WORDS_PATH, HARD_WORDS_PATH

def game_words(game_mode):
    guess_word = get_guess_word(game_mode)
    user_word_format = display_user_word(guess_word)
    return guess_word, user_word_format

'''
    check is letter input by player is in guess word. If it's not, life_count decrement.
    if it is, the letter corresponding is replaced in user_word
'''
def check_letter_loop(player_input, guess_word, letters_played, life_count, user_word_format):
    if player_input not in guess_word and player_input not in letters_played:
        life_count-=1
        letters_played.append(player_input)
    else:
        for index in range(len(guess_word)):
            if player_input == guess_word[index]:
                user_word_format[index] = guess_word[index]

    return life_count, letters_played

'''
    allow player to add word depending the word list (easy or hard).
    if input is valid, append word in the right file
'''
def add_word(new_word, game_mode):
    new_word = str(new_word).strip().lower()

    special_caracter = ["'", "-", " "]
    try: 
        is_valid = True
        for caracter in special_caracter:
            if caracter in new_word:
                get_index_caracter = new_word.index(caracter)
                if new_word[(get_index_caracter)+1] in special_caracter:
                    is_valid = False
                    raise Exception()
    except:
        return "invalid"
    
    if is_valid:
        if game_mode == 0:
            secret_words = open(EASY_WORDS_PATH, "r", encoding="UTF-8")
        else :
            secret_words = open(HARD_WORDS_PATH, "r", encoding="UTF-8")
        
        secret_words_list = secret_words.readlines()
        secret_words.close()

        for index in range(len(secret_words_list)):
            secret_words_list[index] = secret_words_list[index].replace("\n", "")
        if new_word in secret_words_list:
            return False
        
        else:
            if game_mode == 0:
                secret_words = open(EASY_WORDS_PATH, "a", encoding="UTF-8")
            else:
                secret_words = open(HARD_WORDS_PATH, "a", encoding="UTF-8")

            secret_words.write("\n"+new_word)
            secret_words.close()
            return True    

def get_guess_word(game_mode):
    if game_mode == 0:
        with open(EASY_WORDS_PATH,'r', encoding="UTF-8") as secret_words:
            secret_words_list = secret_words.readlines()
            guess_word = list(unidecode(secret_words_list[secrets.randbelow(len(secret_words_list))].strip().upper()))
    else:
        with open(HARD_WORDS_PATH,'r', encoding="UTF-8") as secret_words:
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