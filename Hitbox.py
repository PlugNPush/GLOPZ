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
 
screen = pygame.display.set_mode((l,h)) #on ouvre une fenêtre pygame avec les valeurs l et h données
 
clock = pygame.time.Clock() # on utilise la fonction clock pour controler le framerate du jeu
 
 
class player:
    def __init__(self):  # self définit un objet manipulable pas le joueur , ici le personnage
        self.x = 200     # position x du personnage
        self.y = 300      # position y du personnage
        self.ani_speed_init=4       #vitesse initial de l'animation
        self.ani_speed=self.ani_speed_init       # pour que la vitesse de l'animation soit la même que sa vitesse initiale
        self.ani = glob.glob("marche/bob*.png")      # on utilise le module et la fonction glob pour rechercher les images a charger dans un dossier spécifique (ici marche) et il va charger tous les objets commencant par "bob"
        self.ani.sort()                # ceci va permettre de classer dans l'ordre les images chargées précédemment ( bob1, bob2, bob3 ...)
        self.ani_pos=0                 # on place l'animation a la première frame a la position 0
        self.ani_max = len(self.ani)-1              # on soustrait 1 aux images pour définir l'animation max pour éviter l'erreur "list index out of range" et permettre la répétition des images 
        self.img = pygame.image.load(self.ani[0])        # pygame charge l'image a l'animation 0
        self.update(0)
         
    def update(self, pos):     # après le chargement des images il va être question ici du déplacament du personnage
        if pos == 0:           # si le personnage est immobile, l'image bob0 va s'ouvrir
            self.img = pygame.image.load("bob0.png")
        if pos == 1:            # si la position du personnage est de 1 (il va vers la droite)
            self.ani = glob.glob("marche/bob*.png")         # on va charger les images du perso qui va vers la droite
            self.ani_speed-=1             # la vitesse va être égale a la vitesse de l'animation -1 ( donc 4 ici)
            self.x+=pos+1                 # et on va additionner la nouvelle position du personnage a sa position initiale x définie a 200, de plus , on rajoutte la valeur 1 car sinon le déplacement est trop lent
            if self.ani_speed == 0:            # si l'animation du personnage est de 0 alors il y aura un retours a la valeur 5 de la vitesse initiale
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:         # si l'animation atteind sa frame maximale alors
                    self.ani_pos = 0                     # la position de l'animation ( et non du personnage ) reviens a 0 pour créer une boucle
                else:
                    self.ani_pos+=1
                     
        if pos == -3:             # si le perso a une position de -3 (il retourne en arrière)
            self.ani = glob.glob("marche_gauche/bob*.png")            # on va charger les image du perso qui va vers la gauche
            self.ani_speed-=1                # la vitesse va être égale a la vitesse de l'animation -1 ( donc 4 ici)
            self.x+=pos+1                    # ensuite on utilise les mêmes procédés que lorsque le perso va vers la droite
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos+=1
                     
        screen.blit(self.img,(self.x,self.y))         # on affiche l'image a l'écran sinon rien n'apparait
player1 = player()
pos = 0
             
while 1:
    screen.fill((0,0,0))       #fond noir
    clock.tick(60)             # framerate ( 60 fps)
                               # ensuite vient la gestion des évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            pos = 1            # si la flèche de droite est enfoncée alors le personnage avancera vers la droite
        elif event.type == KEYUP and event.key == K_RIGHT:
            pos = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            pos = -3           # si la flèche gauche est enfoncée alors le personnage avancera vers la gauche
        elif event.type == KEYUP and event.key == K_LEFT:
            pos = 0
    player1.update(pos)         # la nouvelle position du joueur est mise a jours
     
    pygame.display.update()      # chaque boucle de "update" va reblitter le personnage sur l'écran
     
    class hero(pygame.sprite.Sprite):
        def __init__(self):
            self.image_face = pygame.image.load("bob.png").convert_alpha()
            self.position = pygame.Rect(85, 168, 27, 32,)
          
hero = hero()

# -------------------------    hitbox  --------------------

