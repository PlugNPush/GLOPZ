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

#création d'une fenetre
if platform.system() == "Linux":
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
else:
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y), FULLSCREEN)


"""
menu = True
while menu is True:
    # rectangles choix joueurs
    size = (width, height)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    blue = pygame.Color(0, 0, 255)
    green = pygame.Color(0, 255, 0)
    null = pygame.Color(0, 0, 0)
    button_player1 = pygame.Rect(500, 800, 100, 50)
    pygame.draw.rect(screen, red, button_player1)
    button_player2 = pygame.Rect(700, 800, 100, 50)
    pygame.draw.rect(screen, green, button_player2)
    button_player3 = pygame.Rect(900, 800, 100, 50)
    pygame.draw.rect(screen, blue, button_player3)
    button_player4 = pygame.Rect(1100, 800, 100, 50)
    pygame.draw.rect(screen, null, button_player4)
    pygame.display.flip()
    # Rect en bas (largeur)
    rect_players_choice = pygame.Rect(6, 700, WINDOW_X, WINDOW_Y) #x , y
    pygame.draw.rect(screen, color_rect_players, rect_players_choice)
    # rectangle separation
    rect_separation = pygame.Rect(int(WINDOW_X/2), 0, 2, int(WINDOW_Y*0.6659) )
    pygame.draw.rect(screen, red, rect_separation)
"""


BACK_X = 0
BACK_Y = 0

GROUND_Y = int((900 / 1080) * height)
COEF_UP = 1.1
COEF_DOWN = 1.1

UP_MOVE = 30 #vitesse de déplacement
SIDE_MOVE = 10
choice = choice_perso()

isMac = platform.system() == "Darwin" or platform.system() == "Linux"

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

#couleurs 
color_rect_players = (196, 184, 189)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
null = (153, 122, 144)

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
            """
        elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if event.pos[0] >= 500 and event.pos[0] <= 600 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player1 ; 0 pour x et 1 pour y 
                        screen.blit(papacito_image, position_j1)
                        save_chara = 1;
                    elif event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player2
                        screen.blit(sakuya_image, position_j2)
                    elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 800 and event.pos[1] <= 850:#rect player3
                        screen.blit(papacito_image, position_j1)
                    elif event.pos[0] >= 1000 and event.pos[0] <= 1100 and event.pos[1] >= 800 and event.pos[1] <= 850:#rect player4
                        screen.blit(sakuya_image, position_j2)
"""
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
