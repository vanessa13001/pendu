import pygame
import game.__settings__ as settings
import game.words.manage_words as manage_words
from game.scores.manage_scores import update_scores
'''
input_expression : Handles user input for selecting game mode or typing text in the input field.

Args:
    game_mode (int): Current game mode (0 = easy, 1 = hard).
    easy_button_rect (pygame.Rect): Rectangle area for the "Easy" button.
    hard_button_rect (pygame.Rect): Rectangle area for the "Hard" button.
    mouse_position (x=int, y=int): Current position of the mouse.
    user_input (str): Current text input from the user.
    max_value (int): Maximum length allowed for user input.

    Returns:
    tuple: Updated game mode, user input, and a status string:
    - 'quit' if the user exits the game.
    - '' if no significant action is taken.
     - True if the input is confirmed (e.g., Enter key is pressed).
'''
def input_expression(game_mode, easy_button_rect, hard_button_rect, mouse_position, user_input, max_value):

    for event in pygame.event.get():
        # Handle game quit
        if event.type == pygame.QUIT:
            return game_mode, user_input, 'quit'

        # Handle mouse click on the Easy button
        if easy_button_rect.collidepoint(mouse_position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0, user_input, ''

        # Handle mouse click on the Hard button
        if hard_button_rect.collidepoint(mouse_position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 1, user_input, ''

        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Return to a previous menu or cancel
                return game_mode, user_input, False

            if event.key == pygame.K_RETURN and user_input != '':
                # Confirm the input when Enter is pressed
                return game_mode, user_input, True

            elif event.key == pygame.K_BACKSPACE and user_input != '':
                # Remove the last character when Backspace is pressed
                user_input = user_input[:-1]
                return game_mode, user_input, ''

            elif len(user_input) <= max_value:
                # Append valid characters to the user input
                if event.unicode in settings.letters or event.unicode in (" ", "-", "'"):
                    user_input += event.unicode
                    return game_mode, user_input, ''

    # Default return if no specific action occurred
    return game_mode, user_input, ''
'''
input_letter : Processes player input during the game.

Args:
    player (str): Player's name.
    player_input (str): Current letter input.
    guess_word (list[str]): Word to guess as a list of characters.
    letters_played (list[str]): List of already guessed letters.
    life_count (int): Remaining lives.
    user_word_format (list[str]): Current guessed word state.

Returns:
    tuple: (game_mode, user_input, status):
        - 'quit': User exited.
        - '': No action taken.
        - True: Input confirmed

'''
def input_letter(player, player_input, guess_word, letters_played, life_count, user_word_format):

    for event in pygame.event.get():
        # Handle game quit
        if event.type == pygame.QUIT:
            return life_count, player_input, letters_played, 'quit'

        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            # Check if the game is over (no lives or word guessed)
            if life_count == 0 or '_' not in user_word_format:
                if event.key == pygame.K_RETURN:
                    # Update scores and proceed when Enter is pressed
                    update_scores(life_count, user_word_format, player)
                    return life_count, player_input, letters_played, True

            elif event.key == pygame.K_ESCAPE:
                # Exit the current game session
                return life_count, player_input, letters_played, True

            elif event.key == pygame.K_RETURN and player_input != '_':
                # Check the guessed letter and update game state
                life_count, letters_played = manage_words.check_letter_loop(
                    player_input, guess_word, letters_played, life_count, user_word_format
                )
                # Reset player input
                player_input = '_'
                return life_count, player_input, letters_played, ''

            elif event.key == pygame.K_BACKSPACE:
                # Clear the current player input
                player_input = '_'

            else:
                # Validate and format player input
                player_input = event.unicode
                try:
                    player_input = str(player_input).upper()
                    if player_input not in settings.upper_letters:
                        player_input = '_'
                except Exception:
                    player_input = '_'

    # Default return if no specific action occurred
    return life_count, player_input, letters_played, ''