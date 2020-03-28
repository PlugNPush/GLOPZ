import pygame
from pygame.locals import *
from function import *
import os
import platform
#toutes les coordonnées:

pygame.init()

width, height = int(pygame.display.Info().current_w), int(pygame.display.Info().current_h)
WINDOW_X = width
WINDOW_Y = height

BACK_X = 0
BACK_Y = 0

GROUND_Y = int((900 / 1080) * height)
COEF_UP = 1.1
COEF_DOWN = 1.1

UP_MOVE = 30 #vitesse de déplacement
SIDE_MOVE = 10
choice = choice_perso()

isMac = platform.system() == "Darwin"

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
jump_j1 = True
#jump_j1_count = 0
jump_j2 = True
#jump_j2_count = 0
coef_jump_j1 = float(1)
coef_jump_j2 = float(1)
pass_j1 = True
pass_j2 = True

pos_j1 = pos_j1.move(int((0 / 1920) * width), int(GROUND_Y-((30 / 1080) * height)))
pos_j2 = pos_j2.move(int((1500 / 1920) * width), int(GROUND_Y-((30 / 1080) * height)))

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

    
    if keys[K_s] if isMac else keys[K_s]:
        pos_j1 = pos_j1.move(0, UP_MOVE)

    
    if keys[K_z] if isMac else keys[K_w]:
        if jump_j1 == True :
            pos_j1 = pos_j1.move(0, -coef_jump_j1*UP_MOVE)
            #jump_j1_count += 1
            coef_jump_j1 = coef_jump_j1/COEF_UP

        elif pos_j1.y < int(GROUND_Y-((30 / 1080) * height)) :
            if pass_j1 == True :
                coef_jump_j1 = 0.1
                pass_j1 = False

            pos_j1 = pos_j1.move(0, coef_jump_j1*UP_MOVE)
            #jump_j1_count += -1
            coef_jump_j1 = coef_jump_j1*COEF_DOWN
    
    elif pos_j1.y < int(GROUND_Y-((30 / 1080) * height)) :
        if pass_j1 == True :
            coef_jump_j1 = 0.1
            pass_j1 = False

        pos_j1 = pos_j1.move(0, coef_jump_j1*UP_MOVE)
        #jump_j1_count += -1
        coef_jump_j1 = coef_jump_j1*COEF_DOWN
        jump_j1 = False

    if keys[K_d] if isMac else keys[K_d]:
        pos_j1 = pos_j1.move(SIDE_MOVE, 0)
        heading_j1 = 0

    if keys[K_q] if isMac else keys[K_a]:
        pos_j1 = pos_j1.move(-SIDE_MOVE, 0)
        heading_j1 = 1
    
    if coef_jump_j1 < 0.1:
        jump_j1 = False

    if pos_j1.y == int(GROUND_Y-((30 / 1080) * height)):
        coef_jump_j1 = float(1)
        pass_j1 = True
        jump_j1 = True
    #if jump_j1_count > 20 :
    #    jump_j1 = False
    #if jump_j1_count == 0 :
    #    jump_j1 = True

    if keys[K_DOWN]:
        pos_j2 = pos_j2.move(0, UP_MOVE)

    if keys[K_UP]:
        if jump_j2 == True :
            pos_j2 = pos_j2.move(0, -coef_jump_j2*UP_MOVE)
            #jump_j2_count += 1
            coef_jump_j2 = coef_jump_j2/COEF_UP

        elif pos_j2.y < int(GROUND_Y-((30 / 1080) * height)) :
            if pass_j2 == True :
                coef_jump_j2 = 0.1
                pass_j2 = False

            pos_j2 = pos_j2.move(0, coef_jump_j2*UP_MOVE)
            #jump_j2_count += -1
            coef_jump_j2 = coef_jump_j2*COEF_DOWN
    
    elif pos_j2.y < int(GROUND_Y-((30 / 1080) * height)) :
        if pass_j2 == True :
            coef_jump_j2 = 0.1
            pass_j2 = False

        pos_j2 = pos_j2.move(0, coef_jump_j2*UP_MOVE)
        #jump_j2_count += -1
        coef_jump_j2 = coef_jump_j2*COEF_DOWN
        jump_j2 = False

    if keys[K_RIGHT]:
        pos_j2 = pos_j2.move(SIDE_MOVE, 0)
        heading_j2 = 0

    if keys[K_LEFT]:
        pos_j2 = pos_j2.move(-SIDE_MOVE, 0)
        heading_j2 = 1

    if coef_jump_j2 < 0.1:
        jump_j2 = False

    if pos_j2.y == int(GROUND_Y-((30 / 1080) * height)):
        coef_jump_j2 = float(1)
        pass_j2 = True
        jump_j2 = True


    if pos_j1.y >= int(GROUND_Y-((30 / 1080) * height)):
        pos_j1.y = int(GROUND_Y-((30 / 1080) * height))

    if pos_j1.y <= 0:
        pos_j1 = pos_j1.move(0, UP_MOVE)

    if pos_j1.x <= 0:
        pos_j1 = pos_j1.move(SIDE_MOVE, 0)

    if pos_j1.x >= WINDOW_X-110:
        pos_j1 = pos_j1.move(-SIDE_MOVE, 0)
    


    if pos_j2.y >= int(GROUND_Y-((30 / 1080) * height)):
        pos_j2.y = int(GROUND_Y-((30 / 1080) * height))

    if pos_j2.y <= 0:
        pos_j2 = pos_j2.move(0, UP_MOVE)

    if pos_j2.x <= 0:
        pos_j2 = pos_j2.move(SIDE_MOVE, 0)

    if pos_j2.x >= WINDOW_X-110:
        pos_j2 = pos_j2.move(-SIDE_MOVE, 0)




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
