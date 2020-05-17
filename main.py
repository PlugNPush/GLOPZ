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

GROUND_Y = int((752 / 1080) * height)
COEF_UP = 1.1
COEF_DOWN = 1.1

UP_MOVE = 30 #vitesse de déplacement
SIDE_MOVE = 10

LEG_CHANGE = 5
#choice = choice_perso()
#choice_map = int(input("map (1 ou 2) : "))

isMac = platform.system() == "Darwin" or platform.system() == "Linux"

#création d'une fenetre
if platform.system() == "Linux":
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
else:
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y), FULLSCREEN)


curdir = os.path.dirname(os.path.realpath(__file__))
#chargement des images
image_wall = pygame.image.load(curdir + "/images/wallpaper.png").convert()




#joueur 1
j1 = pygame.image.load(curdir + "/images/chara_1_0.png").convert_alpha()
j1_flip = pygame.image.load(curdir + "/images/chara_1_0_flip.png").convert_alpha()
j1_1 = pygame.image.load(curdir + "/images/chara_1_1.png").convert_alpha()
j1_flip_1 = pygame.image.load(curdir + "/images/chara_1_1_flip.png").convert_alpha()
j1_2 = pygame.image.load(curdir + "/images/chara_1_2.png").convert_alpha()
j1_flip_2 = pygame.image.load(curdir + "/images/chara_1_2_flip.png").convert_alpha()
j1 = pygame.transform.scale(j1, (42, 84))
j1_flip = pygame.transform.scale(j1_flip, (42, 84))
j1_1 = pygame.transform.scale(j1_1, (42, 84))
j1_flip_1 = pygame.transform.scale(j1_flip_1, (42, 84))
j1_2 = pygame.transform.scale(j1_2, (42, 84))
j1_flip_2 = pygame.transform.scale(j1_flip_2, (42, 84))
#joueur 2
j2 = pygame.image.load(curdir + "/images/chara_2_0.png").convert_alpha()
j2_flip = pygame.image.load(curdir + "/images/chara_2_0_flip.png").convert_alpha()
j2_1 = pygame.image.load(curdir + "/images/chara_2_1.png").convert_alpha()
j2_flip_1 = pygame.image.load(curdir + "/images/chara_2_1_flip.png").convert_alpha()
j2_2 = pygame.image.load(curdir + "/images/chara_2_2.png").convert_alpha()
j2_flip_2 = pygame.image.load(curdir + "/images/chara_2_2_flip.png").convert_alpha()
j2 = pygame.transform.scale(j2, (42, 84))
j2_flip = pygame.transform.scale(j2_flip, (42, 84))
j2_1 = pygame.transform.scale(j2_1, (42, 84))
j2_flip_1 = pygame.transform.scale(j2_flip_1, (42, 84))
j2_2 = pygame.transform.scale(j2_2, (42, 84))
j2_flip_2 = pygame.transform.scale(j2_flip_2, (42, 84))




map_1 = pygame.image.load(curdir + "/images/maps/map-1.png").convert()
map_1_preview = pygame.transform.scale(map_1, (384, 216))

map_2 = pygame.image.load(curdir + "/images/maps/map_desert.png").convert()
map_2_preview = pygame.transform.scale(map_2, (384, 216))

pos_map_1 = map_1.get_rect()
pos_map_2 = map_2.get_rect()
pos_map_1_preview = map_1_preview.get_rect()
pos_map_2_preview = map_2_preview.get_rect()
pos_map_1_preview.x = 100
pos_map_1_preview.y = 300
pos_map_2_preview.x = 550
pos_map_2_preview.y = 300

retour = pygame.image.load(curdir + "/images/retour_button.png").convert_alpha()
retour = pygame.transform.scale(retour, (122, 40))
pos_retour = retour.get_rect()
pos_retour.x = 10
pos_retour.y = 10

map1_button = pygame.image.load(curdir + "/images/map1_button.png").convert_alpha()
map1_button = pygame.transform.scale(map1_button, (384, 128))
pos_map1_button = map1_button.get_rect()
pos_map1_button.x = 100
pos_map1_button.y = 550

map2_button = pygame.image.load(curdir + "/images/map2_button.png").convert_alpha()
map2_button = pygame.transform.scale(map2_button, (384, 128))
pos_map2_button = map2_button.get_rect()
pos_map2_button.x = 550
pos_map2_button.y = 550

