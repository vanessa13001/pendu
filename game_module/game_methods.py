import game_module.words.manage_words as manage_words
from game_module.scores.manage_scores import load_scores, save_scores, player_id

def launch_game():
    guess_word = manage_words.get_guess_word()
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