class Wall:
    def __init__(self, tile, x, y):
        self.image = pygame.image.load(tile).convert_alpha()                   # texture du mur
        self.position = pygame.Rect((x, y), (LARGEUR_DU_MUR, HAUTEUR_DU_MUR))  # rectangle

for wall in walls:
    if wall.colliderect(player.position):
         player.position = player.old_position


#-------------------------    hitbox copié  -------------------------

import sys, time, random, math, pygame
from pygame.locals import *
from My_Library import *

class Bullet():
    def __init__(self, position):
        self.alive = True
        self.color = (250, 20, 20)
        self.position = Point(position.x, position.y)
        self.velocity = Point(0, 0)
        self.rect = Rect(0, 0, 4, 4)
        self.owner = ""

    def update(self, ticks):
        self.position.x -= self.velocity.x * 10.0
        self.position.y -= self.velocity.y * 10.0
        if self.position.x < 0 or self.position.x > 800 \
           or self.position.y < 0 or self.position.y > 600:
            self.alive = False
        self.rect = Rect(self.position.x, self.position.y, 4, 4)

    def draw(self, surface):
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(surface, self.color, pos, 4, 0)

def fire_cannon(tank):
    position = Point(tank.turret.X, tank.turret.Y)
    bullet = Bullet(position)
    angle = tank.turret.rotation + 90
    bullet.velocity = angular_velocity(angle)
    bullets.append(bullet)
    play_sound(shoot_sound)
    return bullet

def player_fire_cannon():
    bullet = fire_cannon(player)
    bullet.owner = "player"
    bullet.color = (30, 250, 30)

def player2_fire_cannon():
    bullet = fire_cannon(player2)
    bullet.owner = "player2"
    bullet.color = (250, 30, 30)

class Tank(MySprite):
    def __init__(self, tank_file, turret_file):
        MySprite.__init__(self)
        self.load(tank_file, 50, 60, 4)
        self.speed = 0.0
        self.scratch = None
        self.float_pos = Point(0, 0)
        self.velocity = Point(0, 0)
        self.turret = MySprite()
        self.turret = MySprite()
        self.turret.load(turret_file, 32, 64, 4)
        self.fire_timer = 0

    def update(self,ticks):
        # update chassis
        MySprite.update(self, ticks, 100)
        self.rotation = wrap_angle(self.rotation)
        self.scratch = pygame.transform.rotate(self.image, -self.rotation)
        angle = wrap_angle(self.rotation-90)
        self.velocity = angular_velocity(angle)
        self.float_pos.x += self.velocity.x * 2
        self.float_pos.y += self.velocity.y * 2

        # warp tank around screen edges (keep it simple)
        if self.float_pos.x < -50: self.float_pos.x = 800
        elif self.float_pos.x > 800: self.float_pos.x = -50
        if self.float_pos.y < -60: self.float_pos.y = 600
        elif self.float_pos.y > 600: self.float_pos.y = -60

        # transfer float position to integer position for drawing
        self.X = int(self.float_pos.x)
        self.Y = int(self.float_pos.y)

        # update turret
        self.turret.position = (self.X, self.Y)
        self.turret.last_frame = 0
        self.turret.update(ticks, 100)
        self.turret.rotation = wrap_angle(self.turret.rotation)
        angle = wrap_angle(self.turret.rotation)
        self.turret.scratch = pygame.transform.rotate(self.turret.image, -angle)

    def draw(self, surface):
        # draw the chassis
        width, height = self.scratch.get_size()
        center = Point(width/2, height/2)
        surface.blit(self.scratch, (self.X-center.x, self.Y-center.y))        
        # draw the turret
        width, height = self.turret.scratch.get_size()
        center = Point(width/2, height/2)
        surface.blit(self.turret.scratch, (self.turret.X-center.x,
                                           self.turret.Y-center.y))

    def __str__(self):
        return MySprite.__str__(self) + "," + str(self.velocity)

