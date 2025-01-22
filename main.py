import pygame
import pygame_module.display as pygame_display
import terminal_module.display as terminal_display
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
        while True:
            mouse_position = pygame.mouse.get_pos()
            if game_in_main_menu:
                pygame_display.main_menu(screen)
                start_button_rect = pygame_display.main_menu_start_button(screen,start_button_hovered)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        off()
                        return
                    if start_button_rect.collidepoint(mouse_position):
                        start_button_hovered = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            username_input = ''
                            game_in_main_menu = False
                            game_set_up_menu = True
                    else: start_button_hovered = False
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
                            game_set_up_menu = False
                            game_in_main_menu = True
                        elif event.key == pygame.K_BACKSPACE and username_input != '':
                            username_input = username_input[:-1]
                        elif len(username_input) <= 15:
                            username_input += event.unicode
                    
            elif game_started:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        off()
                        return
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