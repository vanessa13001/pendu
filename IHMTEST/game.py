import pygame
from player import Player

"""
Collision entre deux objets : le joueur a besoin d'une HITBOX (boîte entourant le joueur) - pygame.Rect (position X, Y, largeur, hauteur).
"""

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()  # Utilisation correcte de pygame.time.Clock()
        self.player = Player(100, 100)  # Position de départ du joueur
        self.area = pygame.Rect(300, 150, 300, 300)  # Zone définie par un rectangle
        self.area_color = (255, 0, 0)  # Rouge en RGB

    # Méthode de gestion des événements
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Gestion des touches du clavier
        keys = pygame.key.get_pressed()

        # Mouvements horizontaux
        if keys[pygame.K_LEFT]:
            self.player.velocity[0] = -1  # Gauche
        elif keys[pygame.K_RIGHT]:
            self.player.velocity[0] = 1  # Droite
        else:
            self.player.velocity[0] = 0  # Pas de mouvement horizontal

        # Mouvements verticaux
        if keys[pygame.K_UP]:
            self.player.velocity[1] = -1  # Haut
        elif keys[pygame.K_DOWN]:
            self.player.velocity[1] = 1  # Bas
        else:
            self.player.velocity[1] = 0  # Pas de mouvement vertical

    # Méthode de gestion de la logique du jeu
    def update(self):
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.area_color = "blue"
        else:
            self.area_color = "red"

    # Méthode d'affichage
    def display(self):
        self.screen.fill((255, 255, 255))  # Blanc en RGB
        pygame.draw.rect(self.screen, self.area_color, self.area)  # Utilisation correcte de pygame.draw.rect
        self.player.draw(self.screen)
        pygame.display.flip()

    # Boucle de jeu
    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)  # Limitation des FPS à 60


# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((1080, 720))
game = Game(screen)
game.run()

pygame.quit()
