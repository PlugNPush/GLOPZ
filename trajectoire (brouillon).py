import pygame
from pygame.locals import *
from function import *
import os
import platform
from math import *

def f(x):
    return a*X**2+b*X+c

def gun(x):
    x = Vo + cos(a)*t
    y = (-1/2)*g*t**2 + Vo*sin(a)*t + h
    return (x, y)
def bazooka():
    x += Vo
    y = h
    return (x, y)
def grenade():


#widths[i] = 1 + cos(pi/2)*temps[i] + width0[i] # Insérer l'équation ici
#heights[i] = (-1/2)*1*temps[i]**2 + 10*sin(pi/2)*temps[i] + height0[i] # Insérer l'équation ici

# Equation de la gravité
#widths[i] = 3*(temps[i] % 60) + width0[i]  # Insérer l'équation ici
#heights[i] = 2*(temps[i] % 60)**2 + 4*(temps[i] % 60) + height0[i] # Insérer l'équation ici

# Rectiligne
#widths[i] = 3*(temps[i] / 60) + width0[i]  # Insérer l'équation ici
#heights[i] = height0[i] # Insérer l'équation ici

# Formule qui marche pas mais saute
#widths[i] = exp(temps[i] / 60) + width0[i] # Insérer l'équation ici
#heights[i] = (1/60)*1*temps[i]**2 - 5*temps[i] + height0[i] # Insérer l'équation ici


#widths[i] = 50*tan((temps[i] / 100) - 59.7) + width0[i] # Insérer l'équation ici
#heights[i] = (1/200)*10*temps[i]**2 - 10*sin(pi/6)*temps[i] + height0[i] # Insérer l'équation ici

#balle fusil
#widths[i] = 800*cos(0)*(temps[i]/60) + width0[i] # Insérer l'équation ici
#heights[i] = (1/2)*30*(temps[i]/60)**2 - 800*sin(0)*(temps[i]/60) + height0[i] # Insérer l'équation ici g = 30 V0 = 800 a = 0

# la vitesse de la balle doit etre réaliste : _ralentie au début si lancer de manière parabolique
#                                             _accéléré de la pointe vers le sol#



#     ---------------  Projectile   -----------------
# Classe qui gère la balle tirer par le joueur

#from balle import *
class Balle(pygame.sprite.Sprite):

    def __init__(self, joueur):    
        super().__init__()
        self.vitesse = 17
        self.Joueur
        self.image = pygame.image.load('assets/balle.png')      # image représentant la balle la balle
        self.image = pygame.transform.scale(self.image, (50, 50))    # redimensione la balle pour que ce soit réaliste
        self.pos = self.image.get_rect()     # met l'image dans un rectangle pour la délimitation de la hitbox
        self.pos.x = joueur.pos.x + 120
        self.pos.y = joueur.pos.y + 60     # permet d'avoir les balless aux coordonées de la sortie de l'arme

    def move(self):
        self.pos.x += self.vitesse    # permet le mouvement des balles

    def remove(self):
        self.joueur.all_balles.remove(self)

        #verifie si la balle est en collision contre l'autre joueur
        if self.joueur.game.check_collision(self, self.joueur.game.all_joueurs):
            # supprime la balle
            self.remove()

        #vérifie si la balle n'est pas dans le terrain
        if self.pos.x > 1980:    #dans le cas ou la longueur de l'écran est de 1980
            # la balle est suprimé hors de l'écran
            self.remove



#  Dans le main()

from balle import Balle

#fonction pour les joueur

class Joueur(pygame.sprite.Sprite):
    def __init__(self, game)    #hitbox
        super().__init__()
        self.game = game    #hitbox
        self.santé = 50
        self.attack = 10
        self.vitesse = 7
        self.all_balles = pygame.sprite.Group()       # création du groupe de balle
        self.image = pygame.image.load('assets/joueur.png')  # image du joueur
        self.pos = self.image.get_rect()    # rectangle
        self.pos.x = 600
        self.pos.y = 400

def launch_balle(self):
    #ceci est une nouvelle instance de la classe Balle
    #balle = Balle()
    self.all_balles.add(Balle(self))

#détecte si la touche  qui permet de tirer est enclenché pour lancer la balle
if event.key == pygame.[K_v]:
    game.joueur.launch_balle()

#affiche l'ensemble des images de l'ensemble de balle
game.joueur.all_balles.draw(screen)

#récuperer les balles du joueur
for balle in game.joueur.all.balles:
    balle.move()