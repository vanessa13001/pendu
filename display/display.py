import display.__settings__ as settings
import game.scores.manage_scores as scores_display
from display.__settings__ import color, graphics, sfx, PIXELED_FONT, PIXELPLAY_FONT
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

''' Affiche un bouton interactif sur l'écran.

    Returns:
        pygame.Rect: Rectangle correspondant à la zone du bouton.'''

def menu_button(screen, button_id, button_x, button_y, font_size=48, hovered = False):
    button_rect = settings.render_dialog_text(font_size,PIXELED_FONT,button_id)\
        .get_rect(bottomleft=(button_x,button_y))
    if hovered:
        screen.blit(settings.render_dialog_text(font_size,PIXELED_FONT,button_id,color['dark_red']), button_rect)
    else: screen.blit(settings.render_dialog_text(font_size,PIXELED_FONT,button_id,color['white']), button_rect)
    return button_rect


''' Affiche le menu principal avec le titre et l'arrière-plan.

        screen (pygame.Surface): Surface Pygame où le menu principal sera affiché.'''

def main_menu(screen):
    screen.blit(graphics['main_background_clouds'],(0,0))
    screen.blit(graphics['main_middleground_village'],(0,0))
    main_title_rect = settings.render_dialog_text(112,PIXELED_FONT,'Le Pendu')\
        .get_rect(center=(640//2, 480//3.2))
    screen.blit(settings.pixeled_dialog_text\
                (112,'Le Pendu',color['dark_gray']), (main_title_rect[0]+2,main_title_rect[1]+2))
    screen.blit(settings.pixeled_dialog_text\
                (112,'Le Pendu',color['dark_red']), main_title_rect)
    


''' Affiche les boutons du menu principal.
hovereed : booléen indiquant si la souris survole le bouton (change l'apparence si True 

    Returns:
        dict: Dictionnaire contenant les rectangles des boutons avec leurs identifiants.'''

def main_menu_buttons(screen, start_button_hovered, score_button_hovered, words_button_hovered, quit_button_hovered):
    start_button_rect = menu_button(screen,'Jouer',350,250,48,start_button_hovered)
    score_button_rect = menu_button(screen,'Score',350,315,48,score_button_hovered)
    words_button_rect = menu_button(screen,'Mots',350,380,48,words_button_hovered)
    quit_button_rect = menu_button(screen,'Quitter',350,445,48,quit_button_hovered)
    menu_buttons = {"start" : start_button_rect,
                    "score" : score_button_rect,
                    "words" : words_button_rect,
                    "quit" : quit_button_rect}
    return menu_buttons


"""
    Calcule le nombre total de pages nécessaires pour afficher les scores.

    Returns:
        int: Nombre de pages nécessaires pour afficher les scores.
    """

def get_scores_menu_pages():
    scores = scores_display.load_scores()
    players_id = list(scores.keys())
    pages = (len(players_id)//6)+(1 if len(players_id)%6!=0 else 0)
    return pages


'''  Affiche un message indiquant qu'aucun score n'est enregistré.

        screen (pygame.Surface): Surface Pygame où afficher le message.'''

def scores_menu_blank(screen):
    screen.blit(graphics['main_background_clouds'],(0,0))
    screen.blit(graphics['main_middleground_village'],(0,0))
    blank_dialog_rect = settings.render_dialog_text(32,PIXELED_FONT,'Aucun score enregistre')\
        .get_rect(center = (320,240))
    screen.blit(settings.pixeled_dialog_text(32,'Aucun score enregistre'),blank_dialog_rect)




''' affiche le menu des scores avec les joueurs et les flèches de navigation.

        screen (pygame.Surface): surface Pygame où le menu des scores sera affiché.
        page (int): numéro de la page actuellement affichée.
        pages (int): nombre total de pages disponibles.
        left_hovered (bool): indique si la flèche gauche est survolée.
        right_hovered (bool): indique si la flèche droite est survolée.

    Returns:
        tuple: rectangles des flèches gauche et droite.'''

def scores_menu(screen,page,pages,left_hovered, right_hovered):
    screen.blit(graphics['main_background_clouds'],(0,0))
    screen.blit(graphics['main_middleground_village'],(0,0))
    scores_menu_title_rect = settings.render_dialog_text(32,PIXELED_FONT,'Menu des scores')\
        .get_rect(center = (320,60))
    screen.blit(settings.render_dialog_text(32,PIXELED_FONT,'Menu des scores'),scores_menu_title_rect)
    scores = scores_display.load_scores()
    players_id = list(scores.keys())
    player_scores(screen,players_id,scores, page)
    left_arrow_rect, right_arrow_rect = scores_menu_arrows(screen, pages, page, left_hovered, right_hovered)
    return left_arrow_rect, right_arrow_rect



''' affiche les scores des joueurs pour une page donnée.

        screen (pygame.Surface): Surface Pygame où afficher les scores.
        players_id (list): liste des identifiants des joueurs.
        scores (dict): dictionnaire contenant les scores des joueurs.
        page (int): numéro de la page actuelle.'''
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
            player_infos_print =('Karma : ', 'Victoires : ', 'Défaites : ', 30,60,90)
            player_name_shadow = settings.render_dialog_text(36,PIXELED_FONT,players_id[player_id].capitalize(),color['dark_gray'])
            player_name = settings.render_dialog_text(36,PIXELED_FONT,players_id[player_id].capitalize(),color['dark_red'])
            player_name_rect = player_name\
                .get_rect(center=scores_coords[player_id-page*6])
            screen.blit(player_name_shadow,(player_name_rect[0]+1,player_name_rect[1]+1))
            screen.blit(player_name,player_name_rect)
            for info in range(len(player_infos)):
                player_info = settings.render_dialog_text(28, PIXELPLAY_FONT, player_infos_print[info]+\
                    str(scores[players_id[player_id]][player_infos[info]]))
                player_info_rect = player_info\
                    .get_rect(center = (scores_coords[player_id-page*6][0],\
                    scores_coords[player_id-page*6][1]+player_infos_print[info+3]))
                screen.blit(player_info,player_info_rect)
    except IndexError:
        return
    



''' affiche les flèches de navigation pour le menu des scores.

    Returns:
        tuple: Rectangles des flèches gauche et droite.'''
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




''' affiche le menu de configuration de la partie.

        screen (pygame.Surface): surface de Pygame où afficher le menu.
        user_input (str): tetxte saisi par l'utilisateur (mot ou lettre).
        game_mode (int): mode de jeu sélectionné (0 pour difficile, 1 pour facile).
        dialog (str): texte à afficher dans la boîte de dialogue.
        is_add_word (bool|str, optional): indique si un mot est ajouté avec succès, invalide, ou déjà existant.
        new_word (str, optional): mot que l'utilisateur essaie d'ajouter.

    Returns:
        tuple: rectangles des boutons "facile" et "difficile".'''
def game_set_up_menu(screen, user_input, game_mode, dialog, is_add_word=None, new_word=None):
    screen.blit(graphics['main_dialog_box'],(0,-20))
    dialog_input_rect = settings.render_dialog_text(32,PIXELED_FONT,dialog)\
        .get_rect(bottomleft = (120,300))
    user_input_rect = settings.render_dialog_text(32,PIXELED_FONT,user_input)\
        .get_rect(bottomleft = (310,300))
    easy_button_rect = settings.render_dialog_text(42,PIXELPLAY_FONT,'Facile')\
        .get_rect(center=(200,415))
    hard_button_rect = settings.render_dialog_text(42,PIXELPLAY_FONT,'Difficile')\
        .get_rect(center=(440,415))
    if new_word != None:
        add_word_dialog_rect = settings.render_dialog_text(32,PIXELPLAY_FONT,new_word+' a été ajouté').get_rect(center=(320,325))
    if is_add_word == True:
        screen.blit(settings.render_dialog_text(32,PIXELPLAY_FONT,new_word+' a ete ajoute'),add_word_dialog_rect)
    elif is_add_word == 'invalid':
        screen.blit(settings.render_dialog_text(32,PIXELPLAY_FONT,new_word+' est invalide'),add_word_dialog_rect)
    elif is_add_word == False:
        screen.blit(settings.render_dialog_text(32,PIXELPLAY_FONT,new_word+' existe deja'),add_word_dialog_rect)
    if game_mode == 0:
        screen.blit(settings.render_dialog_text(42,PIXELPLAY_FONT,'Difficile', color['white']),hard_button_rect)
        screen.blit(settings.render_dialog_text(42,PIXELPLAY_FONT,'Facile', color['dark_gray']), (easy_button_rect[0]-2, easy_button_rect[1]-2))
        screen.blit(settings.render_dialog_text(42,PIXELPLAY_FONT,'Facile', color['dark_red']), easy_button_rect)
    if game_mode == 1:
        screen.blit(settings.render_dialog_text(42,PIXELPLAY_FONT,'Facile', color['white']),easy_button_rect)
        screen.blit(settings.render_dialog_text(42,PIXELPLAY_FONT,'Difficile', color['dark_gray']), (hard_button_rect[0]-2, hard_button_rect[1]-2))
        screen.blit(settings.render_dialog_text(42,PIXELPLAY_FONT,'Difficile', color['dark_red']), hard_button_rect)
    screen.blit(settings.render_dialog_text(32,PIXELED_FONT,dialog), dialog_input_rect)
    screen.blit(settings.render_dialog_text(32,PIXELED_FONT,user_input),user_input_rect)
    return easy_button_rect, hard_button_rect




''' cela configure et affiche l'environnement de jeu en fonction de l'état de la partie.

        screen (pygame.Surface): afficher l'environnement de jeu.
        life_count (int): nombre de vies restantes.
        user_word_format (str): format du mot à deviner avec les lettres trouvées et les espaces vides.'''
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
    guess_word_rect = settings.render_dialog_text(30, PIXELPLAY_FONT)\
        .get_rect(bottomleft = (120,380))
    letters_played_rect = settings.render_dialog_text(30, PIXELPLAY_FONT)\
        .get_rect(bottomleft = (120,425))
    dialog_input_rect = settings.render_dialog_text(30)\
        .get_rect(bottomleft = (322,425))
    player_input_rect = settings.render_dialog_text(42, PIXELPLAY_FONT)\
        .get_rect(bottomleft = (515,430))
    screen.blit(settings.pixelplay_dialog_text(30, guess_word), guess_word_rect)
    screen.blit(settings.pixeled_dialog_text(30,'votre lettre :'),dialog_input_rect)
    screen.blit(settings.pixelplay_dialog_text(30,' '.join(letters_played),color['dark_red']),letters_played_rect)
    screen.blit(settings.pixelplay_dialog_text(42,player_input), player_input_rect)




''' affiche l'interface principale de jeu avec les informations de progression.

        screen (pygame.Surface): affiche l'interface.
        guess_word (str): mot en cours d'affichage avec des lettres masquées ("_").
        player_input (str): lettre actuellement entrée par le joueur.
        letters_played (list): liste des lettres déjà jouées.'''
def end_message(screen, win_or_lose, guess_word):
    end_message_list = (
        graphics['game_dialog_lost'],
        graphics['game_dialog_won'])
    screen.blit(end_message_list[win_or_lose],(0,-25))
    end_dialog_rect = settings.render_dialog_text(36)\
        .get_rect(bottomleft = (300,323))
    guess_word_rect = settings.render_dialog_text(36,PIXELPLAY_FONT, guess_word)\
        .get_rect(center = (640//2,390))
    screen.blit(settings.render_dialog_text(36,'Ent. pour continuer'), end_dialog_rect)
    screen.blit(settings.render_dialog_text(36,PIXELPLAY_FONT, guess_word), guess_word_rect)