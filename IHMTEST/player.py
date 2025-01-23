import pygame

class Player:
    def __init__(self, x, y):
        # Charger l'image du joueur
        self.image = pygame.image.load('3.png').convert_alpha()  # Utilisez .convert_alpha() pour les images avec transparence

        # Définir un rectangle pour la position et les collisions
        self.rect = self.image.get_rect(topleft=(x, y))

        # Vitesse et vecteur de déplacement
        self.speed = 5
        self.velocity = [0, 0]  # [vx, vy]

    # Méthode pour déplacer le joueur
    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    # Méthode pour dessiner le joueur sur l'écran
    def draw(self, screen):
        screen.blit(self.image, self.rect)
