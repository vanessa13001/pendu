import game_module.words.manage_words as manage_words
from game_module.scores.manage_scores import load_scores, save_scores, player_id

def launch_game(game_mode):
    guess_word = manage_words.get_guess_word(game_mode)
    user_word_format = manage_words.display_user_word(guess_word)
    return guess_word, user_word_format

def update_scores(life_count, user_word_format, player):
    scores = load_scores('game_module/scores/scores_file.json')
    player = str(player).lower()
    player_id(player, scores)
    if life_count == 0:
        scores[player]['losses'] +=1
        scores[player]['win_streak'] = 0
    elif '_' not in user_word_format:
        scores[player]['wins'] +=1
        scores[player]['win_streak'] +=1
    save_scores(scores)

def game_loop(player_input, guess_word, letters_played, life_count, user_word_format):
    if player_input not in guess_word and player_input not in letters_played:
        life_count-=1
    for index in range(len(guess_word)):
        if player_input == guess_word[index]:
            user_word_format[index] = guess_word[index]
    if player_input not in letters_played and player_input not in guess_word:
        letters_played.append(player_input)
    player_input = '_'