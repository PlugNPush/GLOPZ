import pygame
from pygame.locals import *
from function import *
import os
import platform
#toutes les coordonnées:

pygame.init()

width, height = int(pygame.display.Info().current_w), int(pygame.display.Info().current_h)
print(width)
print(height)
WINDOW_X = width
WINDOW_Y = height

BACK_X = 0
BACK_Y = 0

GROUND_Y = int((700 / 1080) * height)
COEF_UP = 1.1
COEF_DOWN = 1.1

UP_MOVE = 30 #vitesse de déplacement
SIDE_MOVE = 10
#choice = choice_perso()

isMac = platform.system() == "Darwin" or platform.system() == "Linux"

#création d'une fenetre
if platform.system() == "Linux":
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
else:
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y), FULLSCREEN)


curdir = os.path.dirname(os.path.realpath(__file__))
#chargement des images
image_wall = pygame.image.load(curdir + "/images/wallpaper.png").convert()

map_1 = pygame.image.load(curdir + "/images/maps/map-1.png").convert()
pos_map_1 = map_1.get_rect()

#joueur 1
j1 = pygame.image.load(curdir + "/images/chara_1_0.png").convert_alpha()
j1_flip = pygame.image.load(curdir + "/images/chara_1_0_flip.png").convert_alpha()
j1 = pygame.transform.scale(j1, (42, 84))
j1_flip = pygame.transform.scale(j1_flip, (42, 84))
#joueur 2
j2 = pygame.image.load(curdir + "/images/chara_2_0.png").convert_alpha()
j2_flip = pygame.image.load(curdir + "/images/chara_2_0_flip.png").convert_alpha()
j2 = pygame.transform.scale(j2, (42, 84))
j2_flip = pygame.transform.scale(j2_flip, (42, 84))
#j1 = pygame.image.load(curdir + choice[0][0]).convert_alpha()
#j1_flip = pygame.image.load(curdir + choice[1][0]).convert_alpha()

#joueur 2
#j2 = pygame.image.load(curdir + choice[0][1]).convert_alpha()
#j2_flip = pygame.image.load(curdir + choice[1][1]).convert_alpha()

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

alive_j1 = True
alive_j2 = True

pos_j1 = pos_j1.move(int((345 / 1920) * width), int(GROUND_Y-((30 / 1080) * height)))
pos_j2 = pos_j2.move(int((1500 / 1920) * width), int(GROUND_Y-((30 / 1080) * height)))

menu = pygame.image.load(curdir + "/images/menu_button.png").convert_alpha()
pos_menu = menu.get_rect()
pos_menu = (WINDOW_X/3, WINDOW_Y/7)
#placement des images
screen.blit(image_wall, (BACK_X, BACK_Y))
screen.blit(j1, pos_j1)
screen.blit(j2, pos_j2)

#raffraichissement de l'écran
pygame.display.flip()

#fréquence de répétition des touches
pygame.key.set_repeat(1, 10)


#couleurs 
color_rect_players = (196, 184, 189)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
null = pygame.Color(166, 253, 255)
# rectangles choix joueurs


button_player1 = pygame.Rect(700, 800, 100, 50)
pygame.draw.rect(screen, red, button_player1)
button_player2 = pygame.Rect(900, 800, 100, 50)
pygame.draw.rect(screen, green, button_player2)
button_player3 = pygame.Rect(1100, 800, 100, 50)
pygame.draw.rect(screen, blue, button_player3)
button_player4 = pygame.Rect(700, 950, 100, 50)
pygame.draw.rect(screen, red, button_player4)
button_player5 = pygame.Rect(900, 950, 100, 50)
pygame.draw.rect(screen, blue, button_player5)
button_player6 = pygame.Rect(1100, 950, 100, 50)
pygame.draw.rect(screen, red, button_player6)
pygame.display.flip()

