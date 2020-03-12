# coding utf-8

import pygame
import random
from pygame.locals import *
from constants import *
from structure_classes import *
from items_classes import *
from characters_classes import *

def init_game():

    # initialize pygame
    pygame.init()

    # create a window 300 x 300 pixels
    window = pygame.display.set_mode((window_side, window_side))

    # showing window caption Macgyver Reloaded
    pygame.display.set_caption("Macgyver Reloaded")

    # creating infinite loop
    main_loop = 1

    # loading Character, Villain and Items from the classes objects
    macgyver = Character('images/ MacGyver.png')
    murdoc = Villain('images/Gardien.png')
    chest = Item('images/chest.png')
    poison  = Item('images/poison.png')
    coins = Item('images/Coins.png')
    tablet = Item('images/Tablet.png')
    champ = pygame.image.load('images/cheers/cheers.GIF')

    # randomising the items positions
    chest.randpos()
    poison.randpos()
    coins.randpos()
    tablet.randpos()


    # main loop
    while  main_loop:  
        # if the player presses escape button or clicks on quit the game closes
        for event in pygame.event.get():
            if event.type == QUIT or  event.type == KEYDOWN and event.key == K_ESCAPE:
                main_loop = 0

        # structure file       
        labstruc = 'labstruc.txt'

        # creates the level from the file
        level = Level(labstruc)
        level.generate()
        level.showscreen(window)

        # making sure the items do not land on a wall
        chest.nowall(level)
        poison.nowall(level)
        coins.nowall(level)
        tablet.nowall(level)

        for event in pygame.event.get():

             # if player presses a following key 
            if event.type == KEYDOWN:
                 # if player presses the right key character moves right
                if event.key == K_RIGHT:
                    macgyver.move('right', level)
                if event.key == K_LEFT:
                    macgyver.move('left', level)
                if event.key == K_UP:
                    macgyver.move('up', level)
                if event.key == K_DOWN:
                    macgyver.move('down', level)

                # verifying if the objects have been collected with class method
                chest.get_items(macgyver)
                poison.get_items(macgyver)
                coins.get_items(macgyver)
                tablet.get_items(macgyver)

                # checking if the character has all the items
                murdoc.Shallnotpass(macgyver)

        # show on the screen
        window.blit(macgyver.character, (macgyver.x, macgyver.y))
        window.blit(murdoc.villain, (murdoc.x, murdoc.y))
        window.blit(chest.image,(chest.x, chest.y))
        window.blit(poison.poison,(poison.x, poison.y))
        window.blit(coins.coins,(coins.x, coins.y))
        window.blit(tablet.tablet,(tablet.x, tablet.y))

        # if level is complete blit champ image
        if murdoc.x == 320:
            window.blit(champ, (41, 75))

        pygame.display.flip()

if __name__=="__main__":
    init_game()    
    pygame.quit()
