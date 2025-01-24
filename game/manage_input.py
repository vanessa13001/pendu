import pygame
import game.__settings__ as settings
import game.words.manage_words as manage_words
from game.scores.manage_scores import update_scores

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
                life_count, letters_played = manage_words.check_letter_loop(player_input, guess_word, letters_played, life_count, user_word_format)
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
                except Exception:
                    player_input = '_'
    return life_count, player_input, letters_played, ''