#boucle en attente d'évènement
on = True
menu_principale = True
menu_personnage = True
game = True
while on:
    while menu_principale: 
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                on = False
                break
            elif keys[K_LALT] and keys[K_F4]:
                on = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if event.pos[0] >= (int(WINDOW_X/3)) and event.pos[0] <= (int(WINDOW_X/3))+613 and event.pos[1] >= (int(WINDOW_Y/7)) and event.pos[1] <= (int(WINDOW_Y/7)) + 203: #play

                        menu_principale = False
                        menu_personnage = True
                    if event.pos[0] >= (int(WINDOW_X/3)) and event.pos[0] <= (int(WINDOW_X/3))+613 and event.pos[1] >= (int(WINDOW_Y/7))+236 and event.pos[1] <= (int(WINDOW_Y/7)) + 441: #exit
                        #pygame.quit()
                        menu_principale = False
                        menu_personnage = False
                        on = False
                        game = False
                        break
                    if event.pos[0] >= (int(WINDOW_X/3)) and event.pos[0] <= (int(WINDOW_X/3))+613 and event.pos[1] >= (int(WINDOW_Y/7))+472 and event.pos[1] <= (int(WINDOW_Y/7)) + 676: #info
                        menu_principale = False
                        menu_personnage = True
        screen.blit(image_wall, (BACK_X, BACK_Y))
        screen.blit(menu, pos_menu)
        pygame.display.flip()
        """Sert à vérifier que la variable personnage n'est pas vide"""
    perso1 = ""
    perso2 = ""
    perso3 = ""
    perso4 = ""
    perso5 = ""
    perso6 = ""
    while menu_personnage:
        screen.blit(image_wall, (BACK_X, BACK_Y))
        pygame.draw.rect(screen, red, button_player6)
        rect_players_choice = pygame.Rect(6, 700, WINDOW_X, WINDOW_Y) 
        pygame.draw.rect(screen, color_rect_players, rect_players_choice)
        rect_separation = pygame.Rect(int(WINDOW_X/2), 0, 2, int(WINDOW_Y*0.6659) )
        pygame.draw.rect(screen, red, rect_separation)
        button_player1 = pygame.Rect(700, 800, 100, 50)
        pygame.draw.rect(screen, red, button_player1)
        button_player2 = pygame.Rect(900, 800, 100, 50)
        pygame.draw.rect(screen, green, button_player2)
        button_player3 = pygame.Rect(1100, 800, 100, 50)
        pygame.draw.rect(screen, blue, button_player3)
        button_player4 = pygame.Rect(700, 950, 100, 50)
        pygame.draw.rect(screen, red, button_player4)
        button_player5 = pygame.Rect(900, 950, 100, 50)
        pygame.draw.rect(screen, blue, button_player5)
        button_player6 = pygame.Rect(1100, 950, 100, 50)
        button_skip = pygame.Rect(1300, 800, 100, 50)
        pygame.draw.rect(screen, red, button_skip)
            
        if perso1: 
            screen.blit(perso1, pos_j1)
        if perso2:
            scren.blit(perso2, pos_)
        pygame.display.flip()
        liste_perso = ["images/chara_1_face.png", "images/chara_2_face.png", "images/chara_3_face.png", "images/chara_4_face.png", "images/chara_5_face.png", "images/chara_6_face.png"]
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                on = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player1 ; 0 pour x et 1 pour y 
                        print("BOUTON 1")
                        perso1 = pygame.image.load(liste_perso[0])
                        break
                    elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player2
                        print("BOUTON 2")
                        #perso2 = pygame.image.load(liste_perso[1])
                        break
                    elif event.pos[0] >= 1100 and event.pos[0] <= 1200 and event.pos[1] >= 800 and event.pos[1] <= 850:#rect player3
                        print("BOUTON 3")
                        #perso3 = pygame.image.load(liste_perso[2])
                        break
                    elif event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                        print("BOUTON 4")
                        #perso4 = pygame.image.load(liste_perso[3])
                    elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                        print("BOUTON 5")
                        #perso5 = pygame.image.load(liste_perso[4])
                    elif event.pos[0] >= 1100 and event.pos[0] <= 1200 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                        print("BOUTON 6")
                        #perso6 = pygame.image.load(liste_perso[5])
                        break
                    elif event.pos[0] >= 1300 and event.pos[0] <= 1400 and event.pos[1] >= 800 and event.pos[1] <= 850:#rect player4
                        print("BOUTON SKIP")
                        menu_personnage = False
                        menu_principale = True
                        game = True
    while game:

        bloc_1 = pygame.Rect(521, 537, 260, 58)
        pygame.draw.rect(screen, red, bloc_1)
        bloc_2 = pygame.Rect(1050, 539, 260, 58)
        pygame.draw.rect(screen, red, bloc_2)
        bloc_3 = pygame.Rect(765, 335, 260, 58)
        pygame.draw.rect(screen, red, bloc_3)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            
            if event.type == QUIT:
                on = False
                break
            
            

        if keys[K_LALT] and keys[K_F4]:
            on = False
            break
        if keys[K_s] if isMac else keys[K_s]:
            pos_j1 = pos_j1.move(0, UP_MOVE)

        
        if keys[K_z] if isMac else keys[K_w]:
            if jump_j1 == True :
                pos_j1 = pos_j1.move(0, int(-coef_jump_j1*UP_MOVE))
                #jump_j1_count += 1
                coef_jump_j1 = coef_jump_j1/COEF_UP

            elif pos_j1.y < int(GROUND_Y-((30 / 1080) * height)) :
                if pass_j1 == True :
                    coef_jump_j1 = 0.1
                    pass_j1 = False

                pos_j1 = pos_j1.move(0, int(coef_jump_j1*UP_MOVE))
                #jump_j1_count += -1
                coef_jump_j1 = coef_jump_j1*COEF_DOWN
        
        elif pos_j1.y < int(GROUND_Y-((30 / 1080) * height)) :
            if pass_j1 == True :
                coef_jump_j1 = 0.1
                pass_j1 = False

            pos_j1 = pos_j1.move(0, int(coef_jump_j1*UP_MOVE))
            #jump_j1_count += -1
            coef_jump_j1 = coef_jump_j1*COEF_DOWN
            jump_j1 = False

        if keys[K_d] if isMac else keys[K_d]:
            pos_j1 = pos_j1.move(SIDE_MOVE, 0)
            heading_j1 = 1

        if keys[K_q] if isMac else keys[K_a]:
            pos_j1 = pos_j1.move(-SIDE_MOVE, 0)
            heading_j1 = 0
        
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
                pos_j2 = pos_j2.move(0, int(-coef_jump_j2*UP_MOVE))
                #jump_j2_count += 1
                coef_jump_j2 = coef_jump_j2/COEF_UP

            elif pos_j2.y < int(GROUND_Y-((30 / 1080) * height)) :
                if pass_j2 == True :
                    coef_jump_j2 = 0.1
                    pass_j2 = False

                pos_j2 = pos_j2.move(0, int(coef_jump_j2*UP_MOVE))
                #jump_j2_count += -1
                coef_jump_j2 = coef_jump_j2*COEF_DOWN
        
        elif pos_j2.y < int(GROUND_Y-((30 / 1080) * height)) :
            if pass_j2 == True :
                coef_jump_j2 = 0.1
                pass_j2 = False

            pos_j2 = pos_j2.move(0, int(coef_jump_j2*UP_MOVE))
            #jump_j2_count += -1
            coef_jump_j2 = coef_jump_j2*COEF_DOWN
            jump_j2 = False

        if keys[K_RIGHT]:
            pos_j2 = pos_j2.move(SIDE_MOVE, 0)
            heading_j2 = 1

        if keys[K_LEFT]:
            pos_j2 = pos_j2.move(-SIDE_MOVE, 0)
            heading_j2 = 0

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

        """bloc 1"""
        if pos_j1.x+42 > bloc_1.x and pos_j1.x+42 < bloc_1.x+10 and pos_j1.y < bloc_1.y+58 and pos_j1.y+84 > bloc_1.y:
            pos_j1.x = bloc_1.x-43

        if pos_j1.x < bloc_1.x+260 and pos_j1.x > bloc_1.x+250 and pos_j1.y < bloc_1.y+58 and pos_j1.y+84 > bloc_1.y:
            pos_j1.x = bloc_1.x+261

        if pos_j1.x+42 >= bloc_1.x and pos_j1.x <= bloc_1.x+260 and pos_j1.y <= bloc_1.y+58 and pos_j1.y >= bloc_1.y:
            pos_j1.y = bloc_1.y+59
            jump_j1 = False

        if pos_j1.x+42 >= bloc_1.x and pos_j1.x <= bloc_1.x+260 and pos_j1.y+84 <= bloc_1.y+58 and pos_j1.y+84 >= bloc_1.y:
            pos_j1.y = bloc_1.y-84
            coef_jump_j1 = float(1)
            pass_j1 = True
            jump_j1 = True
        
        if pos_j2.x+42 > bloc_1.x and pos_j2.x+42 < bloc_1.x+10 and pos_j2.y < bloc_1.y+58 and pos_j2.y+84 > bloc_1.y:
            pos_j2.x = bloc_1.x-43

        if pos_j2.x < bloc_1.x+260 and pos_j2.x > bloc_1.x+250 and pos_j2.y < bloc_1.y+58 and pos_j2.y+84 > bloc_1.y:
            pos_j2.x = bloc_1.x+261

        if pos_j2.x+42 >= bloc_1.x and pos_j2.x <= bloc_1.x+260 and pos_j2.y <= bloc_1.y+58 and pos_j2.y >= bloc_1.y:
            pos_j2.y = bloc_1.y+59
            jump_j2 = False

        if pos_j2.x+42 >= bloc_1.x and pos_j2.x <= bloc_1.x+260 and pos_j2.y+84 <= bloc_1.y+58 and pos_j2.y+84 >= bloc_1.y:
            pos_j2.y = bloc_1.y-84
            coef_jump_j2 = float(1)
            pass_j2 = True
            jump_j2 = True


        """bloc 2"""
        if pos_j1.x+42 > bloc_2.x and pos_j1.x+42 < bloc_2.x+10 and pos_j1.y < bloc_2.y+58 and pos_j1.y+84 > bloc_2.y:
            pos_j1.x = bloc_2.x-43

        if pos_j1.x < bloc_2.x+260 and pos_j1.x > bloc_2.x+250 and pos_j1.y < bloc_2.y+58 and pos_j1.y+84 > bloc_2.y:
            pos_j1.x = bloc_2.x+261

        if pos_j1.x+42 >= bloc_2.x and pos_j1.x <= bloc_2.x+260 and pos_j1.y <= bloc_2.y+58 and pos_j1.y >= bloc_2.y:
            pos_j1.y = bloc_2.y+59
            jump_j1 = False

        if pos_j1.x+42 >= bloc_2.x and pos_j1.x <= bloc_2.x+260 and pos_j1.y+84 <= bloc_2.y+58 and pos_j1.y+84 >= bloc_2.y:
            pos_j1.y = bloc_2.y-84
            coef_jump_j1 = float(1)
            pass_j1 = True
            jump_j1 = True
        
        if pos_j2.x+42 > bloc_2.x and pos_j2.x+42 < bloc_2.x+10 and pos_j2.y < bloc_2.y+58 and pos_j2.y+84 > bloc_2.y:
            pos_j2.x = bloc_2.x-43

        if pos_j2.x < bloc_2.x+260 and pos_j2.x > bloc_2.x+250 and pos_j2.y < bloc_2.y+58 and pos_j2.y+84 > bloc_2.y:
            pos_j2.x = bloc_2.x+261

        if pos_j2.x+42 >= bloc_2.x and pos_j2.x <= bloc_2.x+260 and pos_j2.y <= bloc_2.y+58 and pos_j2.y >= bloc_2.y:
            pos_j2.y = bloc_2.y+59
            jump_j2 = False

        if pos_j2.x+42 >= bloc_2.x and pos_j2.x <= bloc_2.x+260 and pos_j2.y+84 <= bloc_2.y+58 and pos_j2.y+84 >= bloc_2.y:
            pos_j2.y = bloc_2.y-84
            coef_jump_j2 = float(1)
            pass_j2 = True
            jump_j2 = True
        

        """bloc 3"""
        if pos_j1.x+42 > bloc_3.x and pos_j1.x+42 < bloc_3.x+10 and pos_j1.y < bloc_3.y+58 and pos_j1.y+84 > bloc_3.y:
            pos_j1.x = bloc_3.x-43

        if pos_j1.x < bloc_3.x+260 and pos_j1.x > bloc_3.x+250 and pos_j1.y < bloc_3.y+58 and pos_j1.y+84 > bloc_3.y:
            pos_j1.x = bloc_3.x+261

        if pos_j1.x+42 >= bloc_3.x and pos_j1.x <= bloc_3.x+260 and pos_j1.y <= bloc_3.y+58 and pos_j1.y >= bloc_3.y:
            pos_j1.y = bloc_3.y+59
            jump_j1 = False

        if pos_j1.x+42 >= bloc_3.x and pos_j1.x <= bloc_3.x+260 and pos_j1.y+84 <= bloc_3.y+58 and pos_j1.y+84 >= bloc_3.y:
            pos_j1.y = bloc_3.y-84
            coef_jump_j1 = float(1)
            pass_j1 = True
            jump_j1 = True
        
        if pos_j2.x+42 > bloc_3.x and pos_j2.x+42 < bloc_3.x+10 and pos_j2.y < bloc_3.y+58 and pos_j2.y+84 > bloc_3.y:
            pos_j2.x = bloc_3.x-43

        if pos_j2.x < bloc_3.x+260 and pos_j2.x > bloc_3.x+250 and pos_j2.y < bloc_3.y+58 and pos_j2.y+84 > bloc_3.y:
            pos_j2.x = bloc_3.x+261

        if pos_j2.x+42 >= bloc_3.x and pos_j2.x <= bloc_3.x+260 and pos_j2.y <= bloc_3.y+58 and pos_j2.y >= bloc_3.y:
            pos_j2.y = bloc_3.y+59
            jump_j2 = False

        if pos_j2.x+42 >= bloc_3.x and pos_j2.x <= bloc_3.x+260 and pos_j2.y+84 <= bloc_3.y+58 and pos_j2.y+84 >= bloc_3.y:
            pos_j2.y = bloc_3.y-84
            coef_jump_j2 = float(1)
            pass_j2 = True
            jump_j2 = True
        #if pos_j1.x >= 521 and pos_j1.x <= 521+260 and pos_j1.y <= 537+58 and pos_j1.y >= 537:
        #    pos_j1 = pos_j1.move(0, 537+59)
        #if pos_j1.x >= 521 and pos_j1.x <= 521+260 and pos_j1.y <= 537+58 and pos_j1.y >= 537:
        #    pos_j1 = pos_j1.move(0, 537+59)



        #recollage des éléments
        screen.blit(map_1, pos_map_1)

        if alive_j1 == True :
            if heading_j1 == 1:
                screen.blit(j1, pos_j1)
            else:
                screen.blit(j1_flip, pos_j1)
            


        if alive_j2 == True :
            if heading_j2 == 1:
                screen.blit(j2, pos_j2)
            else:
                screen.blit(j2_flip, pos_j2)




        #raffraichissement
        #pygame.draw.rect(screen, red, bloc_1)
        #pygame.draw.rect(screen, red, bloc_2)
        #pygame.draw.rect(screen, red, bloc_3)
        pygame.display.flip()

        pygame.time.delay(16)
pygame.quit()
