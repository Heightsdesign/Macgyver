"""Characters for the Macgyver game"""

# coding utf-8
# imports needed modules
import pygame
from pygame.locals import *
import constants
from structure_classes import *


class Character:
    """Class creating a charater"""

    def __init__(self,  character):
        # character sprite
        self.character = pygame.image.load('images/MacGyver.png').convert()
        # character position on the structure and in pixels
        self.pos_x = 0
        self.pos_y = 0
        self.x = 0
        self.y = 0

    def move(self, direction, level):
        """Method making the character move"""

        self.level = level

        # moving in the right direction
        if direction == 'right':
            # limiting movements to the screen
            if self.pos_x < (sprite_number - 1):
                # if position is not a wall
                if self.level.structure[self.pos_y][self.pos_x+1] != 'm':
                    # move in the indicated position
                    self.pos_x += 1
                    # calculating pixel position
                    self.x = self.pos_x * sprite_size

        # if the key pressed is 'left'
        if direction == 'left':
            # making sure the character doesn't go off screen
            if self.pos_x > 0:
                # making sure the level tile is not a wall
                if self.level.structure[self.pos_y][self.pos_x-1] != 'm':
                    self.pos_x -= 1
                    self.x = self.pos_x * sprite_size

        # if the key pressed is 'up'
        if direction == 'up':
            # making sure the character doesn't go off screen
            if self.pos_y > 0:
                # making sure the level tile is not a wall
                if self.level.structure[self.pos_y-1][self.pos_x] != 'm':
                    self.pos_y -= 1
                    self.y = self.pos_y * sprite_size
        # if the key pressed is 'down'
        if direction == 'down':
            # making sure the character doesn't go off screen
            if self.pos_y < (sprite_number - 1):
                # making sure the level tile is not a wall
                if self.level.structure[self.pos_y+1][self.pos_x] != 'm':
                    self.pos_y += 1
                    self.y = self.pos_y * sprite_size


class Villain:
    """Creating Villain"""
    # initializing villian
    def __init__(self, villain):

        # loading image
        self.villain = pygame.image.load('images/Gardien.png')
        # villain x position
        self.posi_x = 13
        # villain y position
        self.posi_y = 14
        self.x = self.posi_x * sprite_size
        self.y = self.posi_y * sprite_size

    def Shallnotpass(self, player):
        """Makes sure the player has collected all items"""

        self.player = player
        
        # checking if the player's  position is equal to the villain's
        if self.x == player.x and self.y == player.y:
            # checking if the player has collected all the items
            if constants.item_count < 4:
                # if not the player will not pass
                player.y -= 20
                print('You shall not pass me ! You sorry SOB !')
                
            # if the player has all the items
            else:
                # remove the villain from the game, set him off screen
                self.x = 320
                print('Aaah so much craftiness, how could he !?')
                print('You win !')
                player.x += 20
