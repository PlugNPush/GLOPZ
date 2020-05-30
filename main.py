import pygame
from pygame.locals import *
#from function import *
import os
import platform
from pygame import mixer
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
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y),FULLSCREEN)


curdir = os.path.dirname(os.path.realpath(__file__))
#chargement des images
image_wall = pygame.image.load(curdir + "/images/screen_menu.png").convert()
image_wall = pygame.transform.scale(image_wall, (width, height))



#joueur 1
j1 = pygame.image.load(curdir + "/images/chara_1_0.png").convert_alpha()
j1_flip = pygame.image.load(curdir + "/images/chara_1_0_flip.png").convert_alpha()
j1_1 = pygame.image.load(curdir + "/images/chara_1_1.png").convert_alpha()
j1_flip_1 = pygame.image.load(curdir + "/images/chara_1_1_flip.png").convert_alpha()
j1_2 = pygame.image.load(curdir + "/images/chara_1_2.png").convert_alpha()
j1_flip_2 = pygame.image.load(curdir + "/images/chara_1_2_flip.png").convert_alpha()
#resize des sprites joueur
j1 = pygame.transform.scale(j1, (int((42 / 1920) * width), int((84 / 1080) * height)))
j1_flip = pygame.transform.scale(j1_flip, (int((42 / 1920) * width), int((84 / 1080) * height)))
j1_1 = pygame.transform.scale(j1_1, (int((42 / 1920) * width), int((84 / 1080) * height)))
j1_flip_1 = pygame.transform.scale(j1_flip_1, (int((42 / 1920) * width), int((84 / 1080) * height)))
j1_2 = pygame.transform.scale(j1_2, (int((42 / 1920) * width), int((84 / 1080) * height)))
j1_flip_2 = pygame.transform.scale(j1_flip_2, (int((42 / 1920) * width), int((84 / 1080) * height)))
#joueur 2
j2 = pygame.image.load(curdir + "/images/chara_2_0.png").convert_alpha()
j2_flip = pygame.image.load(curdir + "/images/chara_2_0_flip.png").convert_alpha()
j2_1 = pygame.image.load(curdir + "/images/chara_2_1.png").convert_alpha()
j2_flip_1 = pygame.image.load(curdir + "/images/chara_2_1_flip.png").convert_alpha()
j2_2 = pygame.image.load(curdir + "/images/chara_2_2.png").convert_alpha()
j2_flip_2 = pygame.image.load(curdir + "/images/chara_2_2_flip.png").convert_alpha()
j2 = pygame.transform.scale(j2, (int((42 / 1920) * width), int((84 / 1080) * height)))
j2_flip = pygame.transform.scale(j2_flip, (int((42 / 1920) * width), int((84 / 1080) * height)))
j2_1 = pygame.transform.scale(j2_1, (int((42 / 1920) * width), int((84 / 1080) * height)))
j2_flip_1 = pygame.transform.scale(j2_flip_1, (int((42 / 1920) * width), int((84 / 1080) * height)))
j2_2 = pygame.transform.scale(j2_2, (int((42 / 1920) * width), int((84 / 1080) * height)))
j2_flip_2 = pygame.transform.scale(j2_flip_2, (int((42 / 1920) * width), int((84 / 1080) * height)))



#charger les maps
map_1 = pygame.image.load(curdir + "/images/maps/map-1.png").convert()
map_1 = pygame.transform.scale(map_1, (width, height))
map_1_preview = pygame.transform.scale(map_1, (int((384 / 1920) * width), int((216 / 1080) * height)))

map_2 = pygame.image.load(curdir + "/images/maps/map_desert.png").convert()
map_2 = pygame.transform.scale(map_2, (width, height))
map_2_preview = pygame.transform.scale(map_2, (int((384 / 1920) * width), int((216 / 1080) * height)))

map_3 = pygame.image.load(curdir + "/images/maps/hangar.png").convert()
map_3 = pygame.transform.scale(map_3, (width, height))
map_3_preview = pygame.transform.scale(map_3, (int((384 / 1920) * width), int((216 / 1080) * height)))

map_4 = pygame.image.load(curdir + "/images/maps/mars.png").convert()
map_4 = pygame.transform.scale(map_4, (width, height))
map_4_preview = pygame.transform.scale(map_4, (int((384 / 1920) * width), int((216 / 1080) * height)))

pos_map_1 = map_1.get_rect()
pos_map_2 = map_2.get_rect()
pos_map_3 = map_3.get_rect()
pos_map_4 = map_4.get_rect()
pos_map_1_preview = map_1_preview.get_rect()
pos_map_2_preview = map_2_preview.get_rect()
pos_map_3_preview = map_3_preview.get_rect()
pos_map_4_preview = map_4_preview.get_rect()
pos_map_1_preview.x = int((100 / 1920) * width)
pos_map_1_preview.y = int((300 / 1080) * height)
pos_map_2_preview.x = int((550 / 1920) * width)
pos_map_2_preview.y = int((300 / 1080) * height)
pos_map_3_preview.x = int((1000 / 1920) * width)
pos_map_3_preview.y = int((300 / 1080) * height)
pos_map_4_preview.x = int((1450 / 1920) * width)
pos_map_4_preview.y = int((300 / 1080) * height)

retour = pygame.image.load(curdir + "/images/retour_button.png").convert_alpha()
retour = pygame.transform.scale(retour, (int((122 / 1920) * width), int((40 / 1080) * height)))
pos_retour = retour.get_rect()
pos_retour.x = int((10 / 1920) * width)
pos_retour.y = int((10 / 1080) * height)

map1_button = pygame.image.load(curdir + "/images/map1_button.png").convert_alpha()
map1_button = pygame.transform.scale(map1_button, (int((384 / 1920) * width), int((128 / 1080) * height)))
pos_map1_button = map1_button.get_rect()
pos_map1_button.x = int((100 / 1920) * width)
pos_map1_button.y = int((550 / 1080) * height)

map2_button = pygame.image.load(curdir + "/images/map2_button.png").convert_alpha()
map2_button = pygame.transform.scale(map2_button, (int((384 / 1920) * width), int((128 / 1080) * height)))
pos_map2_button = map2_button.get_rect()
pos_map2_button.x = int((550 / 1920) * width)
pos_map2_button.y = int((550 / 1080) * height)

map3_button = pygame.image.load(curdir + "/images/map3_button.png").convert_alpha()
map3_button = pygame.transform.scale(map3_button, (int((384 / 1920) * width), int((128 / 1080) * height)))
pos_map3_button = map3_button.get_rect()
pos_map3_button.x = int((1000 / 1920) * width)
pos_map3_button.y = int((550 / 1080) * height)

map4_button = pygame.image.load(curdir + "/images/map4_button.png").convert_alpha()
map4_button = pygame.transform.scale(map4_button, (int((384 / 1920) * width), int((128 / 1080) * height)))
pos_map4_button = map4_button.get_rect()
pos_map4_button.x = int((1450 / 1920) * width)
pos_map4_button.y = int((550 / 1080) * height)


menu = pygame.image.load(curdir + "/images/menu_button.png").convert_alpha()
pos_menu = menu.get_rect()
pos_menu.x = int(WINDOW_X/2 - (612/2))
pos_menu.y = int(WINDOW_Y/2 - (676/2))

img_info = pygame.image.load(curdir + "/images/info.png").convert_alpha()
pos_info = img_info.get_rect()
pos_info.x = int(WINDOW_X/2 - (1500/2))
pos_info.y = int(WINDOW_Y/2 - (800/2))


face_1 = pygame.image.load(curdir + "/images/chara_1_face.png").convert_alpha()
face_2 = pygame.image.load(curdir + "/images/chara_2_face.png").convert_alpha()
face_3 = pygame.image.load(curdir + "/images/chara_3_face.png").convert_alpha()
face_4 = pygame.image.load(curdir + "/images/chara_4_face.png").convert_alpha()
face_5 = pygame.image.load(curdir + "/images/chara_5_face.png").convert_alpha()
face_6 = pygame.image.load(curdir + "/images/chara_6_face.png").convert_alpha()

face_1 = pygame.transform.scale(face_1, (face_1.get_width()*2, face_1.get_height()*2))
face_2 = pygame.transform.scale(face_2, (face_2.get_width()*2, face_2.get_height()*2))
face_3 = pygame.transform.scale(face_3, (face_3.get_width()*2, face_3.get_height()*2))
face_4 = pygame.transform.scale(face_4, (face_4.get_width()*2, face_4.get_height()*2))
face_5 = pygame.transform.scale(face_5, (face_5.get_width()*2, face_5.get_height()*2))
face_6 = pygame.transform.scale(face_6, (face_6.get_width()*2, face_6.get_height()*2))

