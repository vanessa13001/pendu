import pygame
from game.game_main_menus import main_menu, scores_menu
from game.game_input_menus import add_word_menu, set_up_menu, in_game_menu
from game.__settings__ import game_init, game_off
'''
    define main as a hub for all menus to interact with each other
    each menu has its own while true loop and updates the display
'''
def main():
    try:
        #establish settings variables for game difficulty and inputs
        screen, clock = game_init()
        game_mode = 0
        player=''
        game_menu = "main_menu"

        while True:
            match game_menu:

                case "main_menu":
                    game_menu = main_menu(screen, clock)

                case "scores_menu":
                    game_menu = scores_menu(screen, clock)

                case "add_word_menu":
                    game_menu = add_word_menu(screen, clock, game_mode)

                case "set_up_menu":
                    game_menu, game_mode, player = set_up_menu(screen, clock, game_mode, player)

                case "in_game_menu":
                    game_menu = in_game_menu(screen, clock, game_mode, player)

                case "off" | _:
                    game_off()
                    break
    except KeyboardInterrupt:
        game_off()
    except pygame.error:
        game_off()

main()