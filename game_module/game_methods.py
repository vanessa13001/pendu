import pygame
import game_module.__settings__ as settings
import game_module.words.manage_words as manage_words
from game_module.scores.manage_scores import load_scores, save_scores, player_id

def input_expression(game_mode,easy_button_rect, hard_button_rect, mouse_position, user_input, max_value):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return game_mode, user_input, 'quit'
        if easy_button_rect.collidepoint(mouse_position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0, user_input, ''
        if hard_button_rect.collidepoint(mouse_position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 1, user_input, ''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return game_mode, user_input, False
            if event.key == pygame.K_RETURN and user_input != '':
                return game_mode, user_input, True
            elif event.key == pygame.K_BACKSPACE and user_input != '':
                user_input = user_input[:-1]
                return game_mode, user_input, ''
            elif len(user_input) <= max_value:
                if event.unicode in settings.letters or event.unicode in (" ", "-", "'"):
                    user_input += event.unicode
                    return game_mode, user_input, ''
    return game_mode,user_input, ''

def launch_game(game_mode):
    guess_word = manage_words.get_guess_word(game_mode)
    user_word_format = manage_words.display_user_word(guess_word)
    return guess_word, user_word_format
def input_letter(player, player_input, guess_word, letters_played, life_count, user_word_format):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return life_count, player_input, letters_played, 'quit'
        if event.type == pygame.KEYDOWN:
            if life_count == 0 or '_' not in user_word_format:
                if event.key == pygame.K_RETURN:
                    update_scores(life_count,user_word_format,player)
                    return life_count, player_input, letters_played, True
                    
            elif event.key == pygame.K_ESCAPE:
                return life_count, player_input, letters_played, True
                
            elif event.key == pygame.K_RETURN and player_input != '_':
                life_count, letters_played = check_letter_loop(player_input, guess_word, letters_played, life_count, user_word_format)
                player_input = '_'
                return life_count, player_input, letters_played, ''
            elif event.key == pygame.K_BACKSPACE:
                player_input = '_'
            else:
                player_input = event.unicode
                try:
                    player_input = str(player_input).upper()
                    if player_input not in settings.upper_letters:
                        player_input = '_'
                except Exception: player_input = '_'
    return life_count, player_input, letters_played, ''

def update_scores(life_count, user_word_format, player):
    scores = load_scores('game_module/scores/scores_file.json')
    player = str(player).lower()
    player_id(player, scores)
    if life_count == 0:
        scores[player]['losses'] +=1
        scores[player]['win_streak'] = 0
    elif '_' not in user_word_format:
        scores[player]['wins'] +=1
        scores[player]['win_streak'] +=1
    save_scores(scores)

def check_letter_loop(player_input, guess_word, letters_played, life_count, user_word_format):

    if player_input not in guess_word and player_input not in letters_played:
        life_count-=1
    for index in range(len(guess_word)):
        if player_input == guess_word[index]:
            user_word_format[index] = guess_word[index]
    if player_input not in letters_played and player_input not in guess_word:
        letters_played.append(player_input)

    return life_count, letters_played