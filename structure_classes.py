
"""Level for the MacGyver game"""

# coding utf-8
# import needed modules
import pygame
import random
from pygame.locals import *
from constants import *


class Level:
    def __init__(self, file):
        """Class to structure the level"""
    # uses the file 'labstruc' to create the structure
        self.file = file
        self.structure = 0

    def generate(self):
        """Method class that iterates through the file and map out the level"""
        # opens the file
        with open(self.file, "r") as file:
            level_structure = []

            # iterates through the lines
            for line in file:
                level_line = []

                # iterates through the lettre in the file
                for sprite in line:

                    if sprite != '\n':

                        # adds sprite to the line
                        level_line.append(sprite)

                # adds line ti the structure
                level_structure.append(level_line)

            # saving structure
            self.structure = level_structure

    def showscreen(self, window):
        """Method class adding corresponding images to the strucutre"""
    # initializing tiles, loading images
        floor = pygame.image.load('images/tilefloor.png').convert()
        wall = pygame.image.load('images/tilewall.png').convert()
        start = pygame.image.load('images/tilestart.png').convert()
        finish = pygame.image.load('images/tilestart.png').convert()

        # iterates through the structure
        num_line = 0
        for line in self.structure:
            # iterates through the lines
            num_pos = 0
            for sprite in line:
                # calculating pixel position
                x = num_pos * sprite_size
                y = num_line * sprite_size
                # show on the screen the corresponding tiles
                if sprite == 'm':
                    window.blit(wall, (x, y))
                elif sprite == '0':
                    window.blit(floor, (x, y))
                elif sprite == 'd':
                    window.blit(start, (x, y))
                elif sprite == 'a':
                    window.blit(finish, (x, y))
                num_pos += 1
            num_line += 1





