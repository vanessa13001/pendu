import string, pygame
upper_letters = string.ascii_uppercase
letters = string.ascii_letters
'''
    establish paths to game's data
'''
SCORE_PATH = "./game/scores/scores_file.json"
EASY_WORDS_PATH = "./game/words/words_easy.txt"
HARD_WORDS_PATH = "./game/words/words_hard.txt"

def game_init():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Jeu du pendu')
    pygame.display.set_icon(pygame.image.load('assets/graphics/icon.png'))
    clock = pygame.time.Clock()
    return screen, clock
'''
    clear terminal, terminate pygame module and exit the program
'''
def game_off():
    heavy_clear = "\033[3J\033[1;0H\033[0J"
    print(f"{heavy_clear}", end="", flush=True)
    pygame.quit()
    exit()
'''
    the program sets the time delta on 45 times per second to update
    the screen with new informations on a regular scale
'''
def clock_tick(clock):
    pygame.display.update()
    clock.tick(45)