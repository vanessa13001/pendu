from unidecode import unidecode
from scores.manage_scores import load_scores, save_scores
from words.manage_words import input_guess_letter

def game_loop(life_count, guess_word,user_word_format, scores_file, player):

    letters = []
    scores = load_scores('./scores/scores_file.json')
    
    while life_count >= 0 :
        # guess_letter = unidecode(input("Veuillez entrer une lettre : ").lower()[0:1])
        # if guess_letter in letters:
        #     print(f"Vous avez déjà essayé {guess_letter}")
        #     guess_letter = unidecode(input("Veuillez entrer une lettre : ").lower()[0:1])
        guess_letter = input_guess_letter(letters, user_word_format, life_count)

        letters.append(guess_letter)

        for index in range(len(guess_word)):
            if guess_letter == guess_word[index]:
                user_word_format[index] = guess_word[index]

        print(f"\033[H\033[2J", end="")
        print(' '.join(user_word_format))
        print(f"lettre(s) déjà proposée(s) {' '.join(letters)}")

        if "_" not in user_word_format:
            print("vous avez gagné !! ")
            scores[player]['points'] += 1
            scores[player]['victoires'] += 1

            break
        elif guess_letter not in guess_word and life_count > 0:
            life_count -= 1
            print(f"il vous reste {life_count} vies")

        elif "_" in user_word_format and life_count == 0:    
            print(f"vous avez perdu ! Le mot à deviner était {''.join(guess_word)}")
            life_count -= 1
            if scores[player]['points'] > 0:
                scores[player]['points'] -= 1
            else:
                scores[player]['points'] = 0
            
            scores[player]['defaites'] += 1
        
    save_scores(scores_file, scores)