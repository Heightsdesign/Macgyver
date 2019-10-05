# coding utf-8

import pygame
import random
from pygame.locals import *
from constants import *
from Classes import *

#initialize pygame
pygame.init()

#create a window 300 x 300 pixels
window = pygame.display.set_mode((window_side, window_side))

pygame.display.set_caption("Macgyver Reloaded")

main_loop = 1
macgyver = Character('images/ MacGyver.png')

#main loop
while  main_loop:  
    #if the player presses escape button or clicks on quit the game closes
    for event in pygame.event.get():
        if event.type == QUIT or  event.type == KEYDOWN and event.key == K_ESCAPE:
            main_loop = 0
     #structure file       
    labstruc = 'labstruc.txt'

    #creates the level from the file
    level = Level(labstruc)
    level.generate()
    level.showscreen(window)

    for event in pygame.event.get():
         # if player presses a following key 
        if event.type == KEYDOWN:
             #if player presses the right key character moves right
            if event.key == K_RIGHT:
                macgyver.move('right', level)
            if event.key == K_LEFT:
                macgyver.move('left', level)
            if event.key == K_UP:
                macgyver.move('up', level)
            if event.key == K_DOWN:
                macgyver.move('down', level)
    
   #show on the screen 
    window.blit(macgyver.character, (macgyver.x, macgyver.y))
    pygame.display.flip()



pygame.quit()
