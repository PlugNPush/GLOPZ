import pygame
from pygame.locals import *
from function import *
import os
import platform
from math import *

import sys, glob #on importe les modules

# taille de la fenêtre
h=600 #hauteur
l=1200 # largeur
 
screen = pygame.display.set_mode((l,h)) 
clock = pygame.time.Clock() # controle le framerate du jeu

# -------------------------    hitbox  --------------------

class Wall:
    def __init__(self, tile, x, y):
        self.image = pygame.image.load(tile).convert_alpha()                   # texture du mur
        self.position = pygame.Rect((x, y), (Largeur, Hauteur))  # rectangle

for wall in walls:
    if wall.colliderect(player.position):
         player.position = player.old_position

if self.x <= 0:
    self.x += 1



#-----------------   hitbox 1  -------------------

self.rect = self.image.get_rect(center=(self.px, self.py))


# ---------------------------------------------------------------------------------------------------------------------------
# class game
def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

#classe Joueur
def move right(self):
    #si le joueur1 n'est pas en collision avec le joueur2
    if self.game.check_collision(self, self.game.all.joueur2):
        self.pos.x += self.vitesse

def foward(self):
    #le déplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
    if not self.game.check_collision(self, self.game.all_players):
        self.pos.x -= self.vitesse
