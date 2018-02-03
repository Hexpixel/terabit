"""
terabit game ver. 0.0.6a

>>MIT License

includes:

procedural terrain generation
scripted by: TheGreatRambler and Terapixel :D
"""

# imports

import pygame
import sys
import math
from opensimplex import OpenSimplex
import random



# defines some colors

WHITE = (255, 255, 255),
BLACK = (0, 0, 0),
RED = (255, 0, 0),
GREEN = (63, 163, 47),
BLUE = (131, 177, 255)

# this command initializes the game
pygame.init()

# expand this value to make terrain less 'pointy'
frequency = 20

# Screen dimensions settings

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# height width and height height

HEIGHT_WIDTH = SCREEN_WIDTH / 2
HEIGHT_HEIGHT = SCREEN_HEIGHT / 2

# area

AREA = SCREEN_WIDTH * SCREEN_HEIGHT

""" code to make the game run on your current machine's screen size """

# Make fullscreen
#infoObject = pygame.display.Info()

#SCREEN_WIDTH = infoObject.current_w
#SCREEN_HEIGHT = infoObject.current_h

# terrain block dimensions

BLOCK_WIDTH = 5
BLOCK_HEIGHT = 5

# this command sets a game clock

timer = pygame.time.Clock()


# sets the width and height of the screen display / screen window

game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# sets the game window's left hand upper corner caption

pygame.display.set_caption('terabit ver. 0.0.6')

# frames per second - increase this value to have smoother game play... note to TheGreatRambler: wouldn't advise this for Windows Vista users kek :P

frames_per_second = 120

# player x and y

playerx = 0
playery = 0

# empty array
gamemap = []

terrainnoise = OpenSimplex(seed=random.randint(0, 100000))

def returnarrayindex(xvalue, yvalue):
    x = xvalue * 2 if xvalue >= 0 else xvalue * -2 - 1
    y = yvalue * 2 if yvalue >= 0 else yvalue * -2 - 1
    number = (x * x + x + y) if (x >= y) else (y * y + x)
    return number

def gettopcorner():
    return [playerx - (SCREEN_WIDTH / 2) / BLOCK_WIDTH, playery - (SCREEN_HEIGHT / 2) / BLOCK_HEIGHT]

def drawsquare(x, y, texture):
    topcornerdata = gettopcorner()
    dataforsquare = ((x - topcornerdata[0]) * BLOCK_WIDTH, (y - topcornerdata[1]) * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
    width = 0
    pygame.draw.rect(game_display, texture, dataforsquare, width)

def draw():
    pygame.display.update()
    timer.tick(frames_per_second)


# main function
def main():
    print("Hello!")
    print("Do you like code easter eggs?  Cause' I sure do...")
    print("This is a nice little code easter egg for people who manage to steal this code from me.  By the way, you are now going to die ;)")
    game_display.fill(BLUE)
    for f in range(math.floor(gettopcorner()[0]), math.floor(gettopcorner()[0]) * -1):
        terrainforelement = terrainnoise.noise2d(x = f / frequency, y = 0)
        for g in range(0, math.floor((terrainforelement + 1) * 10)):
            drawsquare(-f, -g + 58, GREEN)


# while loop must go inside main() function.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()

            pygame.display.update()


if __name__ == "__main__":
    main()
