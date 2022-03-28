import sys
import pygame
import random
from settings import Settings
from player import Player
from ground import Ground
import gamefunctions as gf

#load
distance = 0
save = open('Log/save.txt', 'r')
try:
    distance = save.read()
finally:
    save.close()
print(distance)

def run_game(distance):
    fps = 120
    fcclock = pygame.time.Clock()
    distance = int(distance)
    #initialization
    pygame.init()
    #use class
    GameSettings = Settings()

    screen = pygame.display.set_mode(
        (GameSettings.screen_width,GameSettings.screen_height))
    pygame.display.set_caption("Dash")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    #player
    player = Player(screen)
    playerY = 300
    player_movespeed = 10
    player_jumpspeed_global = 1000
    player_jumpspeed = player_jumpspeed_global
    playerHP = 100
    default_isright = True

    #ground
    ground = Ground(screen)
    groundX = 1100
    groundY = 370
    gspeed = 2600


    #main loop
    while True:
        isright_main = gf.player_events()
        isjump_main = gf.player_events_jump()
        ismove_main = gf.player_events_move()
        groundmove_main = gf.ground_events_move()

        #about playerY
        player_jumpspeed += gspeed * 1 / fps

        if playerY > groundY:
            if isjump_main:
                player_jumpspeed = player_jumpspeed_global
                player_jumpspeed = -player_jumpspeed
            else:
                player_jumpspeed = 0
        playerY += player_jumpspeed * 1 / fps

        #about playerHP
        if groundX >=-100 and groundX <=140 and playerY >= 369 and playerY<= 379:
            playerHP = playerHP - 0.1
        if playerHP <= 0:
            playerHP = 0

        #about player direction
        if isright_main == True:
            default_isright = True
        elif isright_main == False:
            default_isright = False
        
        #aboyt player speed
        if groundmove_main == 1 or groundmove_main == 2:
            if player_movespeed < 20:
                player_movespeed = player_movespeed + 0.05
        else:
            player_movespeed = 10

        if groundmove_main == 1:
            groundX = groundX + player_movespeed
        elif groundmove_main == 2:
            groundX = groundX - player_movespeed

        #about distance
        if distance <= 0:
            distance = 0
        elif distance >= 1000000:
            distance = 1000000

        if groundmove_main == 2:
            distance = distance + 1
        elif groundmove_main == 1:
            distance = distance - 1
        print(distance)
        #about groundX
        randomX1 = int(random.uniform(500,1000))
        randomX2 = int(random.uniform(1000,5000))
        if groundX <= -1 * randomX1:
            groundX = 1100
        elif groundX >= randomX2:
            groundX = -220

        #check and save
        gf.check_events(distance)
        #blitme
        screen.fill(GameSettings.bg_color)
        player.blitme(playerY,ismove_main,default_isright,isright_main,isjump_main,screen,playerHP)
        ground.blitme(groundX)
        fcclock.tick(fps)
        pygame.display.flip()

if __name__ == "__main__":
    run_game(distance)
