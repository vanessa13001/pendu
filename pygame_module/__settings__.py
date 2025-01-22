import pygame

color = {
    'middle_gray' : (71,65,53,255),
    'dark_gray' : (42,38,31,255),
    'light_gray' : (119,115,119,255),
    'dark_red' : (192,0,0,255),
    'white' : (255,255,255,255),
}

graphics_directory = 'pygame_assets/graphics/'
font_directory = 'pygame_assets/font/'

def pixeled_font(font_size):
    pygame.font.init()
    return pygame.font.Font(font_directory+'Pixeled English Font.ttf', font_size)
def dialog_text(dialog, font_size):
    pygame.font.init()
    return pixeled_font(int(font_size)).render(dialog, True, 'white')
fonts = {
    'main_title_shadow' : pixeled_font(112).render('Le Pendu', True, color['dark_gray']),
    'main_title' : pixeled_font(112).render('Le Pendu', True, color['dark_red']),
    'main_start_button' : pixeled_font(48).render('Jouer', True, 'white'),
    'main_start_button_hovered' : pixeled_font(48).render('Jouer', True, color['dark_red']),
    'main_score_button' : pixeled_font(48).render('Scores', True, 'white'),
    'main_score_button_hovered' : pixeled_font(48).render('Scores', True, color['dark_red']),
    'main_quit_button' : pixeled_font(48).render('Quitter', True, 'white'),
    'main_quit_button_hovered' : pixeled_font(48).render('Quitter', True, color['dark_red']),
}
graphics = {
    'icon' : pygame.image.load(graphics_directory+'icon.png'),
    'main_dialog_box' : pygame.image.load(graphics_directory+'main_fg_dialog.png'),
    'main_background_clouds' : pygame.image.load(graphics_directory+'main_bg_clouds.png'),
    'main_middleground_village' : pygame.image.load(graphics_directory+'main_mg_village.png'),
    'game_dialog_lost' : pygame.image.load(graphics_directory+'game_fg_lost.png'),
    'game_foreground_filter' : pygame.image.load(graphics_directory+'game_fg_filter.png'),
    'game_middleground_gallowstand' : pygame.image.load(graphics_directory+'game_mg_gallowstand.png'),
    'game_middleground_moon' : pygame.image.load(graphics_directory+'game_mg_moon.png'),
}
def game_background_wrong(amount_of_wrongs):
    background_library = (
        graphics_directory+'game_bg_w0.png',
        graphics_directory+'game_bg_w1.png',
        graphics_directory+'game_bg_w2.png',
        graphics_directory+'game_bg_w3.png',
        graphics_directory+'game_bg_w4.png',
        graphics_directory+'game_bg_w5.png',
        graphics_directory+'game_bg_w6.png',
        graphics_directory+'game_bg_w6.png'
    )
    return pygame.image.load(background_library[amount_of_wrongs])
def game_hangedman_wrong(amount_of_wrongs):
    hangedman_library = (
        graphics_directory+'game_mg_hang0.png',
        graphics_directory+'game_mg_hang1.png',
        graphics_directory+'game_mg_hang2.png',
        graphics_directory+'game_mg_hang3.png',
        graphics_directory+'game_mg_hang4.png',
        graphics_directory+'game_mg_hang5.png',
        graphics_directory+'game_mg_hang6.png',
        graphics_directory+'game_mg_hang7.png'
    )
    return pygame.image.load(hangedman_library[amount_of_wrongs])