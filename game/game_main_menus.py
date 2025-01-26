import pygame
import display.display as display
from display.__settings__ import hovered
import game.scores.manage_scores as manage_scores
from game.__settings__ import clock_tick
'''
    main_menu covers enter and escape input to enter or quit the game,
    and buttons to acces other menus
'''
def main_menu(screen, clock):
    display.pygame_mixer('main_menu_soundtrack')
    while True:
        mouse_position = pygame.mouse.get_pos()
        display.main_menu(screen)
        menu_buttons = display.main_menu_buttons(screen,\
            hovered["start_button"], hovered["score_button"],\
            hovered["words_button"], hovered["quit_button"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "off"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "off"
                if event.key == pygame.K_RETURN:
                    return "set_up_menu"

            if menu_buttons["start"].collidepoint(mouse_position):
                hovered["start_button"] = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "set_up_menu"
            else: hovered["start_button"] = False

            if menu_buttons["score"].collidepoint(mouse_position):
                hovered["score_button"] = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "scores_menu"
            else: hovered["score_button"] = False

            if menu_buttons["words"].collidepoint(mouse_position):
                hovered["words_button"] = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "add_word_menu"
            else: hovered["words_button"] = False

            if menu_buttons["quit"].collidepoint(mouse_position):
                hovered["quit_button"] = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "off"
            else: hovered["quit_button"] = False
        clock_tick(clock)
'''
    scores_menu displays all players names and their data,
    handling multiple pages if needed with arrows buttons and inputs,
    also displaying a button to reset said data and to leave the menu
'''
def scores_menu(screen, clock):
    page = 0
    while True:
        mouse_position = pygame.mouse.get_pos()
        pages = int(display.get_scores_menu_pages())
        if pages == 0:
            display.scores_menu_blank(screen)
        else: 
            left_arrow_rect, right_arrow_rect = \
                display.scores_menu(screen, page, pages, hovered["left"], hovered["right"])
            reset_button_rect = display.menu_button(screen,'Reinitialiser',25,460,32,hovered["reset_button"])
        back_button_rect = display.menu_button(screen,'Retour',460,465,48,hovered["back_button"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "off"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "main_menu"
                elif event.key == pygame.K_RIGHT:
                    if page < pages-1:
                        page+=1
                elif event.key == pygame.K_LEFT:
                    if page > 0:
                        page-=1

            if back_button_rect.collidepoint(mouse_position):
                hovered["back_button"] = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "main_menu"
            else: hovered["back_button"] = False

            if pages!= 0:
                if reset_button_rect.collidepoint(mouse_position):
                    hovered["reset_button"] = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        manage_scores.erase_all_record()
                else: hovered["reset_button"] = False

                if left_arrow_rect.collidepoint(mouse_position):
                    hovered["left"] = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if page > 0:
                            page-=1
                else: hovered["left"] = False

                if right_arrow_rect.collidepoint(mouse_position):
                    hovered["right"] = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if page < pages-1:
                            page+=1
                else: hovered["right"] = False
        clock_tick(clock)