# Hangman Game - Pygame

This project is an implementation of the classic **Hangman** game using the **Pygame** library. The goal of the game is to guess a word by suggesting letters, while avoiding having the character being hanged.

## Requirements

To run this project, you need to have **Python** and **Pygame** installed on your machine.

### Install Pygame

You can install Pygame via `pip` if it's not already installed:

```bash
pip install pygame
```  
***  

# Projet Structure  

The project is organized as follows:  

Hangman-Game/
+ Hangman-Game/
 * pygame_assets/
 * graphics/               # Contains images (backgrounds, icons, game elements)
    * font/                # Contains fonts used for text
    * sfx/                 # Contains sound effects
 * main.py                 # Game entry point
 * settings.py             # Configuration file containing resources and settings
+ README.md                

### Features  
The game offers several features:  

+ **Main Menu**:A menu with options to start a new game, view scores, or quit the game.
+ **Hangman Game**:The player has to guess a word by entering letters, with a limited number of lives before the character is hanged.
+ **Scores**: Ability to view and delete player scores.
+ **Background Music**:Background music for both the main menu and during gameplay.
+ **Visual Effects**: Backgrounds, hanging character, dialogues, and other graphical elements to make the game more interactive.

## How it works 
1. **Main Menu**
   When the game starts, a main menu appears with several buttons:
   + **Play**: Starts a new Hangman game.
   + **Score**s: Displays the saved player scores.  
   + **Quit**: Exits the game.
     
3. **Hangman Game**
   During the game, the player must guess a word by suggesting letters. Each wrong guess results in the hanging character moving forward until the player runs out of lives      or successfully guesses the word.  
   The background and the hanging character change based on the number of remaining lives.  
5. **Score**
   The player can view scores, delete a player, or reset the scores from the score menu.
   ```  
   setting.py  
   ```  
   The ```settings.py``` file contains resources and configurations used in the game. Here's an overview of its contents:
   
   1. **Colors**
      The colors used in the game are defined as RGBA tuples. Here are some examples:
      ```
      color = {  
    'middle_gray' : (71,65,53,255),  
    'dark_gray' : (42,38,31,255),  
    'light_gray' : (119,115,119,255),  
    'dark_red' : (192,0,0,255),  
    'white' : (255,255,255,255),*  

      }   
   ```
   2.**Fonts**
      Fonts are loaded from the ```pygame_assets/font/ directory```. Here's an example of how a font is defined:
      def pixeled_font(font_size):  
    return pygame.font.Font(font_directory+'Pixeled English Font.ttf', int(font_size))


      

   
   







  

