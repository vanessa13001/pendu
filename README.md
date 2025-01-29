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
   * concept arts/        # Contains images (backgrounds, icons, game elements)
   * font/                # Contains fonts used for text
   * graphics/            # Contains images (icones, logos)  
   * sfx/                 # Contains sound effects
 * pygamne_module\
   * _settings_py         # configuration centralizes resources like fonts, colors, sounds, and graphics
   * display.py           # Manages Pygame setup, menus, and gameplay for Hangman.
 * main.py                # Game entry point
 
+ README.md                

### Features  
The game offers several features:  

+ **Main Menu**:A menu with options to start a new game, view scores, or quit the game.
+ **Hangman Game**:The player has to guess a word by entering letters, with a limited number of lives before the character is hanged.
+ **Scores**: The player is able to view or delete all scores saved.
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
   If the player lose, the secret word will be revealed. 
   In order to save the score,  you need to press enter key.
5. **Score**
   The player can view scores or reset the scores from the score menu.

***  
   
## Project Settings  

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
2.   **Fonts**
      Fonts are loaded from the ```pygame_assets/font/ directory```. Here's an example of how a font is defined:
   ```
      def pixeled_font(font_size):  
    return pygame.font.Font(font_directory+'Pixeled English Font.ttf', int(font_size))
   ```
3. **Sound Effects**
     Sound effects are stored in the ```pygame_assets/sfx/ folder```. Example:
   ```sfx = {
    'main_menu_soundtrack' : sfx_directory+'A Singular Perversion.mp3',
    'game_soundtrack' : sfx_directory+'Lightless Dawn.mp3',
   }
   ```  

4. **Graphics**
      Images and backgrounds are stored in the ```pygame_assets/graphics/ folder.```
      Example:
      ```
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
     ```
5. **Backgrounds and Hangman**  
      The game uses different backgrounds and images of the hanging character that change based on the number of remaining lives.
      For example:
      ```
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
   ```

***  
## Running the game

### Start the game  
To start the game, run the ```main.py``` file:  

```bash
python main.py
```  

### Contributing  
This project was made by:  
+ [Vanessa Sabatier](https://github.com/vanessa13001)
+ [Jolyne Mangeot](https://github.com/jolyne-mangeot)
+ [Adeline Patenne](https://github.com/AdelinePat/) 
+ [Florence Navet](https://github.com/florence-navet)

### Licence  
This project is licensed under the MIT License.

```
The contributors have been added in the **Contributors** section at the end of the README.
You can now use this updated version for your project documentation in English!
```