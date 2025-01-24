import pygame
import sys
import secrets
import os

# initialisation de Pygame
pygame.init()

# dimensions de la fenêtre
image = pygame.image.load('image/fond_bleu.jpg')
largeur, hauteur = 800, 500
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du pendu")

# couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
ROSE = (255, 192, 203)
MARRON = (101, 67, 33)
ORANGE = (230,97,29,255)

# police
police = pygame.font.Font('PressStart2P-Regular.ttf', 34)

# charger les mots depuis le fichier texte
def charger_mots(fichier):
    with open(fichier, 'r') as f:
        mots = f.readlines()
    return [mot.strip() for mot in mots]

mots = charger_mots('mots.txt')
mot_a_deviner = secrets.choice(mots).upper()
lettres_trouvees = ['_' for _ in mot_a_deviner]
lettres_ratees = []

# classe Bouton pour gérer les boutons
class Bouton:
    def __init__(self, image_path, position, echelle):
        if not os.path.exists(image_path):
            print(f"Erreur: L'image '{image_path}' n'a pas été trouvée.")
            pygame.quit()
            sys.exit()

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * echelle), int(self.image.get_height() * echelle)))
        self.rect = self.image.get_rect(topleft=position)
        self.position = position

    def dessiner(self, fenetre):
        fenetre.blit(self.image, self.rect.topleft)

    def est_presse(self):
        souris_x, souris_y = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()
        if self.rect.collidepoint(souris_x, souris_y) and clic[0]:
            return True
        return False

# charger les boutons de l'écran d'accueil
start_btn_path = "image/start_btn.png"
exit_btn_path = "image/exit_btn.png"

if not os.path.exists(start_btn_path):
    print(f"Erreur: Le fichier '{start_btn_path}' est introuvable.")
    pygame.quit()
    sys.exit()

if not os.path.exists(exit_btn_path):
    print(f"Erreur: Le fichier '{exit_btn_path}' est introuvable.")
    pygame.quit()
    sys.exit()

# bboutons de démarrage et de sortie
bouton_demarrer = Bouton(start_btn_path, (150, 230), 0.60)
bouton_quitter = Bouton(exit_btn_path, (430, 230), 0.60)

