import pygame_module.__settings__ as settings
from pygame_module.__settings__ import color, fonts
import pygame
def pygame_init():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Jeu du pendu')
    pygame.display.set_icon(settings.icon)
    clock = pygame.time.Clock()
    return screen, clock
def main_menu(screen):
    main_title_shadow_rect = fonts['main_title_shadow'].get_rect()
    main_title_shadow_rect.center = (640//1.99, 480//3.19)
    main_title_rect = fonts['main_title'].get_rect()
    main_title_rect.center = (640//2, 480//3.2)
    screen.blit(settings.main_background_clouds,(0,0))
    screen.blit(settings.main_middleground_village,(0,0))
    screen.blit(fonts['main_title_shadow'], main_title_shadow_rect)
    screen.blit(fonts['main_title'], main_title_rect)
def main_menu_start_button(screen, hovered = False):
    main_start_button = fonts['main_button']
    if hovered:
        main_start_button = fonts['main_button_hovered']
    main_start_button_rect = main_start_button.get_rect()
    main_start_button_rect.center = (420,480//2)
    screen.blit(main_start_button, main_start_button_rect)
    return main_start_button_rect
def game_set_up_menu(screen, username_input):
    screen.blit(settings.main_dialog_box,(0,-20))

    username_input_rect = settings.return_user_input(username_input).get_rect()
    username_input_rect.bottomleft = (680//2,315)
    settings.return_user_input(username_input)
    screen.blit(settings.return_user_input(username_input),username_input_rect)
