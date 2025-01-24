import pygame
import pygame_module.display as pygame_display
import game_module.game_methods as game_methods
import game_module.scores.manage_scores as manage_scores
import game_module.display as terminal_display
import __settings__ as settings
'''
main
'''
def off():
    terminal_display.clear_print()
    pygame.quit()
    exit()

def display_main_menu(screen, start_button_hovered, score_button_hovered, quit_button_hovered):
    start_button_rect = pygame_display.main_menu_button(screen,0,260,start_button_hovered)
    score_button_rect = pygame_display.main_menu_button(screen,1,330,score_button_hovered)
    quit_button_rect = pygame_display.main_menu_button(screen,2,400,quit_button_hovered)
    menu_buttons = {"start" : start_button_rect,
                    "score" : score_button_rect,
                    "quit" : quit_button_rect}
    return menu_buttons


def main():
    screen, clock = pygame_display.pygame_init()
    try:

        start_button_hovered = False
        score_button_hovered = False
        quit_button_hovered = False
        reset_button_hovered = False
        back_button_hovered = False
        left_hovered = False
        right_hovered = False
        game_mode = 0
        username_input = ''
        player_input = '_'
        page = 0

        pygame_display.pygame_mixer('main_menu_soundtrack')
        game_menu = "main_menu" # can be "game_on" , "set_up_menu", "scores_menu"

        while True:
            mouse_position = pygame.mouse.get_pos()
            
            match game_menu:
                case "main_menu":
                    pygame_display.main_menu(screen)
                    
                    menu_button = display_main_menu(screen, start_button_hovered, score_button_hovered, quit_button_hovered)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            off()
                            return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                game_menu = "set_up_menu"
                        if menu_button["start"].collidepoint(mouse_position):
                            start_button_hovered = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_menu = "set_up_menu"
                        else: start_button_hovered = False
                        if menu_button["score"].collidepoint(mouse_position):
                            score_button_hovered = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_menu = "scores_menu"               
                        else: score_button_hovered = False
                        if menu_button["quit"].collidepoint(mouse_position):
                            quit_button_hovered = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                off()
                                return
                        else: quit_button_hovered = False
                case "scores_menu":        
                    pages = int(pygame_display.get_scores_menu_pages())
                    if pages == 0:
                        pygame_display.scores_menu_blank(screen)
                    else: 
                        left_arrow_rect, right_arrow_rect = pygame_display.scores_menu(screen, page, pages,left_hovered, right_hovered)
                        reset_button_rect = pygame_display.scores_menu_buttons(screen,1,25,reset_button_hovered)
                    back_button_rect = pygame_display.scores_menu_buttons(screen,2,460,back_button_hovered)
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
                            back_button_hovered = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_menu = "main_menu"
                        else: back_button_hovered = False
                        if pages!= 0:
                            if reset_button_rect.collidepoint(mouse_position):
                                reset_button_hovered = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    manage_scores.erase_all_record()
                            else: reset_button_hovered = False
                            if left_arrow_rect.collidepoint(mouse_position):
                                left_hovered = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if page > 0:
                                        page-=1
                            else: left_hovered = False
                            if right_arrow_rect.collidepoint(mouse_position):
                                right_hovered = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if page < pages-1:
                                        page+=1
                            else: right_hovered = False

                case "set_up_menu":
                    pygame_display.main_menu(screen)
                    easy_button_rect, hard_button_rect = pygame_display.game_set_up_menu(screen, username_input, game_mode)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            off()
                            return
                        if easy_button_rect.collidepoint(mouse_position):
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_mode = 0
                        if hard_button_rect.collidepoint(mouse_position):
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_mode = 1
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN and username_input != '':
                                player = username_input
                                life_count = 7
                                letters_played = []
                                guess_word, user_word_format = game_methods.launch_game(game_mode)
                                pygame_display.pygame_mixer('game_soundtrack')
                                game_menu = "game_on"
                            elif event.key == pygame.K_BACKSPACE and username_input != '':
                                username_input = username_input[:-1]
                            elif len(username_input) <= 9:
                                if event.unicode in settings.letters:
                                    username_input += event.unicode
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
                                if player_input not in guess_word and player_input not in letters_played:
                                    life_count-=1
                                for index in range(len(guess_word)):
                                    if player_input == guess_word[index]:
                                        user_word_format[index] = guess_word[index]
                                if player_input not in letters_played and player_input not in guess_word:
                                    letters_played.append(player_input)
                                player_input = '_'
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