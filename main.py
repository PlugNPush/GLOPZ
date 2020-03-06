import pygame
from pygame.locals import *
from function import *
import os

#toutes les coordonnées:
                                          #width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
WINDOW_X = 1920
WINDOW_Y = 1080

BACK_X = 0
BACK_Y = 0

GROUND_Y = 770

MOVE = 10 #vitesse de déplacement
choice = choice_perso()
pygame.init()

#création d'une fenetre
screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y), FULLSCREEN)

curdir = os.path.dirname(os.path.realpath(__file__))
#chargement des images
image_wall = pygame.image.load(curdir + "/images/wallpaper.png").convert()

#joueur 1
j1 = pygame.image.load(curdir + choice[0][0]).convert_alpha()
j1_flip = pygame.image.load(curdir + choice[1][0]).convert_alpha()

#joueur 2
j2 = pygame.image.load(curdir + choice[0][1]).convert_alpha()
j2_flip = pygame.image.load(curdir + choice[1][1]).convert_alpha()

pos_j1 = j1.get_rect()
pos_j2 = j2.get_rect()
heading_j1 = 1 #1 = droite; 0 = gauche
heading_j2 = 0


pos_j1 = pos_j1.move(0, GROUND_Y-1)
pos_j2 = pos_j2.move(1500, GROUND_Y-30)

#placement des images
screen.blit(image_wall, (BACK_X, BACK_Y))
screen.blit(j1, pos_j1)
screen.blit(j2, pos_j2)

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

    if keys[K_LALT] and keys[K_F4]:
        game = False

    if keys[K_s]:
        pos_j1 = pos_j1.move(0, MOVE)

    if keys[K_w]:
        pos_j1 = pos_j1.move(0, -MOVE)
    else:
        pos_j1 = pos_j1.move(0, MOVE)

    if keys[K_d]:
        pos_j1 = pos_j1.move(MOVE, 0)
        heading_j1 = 0

    if keys[K_a]:
        pos_j1 = pos_j1.move(-MOVE, 0)
        heading_j1 = 1
    



    if keys[K_DOWN]:
        pos_j2 = pos_j2.move(0, MOVE)

    if keys[K_UP]:
        pos_j2 = pos_j2.move(0, -MOVE)
    else:
        pos_j2 = pos_j2.move(0, MOVE)

    if keys[K_RIGHT]:
        pos_j2 = pos_j2.move(MOVE, 0)
        heading_j2 = 0

    if keys[K_LEFT]:
        pos_j2 = pos_j2.move(-MOVE, 0)
        heading_j2 = 1




    if pos_j1.y >= GROUND_Y:
        pos_j1.y = GROUND_Y-1

    if pos_j1.y <= 0:
        pos_j1 = pos_j1.move(0, MOVE)

    if pos_j1.x <= 0:
        pos_j1 = pos_j1.move(MOVE, 0)

    if pos_j1.x >= WINDOW_X-110:
        pos_j1 = pos_j1.move(-MOVE, 0)
    


    if pos_j2.y >= GROUND_Y-29:
        pos_j2.y = GROUND_Y-30

    if pos_j2.y <= 0:
        pos_j2 = pos_j2.move(0, MOVE)

    if pos_j2.x <= 0:
        pos_j2 = pos_j2.move(MOVE, 0)

    if pos_j2.x >= WINDOW_X-110:
        pos_j2 = pos_j2.move(-MOVE, 0)




    #recollage des éléments
    screen.blit(image_wall, (BACK_X, BACK_Y))
    if heading_j1 == 1:
        screen.blit(j1, pos_j1)
    else:
        screen.blit(j1_flip, pos_j1)
    



    if heading_j2 == 1:
        screen.blit(j2, pos_j2)
    else:
        screen.blit(j2_flip, pos_j2)




    #raffraichissement
    
    pygame.display.flip()

    pygame.time.delay(16)
pygame.quit()
