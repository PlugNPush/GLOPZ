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
        self.position = pygame.Rect((x, y), (LARGEUR_DU_MUR, HAUTEUR_DU_MUR))  # rectangle

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

#classe player
def move right(self):
    #si le joueur1 n'est pas en collision avec le joueur2
    if self.game.check_collision(self, self.game.all.joueur2):
        self.rect.x += self.velocity

def foward(self):
    #le déplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
    if not self.game.check_collision(self, self.game.all_players):
        self.rect.x -= self.velocity



#--------------------------    hitbox copié  ------------------------

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


#--------------    hitbox 2  ----------------

import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

                


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()