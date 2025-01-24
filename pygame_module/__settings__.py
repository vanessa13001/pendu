import pygame
pygame.font.init()
pygame.mixer.init()

color = {
    'middle_gray' : (71,65,53,255),
    'dark_gray' : (42,38,31,255),
    'light_gray' : (119,115,119,255),
    'dark_red' : (192,0,0,255),
    'white' : (255,255,255,255),
}
graphics_directory = 'pygame_assets/graphics/'
font_directory = 'pygame_assets/font/'
sfx_directory = 'pygame_assets/sfx/'

sfx = {
    'main_menu_soundtrack' : sfx_directory+'A Singular Perversion.mp3',
    'game_soundtrack' : sfx_directory+'Lightless Dawn.mp3',
}
def pixeled_font(font_size):
    return pygame.font.Font(font_directory+'Pixeled English Font.ttf', int(font_size))
def pixelplay_font(font_size):
    return pygame.font.Font(font_directory+'pixelplay.ttf', int(font_size))
def pixeled_dialog_text(font_size, dialog='', color='white'):
    return pixeled_font(int(font_size)).render(dialog, True, color)
def pixelplay_dialog_text(font_size, dialog='', color='white'):
    return pixelplay_font(int(font_size)).render(dialog, True, color)
fonts = {
    'main_start_button' : pixeled_font(48).render('Jouer', True, 'white'),
    'main_start_button_hovered' : pixeled_font(48).render('Jouer', True, color['dark_red']),
    'main_score_button' : pixeled_font(48).render('Scores', True, 'white'),
    'main_score_button_hovered' : pixeled_font(48).render('Scores', True, color['dark_red']),
    'main_quit_button' : pixeled_font(48).render('Quitter', True, 'white'),
    'main_quit_button_hovered' : pixeled_font(48).render('Quitter', True, color['dark_red']),
    'scores_delete_button' : pixeled_font(32).render('Supprimer un joueur', True, 'white'),
    'scores_delete_button_hovered' : pixeled_font(32).render('Supprimer un joueur', True, color['dark_red']),
    'scores_reset_button' : pixeled_font(32).render('Reinitialiser', True, 'white'),
    'scores_reset_button_hovered' : pixeled_font(32).render('Reinitialiser', True, color['dark_red']),
    'scores_back_button' : pixeled_font(48).render('Retour', True, 'white'),
    'scores_back_button_hovered' : pixeled_font(48).render('Retour', True, color['dark_red']),
}
graphics = {
    'icon' : pygame.image.load(graphics_directory+'icon.png'),
    'main_dialog_box' : pygame.image.load(graphics_directory+'main_fg_dialog.png'),
    'main_background_clouds' : pygame.image.load(graphics_directory+'main_bg_clouds.png'),
    'main_middleground_village' : pygame.image.load(graphics_directory+'main_mg_village.png'),
    'game_dialog_lost' : pygame.image.load(graphics_directory+'game_fg_lost.png'),
    'game_dialog_won' : pygame.image.load(graphics_directory+'game_fg_won.png'),
    'game_foreground_filter' : pygame.image.load(graphics_directory+'game_fg_filter.png'),
    'game_middleground_gallowstand' : pygame.image.load(graphics_directory+'game_mg_gallowstand.png'),
    'game_middleground_gallowstand_won' : pygame.image.load(graphics_directory+'game_mg_gallowstand_won.png'),
    'game_middleground_moon' : pygame.image.load(graphics_directory+'game_mg_moon.png'),
}
def main_arrows(left_right, hovered=False):
    arrows_sprites_list = (
        graphics_directory+'main_fg_left_arrow_white.png',
        graphics_directory+'main_fg_right_arrow_white.png',
        graphics_directory+'main_fg_left_arrow_red.png',
        graphics_directory+'main_fg_right_arrow_red.png',
    )
    if hovered:
        return pygame.image.load(arrows_sprites_list[left_right+2])
    return pygame.image.load(arrows_sprites_list[left_right])
def game_background(life_count):
    background_library = (
        graphics_directory+'game_bg_w6.png',
        graphics_directory+'game_bg_w6.png',
        graphics_directory+'game_bg_w5.png',
        graphics_directory+'game_bg_w4.png',
        graphics_directory+'game_bg_w3.png',
        graphics_directory+'game_bg_w2.png',
        graphics_directory+'game_bg_w1.png',
        graphics_directory+'game_bg_w0.png',
    )
    return pygame.image.load(background_library[life_count])
def game_hangedman(life_count):
    hangedman_library = (
        graphics_directory+'game_mg_hang7.png',
        graphics_directory+'game_mg_hang6.png',
        graphics_directory+'game_mg_hang5.png',
        graphics_directory+'game_mg_hang4.png',
        graphics_directory+'game_mg_hang3.png',
        graphics_directory+'game_mg_hang2.png',
        graphics_directory+'game_mg_hang1.png',
        graphics_directory+'game_mg_hang0.png',
    )
    return pygame.image.load(hangedman_library[life_count])