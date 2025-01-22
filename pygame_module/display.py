import pygame_module.__settings__ as settings
from pygame_module.__settings__ import color, fonts, graphics
import pygame
def pygame_init():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Jeu du pendu')
    pygame.display.set_icon(graphics['icon'])
    clock = pygame.time.Clock()
    return screen, clock
def main_menu(screen):
    main_title_shadow_rect = fonts['main_title_shadow'].get_rect()
    main_title_shadow_rect.center = (640//1.99, 480//3.19)
    main_title_rect = fonts['main_title'].get_rect()
    main_title_rect.center = (640//2, 480//3.2)
    screen.blit(graphics['main_background_clouds'],(0,0))
    screen.blit(graphics['main_middleground_village'],(0,0))
    screen.blit(fonts['main_title_shadow'], main_title_shadow_rect)
    screen.blit(fonts['main_title'], main_title_rect)
def main_menu_button(screen, button_id, button_y, hovered = False):
    button_list = ('main_start_button', 'main_score_button', 'main_quit_button')
    main_menu_button = fonts[button_list[button_id]]
    if hovered:
        main_menu_button = fonts[button_list[button_id]+'_hovered']
    main_menu_button_rect = main_menu_button.get_rect()
    main_menu_button_rect.bottomleft = (380, button_y)
    screen.blit(main_menu_button, main_menu_button_rect)
    return main_menu_button_rect
def game_set_up_menu(screen, username_input):
    screen.blit(graphics['main_dialog_box'],(0,-20))
    dialog_input_rect = settings.dialog_text('Votre nom :',32).get_rect()
    dialog_input_rect.bottomleft = (120,320)
    username_input_rect = settings.dialog_text(username_input,32).get_rect()
    username_input_rect.bottomleft = (310,320)
    screen.blit(settings.dialog_text('Votre nom :',32), dialog_input_rect)
    screen.blit(settings.dialog_text(username_input,32),username_input_rect)
def game_environment(screen,wrong):
    screen.blit(settings.game_background_wrong(wrong),(0,0))
    if wrong < 3:
        screen.blit(graphics['game_middleground_moon'],(0,0))
    screen.blit(graphics['game_middleground_gallowstand'],(0,0))
    screen.blit(settings.game_hangedman_wrong(wrong),(0,0))
    if wrong > 3:
        screen.blit(graphics['game_foreground_filter'],(0,0))
def game_interface(screen, player_input):
    screen.blit(graphics['main_dialog_box'],(0,60))
    player_input_rect = settings.dialog_text(player_input,48).get_rect()
    player_input_rect.bottomleft = (510,430)
    screen.blit(settings.dialog_text(player_input,48), player_input_rect)
def end_message(screen, win_or_lose):
    end_message_list = (
        graphics['game_dialog_lost'],
        graphics['game_dialog_lost'])
    screen.blit(end_message_list[win_or_lose],(0,-25))
    end_dialog_rect = settings.dialog_text('Ent. pour continuer',32).get_rect()
    end_dialog_rect.bottomleft = (320,320)
    screen.blit(settings.dialog_text('Ent. pour continuer',32), end_dialog_rect)