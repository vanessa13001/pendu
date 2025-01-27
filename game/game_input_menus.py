import pygame
import display.display as display
import game.manage_input as manage_input
import game.words.manage_words as manage_words
from game.__settings__ import clock_tick
'''
    add_word_menu is straightfoward in it handling the input of the user
    to add a word to either list of playable words with buttons and
    pertinent response messages upon filtering the input
'''
def add_word_menu(screen, clock, game_mode):
    is_add_word = None
    user_input = ''
    new_word = ''
    while True:
        mouse_position = pygame.mouse.get_pos()
        display.main_menu(screen)
        easy_button_rect, hard_button_rect = display.game_set_up_menu\
            (screen, user_input, game_mode, 'Votre mot :', is_add_word, new_word)
        game_mode, user_input, correct_input = manage_input.input_expression\
            (game_mode, easy_button_rect, hard_button_rect, mouse_position, user_input,16)
        match correct_input:
            case True:
                new_word = user_input
                is_add_word = manage_words.add_word(new_word, game_mode)
                user_input = ''
            case False:
                return "main_menu"
            case 'quit':
                return "off"
        clock_tick(clock)
'''
    set_up_menu handles the players settings for the game,
    their name and the difficulty they wish to play on,
    before initiating the game's variables
'''
def set_up_menu(screen, clock, game_mode, player):
    if player != '':
        user_input = player
    else: 
        user_input = ''
    while True:
        mouse_position = pygame.mouse.get_pos()
        display.main_menu(screen)
        easy_button_rect, hard_button_rect = display.game_set_up_menu\
            (screen, user_input, game_mode, 'Votre nom :')
        game_mode, user_input, correct_input = manage_input.input_expression\
            (game_mode,easy_button_rect, hard_button_rect, mouse_position, user_input,9)
        match correct_input:
            case True:
                player = user_input
                return "in_game_menu", game_mode, player
            case False:
                return "main_menu", game_mode, player
            case 'quit':
                return "off", None, None
        clock_tick(clock)
'''
    in_game_menu displays the game's interface with a dialog box showing all
    litteral informations such as the guess word, the letters played and
    the user input. when won or lost, a final message is displayed
'''
def in_game_menu(screen, clock, game_mode, player):
    player_input = '_'
    letters_played = []
    life_count = 7
    guess_word, user_word_format = manage_words.game_words(game_mode)
    display.pygame_mixer('game_soundtrack')
    while True:
        display.game_environment(screen, life_count, user_word_format)
        if life_count == 0:
            display.end_message(screen,0,''.join(guess_word))
        
        elif '_' not in user_word_format:
            display.end_message(screen,1,''.join(guess_word))
        
        else: display.game_interface(screen, ' '.join(user_word_format), player_input, letters_played)

        life_count, player_input, letters_played, correct_input = manage_input.input_letter\
            (player, player_input, guess_word, letters_played, life_count, user_word_format)
        match correct_input:
            case True:
                return "main_menu"
            case 'quit':
                return "off"
        clock_tick(clock)