#face_1_big = pygame.transform.scale(face_1, (face_1.get_width()*7, face_1.get_height()*7))
#face_2_big = pygame.transform.scale(face_2, (face_2.get_width()*7, face_2.get_height()*7))
#face_3_big = pygame.transform.scale(face_3, (face_3.get_width()*7, face_3.get_height()*7))
#face_4_big = pygame.transform.scale(face_4, (face_4.get_width()*7, face_4.get_height()*7))
#face_5_big = pygame.transform.scale(face_5, (face_5.get_width()*7, face_5.get_height()*7))
#face_6_big = pygame.transform.scale(face_6, (face_6.get_width()*7, face_6.get_height()*7))

fond_vs = pygame.image.load(curdir + "/images/fond_vs.png").convert_alpha()
vs = pygame.image.load(curdir + "/images/vs.png").convert_alpha()
vs = pygame.transform.scale(vs, (int(vs.get_width()/2), int(vs.get_height()/2)))

choix1 = pygame.image.load(curdir + "/images/choix1.png").convert_alpha()
choix2 = pygame.image.load(curdir + "/images/choix2.png").convert_alpha()
#pos_j2 = j2.get_rect()
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

#raffraichissement de l'écran
pygame.display.flip()

#fréquence de répétition des touches
pygame.key.set_repeat(1, 10)


#couleurs
color_rect_players = pygame.Color(200, 200, 200)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
null = pygame.Color(166, 253, 255)
green2 = pygame.Color(26, 54, 63)

