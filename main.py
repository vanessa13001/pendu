import pygame
import pygame_module.display as pygame_display
import terminal_module.display as terminal_display
import __settings__ as settings
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
        game_in_main_menu = True
        game_started = False
        start_button_hovered = False
        score_button_hovered = False
        quit_button_hovered = False
        username_input = ''
        player_input = ''
        while True:
            mouse_position = pygame.mouse.get_pos()
            if game_in_main_menu:
                pygame_display.main_menu(screen)
                start_button_rect = pygame_display.main_menu_button(screen,0,260,start_button_hovered)
                score_button_rect = pygame_display.main_menu_button(screen,1,330,score_button_hovered)
                quit_button_rect = pygame_display.main_menu_button(screen,2,400,quit_button_hovered)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        off()
                        return
                    if start_button_rect.collidepoint(mouse_position):
                        start_button_hovered = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            game_in_main_menu = False
                            game_set_up_menu = True
                    else: start_button_hovered = False
                    if score_button_rect.collidepoint(mouse_position):
                        score_button_hovered = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pass
                    else: score_button_hovered = False
                    if quit_button_rect.collidepoint(mouse_position):
                        quit_button_hovered = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            off()
                            return
                    else: quit_button_hovered = False
            elif game_set_up_menu:
                pygame_display.main_menu(screen)
                pygame_display.game_set_up_menu(screen, username_input)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        off()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and username_input != '':
                            player_name = username_input
                            wrong = 0
                            game_set_up_menu = False
                            game_started = True
                        elif event.key == pygame.K_BACKSPACE and username_input != '':
                            username_input = username_input[:-1]
                        elif len(username_input) <= 15:
                            username_input += event.unicode
                    
            elif game_started:
                pygame_display.game_environment(screen, wrong)
                if wrong == 7:
                    pygame_display.end_message(screen, 1)
                else: pygame_display.game_interface(screen, player_input)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        off()
                        return
                    if event.type == pygame.KEYDOWN:
                        if wrong == 7:
                            if event.key == pygame.K_RETURN:
                                game_started = False
                                game_in_main_menu = True
                        elif event.key == pygame.K_ESCAPE:
                            game_started = False
                            game_in_main_menu = True
                        elif event.key == pygame.K_RETURN and player_input != "":
                            wrong+=1
                            player_input = ''
                        elif event.key == pygame.K_BACKSPACE and player_input != '':
                            player_input = player_input[:-1]
                        elif len(player_input)<1:
                            player_input += event.unicode
                            try:
                                player_input = str(player_input).upper()
                                if player_input not in settings.upper_letters:
                                    player_input = ''
                            except Exception: player_input = ''
                
            else:
                off()
                return
            pygame.display.update()
            clock.tick(60)
    except KeyboardInterrupt:
        off()
    except pygame.error:
        off()

main()