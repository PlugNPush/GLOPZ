import pygame
from pygame.locals import *
#from function import *
import os
import platform
from pygame import mixer
from math import cos
from math import sin
from math import pi
from math import sqrt
from math import exp
from math import tan
from random import uniform
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


fpsClock = pygame.time.Clock()

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



fond_vs = pygame.image.load(curdir + "/images/fond_vs.png").convert_alpha()
fond_vs = pygame.transform.scale(fond_vs, (width, int((736/1080)* height)))
vs = pygame.image.load(curdir + "/images/vs.png").convert_alpha()
vs = pygame.transform.scale(vs, (int(vs.get_width()/2), int(vs.get_height()/2)))

choix1 = pygame.image.load(curdir + "/images/choix1.png").convert_alpha()
choix2 = pygame.image.load(curdir + "/images/choix2.png").convert_alpha()
choix1 = pygame.transform.scale(choix1, (int((300 / 1920) * width) , int((200 / 1080) * height)))
choix2 = pygame.transform.scale(choix2, (int((300 / 1920) * width) , int((200 / 1080) * height)))

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
button_player2 = pygame.Rect(int((900/ 1920) * width), int((800 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
button_player3 = pygame.Rect(int((1100/ 1920) * width), int((800 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
button_player4 = pygame.Rect(int((700/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
button_player5 = pygame.Rect(int((900/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
button_player6 = pygame.Rect(int((1100/ 1920) * width), int((950 / 1080) * height), int((100 / 1920) * width), int((50 / 1080) * height))
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
jauge_100 = pygame.transform.scale(jauge_100, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_90 = pygame.transform.scale(jauge_90, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_80 = pygame.transform.scale(jauge_80, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_70 = pygame.transform.scale(jauge_70, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_60 = pygame.transform.scale(jauge_60, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_50 = pygame.transform.scale(jauge_50, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_40 = pygame.transform.scale(jauge_40, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_30 = pygame.transform.scale(jauge_30, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_20 = pygame.transform.scale(jauge_20, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_10 = pygame.transform.scale(jauge_10, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))

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
jauge_90_flip  = pygame.transform.scale(jauge_90_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_80_flip  = pygame.transform.scale(jauge_80_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_70_flip  = pygame.transform.scale(jauge_70_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_60_flip  = pygame.transform.scale(jauge_60_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_50_flip  = pygame.transform.scale(jauge_50_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_40_flip  = pygame.transform.scale(jauge_40_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_30_flip  = pygame.transform.scale(jauge_30_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_20_flip  = pygame.transform.scale(jauge_20_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))
jauge_10_flip  = pygame.transform.scale(jauge_10_flip , (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))

#commmune
jauge_0 = pygame.transform.scale(jauge_0, (int((906/5) / 1920 * width), int((155/5) / 1080 * height)))

#position des jauges
pos_jauge_j1 = ((10 / 1920) * width, (10 / 1080) * height)
pos_jauge_j2 = ((1725 / 1920) * width, (10 / 1080) * height)

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

bullet1 = pygame.image.load(curdir + "/images/balle1.png")
bullet2 = pygame.image.load(curdir + "/images/grenade2.png")
bullet3 = pygame.image.load(curdir + "/images/balle2.png")
bullet4 = pygame.image.load(curdir + "/images/balle4.png")
bullet5 = pygame.image.load(curdir + "/images/balle3.png")

bullet1 = pygame.transform.scale(bullet1, (int((4 / 1920) * width), int((4 / 1080) * height)))
bullet2 = pygame.transform.scale(bullet2, (int((20 / 1920) * width), int((21 / 1080) * height)))
bullet3 = pygame.transform.scale(bullet3, (int((4 / 1920) * width), int((4 / 1080) * height)))
bullet4 = pygame.transform.scale(bullet4, (int((23 / 1920) * width), int((5 / 1080) * height)))
bullet5 = pygame.transform.scale(bullet5, (int((2 / 1920) * width), int((2 / 1080) * height)))


#chargement des armes en utilisation J1
ak_neutral_use = pygame.image.load(curdir + "/images/icon/AK/full.png").convert_alpha()
grenade_neutral_use = pygame.image.load(curdir + "/images/icon/grenade/full.png").convert_alpha()
uzi_neutral_use = pygame.image.load(curdir + "/images/icon/UZI/full.png").convert_alpha()
rpg_neutral_use = pygame.image.load(curdir + "/images/icon/RPG/full.png").convert_alpha()
shotgun_neutral_use = pygame.image.load(curdir + "/images/icon/shotgun/full.png").convert_alpha()

ak_neutral_use50 = pygame.image.load(curdir + "/images/icon/AK/full_50.png").convert_alpha()
uzi_neutral_use50 = pygame.image.load(curdir + "/images/icon/UZI/full_50.png").convert_alpha()
shotgun_neutral_use50 = pygame.image.load(curdir + "/images/icon/shotgun/full_50.png").convert_alpha()

ak_neutral_use_empty = pygame.image.load(curdir + "/images/icon/AK/empty.png").convert_alpha()
grenade_neutral_use_empty = pygame.image.load(curdir + "/images/icon/grenade/empty.png").convert_alpha()
uzi_neutral_use_empty = pygame.image.load(curdir + "/images/icon/UZI/empty.png").convert_alpha()
rpg_neutral_use_empty = pygame.image.load(curdir + "/images/icon/RPG/empty.png").convert_alpha()
shotgun_neutral_use_empty = pygame.image.load(curdir + "/images/icon/shotgun/empty.png").convert_alpha()

ak_neutral_use_reload25 = pygame.image.load(curdir + "/images/icon/AK/reload_25.png").convert_alpha()
grenade_neutral_use_reload25 = pygame.image.load(curdir + "/images/icon/grenade/reload_25.png").convert_alpha()
uzi_neutral_use_reload25 = pygame.image.load(curdir + "/images/icon/UZI/reload_25.png").convert_alpha()
rpg_neutral_use_reload25 = pygame.image.load(curdir + "/images/icon/RPG/reload_25.png").convert_alpha()
shotgun_neutral_use_reload25 = pygame.image.load(curdir + "/images/icon/shotgun/reload_25.png").convert_alpha()

ak_neutral_use_reload50 = pygame.image.load(curdir + "/images/icon/AK/reload_50.png").convert_alpha()
grenade_neutral_use_reload50 = pygame.image.load(curdir + "/images/icon/grenade/reload_50.png").convert_alpha()
uzi_neutral_use_reload50 = pygame.image.load(curdir + "/images/icon/UZI/reload_50.png").convert_alpha()
rpg_neutral_use_reload50 = pygame.image.load(curdir + "/images/icon/RPG/reload_50.png").convert_alpha()
shotgun_neutral_use_reload50 = pygame.image.load(curdir + "/images/icon/shotgun/reload_50.png").convert_alpha()

ak_neutral_use_reload75 = pygame.image.load(curdir + "/images/icon/AK/reload_75.png").convert_alpha()
grenade_neutral_use_reload75 = pygame.image.load(curdir + "/images/icon/grenade/reload_75.png").convert_alpha()
uzi_neutral_use_reload75 = pygame.image.load(curdir + "/images/icon/UZI/reload_75.png").convert_alpha()
rpg_neutral_use_reload75 = pygame.image.load(curdir + "/images/icon/RPG/reload_75.png").convert_alpha()
shotgun_neutral_use_reload75 = pygame.image.load(curdir + "/images/icon/shotgun/reload_75.png").convert_alpha()

#redimension des armes en utilisation J2
ak_neutral_use = pygame.transform.scale(ak_neutral_use, (int(463/10), int(469/10)))
grenade_neutral_use = pygame.transform.scale(grenade_neutral_use, (int(463/10), int(469/10)))
uzi_neutral_use = pygame.transform.scale(uzi_neutral_use, (int(463/10), int(469/10)))
rpg_neutral_use = pygame.transform.scale(rpg_neutral_use, (int(463/10), int(469/10)))
shotgun_neutral_use = pygame.transform.scale(shotgun_neutral_use, (int(463/10), int(469/10)))

ak_neutral_use50 = pygame.transform.scale(ak_neutral_use50, (int(463/10), int(469/10)))
uzi_neutral_use50 = pygame.transform.scale(uzi_neutral_use50, (int(463/10), int(469/10)))
shotgun_neutral_use50 = pygame.transform.scale(shotgun_neutral_use50, (int(463/10), int(469/10)))

ak_neutral_use_empty = pygame.transform.scale(ak_neutral_use_empty, (int(463/10), int(469/10)))
grenade_neutral_use_empty = pygame.transform.scale(grenade_neutral_use_empty, (int(463/10), int(469/10)))
uzi_neutral_use_empty = pygame.transform.scale(uzi_neutral_use_empty, (int(463/10), int(469/10)))
rpg_neutral_use_empty = pygame.transform.scale(rpg_neutral_use_empty, (int(463/10), int(469/10)))
shotgun_neutral_use_empty = pygame.transform.scale(shotgun_neutral_use_empty, (int(463/10), int(469/10)))

ak_neutral_use_reload25 = pygame.transform.scale(ak_neutral_use_reload25, (int(463/10), int(469/10)))
grenade_neutral_use_reload25 = pygame.transform.scale(grenade_neutral_use_reload25, (int(463/10), int(469/10)))
uzi_neutral_use_reload25 = pygame.transform.scale(uzi_neutral_use_reload25, (int(463/10), int(469/10)))
rpg_neutral_use_reload25 = pygame.transform.scale(rpg_neutral_use_reload25, (int(463/10), int(469/10)))
shotgun_neutral_use_reload25 = pygame.transform.scale(shotgun_neutral_use_reload25, (int(463/10), int(469/10)))

ak_neutral_use_reload50 = pygame.transform.scale(ak_neutral_use_reload50, (int(463/10), int(469/10)))
grenade_neutral_use_reload50 = pygame.transform.scale(grenade_neutral_use_reload50, (int(463/10), int(469/10)))
uzi_neutral_use_reload50 = pygame.transform.scale(uzi_neutral_use_reload50, (int(463/10), int(469/10)))
rpg_neutral_use_reload50 = pygame.transform.scale(rpg_neutral_use_reload50, (int(463/10), int(469/10)))
shotgun_neutral_use_reload50 = pygame.transform.scale(shotgun_neutral_use_reload50, (int(463/10), int(469/10)))

ak_neutral_use_reload75 = pygame.transform.scale(ak_neutral_use_reload75, (int(463/10), int(469/10)))
grenade_neutral_use_reload75 = pygame.transform.scale(grenade_neutral_use_reload75, (int(463/10), int(469/10)))
uzi_neutral_use_reload75 = pygame.transform.scale(uzi_neutral_use_reload75, (int(463/10), int(469/10)))
rpg_neutral_use_reload75 = pygame.transform.scale(rpg_neutral_use_reload75, (int(463/10), int(469/10)))
shotgun_neutral_use_reload75 = pygame.transform.scale(shotgun_neutral_use_reload75, (int(463/10), int(469/10)))

exp1 = pygame.image.load(curdir + "/images/explosion/1.png").convert_alpha()
exp2 = pygame.image.load(curdir + "/images/explosion/2.png").convert_alpha()
exp3 = pygame.image.load(curdir + "/images/explosion/3.png").convert_alpha()
exp4 = pygame.image.load(curdir + "/images/explosion/4.png").convert_alpha()
exp5 = pygame.image.load(curdir + "/images/explosion/5.png").convert_alpha()
exp6 = pygame.image.load(curdir + "/images/explosion/6.png").convert_alpha()
exp7 = pygame.image.load(curdir + "/images/explosion/7.png").convert_alpha()
exp8 = pygame.image.load(curdir + "/images/explosion/8.png").convert_alpha()
exp9 = pygame.image.load(curdir + "/images/explosion/9.png").convert_alpha()
exp10 = pygame.image.load(curdir + "/images/explosion/10.png").convert_alpha()
exp11 = pygame.image.load(curdir + "/images/explosion/11.png").convert_alpha()
exp12 = pygame.image.load(curdir + "/images/explosion/12.png").convert_alpha()
exp13 = pygame.image.load(curdir + "/images/explosion/13.png").convert_alpha()
exp14 = pygame.image.load(curdir + "/images/explosion/14.png").convert_alpha()
exp15 = pygame.image.load(curdir + "/images/explosion/15.png").convert_alpha()
exp16 = pygame.image.load(curdir + "/images/explosion/16.png").convert_alpha()

exp1 = pygame.transform.scale(exp1, (int((400/1920) * width), int((400 / 1080) * height)))
exp2 = pygame.transform.scale(exp2, (int((400/1920) * width), int((400 / 1080) * height)))
exp3 = pygame.transform.scale(exp3, (int((400/1920) * width), int((400 / 1080) * height)))
exp4 = pygame.transform.scale(exp4, (int((400/1920) * width), int((400 / 1080) * height)))
exp5 = pygame.transform.scale(exp5, (int((400/1920) * width), int((400 / 1080) * height)))
exp6 = pygame.transform.scale(exp6, (int((400/1920) * width), int((400 / 1080) * height)))
exp7 = pygame.transform.scale(exp7, (int((400/1920) * width), int((400 / 1080) * height)))
exp8 = pygame.transform.scale(exp8, (int((400/1920) * width), int((400 / 1080) * height)))
exp9 = pygame.transform.scale(exp9, (int((400/1920) * width), int((400 / 1080) * height)))
exp10 = pygame.transform.scale(exp10, (int((400/1920) * width), int((400 / 1080) * height)))
exp11 = pygame.transform.scale(exp11, (int((400/1920) * width), int((400 / 1080) * height)))
exp12 = pygame.transform.scale(exp12, (int((400/1920) * width), int((400 / 1080) * height)))
exp13 = pygame.transform.scale(exp13, (int((400/1920) * width), int((400 / 1080) * height)))
exp14 = pygame.transform.scale(exp14, (int((400/1920) * width), int((400 / 1080) * height)))
exp15 = pygame.transform.scale(exp15, (int((400/1920) * width), int((400 / 1080) * height)))
exp16 = pygame.transform.scale(exp16, (int((400/1920) * width), int((400 / 1080) * height)))


#positions des armes pour J1
pos_ak_j1 = ((10 / 1920) * width, (1000 / 1080) * height)
pos_grenade_j1 = ((60 / 1920) * width, (1000 / 1080) * height)
pos_uzi_j1 = ((110 / 1920) * width, (1000 / 1080) * height)
pos_rpg_j1 = ((160 / 1920) * width, (1000 / 1080) * height)
pos_shotgun_j1 = ((210 / 1920) * width, (1000 / 1080) * height)

#positions des armes pour J2
pos_shotgun_j2 = (WINDOW_X-((255 / 1920) * width), (1000 / 1080) * height)
pos_rpg_j2 = (WINDOW_X-((205 / 1920) * width), (1000 / 1080) * height)
pos_uzi_j2 = (WINDOW_X-((155 / 1920) * width), (1000 / 1080) * height)
pos_grenade_j2 = (WINDOW_X-((105 / 1920) * width), (1000 / 1080) * height)
pos_ak_j2 = (WINDOW_X-((55 / 1920) * width), (1000 / 1080) * height)

#boucle en attente d'évènement
on = True
menu_principale = True
menu_personnage = True
menu_map = True
game = True
joueur_1 = True
info = True

while on:
    cooldown = False
    cooldown2 = False


    bullets = [0]
    heights = [0]
    widths = [0]
    temps = [0]
    orientations = [0]
    height0 = [0]
    width0 = [0]
    angle0 = [0]
    explosion = [0]

    vie_j1 = 100
    vie_j2 = 100
    
    song_menu = mixer.music.load(curdir + "/audio/music_map_serenite.mp3")
    mixer.music.play(-1)
    game = True
    alive_j1 = True
    alive_j2 = True
    victory = False
    pass_weapon_j1 = True
    pass_weapon_j2 = True
    while menu_principale:
        fpsClock.tick(15)
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
        fpsClock.tick(15)
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

    #On crée une boucle while pour chaque menu : ici pour le menu des personnages
    while menu_personnage:
        fpsClock.tick(15)
        
    #Boucle qui sert aux événements qui suivront : clics
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                on = False
                break
            elif keys[K_ESCAPE]: #Evenement clic sur esc : fin de jeu, retour au menu principal
                game = False
                menu_principale = True
                menu_map = False
                victory = False
                menu_personnage = False
            elif event.type == pygame.MOUSEBUTTONUP: #Dans le cas où l'evenement est un clique de la souris

                if joueur_1 is True: #Tour du joueur pour choisir son personnage
                    if event.button == 1:  #evemenement clique droit
                    #Condition if, elif pour les cliques dans les zones de sekections des joueurs 0 pour x et 1 pour y
                        #Puis on charge les images pour chaque personnage ici le perosnnage 1
                            #Dés que le perosnnage est séléctionné, le tour du joueru 1 est passé (false) et c'est le tour du joueur2(true)
                        if event.pos[0] >= (700 / 1920) * width and event.pos[0] <= (800 / 1920) * width and event.pos[1] >= (800 / 1080) * height and event.pos[1] <= (850 / 1080) * height:
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
                        elif event.pos[0] >= (900 / 1920) * width and event.pos[0] <= (1000 / 1920) * width and event.pos[1] >= (800 / 1080) * height and event.pos[1] <= (850 / 1080) * height: #rect player2
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
                        elif event.pos[0] >= (1100 / 1920) * width and event.pos[0] <= (1200 / 1920) * width and event.pos[1] >= (800 / 1080) * height and event.pos[1] <= (850 / 1080) * height:#rect player3
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
                        elif event.pos[0] >= (700 / 1920) * width and event.pos[0] <= (800 / 1920) * width and event.pos[1] >= (950 / 1080) * height and event.pos[1] <= (1000 / 1080) * height:#rect player4
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
                        elif event.pos[0] >= (900 / 1920) * width and event.pos[0] <= (1000 / 1920) * width and event.pos[1] >= (950 / 1080) * height and event.pos[1] <= (1000 / 1080) * height:#rect player4
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
                        elif event.pos[0] >= (1100 / 1920) * width and event.pos[0] <= (1200 / 1920) * width and event.pos[1] >= (950 / 1080) * height and event.pos[1] <= (1000 / 1080) * height:#rect player4
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

                if joueur_2 is True: # tour du joueur 2
                    if event.button == 1: # meme successions d'étapes que pour le joueur 1
                        if event.pos[0] >= (700 / 1920) * width and event.pos[0] <= (800 / 1920) * width and event.pos[1] >= (800 / 1080) * height and event.pos[1] <= (850 / 1080) * height: #rect player1 ; 0 pour x et 1 pour y
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
                            menu_personnage = False #Apres le choix du personnage du joueur 2, on ferme le menu puis on passe au menu des cartes
                            joueur_2 = False
                            break
                        elif event.pos[0] >= (900 / 1920) * width and event.pos[0] <= (1000 / 1920) * width and event.pos[1] >= (800 / 1080) * height and event.pos[1] <= (850 / 1080) * height: #rect player2
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
                        elif event.pos[0] >= (1100 / 1920) * width and event.pos[0] <= (1200 / 1920) * width and event.pos[1] >= (800 / 1080) * height and event.pos[1] <= (850 / 1080) * height:#rect player3
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
                        elif event.pos[0] >= (700 / 1920) * width and event.pos[0] <= (800 / 1920) * width and event.pos[1] >= (950 / 1080) * height and event.pos[1] <= (1000 / 1080) * height:#rect player4
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
                        elif event.pos[0] >= (900 / 1920) * width and event.pos[0] <= (1000 / 1920) * width and event.pos[1] >= (950 / 1080) * height and event.pos[1] <= (1000 / 1080) * height:#rect player4
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
                        elif event.pos[0] >= (1100 / 1920) * width and event.pos[0] <= (1200 / 1920) * width and event.pos[1] >= (950 / 1080) * height and event.pos[1] <= (1000 / 1080) * height:#rect player4
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
        # on crée les differentes surfaces à base de Rect pour faiire les boutons
        rect_separation = pygame.Rect(int(WINDOW_X/2), int((0 / 1080) * height), int((2 / 1920) * width), int(WINDOW_Y / 1080))
        pygame.draw.rect(screen, red, rect_separation)
        rect_players_choice = pygame.Rect(int((0/ 1920) * width), int((700 / 1080) * height), int(WINDOW_X), int(WINDOW_Y))
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
        screen.blit(vs, (int((WINDOW_X/2)-vs.get_width()/2), int(WINDOW_X/8)))
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
            screen.blit(j1_preview_bis, (int((WINDOW_X/4)-j1_preview_bis.get_width()/2), 50))
        if joueur_1 == False and joueur_2 == False:
            j2_preview_bis = pygame.transform.scale(j2_preview, (j2_preview.get_width()*7, j2_preview.get_height()*7))
            screen.blit(j2_preview_bis, (int((WINDOW_X/2)+(WINDOW_X/4)-j2_preview_bis.get_width()/2), 50))
            screen.blit(j1_preview_bis, (int((WINDOW_X/4)-j1_preview_bis.get_width()/2), 50))
        pygame.display.flip()
        if joueur_1 == False and joueur_2 == False:
            pygame.time.delay(1000)

    while menu_map:
        fpsClock.tick(15)
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
                        SIDE_MOVE = 10
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
                        SIDE_MOVE = 10
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
                        song_map3 = mixer.music.load(curdir + "/audio/music_map_bataille.mp3")
                        mixer.music.play(-1)
                        UP_MOVE = 30
                        SIDE_MOVE = 10
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
                        song_map4 = mixer.music.load(curdir + "/audio/music_map_festif.mp3")
                        mixer.music.play(-1)
                        UP_MOVE = 30
                        SIDE_MOVE = 10
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
    
    reload_status_weapon1_j1 = 0
    reload_status_weapon3_j1 = 0
    reload_status_weapon5_j1 = 0
    reload_status_weapon1_j2 = 0
    reload_status_weapon3_j2 = 0
    reload_status_weapon5_j2 = 0
    
    # Armes non rechargeables
    reload_status_weapon2_j1 = 0
    reload_status_weapon4_j1 = 0
    reload_status_weapon2_j2 = 0
    reload_status_weapon4_j2 = 0
    
    # Quantité de munitions maximales et initiales
    weapon1_j1 = 30
    weapon3_j1 = 20
    weapon5_j1 = 5
    weapon1_j2 = 30
    weapon3_j2 = 20
    weapon5_j2 = 5
    
    count_hit_j1 = 0
    count_hit_j2 = 0
    
    pass_blit_j1 = True
    pass_blit_j2 = True

    
    while game:
        fpsClock.tick(60)
        
        if reload_status_weapon1_j1 > 0:
            reload_status_weapon1_j1 += 1
        if reload_status_weapon2_j1 > 0:
            reload_status_weapon2_j1 += 1
        if reload_status_weapon3_j1 > 0:
            reload_status_weapon3_j1 += 1
        if reload_status_weapon4_j1 > 0:
            reload_status_weapon4_j1 += 1
        if reload_status_weapon5_j1 > 0:
            reload_status_weapon5_j1 += 1
            
        if reload_status_weapon1_j2 > 0:
            reload_status_weapon1_j2 += 1
        if reload_status_weapon2_j2 > 0:
            reload_status_weapon2_j2 += 1
        if reload_status_weapon3_j2 > 0:
            reload_status_weapon3_j2 += 1
        if reload_status_weapon4_j2 > 0:
            reload_status_weapon4_j2 += 1
        if reload_status_weapon5_j2 > 0:
            reload_status_weapon5_j2 += 1
            
        if reload_status_weapon1_j1 > 60*3:
            reload_status_weapon1_j1 = 0
            weapon1_j1 = 30
        if reload_status_weapon2_j1 > 60*2:
            reload_status_weapon2_j1 = 0
        if reload_status_weapon3_j1 > 60*2:
            reload_status_weapon3_j1 = 0
            weapon3_j1 = 20
        if reload_status_weapon4_j1 > 60*3:
            reload_status_weapon4_j1 = 0
        if reload_status_weapon5_j1 > 60*4:
            reload_status_weapon5_j1 = 0
            weapon5_j1 = 5
            
        if reload_status_weapon1_j2 > 60*3:
            reload_status_weapon1_j2 = 0
            weapon1_j2 = 30
        if reload_status_weapon2_j2 > 60*2:
            reload_status_weapon2_j2 = 0
        if reload_status_weapon3_j2 > 60*2:
            reload_status_weapon3_j2 = 0
            weapon3_j2 = 20
        if reload_status_weapon4_j2 > 60*3:
            reload_status_weapon4_j2 = 0
        if reload_status_weapon5_j2 > 60*4:
            reload_status_weapon5_j2 = 0
            weapon5_j2 = 5
        
        # Auto reload
        if reload_status_weapon1_j1 == 0 and weapon1_j1 <= 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/ak47-reload.mp3"))
            reload_status_weapon1_j1 = 1
        if reload_status_weapon3_j1 == 0 and weapon3_j1 <= 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/uzi-reload.mp3"))
            reload_status_weapon3_j1 = 1
        if reload_status_weapon5_j1 == 0 and weapon5_j1 <= 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/shotgun-reload.mp3"))
            reload_status_weapon5_j1 = 1
            
        if reload_status_weapon1_j2 == 0 and weapon1_j2 <= 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/ak47-reload.mp3"))
            reload_status_weapon1_j2 = 1
        if reload_status_weapon3_j2 == 0 and weapon3_j2 <= 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/uzi-reload.mp3"))
            reload_status_weapon3_j2 = 1
        if reload_status_weapon5_j2 == 0 and weapon5_j2 <= 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/shotgun-reload.mp3"))
            reload_status_weapon5_j2 = 1
            
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            
            if event.type == QUIT:
                on = False
                break
            elif keys[K_ESCAPE]:
                game = False
                menu_principale = True
                menu_map = True

            #Changement d'armes joueur 1 (E) et joueur 2 (SHIFT DROITE)
            elif keys[K_e]: # appuie sur la touche e
                if pass_weapon_j1 is True: # le joueur 1 peut changer d'arme
                    count_weapon_j1 += 1 #Compteur qui va permettre de savoir quelle arme il aura
                    pass_weapon_j1 = False # VARIABLE de transition pour eviter une interpretation d'un appuie prolongé
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
        if keys[K_s]:
            pos_j1 = pos_j1.move(0, UP_MOVE)

        
        if keys[K_z]:
            if jump_j1 == True :
                pos_j1 = pos_j1.move(0, int(-coef_jump_j1*UP_MOVE))
                #jump_j1_count += 1
                coef_jump_j1 = coef_jump_j1/COEF_UP

            elif pos_j1.y < int(bloc_base.y-j1.get_height()) :
                if pass_j1 == True :
                    coef_jump_j1 = 0.1
                    pass_j1 = False

                pos_j1 = pos_j1.move(0, int(coef_jump_j1*UP_MOVE))
                #jump_j1_count += -1
                coef_jump_j1 = coef_jump_j1*COEF_DOWN
        
        elif pos_j1.y < int(bloc_base.y-j1.get_height()) :
            if pass_j1 == True :
                coef_jump_j1 = 0.1
                pass_j1 = False

            pos_j1 = pos_j1.move(0, int(coef_jump_j1*UP_MOVE))
            #jump_j1_count += -1
            coef_jump_j1 = coef_jump_j1*COEF_DOWN
            jump_j1 = False

        if keys[K_d]:
            pos_j1 = pos_j1.move(SIDE_MOVE, 0)
            heading_j1 = 1
            move_j1 = True

        if keys[K_q]:
            pos_j1 = pos_j1.move(-SIDE_MOVE, 0)
            heading_j1 = 0
            move_j1 = True
        
        if keys[K_v]:
            # Tirer
            if cooldown == False:
                if count_weapon_j1 == 1 and weapon1_j1 > 0:
                    weapon1_j1 -= 1
                    cooldown = True
                    bullets.append(1)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(uniform(pi/48, -pi/48))
                    explosion.append(0)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rifle-shot.mp3"))
                elif count_weapon_j1 == 3 and weapon3_j1 > 0:
                    weapon3_j1 -= 1
                    cooldown = True
                    bullets.append(3)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(uniform(pi/30, -pi/30))
                    explosion.append(0)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/pistol-shot.mp3"))
                elif count_weapon_j1 == 5 and weapon5_j1 > 0:
                    weapon5_j1 -= 1
                    cooldown = True
                    bullets.append(5)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)
                    
                    bullets.append(5)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)
                    
                    bullets.append(5)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)
                    
                    bullets.append(5)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)
                    
                    bullets.append(5)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/shotgun-shot.mp3"))
                    
                elif count_weapon_j1 == 2 and reload_status_weapon2_j1 == 0:
                    reload_status_weapon2_j1 = 1
                    cooldown = True
                    bullets.append(2)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(0)
                    explosion.append(0)
                elif count_weapon_j1 == 4 and reload_status_weapon4_j1 == 0:
                    reload_status_weapon4_j1 = 1
                    cooldown = True
                    bullets.append(4)
                    heights.append(pos_j1.y)
                    widths.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    temps.append(0)
                    orientations.append(1 if heading_j1 == 1 else -1)
                    height0.append(pos_j1.y)
                    width0.append(pos_j1.x+j1.get_width() if heading_j1 == 1 else pos_j1.x)
                    angle0.append(0)
                    explosion.append(0)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-fire.mp3"))
        else:
            cooldown = False

        if keys[K_r]:
            # Initier le rechargement
            if count_weapon_j1 == 1 and reload_status_weapon1_j1 == 0:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/ak47-reload.mp3"))
                reload_status_weapon1_j1 = 1
            elif count_weapon_j1 == 3 and reload_status_weapon3_j1 == 0:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/uzi-reload.mp3"))
                reload_status_weapon3_j1 = 1
            elif count_weapon_j1 == 5 and reload_status_weapon5_j1 == 0:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/shotgun-reload.mp3"))
                reload_status_weapon5_j1 = 1
            
                
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

            elif pos_j2.y < int(bloc_base.y-j2.get_height()) :
                if pass_j2 == True :
                    coef_jump_j2 = 0.1
                    pass_j2 = False

                pos_j2 = pos_j2.move(0, int(coef_jump_j2*UP_MOVE))
                #jump_j2_count += -1
                coef_jump_j2 = coef_jump_j2*COEF_DOWN
        
        elif pos_j2.y < int(bloc_base.y-j2.get_height()) :
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

        if keys[K_EQUALS] if isMac else keys[K_EXCLAIM]:
            # Tirer
            if cooldown2 == False:
                if count_weapon_j2 == 1 and weapon1_j2 > 0:
                    weapon1_j2 -= 1
                    cooldown2 = True
                    bullets.append(1)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(uniform(pi/48, -pi/48))
                    explosion.append(0)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rifle-shot.mp3"))
                elif count_weapon_j2 == 3 and weapon3_j2 > 0:
                    weapon3_j2 -= 1
                    cooldown2 = True
                    bullets.append(3)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(uniform(pi/30, -pi/30))
                    explosion.append(0)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/pistol-shot.mp3"))
                elif count_weapon_j2 == 5 and weapon5_j2 > 0:
                    weapon5_j2 -= 1
                    cooldown2 = True
                    bullets.append(5)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)

                    bullets.append(5)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)

                    bullets.append(5)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)

                    bullets.append(5)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)

                    bullets.append(5)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(uniform(pi/24, -pi/24))
                    explosion.append(0)

                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/shotgun-shot.mp3"))

                elif count_weapon_j2 == 2 and reload_status_weapon2_j2 == 0:
                    reload_status_weapon2_j2 = 1
                    cooldown2 = True
                    bullets.append(2)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(0)
                    explosion.append(0)

                elif count_weapon_j2 == 4 and reload_status_weapon4_j2 == 0:
                    reload_status_weapon4_j2 = 1
                    cooldown2 = True
                    bullets.append(4)
                    heights.append(pos_j2.y)
                    widths.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    temps.append(0)
                    orientations.append(1 if heading_j2 == 1 else -1)
                    height0.append(pos_j2.y)
                    width0.append(pos_j2.x+j2.get_width() if heading_j2 == 1 else pos_j2.x)
                    angle0.append(0)
                    explosion.append(0)

                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-fire.mp3"))
        else:
            cooldown2 = False
                
        if keys[K_RCTRL]:
            # Initier le rechargement
            if count_weapon_j2 == 1 and reload_status_weapon1_j2 == 0:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/ak47-reload.mp3"))
                reload_status_weapon1_j2 = 1
            if count_weapon_j2 == 3 and reload_status_weapon3_j2 == 0:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/uzi-reload.mp3"))
                reload_status_weapon3_j2 = 1
            if count_weapon_j2 == 5 and reload_status_weapon5_j2 == 0:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/shotgun-reload.mp3"))
                reload_status_weapon5_j2 = 1


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
            if pos_j1.x+j1.get_width() > bloc_1.x and pos_j1.x+j1.get_width() < bloc_1.x + (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() > bloc_1.y:
                pos_j1.x = bloc_1.x-j1.get_width()-1 #par le coté gauche
                
                

            if pos_j1.x < bloc_1.x+bloc_1.w and pos_j1.x > bloc_1.x+bloc_1.w - (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() > bloc_1.y:
                pos_j1.x = bloc_1.x+bloc_1.w +1  #par le coté droit

            if pos_j1.x+j1.get_width() >= bloc_1.x and pos_j1.x <= bloc_1.x+bloc_1.w and pos_j1.y <= bloc_1.y+bloc_1.h and pos_j1.y >= bloc_1.y:
                pos_j1.y = bloc_1.y+bloc_1.h +1 #par dessous
                jump_j1 = False
                

            if pos_j1.x+j1.get_width() >= bloc_1.x and pos_j1.x <= bloc_1.x+bloc_1.w and pos_j1.y+j1.get_height() <= bloc_1.y+bloc_1.h and pos_j1.y+j1.get_height() >= bloc_1.y:
                pos_j1.y = bloc_1.y-j1.get_height() #par dessus
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_1.x and pos_j2.x+j2.get_width() < bloc_1.x + ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_1.y+bloc_1.h and pos_j2.y+j2.get_height() > bloc_1.y:
                pos_j2.x = bloc_1.x-j2.get_width()-1

            if pos_j2.x < bloc_1.x+bloc_1.w and pos_j2.x > bloc_1.x+bloc_1.w - ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_1.y+bloc_1.h and pos_j2.y+j2.get_height() > bloc_1.y:
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
            if pos_j1.x+j1.get_width() > bloc_2.x and pos_j1.x+j1.get_width() < bloc_2.x + (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() > bloc_2.y:
                pos_j1.x = bloc_2.x-j1.get_width()-1

            if pos_j1.x < bloc_2.x+bloc_2.w and pos_j1.x > bloc_2.x+bloc_2.w - (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() > bloc_2.y:
                pos_j1.x = bloc_2.x+bloc_2.w +1

            if pos_j1.x+j1.get_width() >= bloc_2.x and pos_j1.x <= bloc_2.x+bloc_2.w and pos_j1.y <= bloc_2.y+bloc_2.h and pos_j1.y >= bloc_2.y:
                pos_j1.y = bloc_2.y+bloc_2.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_2.x and pos_j1.x <= bloc_2.x+bloc_2.w and pos_j1.y+j1.get_height() <= bloc_2.y+bloc_2.h and pos_j1.y+j1.get_height() >= bloc_2.y:
                pos_j1.y = bloc_2.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_2.x and pos_j2.x+j2.get_width() < bloc_2.x + ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_2.y+bloc_2.h and pos_j2.y+j2.get_height() > bloc_2.y:
                pos_j2.x = bloc_2.x-j2.get_width()-1

            if pos_j2.x < bloc_2.x+bloc_2.w and pos_j2.x > bloc_2.x+bloc_2.w - ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_2.y+bloc_2.h and pos_j2.y+j2.get_height() > bloc_2.y:
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
            if pos_j1.x+j1.get_width() > bloc_3.x and pos_j1.x+j1.get_width() < bloc_3.x + (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() > bloc_3.y:
                pos_j1.x = bloc_3.x-j1.get_width()-1

            if pos_j1.x < bloc_3.x+bloc_3.w and pos_j1.x > bloc_3.x+bloc_3.w - (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() > bloc_3.y:
                pos_j1.x = bloc_3.x+bloc_3.w +1

            if pos_j1.x+j1.get_width() >= bloc_3.x and pos_j1.x <= bloc_3.x+bloc_3.w and pos_j1.y <= bloc_3.y+bloc_3.h and pos_j1.y >= bloc_3.y:
                pos_j1.y = bloc_3.y+bloc_3.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_3.x and pos_j1.x <= bloc_3.x+bloc_3.w and pos_j1.y+j1.get_height() <= bloc_3.y+bloc_3.h and pos_j1.y+j1.get_height() >= bloc_3.y:
                pos_j1.y = bloc_3.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_3.x and pos_j2.x+j2.get_width() < bloc_3.x + ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_3.y+bloc_3.h and pos_j2.y+j2.get_height() > bloc_3.y:
                pos_j2.x = bloc_3.x-j2.get_width()-1

            if pos_j2.x < bloc_3.x+bloc_3.w and pos_j2.x > bloc_3.x+bloc_3.w - ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_3.y+bloc_3.h and pos_j2.y+j2.get_height() > bloc_3.y:
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
            if pos_j1.x+j1.get_width() > bloc_4.x and pos_j1.x+j1.get_width() < bloc_4.x + (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() > bloc_4.y:
                pos_j1.x = bloc_4.x-j1.get_width()-1

            if pos_j1.x < bloc_4.x+bloc_4.w and pos_j1.x > bloc_4.x+bloc_4.w - (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() > bloc_4.y:
                pos_j1.x = bloc_4.x+bloc_4.w +1

            if pos_j1.x+j1.get_width() >= bloc_4.x and pos_j1.x <= bloc_4.x+bloc_4.w and pos_j1.y <= bloc_4.y+bloc_4.h and pos_j1.y >= bloc_4.y:
                pos_j1.y = bloc_4.y+bloc_4.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_4.x and pos_j1.x <= bloc_4.x+bloc_4.w and pos_j1.y+j1.get_height() <= bloc_4.y+bloc_4.h and pos_j1.y+j1.get_height() >= bloc_4.y:
                pos_j1.y = bloc_4.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_4.x and pos_j2.x+j2.get_width() < bloc_4.x + ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_4.y+bloc_4.h and pos_j2.y+j2.get_height() > bloc_4.y:
                pos_j2.x = bloc_4.x-j2.get_width()-1

            if pos_j2.x < bloc_4.x+bloc_4.w and pos_j2.x > bloc_4.x+bloc_4.w - ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_4.y+bloc_4.h and pos_j2.y+j2.get_height() > bloc_4.y:
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
            if pos_j1.x+j1.get_width() > bloc_5.x and pos_j1.x+j1.get_width() < bloc_5.x + (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() > bloc_5.y:
                pos_j1.x = bloc_5.x-j1.get_width()-1

            if pos_j1.x < bloc_5.x+bloc_5.w and pos_j1.x > bloc_5.x+bloc_5.w - (((67.5 / 1920) * width) if count_weapon_j1 == 4 else ((15 / 1920) * width)) and pos_j1.y < bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() > bloc_5.y:
                pos_j1.x = bloc_5.x+bloc_5.w +1

            if pos_j1.x+j1.get_width() >= bloc_5.x and pos_j1.x <= bloc_5.x+bloc_5.w and pos_j1.y <= bloc_5.y+bloc_5.h and pos_j1.y >= bloc_5.y:
                pos_j1.y = bloc_5.y+bloc_5.h +1
                jump_j1 = False

            if pos_j1.x+j1.get_width() >= bloc_5.x and pos_j1.x <= bloc_5.x+bloc_5.w and pos_j1.y+j1.get_height() <= bloc_5.y+bloc_5.h and pos_j1.y+j1.get_height() >= bloc_5.y:
                pos_j1.y = bloc_5.y-j1.get_height()
                coef_jump_j1 = float(1)
                pass_j1 = True
                jump_j1 = True
            
            if pos_j2.x+j2.get_width() > bloc_5.x and pos_j2.x+j2.get_width() < bloc_5.x + ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_5.y+bloc_5.h and pos_j2.y+j2.get_height() > bloc_5.y:
                pos_j2.x = bloc_5.x-j2.get_width()-1

            if pos_j2.x < bloc_5.x+bloc_5.w and pos_j2.x > bloc_5.x+bloc_5.w - ((67.5 / 1920) * width if count_weapon_j2 == 4 else j2.get_width()) and pos_j2.y < bloc_5.y+bloc_5.h and pos_j2.y+j2.get_height() > bloc_5.y:
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
                j1_base_hit = pygame.image.load(curdir_j1 + "/AK/0_hit.png").convert_alpha()
                j1_base_hit_flip = pygame.image.load(curdir_j1 + "/AK/0_flip_hit.png").convert_alpha()
                j1_base_hit_1 = pygame.image.load(curdir_j1 + "/AK/1_hit.png").convert_alpha()
                j1_base_hit_flip_1 = pygame.image.load(curdir_j1 + "/AK/1_flip_hit.png").convert_alpha()
                j1_base_hit_2 = pygame.image.load(curdir_j1 + "/AK/2_hit.png").convert_alpha()
                j1_base_hit_flip_2 = pygame.image.load(curdir_j1 + "/AK/2_flip_hit.png").convert_alpha()
            elif count_weapon_j1 == 2: #grenade
                j1_base = pygame.image.load(curdir_j1 + "/grenade/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/grenade/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/grenade/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/grenade/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/grenade/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/grenade/2_flip.png").convert_alpha()
                j1_base_hit = pygame.image.load(curdir_j1 + "/grenade/0_hit.png").convert_alpha()
                j1_base_hit_flip = pygame.image.load(curdir_j1 + "/grenade/0_flip_hit.png").convert_alpha()
                j1_base_hit_1 = pygame.image.load(curdir_j1 + "/grenade/1_hit.png").convert_alpha()
                j1_base_hit_flip_1 = pygame.image.load(curdir_j1 + "/grenade/1_flip_hit.png").convert_alpha()
                j1_base_hit_2 = pygame.image.load(curdir_j1 + "/grenade/2_hit.png").convert_alpha()
                j1_base_hit_flip_2 = pygame.image.load(curdir_j1 + "/grenade/2_flip_hit.png").convert_alpha()
            elif count_weapon_j1 == 3: #uzi
                j1_base = pygame.image.load(curdir_j1 + "/UZI/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/UZI/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/UZI/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/UZI/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/UZI/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/UZI/2_flip.png").convert_alpha()
                j1_base_hit = pygame.image.load(curdir_j1 + "/UZI/0_hit.png").convert_alpha()
                j1_base_hit_flip = pygame.image.load(curdir_j1 + "/UZI/0_flip_hit.png").convert_alpha()
                j1_base_hit_1 = pygame.image.load(curdir_j1 + "/UZI/1_hit.png").convert_alpha()
                j1_base_hit_flip_1 = pygame.image.load(curdir_j1 + "/UZI/1_flip_hit.png").convert_alpha()
                j1_base_hit_2 = pygame.image.load(curdir_j1 + "/UZI/2_hit.png").convert_alpha()
                j1_base_hit_flip_2 = pygame.image.load(curdir_j1 + "/UZI/2_flip_hit.png").convert_alpha()
            elif count_weapon_j1 == 4: #rpg
                j1_base = pygame.image.load(curdir_j1 + "/RPG/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/RPG/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/RPG/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/RPG/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/RPG/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/RPG/2_flip.png").convert_alpha()
                j1_base_hit = pygame.image.load(curdir_j1 + "/RPG/0_hit.png").convert_alpha()
                j1_base_hit_flip = pygame.image.load(curdir_j1 + "/RPG/0_flip_hit.png").convert_alpha()
                j1_base_hit_1 = pygame.image.load(curdir_j1 + "/RPG/1_hit.png").convert_alpha()
                j1_base_hit_flip_1 = pygame.image.load(curdir_j1 + "/RPG/1_flip_hit.png").convert_alpha()
                j1_base_hit_2 = pygame.image.load(curdir_j1 + "/RPG/2_hit.png").convert_alpha()
                j1_base_hit_flip_2 = pygame.image.load(curdir_j1 + "/RPG/2_flip_hit.png").convert_alpha()
            elif count_weapon_j1 == 5: #shotgun
                j1_base = pygame.image.load(curdir_j1 + "/shotgun/0.png").convert_alpha()
                j1_base_flip = pygame.image.load(curdir_j1 + "/shotgun/0_flip.png").convert_alpha()
                j1_base_1 = pygame.image.load(curdir_j1 + "/shotgun/1.png").convert_alpha()
                j1_base_flip_1 = pygame.image.load(curdir_j1 + "/shotgun/1_flip.png").convert_alpha()
                j1_base_2 = pygame.image.load(curdir_j1 + "/shotgun/2.png").convert_alpha()
                j1_base_flip_2 = pygame.image.load(curdir_j1 + "/shotgun/2_flip.png").convert_alpha()
                j1_base_hit = pygame.image.load(curdir_j1 + "/shotgun/0_hit.png").convert_alpha()
                j1_base_hit_flip = pygame.image.load(curdir_j1 + "/shotgun/0_flip_hit.png").convert_alpha()
                j1_base_hit_1 = pygame.image.load(curdir_j1 + "/shotgun/1_hit.png").convert_alpha()
                j1_base_hit_flip_1 = pygame.image.load(curdir_j1 + "/shotgun/1_flip_hit.png").convert_alpha()
                j1_base_hit_2 = pygame.image.load(curdir_j1 + "/shotgun/2_hit.png").convert_alpha()
                j1_base_hit_flip_2 = pygame.image.load(curdir_j1 + "/shotgun/2_flip_hit.png").convert_alpha()
            j1 = pygame.transform.scale(j1_base, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_flip = pygame.transform.scale(j1_base_flip, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_1 = pygame.transform.scale(j1_base_1, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_flip_1 = pygame.transform.scale(j1_base_flip_1, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_2 = pygame.transform.scale(j1_base_2, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_flip_2 = pygame.transform.scale(j1_base_flip_2, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_hit = pygame.transform.scale(j1_base_hit, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_hit_flip = pygame.transform.scale(j1_base_hit_flip, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_hit_1 = pygame.transform.scale(j1_base_hit_1, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_hit_flip_1 = pygame.transform.scale(j1_base_hit_flip_1, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_hit_2 = pygame.transform.scale(j1_base_hit_2, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
            j1_hit_flip_2 = pygame.transform.scale(j1_base_hit_flip_2, (int((j1_base.get_width()*2 / 1920) * width), int((j1_base.get_height()*2 / 1080) * height)))
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
                
                j2_base_hit = pygame.image.load(curdir_j2 + "/AK/0_hit.png").convert_alpha()
                j2_base_hit_flip = pygame.image.load(curdir_j2 + "/AK/0_flip_hit.png").convert_alpha()
                j2_base_hit_1 = pygame.image.load(curdir_j2 + "/AK/1_hit.png").convert_alpha()
                j2_base_hit_flip_1 = pygame.image.load(curdir_j2 + "/AK/1_flip_hit.png").convert_alpha()
                j2_base_hit_2 = pygame.image.load(curdir_j2 + "/AK/2_hit.png").convert_alpha()
                j2_base_hit_flip_2 = pygame.image.load(curdir_j2 + "/AK/2_flip_hit.png").convert_alpha()
            elif count_weapon_j2 == 2: #grenade
                j2_base = pygame.image.load(curdir_j2 + "/grenade/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/grenade/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/grenade/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/grenade/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/grenade/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/grenade/2_flip.png").convert_alpha()
                
                j2_base_hit = pygame.image.load(curdir_j2 + "/grenade/0_hit.png").convert_alpha()
                j2_base_hit_flip = pygame.image.load(curdir_j2 + "/grenade/0_flip_hit.png").convert_alpha()
                j2_base_hit_1 = pygame.image.load(curdir_j2 + "/grenade/1_hit.png").convert_alpha()
                j2_base_hit_flip_1 = pygame.image.load(curdir_j2 + "/grenade/1_flip_hit.png").convert_alpha()
                j2_base_hit_2 = pygame.image.load(curdir_j2 + "/grenade/2_hit.png").convert_alpha()
                j2_base_hit_flip_2 = pygame.image.load(curdir_j2 + "/grenade/2_flip_hit.png").convert_alpha()
            elif count_weapon_j2 == 3: #uzi
                j2_base = pygame.image.load(curdir_j2 + "/UZI/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/UZI/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/UZI/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/UZI/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/UZI/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/UZI/2_flip.png").convert_alpha()
                
                j2_base_hit = pygame.image.load(curdir_j2 + "/UZI/0_hit.png").convert_alpha()
                j2_base_hit_flip = pygame.image.load(curdir_j2 + "/UZI/0_flip_hit.png").convert_alpha()
                j2_base_hit_1 = pygame.image.load(curdir_j2 + "/UZI/1_hit.png").convert_alpha()
                j2_base_hit_flip_1 = pygame.image.load(curdir_j2 + "/UZI/1_flip_hit.png").convert_alpha()
                j2_base_hit_2 = pygame.image.load(curdir_j2 + "/UZI/2_hit.png").convert_alpha()
                j2_base_hit_flip_2 = pygame.image.load(curdir_j2 + "/UZI/2_flip_hit.png").convert_alpha()
            elif count_weapon_j2 == 4: #rpg
                j2_base = pygame.image.load(curdir_j2 + "/RPG/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/RPG/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/RPG/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/RPG/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/RPG/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/RPG/2_flip.png").convert_alpha()
                
                j2_base_hit = pygame.image.load(curdir_j2 + "/RPG/0_hit.png").convert_alpha()
                j2_base_hit_flip = pygame.image.load(curdir_j2 + "/RPG/0_flip_hit.png").convert_alpha()
                j2_base_hit_1 = pygame.image.load(curdir_j2 + "/RPG/1_hit.png").convert_alpha()
                j2_base_hit_flip_1 = pygame.image.load(curdir_j2 + "/RPG/1_flip_hit.png").convert_alpha()
                j2_base_hit_2 = pygame.image.load(curdir_j2 + "/RPG/2_hit.png").convert_alpha()
                j2_base_hit_flip_2 = pygame.image.load(curdir_j2 + "/RPG/2_flip_hit.png").convert_alpha()
            elif count_weapon_j2 == 5: #shotgun
                j2_base = pygame.image.load(curdir_j2 + "/shotgun/0.png").convert_alpha()
                j2_base_flip = pygame.image.load(curdir_j2 + "/shotgun/0_flip.png").convert_alpha()
                j2_base_1 = pygame.image.load(curdir_j2 + "/shotgun/1.png").convert_alpha()
                j2_base_flip_1 = pygame.image.load(curdir_j2 + "/shotgun/1_flip.png").convert_alpha()
                j2_base_2 = pygame.image.load(curdir_j2 + "/shotgun/2.png").convert_alpha()
                j2_base_flip_2 = pygame.image.load(curdir_j2 + "/shotgun/2_flip.png").convert_alpha()
                
                j2_base_hit = pygame.image.load(curdir_j2 + "/shotgun/0_hit.png").convert_alpha()
                j2_base_hit_flip = pygame.image.load(curdir_j2 + "/shotgun/0_flip_hit.png").convert_alpha()
                j2_base_hit_1 = pygame.image.load(curdir_j2 + "/shotgun/1_hit.png").convert_alpha()
                j2_base_hit_flip_1 = pygame.image.load(curdir_j2 + "/shotgun/1_flip_hit.png").convert_alpha()
                j2_base_hit_2 = pygame.image.load(curdir_j2 + "/shotgun/2_hit.png").convert_alpha()
                j2_base_hit_flip_2 = pygame.image.load(curdir_j2 + "/shotgun/2_flip_hit.png").convert_alpha()
            j2 = pygame.transform.scale(j2_base, (int((j2_base.get_width()*2 / 1920) * width), int((j2_base.get_height()*2 / 1080) * height)))
            j2_flip = pygame.transform.scale(j2_base_flip, (int((j2_base.get_width()*2 / 1920) * width), int((j2_base.get_height()*2 / 1080) * height)))
            j2_1 = pygame.transform.scale(j2_base_1, (int((j2_base.get_width()*2 / 1920) * width), int((j2_base.get_height()*2 / 1080) * height)))
            j2_flip_1 = pygame.transform.scale(j2_base_flip_1, (int((j2_base.get_width()*2 / 1920) * width), int((j2_base.get_height()*2 / 1080) * height)))
            j2_2 = pygame.transform.scale(j2_base_2, (int((j2_base.get_width()*2 / 1920) * width), int((j2_base.get_height()*2 / 1080) * height)))
            j2_flip_2 = pygame.transform.scale(j2_base_flip_2, (int((j2_base.get_width()*2 / 1920) * width), int((j2_base.get_height()*2 / 1080) * height)))
            
            j2_hit = pygame.transform.scale(j2_base_hit, (int((j2_base_hit.get_width()*2 / 1920) * width), int((j2_base_hit.get_height()*2 / 1080) * height)))
            j2_hit_flip = pygame.transform.scale(j2_base_hit_flip, (int((j2_base_hit.get_width()*2 / 1920) * width), int((j2_base_hit.get_height()*2 / 1080) * height)))
            j2_hit_1 = pygame.transform.scale(j2_base_hit_1, (int((j2_base_hit.get_width()*2 / 1920) * width), int((j2_base_hit.get_height()*2 / 1080) * height)))
            j2_hit_flip_1 = pygame.transform.scale(j2_base_hit_flip_1, (int((j2_base_hit.get_width()*2 / 1920) * width), int((j2_base_hit.get_height()*2 / 1080) * height)))
            j2_hit_2 = pygame.transform.scale(j2_base_hit_2, (int((j2_base_hit.get_width()*2 / 1920) * width), int((j2_base_hit.get_height()*2 / 1080) * height)))
            j2_hit_flip_2 = pygame.transform.scale(j2_base_hit_flip_2, (int((j2_base_hit.get_width()*2 / 1920) * width), int((j2_base_hit.get_height()*2 / 1080) * height)))
            pass_blit_j2 = False
        

        


        if alive_j1 == True :
            if heading_j1 == 1:
                if move_j1 == True: #si je joueur a bougé
                    compteur_j1 += 1
                    if compteur_j1 < 10:
                        if count_hit_j1 > 0:
                            count_hit_j1 -= 1
                            screen.blit(j1_hit_1, pos_j1)
                        else:
                            screen.blit(j1_1, pos_j1)
                    elif compteur_j1 < 20:
                        if count_hit_j1 > 0:
                            count_hit_j1 -= 1
                            screen.blit(j1_hit_2, pos_j1)
                        else:
                            screen.blit(j1_2, pos_j1)
                    elif compteur_j1 == 20:
                        if count_hit_j1 > 0:
                            count_hit_j1 -= 1
                            screen.blit(j1_hit_2, pos_j1)
                        else:
                            screen.blit(j1_2, pos_j1)
                        compteur_j1 = 0
                    move_j1 = False

                else:
                    if count_hit_j1 > 0:
                        count_hit_j1 -= 1
                        screen.blit(j1_hit, pos_j1)
                    else:
                        screen.blit(j1, pos_j1)
                    compteur_j1 = 0
            else:
                if move_j1 == True:
                    compteur_j1 += 1
                    if compteur_j1 < 10:
                        if count_hit_j1 > 0:
                            count_hit_j1 -= 1
                            screen.blit(j1_hit_flip_1, pos_j1)
                        else:
                            screen.blit(j1_flip_1, pos_j1)
                    elif compteur_j1 < 20:
                        if count_hit_j1 > 0:
                            count_hit_j1 -= 1
                            screen.blit(j1_hit_flip_2, pos_j1)
                        else:
                            screen.blit(j1_flip_2, pos_j1)
                    elif compteur_j1 == 20:
                        if count_hit_j1 > 0:
                            count_hit_j1 -= 1
                            screen.blit(j1_hit_flip_2, pos_j1)
                        else:
                            screen.blit(j1_flip_2, pos_j1)
                        compteur_j1 = 0
                    move_j1 = False
                else:
                    if count_hit_j1 > 0:
                        count_hit_j1 -= 1
                        screen.blit(j1_hit_flip, pos_j1)
                    else:
                        screen.blit(j1_flip, pos_j1)
                    compteur_j1 = 0
        else :
            game = False
            menu_principale = True
            mixer.music.stop()
            winner = 2
            victory = True
            pos_j1.x = int((345 / 1920) * width)
            pos_j1.y = bloc_base.y-j1.get_height()
            pos_j2.x = int((1500 / 1920) * width)
            pos_j2.y = int(bloc_base.y-j2.get_height())
            

        if alive_j2 == True :
            if heading_j2 == 1:
                if move_j2 == True: #si je joueur a bougé
                    compteur_j2 += 1
                    if compteur_j2 < 10:
                        if count_hit_j2 > 0:
                            count_hit_j2 -= 1
                            screen.blit(j2_hit_1, pos_j2)
                        else:
                            screen.blit(j2_1, pos_j2)
                    elif compteur_j2 < 20:
                        if count_hit_j2 > 0:
                            count_hit_j2 -= 1
                            screen.blit(j2_hit_2, pos_j2)
                        else:
                            screen.blit(j2_2, pos_j2)
                    elif compteur_j2 == 20:
                        if count_hit_j2 > 0:
                            count_hit_j2 -= 1
                            screen.blit(j2_hit_2, pos_j2)
                        else:
                            screen.blit(j2_2, pos_j2)
                        compteur_j2 = 0
                    move_j2 = False

                else:
                    if count_hit_j2 > 0:
                        count_hit_j2 -= 1
                        screen.blit(j2_hit, pos_j2)
                    else:
                        screen.blit(j2, pos_j2)
                    compteur_j2 = 0
            else:
                if move_j2 == True:
                    compteur_j2 += 1
                    if compteur_j2 < 10:
                        if count_hit_j2 > 0:
                            count_hit_j2 -= 1
                            screen.blit(j2_hit_flip_1, pos_j2)
                        else:
                            screen.blit(j2_flip_1, pos_j2)
                    elif compteur_j2 < 20:
                        if count_hit_j2 > 0:
                            count_hit_j2 -= 1
                            screen.blit(j2_hit_flip_2, pos_j2)
                        else:
                            screen.blit(j2_flip_2, pos_j2)
                    elif compteur_j2 == 20:
                        if count_hit_j2 > 0:
                            count_hit_j2 -= 1
                            screen.blit(j2_hit_flip_2, pos_j2)
                        else:
                            screen.blit(j2_flip_2, pos_j2)
                        compteur_j2 = 0
                    move_j2 = False
                else:
                    if count_hit_j2 > 0:
                        count_hit_j2 -= 1
                        screen.blit(j2_hit_flip, pos_j2)
                    else:
                        screen.blit(j2_flip, pos_j2)
                    compteur_j2 = 0
        else :
            game = False
            menu_principale = True
            mixer.music.stop()
            winner = 1
            victory = True
            pos_j1.x = int((345 / 1920) * width)
            pos_j1.y = int(bloc_base.y-j1.get_height())
            pos_j2.x = int((1500 / 1920) * width)
            pos_j2.y = int(bloc_base.y-j2.get_height())

        """Les jauges de vie seront affichées avec un remplissage differrents selon le niveau de vie du personnage"""
        """AFFICHAGE DES JAUGES DE VIE J1"""
        if vie_j1 >= 100:
            screen.blit(jauge_100, pos_jauge_j1)
        elif vie_j1 >= 90:
            screen.blit(jauge_90, pos_jauge_j1)
        elif vie_j1 >= 80:
            screen.blit(jauge_80, pos_jauge_j1)
        elif vie_j1 >= 70:
            screen.blit(jauge_70, pos_jauge_j1)
        elif vie_j1 >= 60:
            screen.blit(jauge_60, pos_jauge_j1)
        elif vie_j1 >= 50:
            screen.blit(jauge_50, pos_jauge_j1)
        elif vie_j1 >= 40:
            screen.blit(jauge_40, pos_jauge_j1)
        elif vie_j1 >= 30:
            screen.blit(jauge_30, pos_jauge_j1)
        elif vie_j1 >= 20:
            screen.blit(jauge_20, pos_jauge_j1)
        elif vie_j1 >= 10:
            screen.blit(jauge_10, pos_jauge_j1)
        elif vie_j1 > 0:
            screen.blit(jauge_0, pos_jauge_j1)
        else:
            winner = 2
            game = False
            menu_principale = True
            victory = True

        """AFFICHAGE DES JAUGES DE VIE J2"""
        if vie_j2 >= 100:
            screen.blit(jauge_100, pos_jauge_j2)
        elif vie_j2 >= 90:
            screen.blit(jauge_90, pos_jauge_j2)
        elif vie_j2 >= 80:
            screen.blit(jauge_80, pos_jauge_j2)
        elif vie_j2 >= 70:
            screen.blit(jauge_70, pos_jauge_j2)
        elif vie_j2 >= 60:
            screen.blit(jauge_60, pos_jauge_j2)
        elif vie_j2 >= 50:
            screen.blit(jauge_50, pos_jauge_j2)
        elif vie_j2 >= 40:
            screen.blit(jauge_40, pos_jauge_j2)
        elif vie_j2 >= 30:
            screen.blit(jauge_30, pos_jauge_j2)
        elif vie_j2 >= 20:
            screen.blit(jauge_20, pos_jauge_j2)
        elif vie_j2 >= 10:
            screen.blit(jauge_10, pos_jauge_j2)
        elif vie_j2 > 0:
            screen.blit(jauge_0, pos_jauge_j2)
        else:
            winner = 1
            game = False
            menu_principale = True
            victory = True

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
        """Affichage des icones d'armes en fonction du nombre de fois où l'on appuie sur la touche"""
        """1: AK; 2:grenade; 3:uzi; 4:rpg; 5:shotgun"""
        if count_weapon_j1 == 6:
            count_weapon_j1 = 1
        if count_weapon_j1 == 1:
            if reload_status_weapon1_j1 == 0:
                if weapon1_j1 > 30/2:
                    screen.blit(ak_neutral_use, pos_ak_j1)
                elif weapon1_j1 > 0:
                    screen.blit(ak_neutral_use50, pos_ak_j1)
                else:
                    screen.blit(ak_neutral_use_empty, pos_ak_j1)
            elif reload_status_weapon1_j1 <= ((60*3)/4) * 1:
                screen.blit(ak_neutral_use_reload25, pos_ak_j1)
            elif reload_status_weapon1_j1 <= ((60*3)/4) * 2:
                screen.blit(ak_neutral_use_reload50, pos_ak_j1)
            elif reload_status_weapon1_j1 <= ((60*3)/4) * 3:
                screen.blit(ak_neutral_use_reload75, pos_ak_j1)
            
        elif count_weapon_j1 == 2:
            if reload_status_weapon2_j1 == 0:
                screen.blit(grenade_neutral_use, pos_grenade_j1)
            elif reload_status_weapon2_j1 <= ((60*2)/4) * 1:
                screen.blit(grenade_neutral_use_reload25, pos_grenade_j1)
            elif reload_status_weapon2_j1 <= ((60*2)/4) * 2:
                screen.blit(grenade_neutral_use_reload50, pos_grenade_j1)
            elif reload_status_weapon2_j1 <= ((60*2)/4) * 3:
                screen.blit(grenade_neutral_use_reload75, pos_grenade_j1)
                
        elif count_weapon_j1 == 3:
            if reload_status_weapon3_j1 == 0:
                if weapon3_j1 > 20/2:
                    screen.blit(uzi_neutral_use, pos_uzi_j1)
                elif weapon3_j1 > 0:
                    screen.blit(uzi_neutral_use50, pos_uzi_j1)
                else:
                    screen.blit(uzi_neutral_use_empty, pos_uzi_j1)
            elif reload_status_weapon3_j1 <= ((60*2)/4) * 1:
                screen.blit(uzi_neutral_use_reload25, pos_uzi_j1)
            elif reload_status_weapon3_j1 <= ((60*2)/4) * 2:
                screen.blit(uzi_neutral_use_reload50, pos_uzi_j1)
            elif reload_status_weapon3_j1 <= ((60*2)/4) * 3:
                screen.blit(uzi_neutral_use_reload75, pos_uzi_j1)
        
            
        elif count_weapon_j1 == 4:
            if reload_status_weapon4_j1 == 0:
                screen.blit(rpg_neutral_use, pos_rpg_j1)
            elif reload_status_weapon4_j1 <= ((60*3)/4) * 1:
                screen.blit(rpg_neutral_use_reload25, pos_rpg_j1)
            elif reload_status_weapon4_j1 <= ((60*3)/4) * 2:
                screen.blit(rpg_neutral_use_reload50, pos_rpg_j1)
            elif reload_status_weapon4_j1 <= ((60*3)/4) * 3:
                screen.blit(rpg_neutral_use_reload75, pos_rpg_j1)
            
        elif count_weapon_j1 == 5:
            if reload_status_weapon5_j1 == 0:
                if weapon5_j1 > 5/2:
                    screen.blit(shotgun_neutral_use, pos_shotgun_j1)
                elif weapon5_j1 > 0:
                    screen.blit(shotgun_neutral_use50, pos_shotgun_j1)
                else:
                    screen.blit(uzi_neutral_use_empty, pos_shotgun_j1)
            elif reload_status_weapon5_j1 <= ((60*4)/4) * 1:
                screen.blit(shotgun_neutral_use_reload25, pos_shotgun_j1)
            elif reload_status_weapon5_j1 <= ((60*4)/4) * 2:
                screen.blit(shotgun_neutral_use_reload50, pos_shotgun_j1)
            elif reload_status_weapon5_j1 <= ((60*4)/4) * 3:
                screen.blit(shotgun_neutral_use_reload75, pos_shotgun_j1)
            

        """COMPTEUR SWITCH ARMES J2"""
        if count_weapon_j2 == 6:
            count_weapon_j2 = 1
        if count_weapon_j2 == 1:
            if reload_status_weapon1_j2 == 0:
                if weapon1_j2 > 30/2:
                    screen.blit(ak_neutral_use, pos_ak_j2)
                elif weapon1_j2 > 0:
                    screen.blit(ak_neutral_use50, pos_ak_j2)
                else:
                    screen.blit(ak_neutral_use_empty, pos_ak_j2)
            elif reload_status_weapon1_j2 <= ((60*3)/4) * 1:
                screen.blit(ak_neutral_use_reload25, pos_ak_j2)
            elif reload_status_weapon1_j2 <= ((60*3)/4) * 2:
                screen.blit(ak_neutral_use_reload50, pos_ak_j2)
            elif reload_status_weapon1_j2 <= ((60*3)/4) * 3:
                screen.blit(ak_neutral_use_reload75, pos_ak_j2)
            
        elif count_weapon_j2 == 2:
            if reload_status_weapon2_j2 == 0:
                screen.blit(grenade_neutral_use, pos_grenade_j2)
            elif reload_status_weapon2_j2 <= ((60*2)/4) * 1:
                screen.blit(grenade_neutral_use_reload25, pos_grenade_j2)
            elif reload_status_weapon2_j2 <= ((60*2)/4) * 2:
                screen.blit(grenade_neutral_use_reload50, pos_grenade_j2)
            elif reload_status_weapon2_j2 <= ((60*2)/4) * 3:
                screen.blit(grenade_neutral_use_reload75, pos_grenade_j2)
                
        elif count_weapon_j2 == 3:
            if reload_status_weapon3_j2 == 0:
                if weapon3_j2 > 20/2:
                    screen.blit(uzi_neutral_use, pos_uzi_j2)
                elif weapon3_j2 > 0:
                    screen.blit(uzi_neutral_use50, pos_uzi_j2)
                else:
                    screen.blit(uzi_neutral_use_empty, pos_uzi_j2)
            elif reload_status_weapon3_j2 <= ((60*2)/4) * 1:
                screen.blit(uzi_neutral_use_reload25, pos_uzi_j2)
            elif reload_status_weapon3_j2 <= ((60*2)/4) * 2:
                screen.blit(uzi_neutral_use_reload50, pos_uzi_j2)
            elif reload_status_weapon3_j2 <= ((60*2)/4) * 3:
                screen.blit(uzi_neutral_use_reload75, pos_uzi_j2)
        
            
        elif count_weapon_j2 == 4:
            if reload_status_weapon4_j2 == 0:
                screen.blit(rpg_neutral_use, pos_rpg_j2)
            elif reload_status_weapon4_j2 <= ((60*3)/4) * 1:
                screen.blit(rpg_neutral_use_reload25, pos_rpg_j2)
            elif reload_status_weapon4_j2 <= ((60*3)/4) * 2:
                screen.blit(rpg_neutral_use_reload50, pos_rpg_j2)
            elif reload_status_weapon4_j2 <= ((60*3)/4) * 3:
                screen.blit(rpg_neutral_use_reload75, pos_rpg_j2)
            
        elif count_weapon_j2 == 5:
            if reload_status_weapon5_j2 == 0:
                if weapon5_j2 > 5/2:
                    screen.blit(shotgun_neutral_use, pos_shotgun_j2)
                elif weapon5_j2 > 0:
                    screen.blit(shotgun_neutral_use50, pos_shotgun_j2)
                else:
                    screen.blit(uzi_neutral_use_empty, pos_shotgun_j2)
            elif reload_status_weapon5_j2 <= ((60*4)/4) * 1:
                screen.blit(shotgun_neutral_use_reload25, pos_shotgun_j2)
            elif reload_status_weapon5_j2 <= ((60*4)/4) * 2:
                screen.blit(shotgun_neutral_use_reload50, pos_shotgun_j2)
            elif reload_status_weapon5_j2 <= ((60*4)/4) * 3:
                screen.blit(shotgun_neutral_use_reload75, pos_shotgun_j2)
        
        lenb = len(bullets)
        for i in range(0, lenb):
            lenb = len(bullets)
            if (i < lenb):
                if bullets[i] == 1:
                    # Attention ! t = temps[i] % 60
                    
                    widths[i] = ((800*cos(angle0[i])*(temps[i]/60))*orientations[i] / 1920) * width + width0[i]
                    heights[i] = (((1/2)*30*(temps[i]/60)**2 - 800*sin(angle0[i])*(temps[i]/60)) / 1080) * height + height0[i]+(40/1080)*height # g = 30 V0 = 800 a = 0
                    temps[i] += 1
                    if widths[i] > bloc_base.x and widths[i] < bloc_base.x + bloc_base.w and heights[i] > bloc_base.y and heights[i] < bloc_base.y + bloc_base.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 1 and widths[i] > bloc_1.x and widths[i] < bloc_1.x + bloc_1.w and heights[i] > bloc_1.y and heights[i] < bloc_1.y + bloc_1.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 2 and widths[i] > bloc_2.x and widths[i] < bloc_2.x + bloc_2.w and heights[i] > bloc_2.y and heights[i] < bloc_2.y + bloc_2.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 3 and widths[i] > bloc_3.x and widths[i] < bloc_3.x + bloc_3.w and heights[i] > bloc_3.y and heights[i] < bloc_3.y + bloc_3.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 4 and widths[i] > bloc_4.x and widths[i] < bloc_4.x + bloc_4.w and heights[i] > bloc_4.y and heights[i] < bloc_4.y + bloc_4.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 5 and widths[i] > bloc_5.x and widths[i] < bloc_5.x + bloc_5.w and heights[i] > bloc_5.y and heights[i] < bloc_5.y + bloc_5.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)

                    elif widths[i] > pos_j1.x and widths[i] < pos_j1.x + j1.get_width() and heights[i] > pos_j1.y and heights[i] < pos_j1.y + j1.get_height():
                        #hitbox j1
                        
                        vie_j1 -= 3
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                        count_hit_j1 = 20
                    
                    elif widths[i] > pos_j2.x and widths[i] < pos_j2.x + j2.get_width() and heights[i] > pos_j2.y and heights[i] < pos_j2.y + j2.get_height():
                        #hitbox j2
                        
                        vie_j2 -= 3
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                        count_hit_j2 = 20
                        
                    elif widths[i] > width or widths[i] < 0 or heights[i] > height:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)

                    else:
                        screen.blit(bullet1, (widths[i], heights[i]))

                    
                        if temps[i] > 60*5:
                            # Mode sans échec
                            temps.pop(i)
                            bullets.pop(i)
                            widths.pop(i)
                            heights.pop(i)
                            orientations.pop(i)
                            width0.pop(i)
                            height0.pop(i)
                            angle0.pop(i)
                            explosion.pop(i)
                    
                    
                elif bullets[i] == 2: #grenade
                    temps[i] += 1
                    if  widths[i] > bloc_base.x and widths[i] < bloc_base.x + bloc_base.w and heights[i] > bloc_base.y and heights[i] < bloc_base.y + bloc_base.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 1 and widths[i] > bloc_1.x and widths[i] < bloc_1.x + bloc_1.w and heights[i] > bloc_1.y and heights[i] < bloc_1.y + bloc_1.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 2 and widths[i] > bloc_2.x and widths[i] < bloc_2.x + bloc_2.w and heights[i] > bloc_2.y and heights[i] < bloc_2.y + bloc_2.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 3 and widths[i] > bloc_3.x and widths[i] < bloc_3.x + bloc_3.w and heights[i] > bloc_3.y and heights[i] < bloc_3.y + bloc_3.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 4 and widths[i] > bloc_4.x and widths[i] < bloc_4.x + bloc_4.w and heights[i] > bloc_4.y and heights[i] < bloc_4.y + bloc_4.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 5 and widths[i] > bloc_5.x and widths[i] < bloc_5.x + bloc_5.w and heights[i] > bloc_5.y and heights[i] < bloc_5.y + bloc_5.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif widths[i] > pos_j1.x and widths[i] < pos_j1.x + j1.get_width() and heights[i] > pos_j1.y and heights[i] < pos_j1.y + j1.get_height() and explosion[i] <= 0:
                        #hitbox j1
                        
                        vie_j1 -= 50
                        count_hit_j1 = 20
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))

                    
                    elif widths[i] > pos_j2.x and widths[i] < pos_j2.x + j2.get_width() and heights[i] > pos_j2.y and heights[i] < pos_j2.y + j2.get_height() and explosion[i] <= 0:
                        #hitbox j2
                        
                        vie_j2 -= 50
                        count_hit_j2 = 20
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))

                    
                    elif widths[i] > width or widths[i] < 0 or heights[i] > height:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)

                    elif explosion[i] <= 0:
                        widths[i] = (400*cos(pi/4)*(temps[i]/60))*orientations[i] + width0[i]
                        heights[i] = (1/2)*300*(temps[i]/60)**2 - 400*sin(pi/4)*(temps[i]/60) + height0[i]+(60/1080)*height #  g = 300 V0 = 400 a = pi/4
                        screen.blit(bullet2, (widths[i], heights[i]))

                    elif explosion[i] > 0:
                        
                        if explosion[i] == 1:
                            screen.blit(exp1, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 2:
                            screen.blit(exp2, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 3:
                            screen.blit(exp3, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 4:
                            screen.blit(exp4, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 5:
                            screen.blit(exp5, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 6:
                            screen.blit(exp6, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 7:
                            screen.blit(exp7, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 8:
                            screen.blit(exp8, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 9:
                            screen.blit(exp9, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 10:
                            screen.blit(exp10, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 11:
                            screen.blit(exp11, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 12:
                            screen.blit(exp12, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 13:
                            screen.blit(exp13, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 14:
                            screen.blit(exp14, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 15:
                            screen.blit(exp15, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 16:
                            screen.blit(exp16, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        explosion[i] += 1
                        if explosion[i] > 16:
                            temps.pop(i)
                            bullets.pop(i)
                            widths.pop(i)
                            heights.pop(i)
                            orientations.pop(i)
                            width0.pop(i)
                            height0.pop(i)
                            angle0.pop(i)
                            explosion.pop(i)
                        

                    
                    
                    else:
                        screen.blit(bullet2, (widths[i], heights[i]))

                    
                        if temps[i] > 60*5:
                            # Mode sans échec
                            temps.pop(i)
                            bullets.pop(i)
                            widths.pop(i)
                            heights.pop(i)
                            orientations.pop(i)
                            width0.pop(i)
                            height0.pop(i)
                            angle0.pop(i)
                            explosion.pop(i)
                    
                      
   
                        
                elif bullets[i] == 3: #uzi
                    widths[i] = ((((800*cos(angle0[i])*(temps[i]/60))*orientations[i]) / 1920) * width) + width0[i]
                    heights[i] = ((((1/2)*30*(temps[i]/60)**2 - 800*sin(angle0[i])*(temps[i]/60)) / 1080) * height) + height0[i]+(60/1080)*height # g = 30 V0 = 800 a = 0
                    temps[i] += 1
                    if widths[i] > bloc_base.x and widths[i] < bloc_base.x + bloc_base.w and heights[i] > bloc_base.y and heights[i] < bloc_base.y + bloc_base.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 1 and widths[i] > bloc_1.x and widths[i] < bloc_1.x + bloc_1.w and heights[i] > bloc_1.y and heights[i] < bloc_1.y + bloc_1.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 2 and widths[i] > bloc_2.x and widths[i] < bloc_2.x + bloc_2.w and heights[i] > bloc_2.y and heights[i] < bloc_2.y + bloc_2.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 3 and widths[i] > bloc_3.x and widths[i] < bloc_3.x + bloc_3.w and heights[i] > bloc_3.y and heights[i] < bloc_3.y + bloc_3.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 4 and widths[i] > bloc_4.x and widths[i] < bloc_4.x + bloc_4.w and heights[i] > bloc_4.y and heights[i] < bloc_4.y + bloc_4.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 5 and widths[i] > bloc_5.x and widths[i] < bloc_5.x + bloc_5.w and heights[i] > bloc_5.y and heights[i] < bloc_5.y + bloc_5.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)

                    elif widths[i] > pos_j1.x and widths[i] < pos_j1.x + j1.get_width() and heights[i] > pos_j1.y and heights[i] < pos_j1.y + j1.get_height():
                        #hitbox j1
                        
                        vie_j1 -= 3
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                        count_hit_j1 = 20
                    
                    elif widths[i] > pos_j2.x and widths[i] < pos_j2.x + j2.get_width() and heights[i] > pos_j2.y and heights[i] < pos_j2.y + j2.get_height():
                        #hitbox j2
                        
                        vie_j2 -= 3
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                        count_hit_j2 = 20
                    
                    elif widths[i] > width or widths[i] < 0 or heights[i] > height:
                            temps.pop(i)
                            bullets.pop(i)
                            widths.pop(i)
                            heights.pop(i)
                            orientations.pop(i)
                            width0.pop(i)
                            height0.pop(i)
                            angle0.pop(i)
                            explosion.pop(i)

                    else:
                        screen.blit(bullet3, (widths[i], heights[i]))

                    
                        if temps[i] > 60*5:
                            # Mode sans échec
                            temps.pop(i)
                            bullets.pop(i)
                            widths.pop(i)
                            heights.pop(i)
                            orientations.pop(i)
                            width0.pop(i)
                            height0.pop(i)
                            angle0.pop(i)
                            explosion.pop(i)
                
                elif bullets[i] == 4: #rocket
                    temps[i] += 1
                    if widths[i] > bloc_base.x and widths[i] < bloc_base.x + bloc_base.w and heights[i] > bloc_base.y and heights[i] < bloc_base.y + bloc_base.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 1 and widths[i] > bloc_1.x and widths[i] < bloc_1.x + bloc_1.w and heights[i] > bloc_1.y and heights[i] < bloc_1.y + bloc_1.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 2 and widths[i] > bloc_2.x and widths[i] < bloc_2.x + bloc_2.w and heights[i] > bloc_2.y and heights[i] < bloc_2.y + bloc_2.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 3 and widths[i] > bloc_3.x and widths[i] < bloc_3.x + bloc_3.w and heights[i] > bloc_3.y and heights[i] < bloc_3.y + bloc_3.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 4 and widths[i] > bloc_4.x and widths[i] < bloc_4.x + bloc_4.w and heights[i] > bloc_4.y and heights[i] < bloc_4.y + bloc_4.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    elif count_bloc >= 5 and widths[i] > bloc_5.x and widths[i] < bloc_5.x + bloc_5.w and heights[i] > bloc_5.y and heights[i] < bloc_5.y + bloc_5.h and explosion[i] <= 0:
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                        
                    elif widths[i] > pos_j1.x and widths[i] < pos_j1.x + j1.get_width() and heights[i] > pos_j1.y and heights[i] < pos_j1.y + j1.get_height() and explosion[i] <= 0:
                        #hitbox j1
                        
                        vie_j1 -= 30
                        count_hit_j1 = 20
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))
                    
                    elif widths[i] > pos_j2.x and widths[i] < pos_j2.x + j2.get_width() and heights[i] > pos_j2.y and heights[i] < pos_j2.y + j2.get_height() and explosion[i] <= 0:
                        #hitbox j2
                        
                        vie_j2 -= 30
                        count_hit_j2 = 20
                        explosion[i] = 1
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(curdir + "/audio/rocket-launcher-explosion.mp3"))

                    
                    elif widths[i] > width or widths[i] < 0 or heights[i] > height:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)

                    elif explosion[i] <= 0:
                        widths[i] = ((((30)*orientations[i]) / 1920) * width) + widths[i]
                        heights[i] = height0[i]+(40/1080)*height
                        screen.blit(bullet4, (widths[i], heights[i]))
                    elif explosion[i] > 0:
                        
                        if explosion[i] == 1:
                            screen.blit(exp1, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 2:
                            screen.blit(exp2, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 3:
                            screen.blit(exp3, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 4:
                            screen.blit(exp4, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 5:
                            screen.blit(exp5, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 6:
                            screen.blit(exp6, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 7:
                            screen.blit(exp7, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 8:
                            screen.blit(exp8, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 9:
                            screen.blit(exp9, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 10:
                            screen.blit(exp10, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 11:
                            screen.blit(exp11, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 12:
                            screen.blit(exp12, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 13:
                            screen.blit(exp13, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 14:
                            screen.blit(exp14, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 15:
                            screen.blit(exp15, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        if explosion[i] == 16:
                            screen.blit(exp16, (int(widths[i]-exp1.get_width()/2), int(heights[i]-exp1.get_height()/2)))
                        explosion[i] += 1
                        if explosion[i] > 16:
                            temps.pop(i)
                            bullets.pop(i)
                            widths.pop(i)
                            heights.pop(i)
                            orientations.pop(i)
                            width0.pop(i)
                            height0.pop(i)
                            angle0.pop(i)
                            explosion.pop(i)
                        

                    
                    
                    else:
                        screen.blit(bullet4, (widths[i], heights[i]))

                    
                        if temps[i] > 60*5:
                            # Mode sans échec
                            temps.pop(i)
                            bullets.pop(i)
                            widths.pop(i)
                            heights.pop(i)
                            orientations.pop(i)
                            width0.pop(i)
                            height0.pop(i)
                            angle0.pop(i)
                            explosion.pop(i)
                    
                elif bullets[i] == 5:
                    widths[i] = ((((800*cos(angle0[i])*(temps[i]/60))*orientations[i]) / 1920) * width) + width0[i]
                    heights[i] = ((((1/2)*30*(temps[i]/60)**2 - 800*sin(angle0[i])*(temps[i]/60)) / 1080) * height) + height0[i]+(60/1080)*height # g = 30 V0 = 800 a = 0
                    temps[i] += 1
                    if widths[i] > bloc_base.x and widths[i] < bloc_base.x + bloc_base.w and heights[i] > bloc_base.y and heights[i] < bloc_base.y + bloc_base.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 1 and widths[i] > bloc_1.x and widths[i] < bloc_1.x + bloc_1.w and heights[i] > bloc_1.y and heights[i] < bloc_1.y + bloc_1.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 2 and widths[i] > bloc_2.x and widths[i] < bloc_2.x + bloc_2.w and heights[i] > bloc_2.y and heights[i] < bloc_2.y + bloc_2.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 3 and widths[i] > bloc_3.x and widths[i] < bloc_3.x + bloc_3.w and heights[i] > bloc_3.y and heights[i] < bloc_3.y + bloc_3.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 4 and widths[i] > bloc_4.x and widths[i] < bloc_4.x + bloc_4.w and heights[i] > bloc_4.y and heights[i] < bloc_4.y + bloc_4.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                    elif count_bloc >= 5 and widths[i] > bloc_5.x and widths[i] < bloc_5.x + bloc_5.w and heights[i] > bloc_5.y and heights[i] < bloc_5.y + bloc_5.h:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)

                    elif widths[i] > pos_j1.x and widths[i] < pos_j1.x + j1.get_width() and heights[i] > pos_j1.y and heights[i] < pos_j1.y + j1.get_height():
                        #hitbox j1
                        
                        vie_j1 -= 3
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                        count_hit_j1 = 20
                    
                    elif widths[i] > pos_j2.x and widths[i] < pos_j2.x + j2.get_width() and heights[i] > pos_j2.y and heights[i] < pos_j2.y + j2.get_height():
                        #hitbox j2
                        
                        vie_j2 -= 3
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)
                        count_hit_j2 = 20
                    
                    elif widths[i] > width or widths[i] < 0 or heights[i] > height:
                        temps.pop(i)
                        bullets.pop(i)
                        widths.pop(i)
                        heights.pop(i)
                        orientations.pop(i)
                        width0.pop(i)
                        height0.pop(i)
                        angle0.pop(i)
                        explosion.pop(i)

                    else:
                        screen.blit(bullet5, (widths[i], heights[i]))

                    
                        if temps[i] > 60*5:
                            # Mode sans échec
                            temps.pop(i)
                            bullets.pop(i)
                            widths.pop(i)
                            heights.pop(i)
                            orientations.pop(i)
                            width0.pop(i)
                            height0.pop(i)
                            angle0.pop(i)
                            explosion.pop(i)
            lenb = len(bullets)
        #raffraichissement
        #pygame.draw.rect(screen, red, bloc_1)
        #pygame.draw.rect(screen, red, bloc_2)
        #pygame.draw.rect(screen, red, bloc_3)
        #pygame.draw.rect(screen, red, bloc_4)
        #pygame.draw.rect(screen, red, bloc_5)
        #pygame.draw.rect(screen, red, bloc_base)
        pygame.display.flip()

        #pygame.time.delay(16)
    passage = True
    while victory == True :
        fpsClock.tick(15)
        if winner == 1 :
            if passage == True :
                win_background = pygame.image.load(curdir + "/images/j1_win.png").convert()
                win_background = pygame.transform.scale(win_background, (width, height))
                passage = False
        else :
            if passage == True :
                win_background = pygame.image.load(curdir + "/images/j2_win.png").convert()
                win_background = pygame.transform.scale(win_background, (width, height))
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
