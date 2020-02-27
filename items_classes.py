"""Item classes for the Macgyver game"""

# coding utf-8
#imports needed modules
import pygame
from pygame.locals import *
import constants
from structure_classes import *


class Item:
    """ Creating items to collect"""
    # initializing items
    def __init__(self, image):
        # loading images
        self.image = pygame.image.load('images/chest.png')
        self.poison = pygame.image.load('images/poison.png')
        self.coins = pygame.image.load('images/Coins.png')
        self.tablet = pygame.image.load('images/Tablet.png')
        # setting default positions to 0
        self.posi_x = 0
        self.posi_y = 0
        self.x = 0
        self.y = 0

    # generating random position
    def randpos(self):

        # making x position random between 1 and 13
        self.posi_x = random.randint(1, 13)
        # making y position random between 1 and 13
        self.posi_y = random.randint(1, 13)
        self.x = self.posi_y * sprite_size
        self.y = self.posi_x * sprite_size

    # checking the item doesn't land on a wall
    def nowall(self, level):

        self.level = level

        # if level tile in structure file labstruc is 'm' (a wall)
        if self.level.structure[self.posi_x][self.posi_y] == 'm':

            # generate a new position until it is not a wall
            while self.level.structure[self.posi_x][self.posi_y] == 'm':
                self.posi_x = random.randint(1, 13)
                self.x = self.posi_x * sprite_size
            else:
                return self.randpos()

    # adding items to the list
    def get_items(self, player):

        self.player = player

        #  checking if player's y position is equal to the item's position
        if self.y == player.y:
            #  if the player's x position is equal to the item's position
            if self.x == player.x:
                # add 1 to item_count
                constants.item_count += 1
                print("you have {} item(s)". format(constants.item_count))
                # remove item from the game / set off screen
                self.x = 320
                self.y = 320

