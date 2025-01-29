import pygame
pygame.font.init()
pygame.mixer.init()
'''
    define assets directory to manage all imports
'''
GRAPHICS_DIRECTORY = 'assets/graphics/'
FONTS_DIRECTORY = 'assets/font/'
SFX_DIRECTORY = 'assets/sfx/'
''''''
PIXELPLAY_FONT = "pixelplay.ttf"
PIXELED_FONT = "Pixeled English Font.ttf"
'''
    establish dictionaries to centralize assets imports
'''
color = {
    'middle_gray' : (71,65,53,255),
    'dark_gray' : (42,38,31,255),
    'light_gray' : (119,115,119,255),
    'dark_red' : (192,0,0,255),
    'white' : (255,255,255,255),
}
''''''
hovered = {
    "start_button" : False,
    "score_button" : False,
    "words_button" : False,
    "quit_button" : False,
    "reset_button" : False,
    "back_button" : False,
    "left" : False,
    "right" : False
}
''''''
sfx = {
    'main_menu_soundtrack' : SFX_DIRECTORY+'A Singular Perversion.mp3',
    'game_soundtrack' : SFX_DIRECTORY+'Lightless Dawn.mp3',
}
''''''
graphics = {
    'icon' : pygame.image.load(GRAPHICS_DIRECTORY+'icon.png'),
    'main_dialog_box' : pygame.image.load(GRAPHICS_DIRECTORY+'main_fg_dialog.png'),
    'main_background_clouds' : pygame.image.load(GRAPHICS_DIRECTORY+'main_bg_clouds.png'),
    'main_middleground_village' : pygame.image.load(GRAPHICS_DIRECTORY+'main_mg_village.png'),
    'game_dialog_lost' : pygame.image.load(GRAPHICS_DIRECTORY+'game_fg_lost.png'),
    'game_dialog_won' : pygame.image.load(GRAPHICS_DIRECTORY+'game_fg_won.png'),
    'game_foreground_filter' : pygame.image.load(GRAPHICS_DIRECTORY+'game_fg_filter.png'),
    'game_middleground_gallowstand' : pygame.image.load(GRAPHICS_DIRECTORY+'game_mg_gallowstand.png'),
    'game_middleground_gallowstand_won' : pygame.image.load(GRAPHICS_DIRECTORY+'game_mg_gallowstand_won.png'),
    'game_middleground_moon' : pygame.image.load(GRAPHICS_DIRECTORY+'game_mg_moon.png'),
}
'''
    render all dialog with parameters
'''
def render_dialog_text(font_size, font_name=PIXELED_FONT, dialog='', color='white'):
    try:
        if font_name in [PIXELED_FONT, PIXELPLAY_FONT]:
            font = pygame.font.Font(FONTS_DIRECTORY+font_name, int(font_size))
            return font.render(dialog, True, color)
        else:
            raise Exception()
    except Exception:
            font = pygame.font.Font(FONTS_DIRECTORY+PIXELPLAY_FONT, int(font_size))
            return font.render(dialog, True, color)
'''
    render scores menu navigation arrows and return their collision
'''     
def main_arrows(left_right, hovered=False):
    arrows_sprites_list = (
        GRAPHICS_DIRECTORY+'main_fg_left_arrow_white.png',
        GRAPHICS_DIRECTORY+'main_fg_right_arrow_white.png',
        GRAPHICS_DIRECTORY+'main_fg_left_arrow_red.png',
        GRAPHICS_DIRECTORY+'main_fg_right_arrow_red.png',
    )
    if hovered:
        return pygame.image.load(arrows_sprites_list[left_right+2])
    return pygame.image.load(arrows_sprites_list[left_right])
'''
    return background asset to display images depending on life count
'''
def game_background(life_count):
    background_library = (
        GRAPHICS_DIRECTORY+'game_bg_w6.png',
        GRAPHICS_DIRECTORY+'game_bg_w6.png',
        GRAPHICS_DIRECTORY+'game_bg_w5.png',
        GRAPHICS_DIRECTORY+'game_bg_w4.png',
        GRAPHICS_DIRECTORY+'game_bg_w3.png',
        GRAPHICS_DIRECTORY+'game_bg_w2.png',
        GRAPHICS_DIRECTORY+'game_bg_w1.png',
        GRAPHICS_DIRECTORY+'game_bg_w0.png',
    )
    return pygame.image.load(background_library[life_count])
''''''
def game_hangedman(life_count):
    hangedman_library = (
        GRAPHICS_DIRECTORY+'game_mg_hang7.png',
        GRAPHICS_DIRECTORY+'game_mg_hang6.png',
        GRAPHICS_DIRECTORY+'game_mg_hang5.png',
        GRAPHICS_DIRECTORY+'game_mg_hang4.png',
        GRAPHICS_DIRECTORY+'game_mg_hang3.png',
        GRAPHICS_DIRECTORY+'game_mg_hang2.png',
        GRAPHICS_DIRECTORY+'game_mg_hang1.png',
        GRAPHICS_DIRECTORY+'game_mg_hang0.png',
    )
    return pygame.image.load(hangedman_library[life_count])