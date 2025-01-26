import string, pygame
upper_letters = string.ascii_uppercase
letters = string.ascii_letters

'''
    establish paths to game's data
'''
SCORE_PATH = "./game/scores/scores_file.json"
EASY_WORDS_PATH = "./game/words/words_easy.txt"
HARD_WORDS_PATH = "./game/words/words_hard.txt"

'''
    clear terminal, terminate pygame module and exit the program
'''
def off():
    heavy_clear = "\033[3J\033[1;0H\033[0J"
    print(f"{heavy_clear}", end="", flush=True)
    pygame.quit()
    exit()