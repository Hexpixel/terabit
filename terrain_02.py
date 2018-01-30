"""
procedural terrain generation for platformer by Terapixel
additional credits: TheGreatRambler
"""

import pygame
import pyglet
import random
import platformer_main

# constants representing the different resources:
GRASS = 0
DIRT = 1
STONE = 2

# constants representing colors:

cobalt_green = (61,145,64)
chocolate = (139,69,19)
gray34 = (87,87,87)

# dictionary for linking colours to their appropriate resources:

colors = {
            GRASS : cobalt_green,
            DIRT : chocolate,
            STONE : gray34,

         }

# list representing tile map:
tile_map = [
             [GRASS, DIRT, STONE]
           ]



def return_terrain():
    # make an empty array:
    terrain_array = []

    """ for loop for procedural terrain generation. """
    for random_platform in range(0, 10):
        # Put random platforms in game - first two values is the width and height (I think?).
        elementtoconsider = [200, 5, random.randrange(0, platformer_main.SCREEN_WIDTH), random.randrange(0, platformer_main.SCREEN_HEIGHT)]

        addtoarray = True
        # makes sure the terrain doesn't collide with other terrain.
        for lengthindex in range(0, len(terrain_array)):
            item = terrain_array[lengthindex]
            if item[2] < elementtoconsider[2] and item[2] + item[0] > elementtoconsider[2] + elementtoconsider[0] and item[3] < elementtoconsider[3] and item[3] + item[1] > elementtoconsider[3] + elementtoconsider[1]:
                    addtoarray = False
            if addtoarray:
                terrain_array.append(elementtoconsider)

        return terrain_array

# call this in platformer_main.py
# return_terrain()
