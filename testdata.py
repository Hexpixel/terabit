"""
procedural terrain generation
scripted by: TheGreatRambler and Terapixel :D
"""

import math
import pygame
from opensimplex import OpenSimplex
import random
import time

WHITE = (255, 255, 255),
BLACK = (0, 0, 0),
RED = (255, 0, 0),
GREEN = (63, 163, 47),
BLUE = (131, 177, 255)

# expand this value to make terrain less "pointy"
frequency = 20

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# block dimensions
BLOCK_WIDTH = 5
BLOCK_HEIGHT = 5

# initializes the game
pygame.init()

#sets a game clock
timer = pygame.time.Clock()
display_width = 800
display_height = 600

# sets the width and height of the screen display / screen window
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# sets the game window's left hand upper corner caption
pygame.display.set_caption('terabit pre-alpha')
frames_per_second = 60

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

def main():
    print("Hello")
    pygame.init()
    game_display.fill(BLUE)
    for f in range(math.floor(gettopcorner()[0]), math.floor(gettopcorner()[0]) * -1):
        terrainforelement = terrainnoise.noise2d(x = f / frequency, y = 0)
        for g in range(0, math.floor((terrainforelement + 1) * 10)):
            drawsquare(-f, -g + 59, GREEN)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

if __name__ == "__main__":
    main()