# rectangles choix joueurs
button_player1 = pygame.Rect(int((700/ 1920) * width), int((800 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
pygame.draw.rect(screen, red, button_player1)
button_player2 = pygame.Rect(int((900/ 1920) * width), int((800 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
pygame.draw.rect(screen, green, button_player2)
button_player3 = pygame.Rect(int((1100/ 1920) * width), int((800 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
pygame.draw.rect(screen, blue, button_player3)
button_player4 = pygame.Rect(int((700/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
pygame.draw.rect(screen, red, button_player4)
button_player5 = pygame.Rect(int((900/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
pygame.draw.rect(screen, blue, button_player5)
button_player6 = pygame.Rect(int((1100/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
pygame.draw.rect(screen, red, button_player6)
pygame.display.flip()

"""JAUGE"""
#commune 
jauge_100 = pygame.image.load(curdir + "/images/hp_full.png").convert_alpha()

#chargment des jauges de vie J1
jauge_90 = pygame.image.load(curdir + "/images/hp_90.png").convert_alpha()
jauge_80 = pygame.image.load(curdir + "/images/hp_80.png").convert_alpha()
jauge_70 = pygame.image.load(curdir + "/images/hp_70.png").convert_alpha()
jauge_60 = pygame.image.load(curdir + "/images/hp_60.png").convert_alpha()
jauge_50 = pygame.image.load(curdir + "/images/hp_50.png").convert_alpha()
jauge_40 = pygame.image.load(curdir + "/images/hp_40.png").convert_alpha()
jauge_30 = pygame.image.load(curdir + "/images/hp_30.png").convert_alpha()
jauge_20 = pygame.image.load(curdir + "/images/hp_20.png").convert_alpha()
jauge_10 = pygame.image.load(curdir + "/images/hp_10.png").convert_alpha()
jauge_0 = pygame.image.load(curdir + "/images/hp_0.png").convert_alpha()

#redimmension des jauges J1
jauge_100 = pygame.transform.scale(jauge_100, (int(906/5), int(155/5) ))
jauge_90 = pygame.transform.scale(jauge_90, (int(906/5), int(155/5) ))
jauge_80 = pygame.transform.scale(jauge_80, (int(906/5), int(155/5) ))
jauge_70 = pygame.transform.scale(jauge_70, (int(906/5), int(155/5) ))
jauge_60 = pygame.transform.scale(jauge_60, (int(906/5), int(155/5) ))
jauge_50 = pygame.transform.scale(jauge_50, (int(906/5), int(155/5) ))
jauge_40 = pygame.transform.scale(jauge_40, (int(906/5), int(155/5) ))
jauge_30 = pygame.transform.scale(jauge_30, (int(906/5), int(155/5) ))
jauge_20 = pygame.transform.scale(jauge_20, (int(906/5), int(155/5) ))
jauge_10 = pygame.transform.scale(jauge_10, (int(906/5), int(155/5) ))

#charmgement des images flip J2
jauge_90_flip = pygame.image.load(curdir + "/images/hp_90_flip.png").convert_alpha()
jauge_80_flip = pygame.image.load(curdir + "/images/hp_80_flip.png").convert_alpha()
jauge_70_flip = pygame.image.load(curdir + "/images/hp_70_flip.png").convert_alpha()
jauge_60_flip = pygame.image.load(curdir + "/images/hp_60_flip.png").convert_alpha()
jauge_50_flip = pygame.image.load(curdir + "/images/hp_50_flip.png").convert_alpha()
jauge_40_flip = pygame.image.load(curdir + "/images/hp_40_flip.png").convert_alpha()
jauge_30_flip = pygame.image.load(curdir + "/images/hp_30_flip.png").convert_alpha()
jauge_20_flip = pygame.image.load(curdir + "/images/hp_20_flip.png").convert_alpha()
jauge_10_flip = pygame.image.load(curdir + "/images/hp_10_flip.png").convert_alpha()

#redimension des jauges J2
jauge_90_flip  = pygame.transform.scale(jauge_90_flip , (int(906/5), int(155/5) ))
jauge_80_flip  = pygame.transform.scale(jauge_80_flip , (int(906/5), int(155/5) ))
jauge_70_flip  = pygame.transform.scale(jauge_70_flip , (int(906/5), int(155/5) ))
jauge_60_flip  = pygame.transform.scale(jauge_60_flip , (int(906/5), int(155/5) ))
jauge_50_flip  = pygame.transform.scale(jauge_50_flip , (int(906/5), int(155/5) ))
jauge_40_flip  = pygame.transform.scale(jauge_40_flip , (int(906/5), int(155/5) ))
jauge_30_flip  = pygame.transform.scale(jauge_30_flip , (int(906/5), int(155/5) ))
jauge_20_flip  = pygame.transform.scale(jauge_20_flip , (int(906/5), int(155/5) ))
jauge_10_flip  = pygame.transform.scale(jauge_10_flip , (int(906/5), int(155/5) ))

#commmune
jauge_0 = pygame.transform.scale(jauge_0, (int(906/5), int(155/5) ))

#position des jauges
pos_jauge_j1 = (10, 10)
pos_jauge_j2 = (1725, 10)

"""MENU ARMES"""
count_weapon_j1 = 0
count_weapon_j2 = 0

#chargememnt des armes
ak_neutral = pygame.image.load(curdir + "/images/icon/AK/neutral.png").convert_alpha()
grenade_neutral = pygame.image.load(curdir + "/images/icon/grenade/neutral.png").convert_alpha()
uzi_neutral = pygame.image.load(curdir + "/images/icon/UZI/neutral.png").convert_alpha()
rpg_neutral = pygame.image.load(curdir + "/images/icon/RPG/neutral.png").convert_alpha()
shotgun_neutral = pygame.image.load(curdir + "/images/icon/shotgun/neutral.png").convert_alpha()

#redimension des armes
ak_neutral = pygame.transform.scale(ak_neutral, (int(463/10), int(469/10) ))
grenade_neutral = pygame.transform.scale(grenade_neutral, (int(463/10), int(469/10) ))
uzi_neutral = pygame.transform.scale(uzi_neutral, (int(463/10), int(469/10) ))
rpg_neutral = pygame.transform.scale(rpg_neutral, (int(463/10), int(469/10) ))
shotgun_neutral = pygame.transform.scale(shotgun_neutral, (int(463/10), int(469/10) ))

#chargement des armes en utilisation J1
ak_neutral_use = pygame.image.load(curdir + "/images/icon/AK/full.png").convert_alpha()
grenade_neutral_use = pygame.image.load(curdir + "/images/icon/grenade/full.png").convert_alpha()
uzi_neutral_use = pygame.image.load(curdir + "/images/icon/UZI/full.png").convert_alpha()
rpg_neutral_use = pygame.image.load(curdir + "/images/icon/RPG/full.png").convert_alpha()
shotgun_neutral_use = pygame.image.load(curdir + "/images/icon/shotgun/full.png").convert_alpha()

#redimension des armes en utilisation J2
ak_neutral_use = pygame.transform.scale(ak_neutral_use,  (int(463/10), int(469/10) ))
grenade_neutral_use = pygame.transform.scale(grenade_neutral_use,  (int(463/10), int(469/10) ))
uzi_neutral_use = pygame.transform.scale(uzi_neutral_use,  (int(463/10), int(469/10) ))
rpg_neutral_use = pygame.transform.scale(rpg_neutral_use,  (int(463/10), int(469/10) ))
shotgun_neutral_use = pygame.transform.scale(shotgun_neutral_use,  (int(463/10), int(469/10) ))

#positions des armes pour J1
pos_ak_j1 = (10, 1000)
pos_grenade_j1 = (60, 1000)
pos_uzi_j1 = (110, 1000)
pos_rpg_j1 = (160, 1000)
pos_shotgun_j1 = (210, 1000)

#positions des armes pour J2
pos_shotgun_j2 = (WINDOW_X-255, 1000)
pos_rpg_j2 = (WINDOW_X-205, 1000)
pos_uzi_j2 = (WINDOW_X-155, 1000)
pos_grenade_j2 = (WINDOW_X-105, 1000)
pos_ak_j2 = (WINDOW_X-55, 1000)

#boucle en attente d'évènement
on = True
menu_principale = True
menu_personnage = True
menu_map = True
game = True
joueur_1 = True
info = True

while on:
    song_menu = mixer.music.load(curdir + "/audio/music_map_serenite.mp3")
    mixer.music.play(-1)
    game = True
    alive_j1 = True
    alive_j2 = True
    victory = False
    pass_weapon_j1 = True
    pass_weapon_j2 = True
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
                    if event.pos[0] >= (int(WINDOW_X/2 - (612/2))) and event.pos[0] <= (int(WINDOW_X/2 - (612/2)))+612 and event.pos[1] >= (int(WINDOW_Y/2 - (676/2))) and event.pos[1] <= (int(WINDOW_Y/2 - (676/2))) + 203: #play
                        menu_principale = False
                        menu_personnage = True
                        game = True
                        info = False
                        menu_map = True
                        joueur_1 = True
                        joueur_2 = False

                    if event.pos[0] >= (int(WINDOW_X/2 - (612/2))) and event.pos[0] <= (int(WINDOW_X/2 - (612/2)))+612 and event.pos[1] >= (int(WINDOW_Y/2 - (676/2)))+236 and event.pos[1] <= (int(WINDOW_Y/2 - (676/2))) + 441: #exit
                        #pygame.quit()
                        menu_principale = False
                        menu_personnage = False
                        menu_map = False
                        on = False
                        game = False
                        info = False
                        break

                    if event.pos[0] >= (int(WINDOW_X/2 - (612/2))) and event.pos[0] <= (int(WINDOW_X/2 - (612/2)))+612 and event.pos[1] >= (int(WINDOW_Y/2 - (676/2)))+472 and event.pos[1] <= (int(WINDOW_Y/2 - (676/2))) + 676: #info
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
                    if event.pos[0] >= (10 / 1920) * width and event.pos[0] <= (132 / 1920) * width and event.pos[1] >= (10 / 1080) * height and event.pos[1] <= (50 / 1080) * height:
                        menu_principale = True
                        menu_map = False
                        info = False
                        print("RETOUR")
                        break
        screen.blit(image_wall, (BACK_X, BACK_Y))
        screen.blit(retour, pos_retour)
        screen.blit(img_info, pos_info)
        pygame.display.flip()

    while menu_personnage:

        

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                on = False
                break
            elif keys[K_ESCAPE]:
                game = False
                menu_principale = True
                menu_map = False
                victory = False
                menu_personnage = False
            elif event.type == pygame.MOUSEBUTTONUP:

                if joueur_1 is True:
                    if event.button == 1:
                        if event.pos[0] >= (700 / 1920) * width and event.pos[0] <= (800 / 1920) * width and event.pos[1] >= (800 / 1080) * height and event.pos[1] <= (850 / 1080) * height: #rect player1 ; 0 pour x et 1 pour y
                            print("BOUTON 1")
                            curdir_j1 = curdir + "/images/characters/1"
                            j1 = pygame.image.load(curdir + "/images/chara_1_0.png").convert_alpha()
                            j1_flip = pygame.image.load(curdir + "/images/chara_1_0_flip.png").convert_alpha()
                            j1_1 = pygame.image.load(curdir + "/images/chara_1_1.png").convert_alpha()
                            j1_flip_1 = pygame.image.load(curdir + "/images/chara_1_1_flip.png").convert_alpha()
                            j1_2 = pygame.image.load(curdir + "/images/chara_1_2.png").convert_alpha()
                            j1_flip_2 = pygame.image.load(curdir + "/images/chara_1_2_flip.png").convert_alpha()
                            pos_j1 = j1.get_rect()
                            j1_preview = face_1
                            j1 = pygame.transform.scale(j1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip = pygame.transform.scale(j1_flip, (j1.get_width()*2, j1.get_height()*2))
                            j1_1 = pygame.transform.scale(j1_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_1 = pygame.transform.scale(j1_flip_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_2 = pygame.transform.scale(j1_2, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_2 = pygame.transform.scale(j1_flip_2, (j1.get_width()*2, j1.get_height()*2))
                            joueur_1 = False
                            joueur_2 = True
                            break
                        elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player2
                            print("BOUTON 2")
                            curdir_j1 = curdir + "/images/characters/2"
                            j1 = pygame.image.load(curdir + "/images/chara_2_0.png").convert_alpha()
                            j1_flip = pygame.image.load(curdir + "/images/chara_2_0_flip.png").convert_alpha()
                            j1_1 = pygame.image.load(curdir + "/images/chara_2_1.png").convert_alpha()
                            j1_flip_1 = pygame.image.load(curdir + "/images/chara_2_1_flip.png").convert_alpha()
                            j1_2 = pygame.image.load(curdir + "/images/chara_2_2.png").convert_alpha()
                            j1_flip_2 = pygame.image.load(curdir + "/images/chara_2_2_flip.png").convert_alpha()
                            pos_j1 = j1.get_rect()
                            j1_preview = face_2

                            j1 = pygame.transform.scale(j1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip = pygame.transform.scale(j1_flip, (j1.get_width()*2, j1.get_height()*2))
                            j1_1 = pygame.transform.scale(j1_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_1 = pygame.transform.scale(j1_flip_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_2 = pygame.transform.scale(j1_2, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_2 = pygame.transform.scale(j1_flip_2, (j1.get_width()*2, j1.get_height()*2))
                            joueur_1 = False
                            joueur_2 = True
                            break
                        elif event.pos[0] >= 1100 and event.pos[0] <= 1200 and event.pos[1] >= 800 and event.pos[1] <= 850:#rect player3
                            print("BOUTON 3")
                            curdir_j1 = curdir + "/images/characters/3"
                            j1 = pygame.image.load(curdir + "/images/chara_3_0.png").convert_alpha()
                            j1_flip = pygame.image.load(curdir + "/images/chara_3_0_flip.png").convert_alpha()
                            j1_1 = pygame.image.load(curdir + "/images/chara_3_1.png").convert_alpha()
                            j1_flip_1 = pygame.image.load(curdir + "/images/chara_3_1_flip.png").convert_alpha()
                            j1_2 = pygame.image.load(curdir + "/images/chara_3_2.png").convert_alpha()
                            j1_flip_2 = pygame.image.load(curdir + "/images/chara_3_2_flip.png").convert_alpha()
                            pos_j1 = j1.get_rect()
                            j1_preview = face_3

                            j1 = pygame.transform.scale(j1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip = pygame.transform.scale(j1_flip, (j1.get_width()*2, j1.get_height()*2))
                            j1_1 = pygame.transform.scale(j1_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_1 = pygame.transform.scale(j1_flip_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_2 = pygame.transform.scale(j1_2, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_2 = pygame.transform.scale(j1_flip_2, (j1.get_width()*2, j1.get_height()*2))
                            joueur_1 = False
                            joueur_2 = True
                            break
                        elif event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                            print("BOUTON 4")
                            curdir_j1 = curdir + "/images/characters/4"
                            j1 = pygame.image.load(curdir + "/images/chara_4_0.png").convert_alpha()
                            j1_flip = pygame.image.load(curdir + "/images/chara_4_0_flip.png").convert_alpha()
                            j1_1 = pygame.image.load(curdir + "/images/chara_4_1.png").convert_alpha()
                            j1_flip_1 = pygame.image.load(curdir + "/images/chara_4_1_flip.png").convert_alpha()
                            j1_2 = pygame.image.load(curdir + "/images/chara_4_2.png").convert_alpha()
                            j1_flip_2 = pygame.image.load(curdir + "/images/chara_4_2_flip.png").convert_alpha()
                            pos_j1 = j1.get_rect()
                            j1_preview = face_4

                            j1 = pygame.transform.scale(j1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip = pygame.transform.scale(j1_flip, (j1.get_width()*2, j1.get_height()*2))
                            j1_1 = pygame.transform.scale(j1_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_1 = pygame.transform.scale(j1_flip_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_2 = pygame.transform.scale(j1_2, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_2 = pygame.transform.scale(j1_flip_2, (j1.get_width()*2, j1.get_height()*2))
                            joueur_1 = False
                            joueur_2 = True
                            break
                        elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                            print("BOUTON 5")
                            curdir_j1 = curdir + "/images/characters/5"
                            j1 = pygame.image.load(curdir + "/images/chara_5_0.png").convert_alpha()
                            j1_flip = pygame.image.load(curdir + "/images/chara_5_0_flip.png").convert_alpha()
                            j1_1 = pygame.image.load(curdir + "/images/chara_5_1.png").convert_alpha()
                            j1_flip_1 = pygame.image.load(curdir + "/images/chara_5_1_flip.png").convert_alpha()
                            j1_2 = pygame.image.load(curdir + "/images/chara_5_2.png").convert_alpha()
                            j1_flip_2 = pygame.image.load(curdir + "/images/chara_5_2_flip.png").convert_alpha()
                            pos_j1 = j1.get_rect()
                            j1_preview = face_5

                            j1 = pygame.transform.scale(j1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip = pygame.transform.scale(j1_flip, (j1.get_width()*2, j1.get_height()*2))
                            j1_1 = pygame.transform.scale(j1_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_1 = pygame.transform.scale(j1_flip_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_2 = pygame.transform.scale(j1_2, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_2 = pygame.transform.scale(j1_flip_2, (j1.get_width()*2, j1.get_height()*2))
                            joueur_1 = False
                            joueur_2 = True
                            break
                        elif event.pos[0] >= 1100 and event.pos[0] <= 1200 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                            print("BOUTON 6")
                            curdir_j1 = curdir + "/images/characters/6"
                            j1 = pygame.image.load(curdir + "/images/chara_6_0.png").convert_alpha()
                            j1_flip = pygame.image.load(curdir + "/images/chara_6_0_flip.png").convert_alpha()
                            j1_1 = pygame.image.load(curdir + "/images/chara_6_1.png").convert_alpha()
                            j1_flip_1 = pygame.image.load(curdir + "/images/chara_6_1_flip.png").convert_alpha()
                            j1_2 = pygame.image.load(curdir + "/images/chara_6_2.png").convert_alpha()
                            j1_flip_2 = pygame.image.load(curdir + "/images/chara_6_2_flip.png").convert_alpha()
                            pos_j1 = j1.get_rect()
                            j1_preview = face_6

                            j1 = pygame.transform.scale(j1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip = pygame.transform.scale(j1_flip, (j1.get_width()*2, j1.get_height()*2))
                            j1_1 = pygame.transform.scale(j1_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_1 = pygame.transform.scale(j1_flip_1, (j1.get_width()*2, j1.get_height()*2))
                            j1_2 = pygame.transform.scale(j1_2, (j1.get_width()*2, j1.get_height()*2))
                            j1_flip_2 = pygame.transform.scale(j1_flip_2, (j1.get_width()*2, j1.get_height()*2))
                            joueur_1 = False
                            joueur_2 = True
                            break

                if joueur_2 is True:
                    if event.button == 1:
                        if event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player1 ; 0 pour x et 1 pour y 
                            curdir_j2 = curdir + "/images/characters/1"
                            j2 = pygame.image.load(curdir + "/images/chara_1_0.png").convert_alpha()
                            j2_flip = pygame.image.load(curdir + "/images/chara_1_0_flip.png").convert_alpha()
                            j2_1 = pygame.image.load(curdir + "/images/chara_1_1.png").convert_alpha()
                            j2_flip_1 = pygame.image.load(curdir + "/images/chara_1_1_flip.png").convert_alpha()
                            j2_2 = pygame.image.load(curdir + "/images/chara_1_2.png").convert_alpha()
                            j2_flip_2 = pygame.image.load(curdir + "/images/chara_1_2_flip.png").convert_alpha()
                            pos_j2 = j2.get_rect()
                            j2_preview = face_1

                            j2 = pygame.transform.scale(j2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip = pygame.transform.scale(j2_flip, (j2.get_width()*2, j2.get_height()*2))
                            j2_1 = pygame.transform.scale(j2_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_1 = pygame.transform.scale(j2_flip_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_2 = pygame.transform.scale(j2_2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_2 = pygame.transform.scale(j2_flip_2, (j2.get_width()*2, j2.get_height()*2))
                            menu_personnage = False
                            joueur_2 = False
                            break
                        elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 800 and event.pos[1] <= 850: #rect player2
                            curdir_j2 = curdir + "/images/characters/2"
                            j2 = pygame.image.load(curdir + "/images/chara_2_0.png").convert_alpha()
                            j2_flip = pygame.image.load(curdir + "/images/chara_2_0_flip.png").convert_alpha()
                            j2_1 = pygame.image.load(curdir + "/images/chara_2_1.png").convert_alpha()
                            j2_flip_1 = pygame.image.load(curdir + "/images/chara_2_1_flip.png").convert_alpha()
                            j2_2 = pygame.image.load(curdir + "/images/chara_2_2.png").convert_alpha()
                            j2_flip_2 = pygame.image.load(curdir + "/images/chara_2_2_flip.png").convert_alpha()
                            pos_j2 = j2.get_rect()
                            j2_preview = face_2

                            j2 = pygame.transform.scale(j2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip = pygame.transform.scale(j2_flip, (j2.get_width()*2, j2.get_height()*2))
                            j2_1 = pygame.transform.scale(j2_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_1 = pygame.transform.scale(j2_flip_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_2 = pygame.transform.scale(j2_2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_2 = pygame.transform.scale(j2_flip_2, (j2.get_width()*2, j2.get_height()*2))
                            menu_personnage = False
                            joueur_2 = False
                            break
                        elif event.pos[0] >= 1100 and event.pos[0] <= 1200 and event.pos[1] >= 800 and event.pos[1] <= 850:#rect player3
                            curdir_j2 = curdir + "/images/characters/3"
                            j2 = pygame.image.load(curdir + "/images/chara_3_0.png").convert_alpha()
                            j2_flip = pygame.image.load(curdir + "/images/chara_3_0_flip.png").convert_alpha()
                            j2_1 = pygame.image.load(curdir + "/images/chara_3_1.png").convert_alpha()
                            j2_flip_1 = pygame.image.load(curdir + "/images/chara_3_1_flip.png").convert_alpha()
                            j2_2 = pygame.image.load(curdir + "/images/chara_3_2.png").convert_alpha()
                            j2_flip_2 = pygame.image.load(curdir + "/images/chara_3_2_flip.png").convert_alpha()
                            pos_j2 = j2.get_rect()
                            j2_preview = face_3

                            j2 = pygame.transform.scale(j2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip = pygame.transform.scale(j2_flip, (j2.get_width()*2, j2.get_height()*2))
                            j2_1 = pygame.transform.scale(j2_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_1 = pygame.transform.scale(j2_flip_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_2 = pygame.transform.scale(j2_2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_2 = pygame.transform.scale(j2_flip_2, (j2.get_width()*2, j2.get_height()*2))
                            menu_personnage = False
                            joueur_2 = False
                            break
                        elif event.pos[0] >= 700 and event.pos[0] <= 800 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                            curdir_j2 = curdir + "/images/characters/4"
                            j2 = pygame.image.load(curdir + "/images/chara_4_0.png").convert_alpha()
                            j2_flip = pygame.image.load(curdir + "/images/chara_4_0_flip.png").convert_alpha()
                            j2_1 = pygame.image.load(curdir + "/images/chara_4_1.png").convert_alpha()
                            j2_flip_1 = pygame.image.load(curdir + "/images/chara_4_1_flip.png").convert_alpha()
                            j2_2 = pygame.image.load(curdir + "/images/chara_4_2.png").convert_alpha()
                            j2_flip_2 = pygame.image.load(curdir + "/images/chara_4_2_flip.png").convert_alpha()
                            pos_j2 = j2.get_rect()
                            j2_preview = face_4

                            j2 = pygame.transform.scale(j2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip = pygame.transform.scale(j2_flip, (j2.get_width()*2, j2.get_height()*2))
                            j2_1 = pygame.transform.scale(j2_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_1 = pygame.transform.scale(j2_flip_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_2 = pygame.transform.scale(j2_2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_2 = pygame.transform.scale(j2_flip_2, (j2.get_width()*2, j2.get_height()*2))
                            menu_personnage = False
                            joueur_2 = False
                            break
                        elif event.pos[0] >= 900 and event.pos[0] <= 1000 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                            curdir_j2 = curdir + "/images/characters/5"
                            j2 = pygame.image.load(curdir + "/images/chara_5_0.png").convert_alpha()
                            j2_flip = pygame.image.load(curdir + "/images/chara_5_0_flip.png").convert_alpha()
                            j2_1 = pygame.image.load(curdir + "/images/chara_5_1.png").convert_alpha()
                            j2_flip_1 = pygame.image.load(curdir + "/images/chara_5_1_flip.png").convert_alpha()
                            j2_2 = pygame.image.load(curdir + "/images/chara_5_2.png").convert_alpha()
                            j2_flip_2 = pygame.image.load(curdir + "/images/chara_5_2_flip.png").convert_alpha()
                            pos_j2 = j2.get_rect()
                            j2_preview = face_5

                            j2 = pygame.transform.scale(j2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip = pygame.transform.scale(j2_flip, (j2.get_width()*2, j2.get_height()*2))
                            j2_1 = pygame.transform.scale(j2_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_1 = pygame.transform.scale(j2_flip_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_2 = pygame.transform.scale(j2_2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_2 = pygame.transform.scale(j2_flip_2, (j2.get_width()*2, j2.get_height()*2))
                            menu_personnage = False
                            joueur_2 = False
                            break
                        elif event.pos[0] >= 1100 and event.pos[0] <= 1200 and event.pos[1] >= 950 and event.pos[1] <= 1000:#rect player4
                            curdir_j2 = curdir + "/images/characters/6"
                            j2 = pygame.image.load(curdir + "/images/chara_6_0.png").convert_alpha()
                            j2_flip = pygame.image.load(curdir + "/images/chara_6_0_flip.png").convert_alpha()
                            j2_1 = pygame.image.load(curdir + "/images/chara_6_1.png").convert_alpha()
                            j2_flip_1 = pygame.image.load(curdir + "/images/chara_6_1_flip.png").convert_alpha()
                            j2_2 = pygame.image.load(curdir + "/images/chara_6_2.png").convert_alpha()
                            j2_flip_2 = pygame.image.load(curdir + "/images/chara_6_2_flip.png").convert_alpha()
                            pos_j2 = j2.get_rect()
                            j2_preview = face_6

                            j2 = pygame.transform.scale(j2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip = pygame.transform.scale(j2_flip, (j2.get_width()*2, j2.get_height()*2))
                            j2_1 = pygame.transform.scale(j2_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_1 = pygame.transform.scale(j2_flip_1, (j2.get_width()*2, j2.get_height()*2))
                            j2_2 = pygame.transform.scale(j2_2, (j2.get_width()*2, j2.get_height()*2))
                            j2_flip_2 = pygame.transform.scale(j2_flip_2, (j2.get_width()*2, j2.get_height()*2))
                            menu_personnage = False
                            joueur_2 = False
                            break
        screen.blit(fond_vs, (BACK_X, BACK_Y))

        rect_separation = pygame.Rect(int((WINDOW_X/2)/ 1920 * width), int((0 / 1080) * height), int((2 / 1920) * width), int((WINDOW_Y / 1080) * height))
        pygame.draw.rect(screen, red, rect_separation)
        rect_players_choice = pygame.Rect(int((0/ 1920) * width), int((700 / 1080) * height), int((WINDOW_X / 1920) * width), int((WINDOW_Y / 1080) * height))
        pygame.draw.rect(screen, color_rect_players, rect_players_choice)
        button_player1 = pygame.Rect(int((700/ 1920) * width), int((800 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
        pygame.draw.rect(screen, green2, button_player1)
        button_player2 = pygame.Rect(int((900/ 1920) * width), int((800 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
        pygame.draw.rect(screen, green2, button_player2)
        button_player3 = pygame.Rect(int((1100/ 1920) * width), int((800 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
        pygame.draw.rect(screen, green2, button_player3)
        button_player4 = pygame.Rect(int((700/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
        pygame.draw.rect(screen, green2, button_player4)
        button_player5 = pygame.Rect(int((900/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
        pygame.draw.rect(screen, green2, button_player5)
        button_player6 = pygame.Rect(int((1100/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
        pygame.draw.rect(screen, green2, button_player6)
        screen.blit(vs, (int((WINDOW_X/2)-vs.get_width()/2), int(((WINDOW_X/2)/2)/2)))
        screen.blit(face_1, (int(button_player1.x+(button_player1.w/2)-face_1.get_width()/2), int(button_player1.y-face_1.get_height()+20)))
        screen.blit(face_2, (int(button_player2.x+(button_player2.w/2)-face_2.get_width()/2), int(button_player2.y-face_2.get_height()+20)))
        screen.blit(face_3, (int(button_player3.x+(button_player3.w/2)-face_3.get_width()/2), int(button_player3.y-face_3.get_height()+20)))
        screen.blit(face_4, (int(button_player4.x+(button_player4.w/2)-face_4.get_width()/2), int(button_player4.y-face_4.get_height()+20)))
        screen.blit(face_5, (int(button_player5.x+(button_player5.w/2)-face_5.get_width()/2), int(button_player5.y-face_5.get_height()+20)))
        screen.blit(face_6, (int(button_player6.x+(button_player6.w/2)-face_6.get_width()/2), int(button_player6.y-face_6.get_height()+20)))
        if joueur_1 == True:
            screen.blit(choix1, (100, int((3/4)*WINDOW_Y)))
        if joueur_2 == True:
            screen.blit(choix2, (WINDOW_X-100-choix2.get_width(), int((3/4)*WINDOW_Y)))
        if joueur_1 == False and joueur_2 == True:
            j1_preview_bis = pygame.transform.scale(j1_preview, (j1_preview.get_width()*7, j1_preview.get_height()*7))
            screen.blit(j1_preview_bis, (int(((WINDOW_X/2)/2)-j1_preview_bis.get_width()/2), 50))
        if joueur_1 == False and joueur_2 == False:
            j2_preview_bis = pygame.transform.scale(j2_preview, (j2_preview.get_width()*7, j2_preview.get_height()*7))
            screen.blit(j2_preview_bis, (int(((WINDOW_X/2)+(WINDOW_X/2)/2)-j2_preview_bis.get_width()/2), 50))
            screen.blit(j1_preview_bis, ((int(((WINDOW_X/2)/2)-j1_preview_bis.get_width()/2), 50)))
        pygame.display.flip()
        if joueur_1 == False and joueur_2 == False:
            pygame.time.delay(1000)

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
                        mixer.music.stop()
                        song_map1 = mixer.music.load(curdir + "/audio/music_map_la_street.mp3")
                        mixer.music.play(-1)
                        UP_MOVE = 30
                        COEF_UP = 1.1
                        COEF_DOWN = 1.1
                        choice_map = 1
                        count_bloc = 3
                        bloc_1 = pygame.Rect(int((521/ 1920) * width), int((537 / 1080) * height), int((260 / 1920) * width), int((58 / 1080) * height))
                        bloc_2 = pygame.Rect(int((1050/ 1920) * width), int((539 / 1080) * height), int((260 / 1920) * width), int((58 / 1080) * height))
                        bloc_3 = pygame.Rect(int((765/ 1920) * width), int((335 / 1080) * height), int((260 / 1920) * width), int((58 / 1080) * height))
                        bloc_base = pygame.Rect(int((313/ 1920) * width), int((751 / 1080) * height), int((1263 / 1920) * width), int((300 / 1080) * height))
                        pos_j1.x = int((345 / 1920) * width)
                        pos_j1.y = int(bloc_base.y-j1.get_height())
                        pos_j2.x = int((1500 / 1920) * width)
                        pos_j2.y = int(bloc_base.y-j2.get_height())
                        break
                    
                    if event.pos[0] >= pos_map2_button.x and event.pos[0] <= pos_map2_button.x + map2_button.get_width() and event.pos[1] >= pos_map2_button.y and event.pos[1] <= pos_map2_button.y + map2_button.get_height():
                        menu_map = False
                        game = True
                        mixer.music.stop()
                        song_map2 = mixer.music.load(curdir + "/audio/music_map_tension.mp3")
                        mixer.music.play(-1)
                        UP_MOVE = 30
                        COEF_UP = 1.1
                        COEF_DOWN = 1.2
                        choice_map = 2
                        count_bloc = 5
                        bloc_1 = pygame.Rect(int((104/ 1920) * width), int((649 / 1080) * height), int((1718 / 1920) * width), int((200 / 1080) * height))
                        bloc_2 = pygame.Rect(int((200/ 1920) * width), int((550 / 1080) * height), int((797 / 1920) * width), int((200 / 1080) * height))
                        bloc_3 = pygame.Rect(int((1234/ 1920) * width), int((550 / 1080) * height), int((398 / 1920) * width), int((200 / 1080) * height))
                        bloc_4 = pygame.Rect(int((408/ 1920) * width), int((450 / 1080) * height), int((101 / 1920) * width), int((200 / 1080) * height))
                        bloc_5 = pygame.Rect(int((1426/ 1920) * width), int((450 / 1080) * height), int((101 / 1920) * width), int((200 / 1080) * height))
                        bloc_base = pygame.Rect(int((0/ 1920) * width), int((749 / 1080) * height), int((1920 / 1920) * width), int((300 / 1080) * height))
                        pos_j1.x = int((0 / 1920) * width)
                        pos_j1.y = int(bloc_base.y-j1.get_height())
                        pos_j2.x = int((1850 / 1920) * width)
                        pos_j2.y = int(bloc_base.y-j2.get_height())
                        break

                    if event.pos[0] >= pos_map3_button.x and event.pos[0] <= pos_map3_button.x + map3_button.get_width() and event.pos[1] >= pos_map3_button.y and event.pos[1] <= pos_map3_button.y + map3_button.get_height():
                        menu_map = False
                        game = True
                        mixer.music.stop()
                        song_map3 = mixer.music.load(curdir + "/audio/music_map_festif.mp3")
                        mixer.music.play(-1)
                        UP_MOVE = 30
                        COEF_UP = 1.08
                        COEF_DOWN = 1.1
                        choice_map = 3
                        count_bloc = 1
                        bloc_1 = pygame.Rect(int((321/ 1920) * width), int((587 / 1080) * height), int((1251 / 1920) * width), int((60 / 1080) * height))
                        bloc_base = pygame.Rect(int((0/ 1920) * width), int((884 / 1080) * height), int((1920 / 1920) * width), int((300 / 1080) * height))
                        pos_j1.x = int((100 / 1920) * width)
                        pos_j1.y = int(bloc_base.y-j1.get_height())
                        pos_j2.x = int((1820 / 1920) * width)
                        pos_j2.y = int(bloc_base.y-j2.get_height())
                        break
                        
                    if event.pos[0] >= pos_map4_button.x and event.pos[0] <= pos_map4_button.x + map4_button.get_width() and event.pos[1] >= pos_map4_button.y and event.pos[1] <= pos_map4_button.y + map4_button.get_height():
                        menu_map = False
                        game = True
                        mixer.music.stop()
                        song_map4 = mixer.music.load(curdir + "/audio/music_map_bataille.mp3")
                        mixer.music.play(-1)
                        UP_MOVE = 30
                        COEF_UP = 1.03
                        COEF_DOWN = 1.03
                        choice_map = 4
                        count_bloc = 0
                        bloc_base = pygame.Rect(int((0/ 1920) * width), int((1000 / 1080) * height), int((1920 / 1920) * width), int((300 / 1080) * height))
                        pos_j1.x = int((100 / 1920) * width)
                        pos_j1.y = int(bloc_base.y-j1.get_height())
                        pos_j2.x = int((1820 / 1920) * width)
                        pos_j2.y = int(bloc_base.y-j2.get_height())
                        break
        screen.blit(image_wall, (BACK_X, BACK_Y))
        screen.blit(map_1_preview, pos_map_1_preview)
        screen.blit(map_2_preview, pos_map_2_preview)
        screen.blit(map_3_preview, pos_map_3_preview)
        screen.blit(map_4_preview, pos_map_4_preview)
        screen.blit(map1_button, pos_map1_button)
        screen.blit(map2_button, pos_map2_button)
        screen.blit(map3_button, pos_map3_button)
        screen.blit(map4_button, pos_map4_button)
        pygame.display.flip()
        
    UP_MOVE = int((UP_MOVE / 1080) * height)
    SIDE_MOVE = int((SIDE_MOVE / 1920) * width)
    count_weapon_j1 = 1
    count_weapon_j2 = 1
    pass_blit_j1 = True
    pass_blit_j2 = True
    while game:
        

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            
            if event.type == QUIT:
                on = False
                break
            elif keys[K_ESCAPE]:
                game = False
                menu_principale = True
                menu_map = True

#switch des armes
            elif keys[K_e]:
                if pass_weapon_j1 is True:
                    count_weapon_j1 += 1
                    pass_weapon_j1 = False
                    pass_blit_j1 = True
            else:
                pass_weapon_j1 = True   

            if keys[K_RSHIFT]:
                if pass_weapon_j2 is True:
                    count_weapon_j2 += 1
                    pass_weapon_j2 = False
                    pass_blit_j2 = True
            else:
                pass_weapon_j2 = True

                 

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
            if pos_j1.x+j1.get_width() > bloc_1.x and pos_j1.x+j1.get_width() < bloc_1.x+((15 / 1920) * width) and pos_j1.y < bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() > bloc_1.y:
                pos_j1.x = bloc_1.x-j1.get_width()-1 #par le coté gauche
                

            if pos_j1.x < bloc_1.x+bloc_1.w and pos_j1.x > bloc_1.x+bloc_1.w - ((15 / 1920) * width) and pos_j1.y < bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() > bloc_1.y:
                pos_j1.x = bloc_1.x+bloc_1.w +1  #par le coté droit

            if pos_j1.x+j1.get_width() >= bloc_1.x and pos_j1.x <= bloc_1.x+bloc_1.w and pos_j1.y <= bloc_1.y+bloc_1.h and pos_j1.y >= bloc_1.y:
                pos_j1.y = bloc_1.y+bloc_1.h +1 #par dessous
                jump_j1 = False
                

            if pos_j1.x+j1.get_width() >= bloc_1.x and pos_j1.x <= bloc_1.x+bloc_1.w and pos_j1.y+j1.get_height() <= bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() >= bloc_1.y:
                pos_j1.y = bloc_1.y-j1.get_height() #par dessus
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_1.x and pos_j2.x+j2.get_width() < bloc_1.x+((15 / 1920) * width) and pos_j2.y < bloc_1.y+bloc_1.h and pos_j2.y+j2.get_height() > bloc_1.y:
                pos_j2.x = bloc_1.x-j2.get_width()-1

            if pos_j2.x < bloc_1.x+bloc_1.w and pos_j2.x > bloc_1.x+bloc_1.w - ((15 / 1920) * width) and pos_j2.y < bloc_1.y+bloc_1.h and pos_j2.y+j2.get_height() > bloc_1.y:
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
            if pos_j1.x+j1.get_width() > bloc_2.x and pos_j1.x+j1.get_width() < bloc_2.x+((15 / 1920) * width) and pos_j1.y < bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() > bloc_2.y:
                pos_j1.x = bloc_2.x-j1.get_width()-1

            if pos_j1.x < bloc_2.x+bloc_2.w and pos_j1.x > bloc_2.x+bloc_2.w - ((15 / 1920) * width) and pos_j1.y < bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() > bloc_2.y:
                pos_j1.x = bloc_2.x+bloc_2.w +1

            if pos_j1.x+j1.get_width() >= bloc_2.x and pos_j1.x <= bloc_2.x+bloc_2.w and pos_j1.y <= bloc_2.y+bloc_2.h and pos_j1.y >= bloc_2.y:
                pos_j1.y = bloc_2.y+bloc_2.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_2.x and pos_j1.x <= bloc_2.x+bloc_2.w and pos_j1.y+j1.get_height() <= bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() >= bloc_2.y:
                pos_j1.y = bloc_2.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_2.x and pos_j2.x+j2.get_width() < bloc_2.x+((15 / 1920) * width) and pos_j2.y < bloc_2.y+bloc_2.h and pos_j2.y+j2.get_height() > bloc_2.y:
                pos_j2.x = bloc_2.x-j2.get_width()-1

            if pos_j2.x < bloc_2.x+bloc_2.w and pos_j2.x > bloc_2.x+bloc_2.w - ((15 / 1920) * width) and pos_j2.y < bloc_2.y+bloc_2.h and pos_j2.y+j2.get_height() > bloc_2.y:
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
            if pos_j1.x+j1.get_width() > bloc_3.x and pos_j1.x+j1.get_width() < bloc_3.x+((15 / 1920) * width) and pos_j1.y < bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() > bloc_3.y:
                pos_j1.x = bloc_3.x-j1.get_width()-1

            if pos_j1.x < bloc_3.x+bloc_3.w and pos_j1.x > bloc_3.x+bloc_3.w - ((15 / 1920) * width) and pos_j1.y < bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() > bloc_3.y:
                pos_j1.x = bloc_3.x+bloc_3.w +1

            if pos_j1.x+j1.get_width() >= bloc_3.x and pos_j1.x <= bloc_3.x+bloc_3.w and pos_j1.y <= bloc_3.y+bloc_3.h and pos_j1.y >= bloc_3.y:
                pos_j1.y = bloc_3.y+bloc_3.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_3.x and pos_j1.x <= bloc_3.x+bloc_3.w and pos_j1.y+j1.get_height() <= bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() >= bloc_3.y:
                pos_j1.y = bloc_3.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_3.x and pos_j2.x+j2.get_width() < bloc_3.x+((15 / 1920) * width) and pos_j2.y < bloc_3.y+bloc_3.h and pos_j2.y+j2.get_height() > bloc_3.y:
                pos_j2.x = bloc_3.x-j2.get_width()-1

            if pos_j2.x < bloc_3.x+bloc_3.w and pos_j2.x > bloc_3.x+bloc_3.w - ((15 / 1920) * width) and pos_j2.y < bloc_3.y+bloc_3.h and pos_j2.y+j2.get_height() > bloc_3.y:
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
            if pos_j1.x+j1.get_width() > bloc_4.x and pos_j1.x+j1.get_width() < bloc_4.x+((15 / 1920) * width) and pos_j1.y < bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() > bloc_4.y:
                pos_j1.x = bloc_4.x-j1.get_width()-1

            if pos_j1.x < bloc_4.x+bloc_4.w and pos_j1.x > bloc_4.x+bloc_4.w - ((15 / 1920) * width) and pos_j1.y < bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() > bloc_4.y:
                pos_j1.x = bloc_4.x+bloc_4.w +1

            if pos_j1.x+j1.get_width() >= bloc_4.x and pos_j1.x <= bloc_4.x+bloc_4.w and pos_j1.y <= bloc_4.y+bloc_4.h and pos_j1.y >= bloc_4.y:
                pos_j1.y = bloc_4.y+bloc_4.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_4.x and pos_j1.x <= bloc_4.x+bloc_4.w and pos_j1.y+j1.get_height() <= bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() >= bloc_4.y:
                pos_j1.y = bloc_4.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_4.x and pos_j2.x+j2.get_width() < bloc_4.x+((15 / 1920) * width) and pos_j2.y < bloc_4.y+bloc_4.h and pos_j2.y+j2.get_height() > bloc_4.y:
                pos_j2.x = bloc_4.x-j2.get_width()-1

            if pos_j2.x < bloc_4.x+bloc_4.w and pos_j2.x > bloc_4.x+bloc_4.w - ((15 / 1920) * width) and pos_j2.y < bloc_4.y+bloc_4.h and pos_j2.y+j2.get_height() > bloc_4.y:
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
            if pos_j1.x+j1.get_width() > bloc_5.x and pos_j1.x+j1.get_width() < bloc_5.x+((15 / 1920) * width) and pos_j1.y < bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() > bloc_5.y:
                pos_j1.x = bloc_5.x-j1.get_width()-1

            if pos_j1.x < bloc_5.x+bloc_5.w and pos_j1.x > bloc_5.x+bloc_5.w - ((15 / 1920) * width) and pos_j1.y < bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() > bloc_5.y:
                pos_j1.x = bloc_5.x+bloc_5.w +1

            if pos_j1.x+j1.get_width() >= bloc_5.x and pos_j1.x <= bloc_5.x+bloc_5.w and pos_j1.y <= bloc_5.y+bloc_5.h and pos_j1.y >= bloc_5.y:
                pos_j1.y = bloc_5.y+bloc_5.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_5.x and pos_j1.x <= bloc_5.x+bloc_5.w and pos_j1.y+j1.get_height() <= bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() >= bloc_5.y:
                pos_j1.y = bloc_5.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_5.x and pos_j2.x+j2.get_width() < bloc_5.x+((15 / 1920) * width) and pos_j2.y < bloc_5.y+bloc_5.h and pos_j2.y+j2.get_height() > bloc_5.y:
                pos_j2.x = bloc_5.x-j2.get_width()-1

            if pos_j2.x < bloc_5.x+bloc_5.w and pos_j2.x > bloc_5.x+bloc_5.w - ((15 / 1920) * width) and pos_j2.y < bloc_5.y+bloc_5.h and pos_j2.y+j2.get_height() > bloc_5.y:
                pos_j2.x = bloc_5.x+bloc_5.w +1

            if pos_j2.x+j2.get_width() >= bloc_5.x and pos_j2.x <= bloc_5.x+bloc_5.w and pos_j2.y <= bloc_5.y+bloc_5.h and pos_j2.y >= bloc_5.y:
                pos_j2.y = bloc_5.y+bloc_5.h +1
                jump_j2 = False

            if pos_j2.x+j2.get_width() >= bloc_5.x and pos_j2.x <= bloc_5.x+bloc_5.w and pos_j2.y+j2.get_height() <= bloc_5.y+bloc_5.h and pos_j2.y+j2.get_height() >= bloc_5.y:
                pos_j2.y = bloc_5.y-j2.get_height()
                coef_jump_j2 = float(1)
                pass_j2 = True
                jump_j2 = True


        if pos_j1.y == int(bloc_base.y-j1.get_height()) and pos_j1.x > bloc_base.x and pos_j1.x < bloc_base.x + bloc_base.w:
            coef_jump_j1 = float(1)
            pass_j1 = True
            jump_j1 = True

        if pos_j2.y == int(bloc_base.y-j2.get_height()):
            coef_jump_j2 = float(1)
            pass_j2 = True
            jump_j2 = True


        if pos_j1.y >= int(bloc_base.y-j1.get_height()) and pos_j1.x > bloc_base.x and pos_j1.x < bloc_base.x + bloc_base.w:
            pos_j1.y = int(bloc_base.y-j1.get_height())

        if pos_j2.y >= int(bloc_base.y-j2.get_height()) and pos_j2.x > bloc_base.x and pos_j2.x < bloc_base.x + bloc_base.w:
            pos_j2.y = int(bloc_base.y-j2.get_height())



        if pos_j1.y >= int(bloc_base.y-j1.get_height()) and pos_j1.x+j1.get_width() < bloc_base.x :
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


        if pos_j2.y >= int(bloc_base.y-j2.get_height()) and pos_j2.x+j2.get_width() < bloc_base.x :
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


        if pos_j1.y >= int(bloc_base.y-j1.get_height()) and pos_j1.x > bloc_base.x + bloc_base.w :
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


        if pos_j2.y >= int(bloc_base.y-j2.get_height()) and pos_j2.x > bloc_base.x + bloc_base.w :
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
        if choice_map == 3:
            screen.blit(map_3, pos_map_3)
        if choice_map == 4:
            screen.blit(map_4, pos_map_4)

        if pass_blit_j1 == True:
            if count_weapon_j1 == 6:
                count_weapon_j1 = 1
            if count_weapon_j1 == 1: #AK
                j1_base = pygame.image.load(curdir_j1 + "/AK/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/AK/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/AK/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/AK/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/AK/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/AK/2_flip.png").convert_alpha()
            elif count_weapon_j1 == 2: #grenade
                j1_base = pygame.image.load(curdir_j1 + "/grenade/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/grenade/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/grenade/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/grenade/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/grenade/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/grenade/2_flip.png").convert_alpha()
            elif count_weapon_j1 == 3: #uzi
                j1_base = pygame.image.load(curdir_j1 + "/UZI/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/UZI/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/UZI/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/UZI/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/UZI/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/UZI/2_flip.png").convert_alpha()
            elif count_weapon_j1 == 4: #rpg
                j1_base = pygame.image.load(curdir_j1 + "/RPG/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/RPG/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/RPG/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/RPG/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/RPG/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/RPG/2_flip.png").convert_alpha()
            elif count_weapon_j1 == 5: #shotgun
                j1_base = pygame.image.load(curdir_j1 + "/shotgun/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/shotgun/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/shotgun/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/shotgun/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/shotgun/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/shotgun/2_flip.png").convert_alpha()
            j1 = pygame.transform.scale(j1_base, (j1_base.get_width()*2, j1_base.get_height()*2))
            j1_flip = pygame.transform.scale(j1_base_flip, (j1_base.get_width()*2, j1_base.get_height()*2))
            j1_1 = pygame.transform.scale(j1_base_1, (j1_base.get_width()*2, j1_base.get_height()*2))
            j1_flip_1 = pygame.transform.scale(j1_base_flip_1, (j1_base.get_width()*2, j1_base.get_height()*2))
            j1_2 = pygame.transform.scale(j1_base_2, (j1_base.get_width()*2, j1_base.get_height()*2))
            j1_flip_2 = pygame.transform.scale(j1_base_flip_2, (j1_base.get_width()*2, j1_base.get_height()*2))
            pass_blit_j1 = False


        if pass_blit_j2 == True:
            if count_weapon_j2 == 6:
                count_weapon_j2 = 1
            if count_weapon_j2 == 1: #AK
                j2_base = pygame.image.load(curdir_j2 + "/AK/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/AK/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/AK/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/AK/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/AK/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/AK/2_flip.png").convert_alpha()
            elif count_weapon_j2 == 2: #grenade
                j2_base = pygame.image.load(curdir_j2 + "/grenade/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/grenade/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/grenade/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/grenade/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/grenade/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/grenade/2_flip.png").convert_alpha()
            elif count_weapon_j2 == 3: #uzi
                j2_base = pygame.image.load(curdir_j2 + "/UZI/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/UZI/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/UZI/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/UZI/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/UZI/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/UZI/2_flip.png").convert_alpha()
            elif count_weapon_j2 == 4: #rpg
                j2_base = pygame.image.load(curdir_j2 + "/RPG/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/RPG/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/RPG/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/RPG/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/RPG/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/RPG/2_flip.png").convert_alpha()
            elif count_weapon_j2 == 5: #shotgun
                j2_base = pygame.image.load(curdir_j2 + "/shotgun/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/shotgun/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/shotgun/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/shotgun/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/shotgun/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/shotgun/2_flip.png").convert_alpha()
            j2 = pygame.transform.scale(j2_base, (j2_base.get_width()*2, j2_base.get_height()*2))
            j2_flip = pygame.transform.scale(j2_base_flip, (j2_base.get_width()*2, j2_base.get_height()*2))
            j2_1 = pygame.transform.scale(j2_base_1, (j2_base.get_width()*2, j2_base.get_height()*2))
            j2_flip_1 = pygame.transform.scale(j2_base_flip_1, (j2_base.get_width()*2, j2_base.get_height()*2))
            j2_2 = pygame.transform.scale(j2_base_2, (j2_base.get_width()*2, j2_base.get_height()*2))
            j2_flip_2 = pygame.transform.scale(j2_base_flip_2, (j2_base.get_width()*2, j2_base.get_height()*2))
            pass_blit_j2 = False
        

        


        if alive_j1 == True :
            if heading_j1 == 1:
                if move_j1 == True: #si je joueur a bougé
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
            mixer.music.stop()
            winner = 2
            victory = True
            pos_j1.x = int(int((345 / 1920) * width))
            pos_j1.y = int(bloc_base.y-((j1.get_height() / 1080) * height))
            pos_j2.x = int(int((1500 / 1920) * width))
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
            mixer.music.stop()
            winner = 1
            victory = True
            pos_j1.x = int(int((345 / 1920) * width))
            pos_j1.y = int(bloc_base.y-((j1.get_height() / 1080) * height))
            pos_j2.x = int(int((1500 / 1920) * width))
            pos_j2.y = int(bloc_base.y-((j2.get_height() / 1080) * height))


        """AFFICHAGE DES JAUGES DE VIE J1"""
        screen.blit(jauge_100, pos_jauge_j1)

        """AFFICHAGE DES JAUGES DE VIE J2"""
        screen.blit(jauge_100, pos_jauge_j2)

        """AFFICHAGE DES ARMES J1"""
        screen.blit(ak_neutral, pos_ak_j1)
        screen.blit(grenade_neutral, pos_grenade_j1)
        screen.blit(uzi_neutral, pos_uzi_j1)
        screen.blit(rpg_neutral, pos_rpg_j1)
        screen.blit(shotgun_neutral, pos_shotgun_j1)

        """AFFICHAGE DES ARMES J2"""
        screen.blit(shotgun_neutral, pos_shotgun_j2)
        screen.blit(rpg_neutral, pos_rpg_j2)
        screen.blit(uzi_neutral, pos_uzi_j2)
        screen.blit(grenade_neutral, pos_grenade_j2)
        screen.blit(ak_neutral, pos_ak_j2)

        """COMPTEUR SWITCH ARMES J1"""
        if count_weapon_j1 == 6:
            count_weapon_j1 = 1
        if count_weapon_j1 == 1:
            screen.blit(ak_neutral_use, pos_ak_j1)
        elif count_weapon_j1 == 2:
            screen.blit(grenade_neutral_use, pos_grenade_j1)
        elif count_weapon_j1 == 3:
            screen.blit(uzi_neutral_use, pos_uzi_j1)
        elif count_weapon_j1 == 4:
            screen.blit(rpg_neutral_use, pos_rpg_j1)
        elif count_weapon_j1 == 5:
            screen.blit(shotgun_neutral_use, pos_shotgun_j1)

        """COMPTEUR SWITCH ARMES J2"""
        if count_weapon_j2 == 6:
            count_weapon_j2 = 1
        if count_weapon_j2 == 1:
            screen.blit(ak_neutral_use, pos_ak_j2)
        elif count_weapon_j2 == 2:
            screen.blit(grenade_neutral_use, pos_grenade_j2)
        elif count_weapon_j2 == 3:
            screen.blit(uzi_neutral_use, pos_uzi_j2)
        elif count_weapon_j2 == 4:
            screen.blit(rpg_neutral_use, pos_rpg_j2)
        elif count_weapon_j2 == 5:
            screen.blit(shotgun_neutral_use, pos_shotgun_j2)

        #raffraichissement
        #pygame.draw.rect(screen, red, bloc_1)
        #pygame.draw.rect(screen, red, bloc_2)
        #pygame.draw.rect(screen, red, bloc_3)
        #pygame.draw.rect(screen, red, bloc_4)
        #pygame.draw.rect(screen, red, bloc_5)
        #pygame.draw.rect(screen, red, bloc_base)
        pygame.display.flip()

        pygame.time.delay(16)
    passage = True
    while victory == True :
        if winner == 1 :
            if passage == True :
                win_background = pygame.image.load(curdir + "/images/j1_win.png").convert()
                passage = False
        else :
            if passage == True :
                win_background = pygame.image.load(curdir + "/images/j2_win.png").convert()
                passage = False
        
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
                    if event.pos[0] >= (522 / 1920) * width and event.pos[0] <= (662 / 1920) * width and event.pos[1] >= (736 / 1080) * height and event.pos[1] <= (822 / 1080) * height:
                        victory = False
                        menu_principale = True

        screen.blit(win_background, (BACK_X, BACK_Y))
        pygame.display.flip()
        
pygame.quit()
