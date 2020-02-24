"""Classes for the MacGyver game"""

# coding utf-8
# import needed modules
import pygame
import random
from pygame.locals import *
from constants import *

item_count = 0


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
        # making the variable item_count global
        global item_count
        # checking if the players x position is equal to the villain's
        if self.x == player.x:
            # checking if the players y position is equal to the villain's
            if self.y == player.y:
                # checking if the player has collected all the items
                if item_count < 4:
                    # if not the player will not pass
                    player.y -= 20
                    print('You shall not pass me ! You sorry SOB !')

                # if the player has all the items
                else:
                    # remove the villain from the game, set him off screen
                    self.x = 320
                    print('Aaah so much craftiness, how could he !?')
                    player.x += 20


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

    # listing the items
    def listitems(self, items=None):

        if item is None:
            # creating an empty list
            self.items = []
        else: self.items = items

    # adding items to the list
    def Getitems(self, player):

        self.player = player
        # using the item_count variable as global
        global item_count

        #  checking if player's y position is equal to the item's position
        if self.y == player.y:
            #  if the player's x position is equal to the item's position
            if self.x == player.x:
                # add 1 to item_count
                item_count += 1
                print("you have {} item(s)". format(item_count))

                # remove item from the game / set off screen
                self.x = 320
                self.y = 320
