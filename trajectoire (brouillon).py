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


# la vitesse de la balle doit etre réaliste : _ralentie au début si lancer de manière parabolique
#                                             _accéléré de la pointe vers le sol#



#     ---------------  Projectile   -----------------
# définie la classe qui va gerer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):    
        super().__init__()
        self.velocity = 5
        self.player
        self.image = pygame.image.load('assets/projectile.png') #la balle
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect() #met l'image dans un rectangle
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 60     #permet d'avoir les projectiles au plus proches des joueurs

    def move(self):
        self.rect.x += self.velocity

    def remove(self):
        self.player.all_projectiles.remove(self)

        #verifie si le projectile entre en collision avec un monstre
        if self.player.game.check_collision(self, self.player.game.all_players):
            #supprimer le projectile
            self.remove()

        #vérifier si notre projectile n'est plus présent
        if self.rect.x > 1080:
            #suprimer le projectile (en dehors de l'écran)
            self.remove



#  Dans le main()

from projectile import Projectile

#fonction pour les joueur

class Player(pygame.sprite.Sprite):
    def __init__(self, game)    #hitbox
        super().__init__()
        self.game = game    #hitbox
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')# image du joueur
        self.rect = self.image.get_rect() # rectangle
        self.rect.x = 400
        self.rect.y = 500

def launch_projectile(self):
    #creer une nouvelle instance de la classe Projectile
    #projectile = Projectile()
    self.all_projectiles.add(Projectile(self))

# on modifie dans la fonction qui s'occupe de faire ne sorte que le jouer tire en appuyant sur espace


#détecter si la touche "tirer" est enclenché pour lancer notre projectile
if event.key == pygame.K_v:
    game.player.launch_projectile()

#afficher l'ensemble des images de mon groupe de projectile
game.player.all_projectiles.draw(screen)

#récuperer les projectiles du joueur
for projectile in game.player.all.projectiles:
    projectile.move()