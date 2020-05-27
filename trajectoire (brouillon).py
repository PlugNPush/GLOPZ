import pygame
from pygame.locals import *
from function import *
import os
import platform
from math import *

def f(x):
    return a*X**2+b*X+c

# la vitesse de la balle doit etre réaliste : _ralentie au début si lancer de manière parabolique
#                                             _accéléré de la pointe vers le sol#



#     ---------------  Projectile   -----------------
class Projectile(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png') #la balle
        self.rect = self.image.get_rect() #met l'image dans un rectangle


#  Dans le main()

from projectile import Projectile

#fonction pour les joueur

class Player(pygame.sprite.Sprite):
    super().__init__()
    self.health = 100
    self.max_health = 100
    self.attack = 10
    self.velocity = 5
    self.all_projectiles = pygame.sprite.Groupe()
    self.image = pygame.image.load('assets/player.png')# image du joueur
    self.rect = self.image.get_rect()
    self.rect.x = 400
    self.rect.y = 500

def launch_projectile(self):
    #creer une nouvelle instance de la classe Projectile
    #projectile = Projectile()
    self.all_projectiles.add(Projectile())

# on modifie dans la fonction qui s'occupe de faire ne sorte que le jouer tire en appuyant sur espace



