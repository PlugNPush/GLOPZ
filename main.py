import pygame
from pygame.locals import *
from function import *
import os

 #toutes les coordonnées:

WINDOW_X = 1000
WINDOW_Y = 600

BACK_X = 0
BACK_Y = -400

GROUND_Y = 360



pygame.init()


#création d'une fenetre
screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

curdir = os.path.dirname(os.path.realpath(__file__))
#chargement des images
image_wall = pygame.image.load(curdir + "/images/wallpaper.png").convert()
perso = pygame.image.load(curdir + "/images/sakuya.png").convert_alpha()
perso_flip = pygame.image.load(curdir + "/images/sakuya_flip.png").convert_alpha()

pos_perso = perso.get_rect()
heading = 1 #1 = droite; 0 = gauche


pos_perso = pos_perso.move(0, GROUND_Y-1)


#placement des images
screen.blit(image_wall, (BACK_X, BACK_Y))
screen.blit(perso, pos_perso)

#raffraichissement de l'écran
pygame.display.flip()

#fréquence de répétition des touches
pygame.key.set_repeat(1, 10)

#boucle en attente d'évènement
game = True
while game:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            game = False

    if keys[K_DOWN]:
        pos_perso = pos_perso.move(0, 5)

    if keys[K_UP]:
        pos_perso = pos_perso.move(0, -5)
    else:
        pos_perso = pos_perso.move(0, 5)

    if keys[K_RIGHT]:
        pos_perso = pos_perso.move(5, 0)
        heading = 0

    if keys[K_LEFT]:
        pos_perso = pos_perso.move(-5, 0)
        heading = 1

    if pos_perso.y >= GROUND_Y:
        pos_perso.y = GROUND_Y-1

    if pos_perso.y <= 0:
        pos_perso = pos_perso.move(0, 5)

    if pos_perso.x <= 0:
        pos_perso = pos_perso.move(5, 0)

    if pos_perso.x >= WINDOW_X-110:
        pos_perso = pos_perso.move(-5, 0)

    #recollage des éléments
    screen.blit(image_wall, (BACK_X, BACK_Y))
    if heading == 1:
        screen.blit(perso, pos_perso)
    else:
        screen.blit(perso_flip, pos_perso)

    #raffraichissement
    pygame.display.flip()

    pygame.time.delay(16)
pygame.quit()
