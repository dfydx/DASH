from pygame.constants import K_SPACE
from player import Player
import sys
import pygame
import time


def check_events(distance):
    #close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #save
            if distance <= 0:
                distance = 0
            save = open('Log/save.txt', 'w')
            save.write( str(distance) )
            #close
            pygame.quit()
            sys.exit()

def player_events():
    #about player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        return False
    elif keys[pygame.K_d]:
        return True

def player_events_jump():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[K_SPACE]:
        return True
    else:
        return False

def player_events_move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w]:
        return True
    else:
        return False

def ground_events_move():
    ground_events = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        ground_events = 1
    elif keys[pygame.K_d]:
        ground_events = 2
    else:
        ground_events = None
    return ground_events