print(pos_map1_button.x)
print(pos_map1_button.y)
print(map1_button.get_width())
print(map1_button.get_height())

menu = pygame.image.load(curdir + "/images/menu_button.png").convert_alpha()
pos_menu = menu.get_rect()
pos_menu.x = WINDOW_X/3
pos_menu.y = WINDOW_Y/7


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

compteur_j1 = 0
compteur_j2 = 0

move_j1 = False
move_j2 = False






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
menu_map = True
game = True
joueur_1 = True
info = True
while on:
    game = True
    alive_j1 = True
    alive_j2 = True
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
                        game = True
                        info = False

                    if event.pos[0] >= (int(WINDOW_X/3)) and event.pos[0] <= (int(WINDOW_X/3))+613 and event.pos[1] >= (int(WINDOW_Y/7))+236 and event.pos[1] <= (int(WINDOW_Y/7)) + 441: #exit
                        #pygame.quit()
                        menu_principale = False
                        menu_personnage = False
                        on = False
                        game = False
                        info = False
                        break

                    if event.pos[0] >= (int(WINDOW_X/3)) and event.pos[0] <= (int(WINDOW_X/3))+613 and event.pos[1] >= (int(WINDOW_Y/7))+472 and event.pos[1] <= (int(WINDOW_Y/7)) + 676: #info
                        menu_principale = False
                        menu_personnage = False
                        game = False
                        info = True
        screen.blit(image_wall, (BACK_X, BACK_Y))
        screen.blit(menu, pos_menu)
        pygame.display.flip()
    
    while info:
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
                    if event.pos[0] >= 10 and event.pos[0] <= 132 and event.pos[1] >= 10 and event.pos[1] <= 50:
                        menu_principale = True
                        menu_map = False
                        info = False
                        print("RETOUR")
                        break
        screen.blit(image_wall, (BACK_X, BACK_Y))
        screen.blit(retour, pos_retour)
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
            scren.blit(perso2, pos_j1)
       # if perso3:
       #     screen.blit(perso3, pos_j1)
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
                        if joueur_1 is True:
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
                        menu_map = True
    while menu_map:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                on = False
                menu_map = False
                menu_principale = False
                game = False
                menu_personnage = False
                break
            elif keys[K_LALT] and keys[K_F4]:
                on = False
                menu_map = False
                menu_principale = False
                game = False
                menu_personnage = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if event.pos[0] >= pos_map1_button.x and event.pos[0] <= pos_map1_button.x + map1_button.get_width() and event.pos[1] >= pos_map1_button.y and event.pos[1] <= pos_map1_button.y + map1_button.get_height():
                        menu_map = False
                        game = True
                        
                        choice_map = 1
                        count_bloc = 3
                        bloc_1 = pygame.Rect(521, 537, 260, 58)
                        bloc_2 = pygame.Rect(1050, 539, 260, 58)
                        bloc_3 = pygame.Rect(765, 335, 260, 58)
                        bloc_base = pygame.Rect(313, 751, 1263, 300)
                        pos_j1.x = int((345 / 1920) * width)
                        pos_j1.y = int(bloc_base.y-((j1.get_height() / 1080) * height))
                        pos_j2.x = int((1500 / 1920) * width)
                        pos_j2.y = int(bloc_base.y-((j2.get_height() / 1080) * height))
                        break
                    
                    if event.pos[0] >= pos_map2_button.x and event.pos[0] <= pos_map2_button.x + map2_button.get_width() and event.pos[1] >= pos_map2_button.y and event.pos[1] <= pos_map2_button.y + map2_button.get_height():
                        menu_map = False
                        game = True
                        choice_map = 2
                        count_bloc = 5
                        bloc_1 = pygame.Rect(104, 649, 1718, 200)
                        bloc_2 = pygame.Rect(200, 550, 797, 200)
                        bloc_3 = pygame.Rect(1234, 550, 398, 200)
                        bloc_4 = pygame.Rect(408, 450, 101, 200)
                        bloc_5 = pygame.Rect(1426, 450, 101, 200)
                        bloc_base = pygame.Rect(0, 749, 1920, 300)
                        pos_j1.x = int((0 / 1920) * width)
                        pos_j1.y = int(bloc_base.y-((j1.get_height() / 1080) * height))
                        pos_j2.x = int((1850 / 1920) * width)
                        pos_j2.y = int(bloc_base.y-((j2.get_height() / 1080) * height))
                        break
        screen.blit(image_wall, (BACK_X, BACK_Y))
        screen.blit(map_1_preview, pos_map_1_preview)
        screen.blit(map_2_preview, pos_map_2_preview)
        screen.blit(map1_button, pos_map1_button)
        screen.blit(map2_button, pos_map2_button)
        pygame.display.flip()
    while game:
        

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            
            if event.type == QUIT:
                on = False
                break
            elif keys[K_ESCAPE]:
                game = False
                menu_personnage = True
            
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

            elif pos_j1.y < int(bloc_base.y-((j1.get_height() / 1080) * height)) :
                if pass_j1 == True :
                    coef_jump_j1 = 0.1
                    pass_j1 = False

                pos_j1 = pos_j1.move(0, int(coef_jump_j1*UP_MOVE))
                #jump_j1_count += -1
                coef_jump_j1 = coef_jump_j1*COEF_DOWN
        
        elif pos_j1.y < int(bloc_base.y-((j1.get_height() / 1080) * height)) :
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
            move_j1 = True

        if keys[K_q] if isMac else keys[K_a]:
            pos_j1 = pos_j1.move(-SIDE_MOVE, 0)
            heading_j1 = 0
            move_j1 = True
        
        if coef_jump_j1 < 0.1:
            jump_j1 = False

        
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

            elif pos_j2.y < int(bloc_base.y-((j2.get_height() / 1080) * height)) :
                if pass_j2 == True :
                    coef_jump_j2 = 0.1
                    pass_j2 = False

                pos_j2 = pos_j2.move(0, int(coef_jump_j2*UP_MOVE))
                #jump_j2_count += -1
                coef_jump_j2 = coef_jump_j2*COEF_DOWN
        
        elif pos_j2.y < int(bloc_base.y-((j2.get_height() / 1080) * height)) :
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
            move_j2 = True

        if keys[K_LEFT]:
            pos_j2 = pos_j2.move(-SIDE_MOVE, 0)
            heading_j2 = 0
            move_j2 = True

        if coef_jump_j2 < 0.1:
            jump_j2 = False

        
        if pos_j1.y <= 0:
            pos_j1 = pos_j1.move(0, UP_MOVE)

        if pos_j1.x <= 0:
            pos_j1 = pos_j1.move(SIDE_MOVE, 0)

        if pos_j1.x >= WINDOW_X-j1.get_width():
            pos_j1 = pos_j1.move(-SIDE_MOVE, 0)
        


        
        if pos_j2.y <= 0:
            pos_j2 = pos_j2.move(0, UP_MOVE)

        if pos_j2.x <= 0:
            pos_j2 = pos_j2.move(SIDE_MOVE, 0)

        if pos_j2.x >= WINDOW_X-j2.get_width():
            pos_j2 = pos_j2.move(-SIDE_MOVE, 0)
        """bloc 1"""
        if count_bloc >= 1:
            if pos_j1.x+j1.get_width() > bloc_1.x and pos_j1.x+j1.get_width() < bloc_1.x+10 and pos_j1.y < bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() > bloc_1.y:
                pos_j1.x = bloc_1.x-j1.get_width()-1

            if pos_j1.x < bloc_1.x+bloc_1.w and pos_j1.x > bloc_1.x+bloc_1.w - 10 and pos_j1.y < bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() > bloc_1.y:
                pos_j1.x = bloc_1.x+bloc_1.w +1

            if pos_j1.x+j1.get_width() >= bloc_1.x and pos_j1.x <= bloc_1.x+bloc_1.w and pos_j1.y <= bloc_1.y+bloc_1.h and pos_j1.y >= bloc_1.y:
                pos_j1.y = bloc_1.y+bloc_1.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_1.x and pos_j1.x <= bloc_1.x+bloc_1.w and pos_j1.y+j1.get_height() <= bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() >= bloc_1.y:
                pos_j1.y = bloc_1.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_1.x and pos_j2.x+j2.get_width() < bloc_1.x+10 and pos_j2.y < bloc_1.y+bloc_1.h and pos_j2.y+j2.get_height() > bloc_1.y:
                pos_j2.x = bloc_1.x-j2.get_width()-1

            if pos_j2.x < bloc_1.x+bloc_1.w and pos_j2.x > bloc_1.x+bloc_1.w - 10 and pos_j2.y < bloc_1.y+bloc_1.h and pos_j2.y+j2.get_height() > bloc_1.y:
                pos_j2.x = bloc_1.x+bloc_1.w +1

            if pos_j2.x+j2.get_width() >= bloc_1.x and pos_j2.x <= bloc_1.x+bloc_1.w and pos_j2.y <= bloc_1.y+bloc_1.h and pos_j2.y >= bloc_1.y:
                pos_j2.y = bloc_1.y+bloc_1.h +1
                jump_j2 = False

            if pos_j2.x+j2.get_width() >= bloc_1.x and pos_j2.x <= bloc_1.x+bloc_1.w and pos_j2.y+j2.get_height() <= bloc_1.y+bloc_1.h and pos_j2.y+j2.get_height() >= bloc_1.y:
                pos_j2.y = bloc_1.y-j2.get_height()
                coef_jump_j2 = float(1)
                pass_j2 = True
                jump_j2 = True


        """bloc 2"""
        if count_bloc >= 2:
            if pos_j1.x+j1.get_width() > bloc_2.x and pos_j1.x+j1.get_width() < bloc_2.x+10 and pos_j1.y < bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() > bloc_2.y:
                pos_j1.x = bloc_2.x-j1.get_width()-1

            if pos_j1.x < bloc_2.x+bloc_2.w and pos_j1.x > bloc_2.x+bloc_2.w - 10 and pos_j1.y < bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() > bloc_2.y:
                pos_j1.x = bloc_2.x+bloc_2.w +1

            if pos_j1.x+j1.get_width() >= bloc_2.x and pos_j1.x <= bloc_2.x+bloc_2.w and pos_j1.y <= bloc_2.y+bloc_2.h and pos_j1.y >= bloc_2.y:
                pos_j1.y = bloc_2.y+bloc_2.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_2.x and pos_j1.x <= bloc_2.x+bloc_2.w and pos_j1.y+j1.get_height() <= bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() >= bloc_2.y:
                pos_j1.y = bloc_2.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_2.x and pos_j2.x+j2.get_width() < bloc_2.x+10 and pos_j2.y < bloc_2.y+bloc_2.h and pos_j2.y+j2.get_height() > bloc_2.y:
                pos_j2.x = bloc_2.x-j2.get_width()-1

            if pos_j2.x < bloc_2.x+bloc_2.w and pos_j2.x > bloc_2.x+bloc_2.w - 10 and pos_j2.y < bloc_2.y+bloc_2.h and pos_j2.y+j2.get_height() > bloc_2.y:
                pos_j2.x = bloc_2.x+bloc_2.w +1

            if pos_j2.x+j2.get_width() >= bloc_2.x and pos_j2.x <= bloc_2.x+bloc_2.w and pos_j2.y <= bloc_2.y+bloc_2.h and pos_j2.y >= bloc_2.y:
                pos_j2.y = bloc_2.y+bloc_2.h +1
                jump_j2 = False

            if pos_j2.x+j2.get_width() >= bloc_2.x and pos_j2.x <= bloc_2.x+bloc_2.w and pos_j2.y+j2.get_height() <= bloc_2.y+bloc_2.h and pos_j2.y+j2.get_height() >= bloc_2.y:
                pos_j2.y = bloc_2.y-j2.get_height()
                coef_jump_j2 = float(1)
                pass_j2 = True
                jump_j2 = True
        

        """bloc 3"""
        if count_bloc >= 3:
            if pos_j1.x+j1.get_width() > bloc_3.x and pos_j1.x+j1.get_width() < bloc_3.x+10 and pos_j1.y < bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() > bloc_3.y:
                pos_j1.x = bloc_3.x-j1.get_width()-1

            if pos_j1.x < bloc_3.x+bloc_3.w and pos_j1.x > bloc_3.x+bloc_3.w - 10 and pos_j1.y < bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() > bloc_3.y:
                pos_j1.x = bloc_3.x+bloc_3.w +1

            if pos_j1.x+j1.get_width() >= bloc_3.x and pos_j1.x <= bloc_3.x+bloc_3.w and pos_j1.y <= bloc_3.y+bloc_3.h and pos_j1.y >= bloc_3.y:
                pos_j1.y = bloc_3.y+bloc_3.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_3.x and pos_j1.x <= bloc_3.x+bloc_3.w and pos_j1.y+j1.get_height() <= bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() >= bloc_3.y:
                pos_j1.y = bloc_3.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_3.x and pos_j2.x+j2.get_width() < bloc_3.x+10 and pos_j2.y < bloc_3.y+bloc_3.h and pos_j2.y+j2.get_height() > bloc_3.y:
                pos_j2.x = bloc_3.x-j2.get_width()-1

            if pos_j2.x < bloc_3.x+bloc_3.w and pos_j2.x > bloc_3.x+bloc_3.w - 10 and pos_j2.y < bloc_3.y+bloc_3.h and pos_j2.y+j2.get_height() > bloc_3.y:
                pos_j2.x = bloc_3.x+bloc_3.w +1

            if pos_j2.x+j2.get_width() >= bloc_3.x and pos_j2.x <= bloc_3.x+bloc_3.w and pos_j2.y <= bloc_3.y+bloc_3.h and pos_j2.y >= bloc_3.y:
                pos_j2.y = bloc_3.y+bloc_3.h +1
                jump_j2 = False

            if pos_j2.x+j2.get_width() >= bloc_3.x and pos_j2.x <= bloc_3.x+bloc_3.w and pos_j2.y+j2.get_height() <= bloc_3.y+bloc_3.h and pos_j2.y+j2.get_height() >= bloc_3.y:
                pos_j2.y = bloc_3.y-j2.get_height()
                coef_jump_j2 = float(1)
                pass_j2 = True
                jump_j2 = True


        if count_bloc >= 4:
            if pos_j1.x+j1.get_width() > bloc_4.x and pos_j1.x+j1.get_width() < bloc_4.x+10 and pos_j1.y < bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() > bloc_4.y:
                pos_j1.x = bloc_4.x-j1.get_width()-1

            if pos_j1.x < bloc_4.x+bloc_4.w and pos_j1.x > bloc_4.x+bloc_4.w - 10 and pos_j1.y < bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() > bloc_4.y:
                pos_j1.x = bloc_4.x+bloc_4.w +1

            if pos_j1.x+j1.get_width() >= bloc_4.x and pos_j1.x <= bloc_4.x+bloc_4.w and pos_j1.y <= bloc_4.y+bloc_4.h and pos_j1.y >= bloc_4.y:
                pos_j1.y = bloc_4.y+bloc_4.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_4.x and pos_j1.x <= bloc_4.x+bloc_4.w and pos_j1.y+j1.get_height() <= bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() >= bloc_4.y:
                pos_j1.y = bloc_4.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_4.x and pos_j2.x+j2.get_width() < bloc_4.x+10 and pos_j2.y < bloc_4.y+bloc_4.h and pos_j2.y+j2.get_height() > bloc_4.y:
                pos_j2.x = bloc_4.x-j2.get_width()-1

            if pos_j2.x < bloc_4.x+bloc_4.w and pos_j2.x > bloc_4.x+bloc_4.w - 10 and pos_j2.y < bloc_4.y+bloc_4.h and pos_j2.y+j2.get_height() > bloc_4.y:
                pos_j2.x = bloc_4.x+bloc_4.w +1

            if pos_j2.x+j2.get_width() >= bloc_4.x and pos_j2.x <= bloc_4.x+bloc_4.w and pos_j2.y <= bloc_4.y+bloc_4.h and pos_j2.y >= bloc_4.y:
                pos_j2.y = bloc_4.y+bloc_4.h +1
                jump_j2 = False

            if pos_j2.x+j2.get_width() >= bloc_4.x and pos_j2.x <= bloc_4.x+bloc_4.w and pos_j2.y+j2.get_height() <= bloc_4.y+bloc_4.h and pos_j2.y+j2.get_height() >= bloc_4.y:
                pos_j2.y = bloc_4.y-j2.get_height()
                coef_jump_j2 = float(1)
                pass_j2 = True
                jump_j2 = True
        

        if count_bloc >= 5:
            if pos_j1.x+j1.get_width() > bloc_5.x and pos_j1.x+j1.get_width() < bloc_5.x+10 and pos_j1.y < bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() > bloc_5.y:
                pos_j1.x = bloc_5.x-j1.get_width()-1

            if pos_j1.x < bloc_5.x+bloc_5.w and pos_j1.x > bloc_5.x+bloc_5.w - 10 and pos_j1.y < bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() > bloc_5.y:
                pos_j1.x = bloc_5.x+bloc_5.w +1

            if pos_j1.x+j1.get_width() >= bloc_5.x and pos_j1.x <= bloc_5.x+bloc_5.w and pos_j1.y <= bloc_5.y+bloc_5.h and pos_j1.y >= bloc_5.y:
                pos_j1.y = bloc_5.y+bloc_5.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_5.x and pos_j1.x <= bloc_5.x+bloc_5.w and pos_j1.y+j1.get_height() <= bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() >= bloc_5.y:
                pos_j1.y = bloc_5.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_5.x and pos_j2.x+j2.get_width() < bloc_5.x+10 and pos_j2.y < bloc_5.y+bloc_5.h and pos_j2.y+j2.get_height() > bloc_5.y:
                pos_j2.x = bloc_5.x-j2.get_width()-1

            if pos_j2.x < bloc_5.x+bloc_5.w and pos_j2.x > bloc_5.x+bloc_5.w - 10 and pos_j2.y < bloc_5.y+bloc_5.h and pos_j2.y+j2.get_height() > bloc_5.y:
                pos_j2.x = bloc_5.x+bloc_5.w +1

            if pos_j2.x+j2.get_width() >= bloc_5.x and pos_j2.x <= bloc_5.x+bloc_5.w and pos_j2.y <= bloc_5.y+bloc_5.h and pos_j2.y >= bloc_5.y:
                pos_j2.y = bloc_5.y+bloc_5.h +1
                jump_j2 = False

            if pos_j2.x+j2.get_width() >= bloc_5.x and pos_j2.x <= bloc_5.x+bloc_5.w and pos_j2.y+j2.get_height() <= bloc_5.y+bloc_5.h and pos_j2.y+j2.get_height() >= bloc_5.y:
                pos_j2.y = bloc_5.y-j2.get_height()
                coef_jump_j2 = float(1)
                pass_j2 = True
                jump_j2 = True


        if pos_j1.y == int(bloc_base.y-((j1.get_height() / 1080) * height)) and pos_j1.x > bloc_base.x and pos_j1.x < bloc_base.x + bloc_base.w:
            coef_jump_j1 = float(1)
            pass_j1 = True
            jump_j1 = True

        if pos_j2.y == int(bloc_base.y-((j2.get_height() / 1080) * height)):
            coef_jump_j2 = float(1)
            pass_j2 = True
            jump_j2 = True


        if pos_j1.y >= int(bloc_base.y-((j1.get_height() / 1080) * height)) and pos_j1.x > bloc_base.x and pos_j1.x < bloc_base.x + bloc_base.w:
            pos_j1.y = int(bloc_base.y-((j1.get_height() / 1080) * height))

        if pos_j2.y >= int(bloc_base.y-((j2.get_height() / 1080) * height)) and pos_j2.x > bloc_base.x and pos_j2.x < bloc_base.x + bloc_base.w:
            pos_j2.y = int(bloc_base.y-((j2.get_height() / 1080) * height))



        if pos_j1.y >= int(bloc_base.y-((j1.get_height() / 1080) * height)) and pos_j1.x+j1.get_width() < bloc_base.x :
            jump_j1 = False
            if pass_j1 == True :
                coef_jump_j1 = 0.1
                pass_j1 = False
            down = int(coef_jump_j1*UP_MOVE) #pour éviter le overflow
            if down > 1000 :
                coef_jump_j1 = 100
            pos_j1 = pos_j1.move(0, down)
            coef_jump_j1 = coef_jump_j1*COEF_DOWN

        if pos_j1.y >= height - j1.get_height() - 1:
            alive_j1 = False


        if pos_j2.y >= int(bloc_base.y-((j2.get_height() / 1080) * height)) and pos_j2.x+j2.get_width() < bloc_base.x :
            jump_j2 = False
            if pass_j2 == True :
                coef_jump_j2 = 0.1
                pass_j2 = False
            down = int(coef_jump_j2*UP_MOVE) #pour éviter le overflow
            if down > 1000 :
                coef_jump_j2 = 100
            pos_j2 = pos_j2.move(0, down)
            coef_jump_j2 = coef_jump_j2*COEF_DOWN

        if pos_j2.y >= height - j2.get_height() - 1:
            alive_j2 = False


        if pos_j1.y >= int(bloc_base.y-((j1.get_height() / 1080) * height)) and pos_j1.x > bloc_base.x + bloc_base.w :
            jump_j1 = False
            if pass_j1 == True :
                coef_jump_j1 = 0.1
                pass_j1 = False
            down = int(coef_jump_j1*UP_MOVE) #pour éviter le overflow
            if down > 1000 :
                coef_jump_j1 = 100
            pos_j1 = pos_j1.move(0, down)
            coef_jump_j1 = coef_jump_j1*COEF_DOWN

        if pos_j1.y >= height - j1.get_height() - 1:
            alive_j1 = False


        if pos_j2.y >= int(bloc_base.y-((j2.get_height() / 1080) * height)) and pos_j2.x > bloc_base.x + bloc_base.w :
            jump_j2 = False
            if pass_j2 == True :
                coef_jump_j2 = 0.1
                pass_j2 = False
            down = int(coef_jump_j2*UP_MOVE) #pour éviter le overflow
            if down > 1000 :
                coef_jump_j2 = 100
            pos_j2 = pos_j2.move(0, down)
            coef_jump_j2 = coef_jump_j2*COEF_DOWN

        if pos_j2.y >= height - j2.get_height() - 1:
            alive_j2 = False

        #recollage des éléments
        if choice_map == 1:
            screen.blit(map_1, pos_map_1)
        if choice_map == 2:
            screen.blit(map_2, pos_map_2)




        if alive_j1 == True :
            if heading_j1 == 1:
                if move_j1 == True:
                    compteur_j1 += 1
                    if compteur_j1 < 10:
                        screen.blit(j1_1, pos_j1)
                    elif compteur_j1 < 20:
                        screen.blit(j1_2, pos_j1)
                    elif compteur_j1 == 20:
                        screen.blit(j1_2, pos_j1)
                        compteur_j1 = 0
                    move_j1 = False

                else:
                    screen.blit(j1, pos_j1)
                    compteur_j1 = 0
            else:
                if move_j1 == True:
                    compteur_j1 += 1
                    if compteur_j1 < 10:
                        screen.blit(j1_flip_1, pos_j1)
                    elif compteur_j1 < 20:
                        screen.blit(j1_flip_2, pos_j1)
                    elif compteur_j1 == 20:
                        screen.blit(j1_flip_2, pos_j1)
                        compteur_j1 = 0
                    move_j1 = False
                else:
                    screen.blit(j1_flip, pos_j1)
                    compteur_j1 = 0
        else :
            game = False
            menu_principale = True
            pos_j1.x = int((345 / 1920) * width)
            pos_j1.y = int(bloc_base.y-((j1.get_height() / 1080) * height))
            pos_j2.x = int((1500 / 1920) * width)
            pos_j2.y = int(bloc_base.y-((j2.get_height() / 1080) * height))
            


        if alive_j2 == True :
            if heading_j2 == 1:
                if move_j2 == True:
                    compteur_j2 += 1
                    if compteur_j2 < 10:
                        screen.blit(j2_1, pos_j2)
                    elif compteur_j2 < 20:
                        screen.blit(j2_2, pos_j2)
                    elif compteur_j2 == 20:
                        screen.blit(j2_2, pos_j2)
                        compteur_j2 = 0
                    move_j2 = False

                else:
                    screen.blit(j2, pos_j2)
                    compteur_j2 = 0
            else:
                if move_j2 == True:
                    compteur_j2 += 1
                    if compteur_j2 < 10:
                        screen.blit(j2_flip_1, pos_j2)
                    elif compteur_j2 < 20:
                        screen.blit(j2_flip_2, pos_j2)
                    elif compteur_j2 == 20:
                        screen.blit(j2_flip_2, pos_j2)
                        compteur_j2 = 0
                    move_j2 = False
                else:
                    screen.blit(j2_flip, pos_j2)
                    compteur_j2 = 0
        else :
            game = False
            menu_principale = True
            pos_j1.x = int((345 / 1920) * width)
            pos_j1.y = int(bloc_base.y-((j1.get_height() / 1080) * height))
            pos_j2.x = int((1500 / 1920) * width)
            pos_j2.y = int(bloc_base.y-((j2.get_height() / 1080) * height))




        #raffraichissement
        #pygame.draw.rect(screen, red, bloc_1)
        #pygame.draw.rect(screen, red, bloc_2)
        #pygame.draw.rect(screen, red, bloc_3)
        #pygame.draw.rect(screen, red, bloc_4)
        #pygame.draw.rect(screen, red, bloc_5)
        #pygame.draw.rect(screen, red, bloc_base)
        pygame.display.flip()

        pygame.time.delay(16)
pygame.quit()
