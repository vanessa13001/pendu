import pygame
import pygame_module.display as pygame_display
import game_module.game_methods as game_methods
import game_module.scores.manage_scores as manage_scores
import game_module.words.manage_words as manage_words
import game_module.display as terminal_display
import __settings__ as settings
from __settings__ import hovered
'''
main
'''
def off():
    terminal_display.clear_print()
    pygame.quit()
    exit()

def main():
    screen, clock = pygame_display.pygame_init()
    try:

        game_mode = 0
        user_input = ''
        player=''

        pygame_display.pygame_mixer('main_menu_soundtrack')
        game_menu = "main_menu"

        while True:
            mouse_position = pygame.mouse.get_pos()
            
            match game_menu:
                case "main_menu":
                    pygame_display.main_menu(screen)
                    menu_buttons = pygame_display.main_menu_buttons(screen,\
                        hovered["start_button"], hovered["score_button"],\
                        hovered["words_button"], hovered["quit_button"])

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            off()
                            return
                        
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                off()
                                return
                            if event.key == pygame.K_RETURN:
                                if player != '':
                                    user_input = player
                                game_menu = "set_up_menu"

                        if menu_buttons["start"].collidepoint(mouse_position):
                            hovered["start_button"] = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if player != '':
                                    user_input = player
                                game_menu = "set_up_menu"
                        else: hovered["start_button"] = False

                        if menu_buttons["score"].collidepoint(mouse_position):
                            hovered["score_button"] = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                page = 0
                                game_menu = "scores_menu"
                        else: hovered["score_button"] = False

                        if menu_buttons["words"].collidepoint(mouse_position):
                            hovered["words_button"] = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                is_add_word = None
                                user_input = ''
                                new_word = ''
                                game_menu = "add_word_menu"
                        else: hovered["words_button"] = False

                        if menu_buttons["quit"].collidepoint(mouse_position):
                            hovered["quit_button"] = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                off()
                                return
                        else: hovered["quit_button"] = False
                case "scores_menu":        
                    pages = int(pygame_display.get_scores_menu_pages())
                    if pages == 0:
                        pygame_display.scores_menu_blank(screen)
                    else: 
                        left_arrow_rect, right_arrow_rect = \
                            pygame_display.scores_menu(screen, page, pages, hovered["left"], hovered["right"])
                        reset_button_rect = pygame_display.menu_button(screen,'Reinitialiser',25,460,32,hovered["reset_button"])
                    back_button_rect = pygame_display.menu_button(screen,'Retour',460,465,48,hovered["back_button"])
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            off()
                            return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                game_menu = "main_menu"
                            elif event.key == pygame.K_RIGHT:
                                if page < pages-1:
                                    page+=1
                            elif event.key == pygame.K_LEFT:
                                if page > 0:
                                    page-=1

                        if back_button_rect.collidepoint(mouse_position):
                            hovered["back_button"] = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_menu = "main_menu"
                        else: hovered["back_button"] = False
                        if pages!= 0:
                            if reset_button_rect.collidepoint(mouse_position):
                                hovered["reset_button"] = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    manage_scores.erase_all_record()
                            else: hovered["reset_button"] = False
                            if left_arrow_rect.collidepoint(mouse_position):
                                hovered["left"] = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if page > 0:
                                        page-=1
                            else: hovered["left"] = False
                            if right_arrow_rect.collidepoint(mouse_position):
                                hovered["right"] = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if page < pages-1:
                                        page+=1
                            else: hovered["right"] = False
                case "add_word_menu":
                    pygame_display.main_menu(screen)
                    easy_button_rect, hard_button_rect = \
                        pygame_display.game_set_up_menu(screen, user_input, game_mode, 'Votre mot :', is_add_word, new_word)
                    game_mode, user_input, correct_input = game_methods.input_expression\
                        (game_mode, easy_button_rect, hard_button_rect, mouse_position, user_input,16)
                    match correct_input:
                        case True:
                            new_word = user_input
                            is_add_word = manage_words.add_word(new_word, game_mode)
                            user_input = ''
                        case False:
                            user_input = ''
                            game_menu = "main_menu"
                        case 'quit':
                            off()
                            return
                case "set_up_menu":
                    pygame_display.main_menu(screen)
                    easy_button_rect, hard_button_rect = pygame_display.game_set_up_menu(screen, user_input, game_mode, 'Votre nom :')
                    game_mode, user_input, correct_input = game_methods.input_expression\
                        (game_mode,easy_button_rect, hard_button_rect, mouse_position, user_input,9)
                    match correct_input:
                        case True:
                            player = user_input
                            user_input = ''
                            player_input = '_'
                            letters_played = []
                            life_count = 7
                            guess_word, user_word_format = game_methods.launch_game(game_mode)
                            pygame_display.pygame_mixer('game_soundtrack')         
                            game_menu = "game_on"
                        case False:
                            user_input = ''
                            game_menu = "main_menu"
                        case 'quit':
                            off()
                            return
                case "game_on":
                    pygame_display.game_environment(screen, life_count, user_word_format)
                    if life_count == 0:
                        pygame_display.end_message(screen,0,''.join(guess_word))
                    elif '_' not in user_word_format:
                        pygame_display.end_message(screen,1,''.join(guess_word))
                    else: pygame_display.game_interface(screen, ' '.join(user_word_format), player_input, letters_played)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            off()
                            return
                        if event.type == pygame.KEYDOWN:
                            if life_count == 0 or '_' not in user_word_format:
                                if event.key == pygame.K_RETURN:
                                    game_methods.update_scores(life_count,user_word_format,player)
                                    pygame_display.pygame_mixer('main_menu_soundtrack')
                                    game_menu = "main_menu"
                            elif event.key == pygame.K_ESCAPE:
                                pygame_display.pygame_mixer('main_menu_soundtrack')
                                game_menu = "main_menu"
                            elif event.key == pygame.K_RETURN and player_input != '_':
                                life_count = game_methods.game_loop(player_input, guess_word, letters_played, life_count, user_word_format)
                            elif event.key == pygame.K_BACKSPACE:
                                player_input = '_'
                            else:
                                player_input = event.unicode
                                try:
                                    player_input = str(player_input).upper()
                                    if player_input not in settings.upper_letters:
                                        player_input = '_'
                                except Exception: player_input = '_'
                case _:
                    off()
                    return
                
            pygame.display.update()
            clock.tick(45)

    except KeyboardInterrupt:
        off()
    except pygame.error:
        off()

main()