# this function initializes the game
def game_init():
    global screen, backbuffer, font, timer, player_group, player, \
           player2, bullets

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    backbuffer = pygame.Surface((800, 600))
    pygame.display.set_caption("Tank Battle Game")
    font = pygame.font.Font(None, 30)
    timer = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    # create player tank
    player = Tank("tank.png", "turret.png")
    player.float_pos = Point(400, 300)

    # create second player tank
    player2 = Tank("enemy_tank.png", "enemy_turret.png")
    player2.float_pos = Point(random.randint(50, 760), 50)

    # create bullets
    bullets = list()

# this function initializes the audio system
def audio_init():
    global shoot_sound, boom_sound

    # initialize the audio mixer
    pygame.mixer.init()

    # load sound files
    shoot_sound = pygame.mixer.Sound("shoot.wav")
    boom_sound = pygame.mixer.Sound("boom.wav")

# this function uses any available channel to play a sound clip
def play_sound(sound):
    channel = pygame.mixer.find_channel(True)
    channel.set_volume(0.5)
    channel.play(sound)

# main program begins
game_init()
audio_init()
game_over = False
player_score = 0
player2_score = 0
last_time = 0
action1 = False
action2 = False
action3 = False
action4 = False
action5 = False
action6 = False

# main loop
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    # event section
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                action1 = True
            if event.key == pygame.K_RIGHT:
                action2 = True
            if event.key == pygame.K_a:
                action3 = True
            if event.key == pygame.K_d:
                action4 = True
            if event.key == pygame.K_UP:
                action5 = True
            if event.key == pygame.K_w:
                action6 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                action1 = False
            if event.key == pygame.K_RIGHT:
                action2 = False
            if event.key == pygame.K_a:
                action3 = False
            if event.key == pygame.K_d:
                action4 = False
            if event.key == pygame.K_UP:
                action5 = False
            if event.key == pygame.K_w:
                action6 = False

    if action1 == True:
        player.rotation -= 4.0
        player.turret.rotation -= 4.0
    if action2 == True:
        player.rotation += 4.0
        player.turret.rotation += 4.0
    if action3 == True:
        player2.rotation -= 4.0
        player2.turret.rotation -= 4.0
    if action4 == True:
        player2.rotation += 4.0
        player2.turret.rotation += 4.0
    if action5 == True:
        if ticks > player.fire_timer + 1000:
            player.fire_timer = ticks
            player_fire_cannon()
    if action6 == True:
        if ticks > player2.fire_timer + 1000:
            player2.fire_timer = ticks
            player2_fire_cannon()


    # update section
    if not game_over:
        # move tank
        player.update(ticks)

        # update player two
        player2.update(ticks)

        # update bullets
        for bullet in bullets:
                bullet.update(ticks)
                if bullet.owner == "player":
                    if pygame.sprite.collide_rect(bullet, player2):
                        player_score += 1
                        bullet.alive = False
                        play_sound(boom_sound)
                elif bullet.owner == "player2":
                    if pygame.sprite.collide_rect(bullet, player):
                        player2_score += 1
                        bullet.alive = False
                        play_sound(boom_sound)

    # drawing section
    backbuffer.fill((100, 100, 20))

    for bullet in bullets:
        bullet.draw(backbuffer)

    player.draw(backbuffer)

    player2.draw(backbuffer)

    screen.blit(backbuffer, (0, 0))

    if not game_over:
        print_text(font, 0, 0, "PLAYER 1: " + str(player_score))
        print_text(font, 650, 0, "PLAYER 2: " + str(player2_score))
    else:
        print_text(font, 0, 0, "GAME OVER")

    pygame.display.update()

# remove expired bullets
    for bullet in bullets:
        if bullet.alive == False:
            bullets.remove(bullet)



def update(self, ticks):
    self.position.x -= self.velocity.x * 10.0
    self.position.y -= self.velocity.y * 10.0
    if self.position.x < 0 or self.position.x > 800 \
       or self.position.y < 0 or self.position.y > 600:
        self.alive = False
    self.rect = Rect(self.position.x, self.position.y, 4, 4)

def draw(self, surface):
    pos = (int(self.position.x), int(self.position.y))
    pygame.draw.circle(surface, self.color, pos, 4, 0)