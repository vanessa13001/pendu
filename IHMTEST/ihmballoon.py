import pygame


pygame.init()

res = (640, 480)

"""
# Commentaires sur les événements
Quit : fermeture ou alt+F4
KEYDOWN : Touche du clavier enfoncée - #event.key - événement propre à chaque touche du clavier
KEYUP : Touche du clavier relâchée - #event.key
MOUSEBUTTONDOWN : Bouton de la souris appuyé - #event.pos (tuple de deux valeurs au moment du clic de la souris)
MOUSEBUTTONUP : Bouton de la souris relâché - idem que down, et event.button (qui prendra une valeur différente selon le bouton appuyé)
MOUSEMOTION : Mouvement de la souris
"""

"""
Dictionnaire pygame.key.get_pressed()
1 pour appuyé
0 pour relaché
"""

"""
Attributs : - points de vie
                - compétences
                - Armes
Méthodes :  - se déplacer
                    - Etre bloquer

couper son jeu en différentes scènes :(chaque scène est un objet) - chaque scène auront des caractèristiques communes et propres à chacunes d'elles.
- Menu
- Niveau
- Boss

Ex: une class scène et de la faire hériter à chacune des scène (menu, level 1) qu'on souhaite avoir
"""

# Paramètre de la fenêtre, retourne aussi un objet surface
screen = pygame.display.set_mode(res)

# Chargement de l'image
<<<<<<< HEAD
image = pygame.image.load('3.png').convert()
=======
image = pygame.image.load('./IHMTEST/2.png').convert()
>>>>>>> f6d1b0f20dbf930c97f077eaf873ba33bd05cf4c

# Position initiale de l'image
x = 0
y = 0

clock = pygame.time.Clock()

running = True

while running:
    # Remplir l'écran avec une couleur noire avant de redessiner l'image
    screen.fill((0, 0, 0))  # Fond noir

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Si la fenêtre est fermée, on arrête la boucle

    # Vérifier si une touche a été enfoncée
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 1  # Déplacer l'image à gauche
    if pressed[pygame.K_RIGHT]:
        x += 1  # Déplacer l'image à droite
    if pressed[pygame.K_UP]:
        y -= 1  # Déplacer l'image vers le haut
    if pressed[pygame.K_DOWN]:
        y += 1  # Déplacer l'image vers le bas

    # Affichage de l'image à la nouvelle position (x, y)
    screen.blit(image, (x, y))

    # Mise à jour de l'affichage
    pygame.display.flip()
    clock.tick(60) #60frames par secondes

pygame.quit()