# fonction pour dessiner l'écran d'accueil avec un titre
def dessiner_ecran_accueil():
    image = pygame.image.load('image/nuage.jpg')
    fenetre.blit(image, (0, 0))
    resized_image = pygame.transform.scale(image, (800, 500))
    fenetre.blit(resized_image, (0, 0))

    # ajouter un titre
    titre = police.render("Jeu du Pendu", True, ORANGE)  # créer le titre
    fenetre.blit(titre, (largeur // 2 - titre.get_width() // 1.8, 90))  # pour placer le titre au centre en haut

    # dessiner les boutons
    bouton_demarrer.dessiner(fenetre)
    bouton_quitter.dessiner(fenetre)

    pygame.display.update()


''' de la ligne 97 à 150 c'est tout mon pendu qui se dessine en fonction des errreurs utilisateur '''
# fonction pour dessiner le pendu
def dessiner_pendu(erreurs):
    # hauteur et décalage horizontal
    decalage_y = 40  # déplacement de 40 pixels vers le haut
    decalage_x = 40  # déplacement de 40 pixels vers la gauche
    taille_agrandie = 1  # facteur d'agrandissement des éléments

    # base du pendu
    if erreurs >= 1:  # la base
        pygame.draw.line(fenetre, MARRON, (140 - decalage_x, 370 - decalage_y), (200 - decalage_x, 370 - decalage_y), 3)
    if erreurs >= 2:  # poteau vertical
        pygame.draw.line(fenetre, MARRON, 
                        (170 - decalage_x, 370 - decalage_y), 
                        (170 - decalage_x, 220 - decalage_y), 
                         int(3 * taille_agrandie))  # agrandir le poteau
    if erreurs >= 3:  # barre horizontale de la potence
        pygame.draw.line(fenetre, MARRON, 
                        (170 - decalage_x, 220 - decalage_y), 
                        (220 - decalage_x, 220 - decalage_y), 
                         int(3 * taille_agrandie))  # agrandir la barre horizontale
    if erreurs >= 4:  # corde
        pygame.draw.line(fenetre, MARRON, 
                        (220 - decalage_x, 220 - decalage_y), 
                        (220 - decalage_x, 240 - decalage_y), 
                         int(3 * taille_agrandie))  # agrandir la corde
    if erreurs >= 5:  # tête
        # remplir l'intérieur de la tête en rose
        pygame.draw.circle(fenetre, ROSE, (220 - decalage_x, 245 - decalage_y), int(15 * taille_agrandie))
        # bordure rouge
        pygame.draw.circle(fenetre, ROUGE, (220 - decalage_x, 245 - decalage_y), int(15 * taille_agrandie), 2)  
    if erreurs >= 6:  # corps
        pygame.draw.line(fenetre, ROUGE, 
                        (220 - decalage_x, 257 - decalage_y), 
                        (220 - decalage_x, 297 - decalage_y), 
                         int(3 * taille_agrandie))  # agrandir le corps
    if erreurs >= 7:  # bras gauche
        pygame.draw.line(fenetre, ROUGE, 
                        (220 - decalage_x, 270 - decalage_y), 
                        (205 - decalage_x, 285 - decalage_y), 
                         int(3 * taille_agrandie))  # agrandir les bras
    if erreurs >= 8:  # bras droit
        pygame.draw.line(fenetre, ROUGE, 
                        (220 - decalage_x, 270 - decalage_y), 
                        (235 - decalage_x, 285 - decalage_y), 
                         int(3 * taille_agrandie))  # agrandir les bras
    if erreurs >= 9:  # jambe gauche
        pygame.draw.line(fenetre, ROUGE, 
                        (220 - decalage_x, 297 - decalage_y), 
                        (210 - decalage_x, 325 - decalage_y), 
                         int(3 * taille_agrandie))  # agrandir les jambes
    if erreurs >= 10:  # jambe droite
        pygame.draw.line(fenetre, ROUGE, 
                        (220 - decalage_x, 297 - decalage_y), 
                        (230 - decalage_x, 325 - decalage_y), 
                         int(3 * taille_agrandie))  # agrandir les jambes



# dessiner le jeu du pendu
def dessiner_jeu():
    # Fond
    fenetre.blit(image, (0, 0))
    resized_image = pygame.transform.scale(image, (800, 500))
    fenetre.blit(resized_image, (0, 0))

    # dessiner le mot à deviner
    mot_affiche = ' '.join(lettres_trouvees)
    texte_mot = police.render(mot_affiche, True, ORANGE)
    fenetre.blit(texte_mot, (largeur // 2 - texte_mot.get_width() // 2, hauteur // 2 - texte_mot.get_height() // 2))

    # lettres ratées
    texte_ratees = police.render(' '.join(lettres_ratees), True, ORANGE)
    fenetre.blit(texte_ratees, (largeur // 2 - texte_ratees.get_width() // 2, hauteur // 2 + texte_ratees.get_height()))

    # dessiner le pendu en fonction des erreurs
    dessiner_pendu(len(lettres_ratees))

    pygame.display.flip()

# oucle principale du jeu
jeu_en_cours = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if jeu_en_cours:
            if event.type == pygame.KEYDOWN:
                lettre = event.unicode.upper()
                if lettre.isalpha() and lettre not in lettres_trouvees and lettre not in lettres_ratees:
                    if lettre in mot_a_deviner:
                        for i, l in enumerate(mot_a_deviner):
                            if l == lettre:
                                lettres_trouvees[i] = lettre
                    else:
                        lettres_ratees.append(lettre)

    if not jeu_en_cours:
        dessiner_ecran_accueil()

        if bouton_demarrer.est_presse():
            jeu_en_cours = True
            mot_a_deviner = secrets.choice(mots).upper()
            lettres_trouvees = ['_' for _ in mot_a_deviner]
            lettres_ratees = []

        if bouton_quitter.est_presse():
            pygame.quit()
            sys.exit()
    else:
        dessiner_jeu()

        if '_' not in lettres_trouvees:
            print(">>> t'es le boss que tu penses être <<<")
            jeu_en_cours = False
        elif len(lettres_ratees) >= 10:  # 10 erreurs = pendu complet
            print(f"you so bad! le mot était : {mot_a_deviner}")
            jeu_en_cours = False

    pygame.display.update()
    pygame.time.Clock().tick(60)




