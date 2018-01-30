"""
procedural terrain generation for platformer by Terapixel
additional credits: TheGreatRambler
"""

import pygame
import pyglet
import math
import noise

# Do this --> pip install OpenSimplex

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

    terrainnoise = OpenSimplex(seed=random.random())

    terrain_array = []

    """ for loop for procedural terrain generation. """
    for xval in range(0, platformer_main.SCREEN_WIDTH):
        height = math.floor((platformer_main.SCREEN_HEIGHT / 2) * (terrainnoise.noise2d(x=xval, y=0) + 1))
        element = [1, height, xval, platformer_main.SCREEN_HEIGHT - height]
        terrain_array.append(element)

    return terrain_array

# call this in platformer_main.py
# return_terrain()
