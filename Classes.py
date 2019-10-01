#coding utf-8

import pygame
from pygame.locals import *
from constants import *

class Level:
    def __init__(self, file):

        self.file = file
        self.structure  = 0

    def generate(self):

        with open(self.file, "r") as file:
            level_structure = []

            for line in file:
                level_line = []

                for sprite in line :

                    if sprite != '\n':

                        level_line.append(sprite)

                level_structure.append(level_line)

            self.structure = level_structure

    def showscreen(self, window):
        floor =  pygame.image.load('tilefloor.png').convert()
        wall = pygame.image.load('tilewall.png').convert()
        start = pygame.image.load('tilestart.png').convert()
        finish = pygame.image.load('tilestart.png').convert()

        num_line = 0
        for line in self.structure:
            num_pos = 0
            for sprite in line:

                x = num_pos * sprite_size
                y = num_line * sprite_size

                if sprite == 'm':
                    window.blit(wall, (x,y))
                elif sprite == '0':
                    window.blit(floor, (x,y))
                elif sprite == 'd':
                    window.blit(start, (x,y))
                elif sprite == 'a':
                    window.blit(finish, (x,y))
                num_pos += 1
            num_line += 1
            


class Character:

    def __init__(self,  character):

        self.character = pygame.image.load('MacGyver.png').convert()

        self.pos_x = 0
        self.pos_y = 0
        self.x = 0
        self.y = 0

    def move(self, direction):

        if direction == 'right':

            if self.pos_x < (sprite_number - 1):

                if self.level.strucutre[self.pos_y][self.pos_x+1] != 'm':
                    self.pos_x += 1
                    self.x = self.pos_x * sprite_size
            self.direction = self.character

        if direction == 'left':

            if self.pos_x > 0:

                if self.level.structure[self.pos_y][self.pos_x-1] != 'm':
                    self.pos_x -= 1
                    self.x = self.pos_x * sprite_size
            self.direction = self.character

        if direction == 'up':

            if self.pos_y > 0:
                if self.level.structure[self.pos_y-1][self.pos_x] != 'm':
                    self.pos_y -= 1
                    self.y = self.pos_y * sprite_size
            self.direction = self.character

        if direction == 'down':

            if self.pos_y < (sprite_number -1):

                if self.level.structure[self.pos_y+1][self.pos_x] != 'm':
                    self.pos_y+1
                    self.y = self.pos_y * sprite_size
            self.direction = self.character
                    
                    

        

        

        
        
        
        
     
