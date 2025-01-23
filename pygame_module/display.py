import pygame_module.__settings__ as settings
import game_module.scores.manage_scores as scores_display
from pygame_module.__settings__ import color, fonts, graphics, sfx
import pygame
def pygame_init():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Jeu du pendu')
    pygame.display.set_icon(graphics['icon'])
    clock = pygame.time.Clock()
    return screen, clock
def pygame_mixer(music_name):
    pygame.mixer.music.load(sfx[music_name])
    pygame.mixer.music.play(-1,0,3)
def main_menu(screen):
    screen.blit(graphics['main_background_clouds'],(0,0))
    screen.blit(graphics['main_middleground_village'],(0,0))
    main_title_shadow_rect = settings.pixeled_dialog_text(112,'Le Pendu').get_rect()
    main_title_shadow_rect.center = (640//1.99, 480//3.19)
    main_title_rect = settings.pixeled_dialog_text(112,'Le Pendu').get_rect()
    main_title_rect.center = (640//2, 480//3.2)
    screen.blit(settings.pixeled_dialog_text\
                (112,'Le Pendu',color['dark_gray']), main_title_shadow_rect)
    screen.blit(settings.pixeled_dialog_text\
                (112,'Le Pendu',color['dark_red']), main_title_rect)
def main_menu_button(screen, button_id, button_y, hovered = False):
    button_list = ('main_start_button', 'main_score_button', 'main_quit_button')
    main_menu_button = fonts[button_list[button_id]]
    if hovered:
        main_menu_button = fonts[button_list[button_id]+'_hovered']
    main_menu_button_rect = main_menu_button.get_rect()
    main_menu_button_rect.bottomleft = (350, button_y)
    screen.blit(main_menu_button, main_menu_button_rect)
    return main_menu_button_rect
def get_scores_menu_pages():
    scores = scores_display.load_scores()
    players_id = list(scores.keys())
    pages = (len(players_id)//6)+(1 if len(players_id)%6!=0 else 0)
    return pages
def scores_menu_blank(screen):
    screen.blit(graphics['main_background_clouds'],(0,0))
    screen.blit(graphics['main_middleground_village'],(0,0))
    blank_dialog_rect = settings.pixeled_dialog_text(32,'Aucun score enregistre').get_rect()
    blank_dialog_rect.center = (320,240)
    screen.blit(settings.pixeled_dialog_text(32,'Aucun score enregistre'),blank_dialog_rect)
def scores_menu(screen,page,pages,left_hovered, right_hovered):
    screen.blit(graphics['main_background_clouds'],(0,0))
    screen.blit(graphics['main_middleground_village'],(0,0))
    scores_menu_title_rect = settings.pixeled_dialog_text(32, 'Menu des scores').get_rect()
    scores_menu_title_rect.center = (320,60)
    screen.blit(settings.pixeled_dialog_text(32, 'Menu des scores'),scores_menu_title_rect)
    scores = scores_display.load_scores()
    players_id = list(scores.keys())
    player_scores(screen,players_id,scores, page)
    left_arrow_rect, right_arrow_rect = scores_menu_arrows(screen, pages, page, left_hovered, right_hovered)
    return left_arrow_rect, right_arrow_rect
def player_scores(screen,players_id,scores, page):
    x =(120,320,520)
    y =(120,280)
    scores_coords =(
        (x[0],y[0]),(x[1],y[0]),(x[2],y[0]),
        (x[0],y[1]),(x[1],y[1]),(x[2],y[1]),
    )
    try:
        for player_id in range(page*6, page*6+6):
            player_infos = list(scores[players_id[player_id]].keys())
            player_infos_print =('Win streak : ', 'Victoires : ', 'Défaites : ', 30,60,90)
            player_name_rect = settings.pixeled_dialog_text(36,players_id[player_id],color['dark_red']).get_rect()
            player_name_rect.center = scores_coords[player_id-page*6]
            screen.blit(settings.pixeled_dialog_text(36,players_id[player_id],color['dark_gray']),(player_name_rect[0]+1,player_name_rect[1]+1))
            screen.blit(settings.pixeled_dialog_text(36,players_id[player_id],color['dark_red']),player_name_rect)
            for info in range(len(player_infos)):
                player_info_rect = settings.pixelplay_dialog_text(28,player_infos_print[info]+\
                    str(scores[players_id[player_id]][player_infos[info]])).get_rect()
                player_info_rect.center = (scores_coords[player_id-page*6][0],\
                    scores_coords[player_id-page*6][1]+player_infos_print[info+3])
                screen.blit(settings.pixelplay_dialog_text(28,player_infos_print[info]+\
                    str(scores[players_id[player_id]][player_infos[info]])),player_info_rect)
    except IndexError:
        return
def scores_menu_buttons(screen,button_id,button_x,hovered = False):
    button_list = ('scores_delete_button', 'scores_reset_button', 'scores_back_button')
    main_menu_button = fonts[button_list[button_id]]
    if hovered:
        main_menu_button = fonts[button_list[button_id]+'_hovered']
    main_menu_button_rect = main_menu_button.get_rect()
    main_menu_button_rect.bottomleft= (button_x, 465)
    screen.blit(main_menu_button, main_menu_button_rect)
    return main_menu_button_rect
def scores_menu_arrows(screen, pages, page, left_hovered, right_hovered):
    if pages > 1 and page >= 1:
        screen.blit(settings.main_arrows(0, left_hovered),(0,0))
        left_arrow_rect = pygame.Rect(256,418,44,32)
    else : left_arrow_rect = pygame.Rect(256,418,44,32)
    if page < pages-1:
        screen.blit(settings.main_arrows(1,right_hovered),(0,0))
        right_arrow_rect = pygame.Rect(340,418,44,32)
    else : right_arrow_rect = pygame.Rect(-340,418,44,32)
    return left_arrow_rect, right_arrow_rect
def game_set_up_menu(screen, username_input):
    screen.blit(graphics['main_dialog_box'],(0,-20))
    dialog_input_rect = settings.pixeled_dialog_text(32,'Votre nom :').get_rect()
    dialog_input_rect.bottomleft = (120,320)
    username_input_rect = settings.pixeled_dialog_text(32,username_input).get_rect()
    username_input_rect.bottomleft = (310,320)
    screen.blit(settings.pixeled_dialog_text(32,'Votre nom :'), dialog_input_rect)
    screen.blit(settings.pixeled_dialog_text(32,username_input),username_input_rect)
def game_environment(screen,life_count, user_word_format):
    screen.blit(settings.game_background(life_count),(0,0))
    if life_count > 3:
        screen.blit(graphics['game_middleground_moon'],(0,0))
    if '_' not in user_word_format:
        screen.blit(graphics['game_middleground_gallowstand_won'],(0,0))
    else: screen.blit(graphics['game_middleground_gallowstand'],(0,0))
    screen.blit(settings.game_hangedman(life_count),(0,0))
    if life_count < 3:
        screen.blit(graphics['game_foreground_filter'],(0,0))
def game_interface(screen, guess_word, player_input, letters_played):
    screen.blit(graphics['main_dialog_box'],(0,60))
    guess_word_rect = settings.pixelplay_dialog_text(30).get_rect()
    guess_word_rect.bottomleft = (120,380)
    letters_played_rect = settings.pixelplay_dialog_text(30).get_rect()
    letters_played_rect.bottomleft = (120,425)
    dialog_input_rect = settings.pixeled_dialog_text(30).get_rect()
    dialog_input_rect.bottomleft = (322,425)
    player_input_rect = settings.pixelplay_dialog_text(42).get_rect()
    player_input_rect.bottomleft = (515,430)
    screen.blit(settings.pixelplay_dialog_text(30, guess_word), guess_word_rect)
    screen.blit(settings.pixeled_dialog_text(30,'votre lettre :'),dialog_input_rect)
    screen.blit(settings.pixelplay_dialog_text(30,' '.join(letters_played),color['dark_red']),letters_played_rect)
    screen.blit(settings.pixelplay_dialog_text(42,player_input), player_input_rect)
def end_message(screen, win_or_lose, guess_word):
    end_message_list = (
        graphics['game_dialog_lost'],
        graphics['game_dialog_won'])
    screen.blit(end_message_list[win_or_lose],(0,-25))
    end_dialog_rect = settings.pixeled_dialog_text(36).get_rect()
    end_dialog_rect.bottomleft = (300,323)
    guess_word_rect = settings.pixelplay_dialog_text(36, guess_word).get_rect()
    guess_word_rect.center = (640//2,390)
    screen.blit(settings.pixeled_dialog_text(36,'Ent. pour continuer'), end_dialog_rect)
    screen.blit(settings.pixelplay_dialog_text(36, guess_word), guess_word_rect)