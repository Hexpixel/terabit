"""
game ver. 0.0.6a

procedural terrain generation
scripted by: TheGreatRambler and Terapixel :D
"""

#imports

import math
import pygame
from opensimplex import OpenSimplex
import random
import char

WHITE = (255, 255, 255),
BLACK = (0, 0, 0),
RED = (255, 0, 0),
GREEN = (63, 163, 47),
BLUE = (131, 177, 255)

# initializes the game
pygame.init()

# expand this value to make terrain less "pointy"
frequency = 20

# Screen dimensions settings

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



HEIGHT_WIDTH, HEIGHT_HEIGHT = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
AREA = SCREEN_WIDTH * SCREEN_HEIGHT

# Make fullscreen
#infoObject = pygame.display.Info()

#SCREEN_WIDTH = infoObject.current_w
#SCREEN_HEIGHT = infoObject.current_h

# block dimensions
BLOCK_WIDTH = 5
BLOCK_HEIGHT = 5

#sets a game clock
timer = pygame.time.Clock()


# sets the width and height of the screen display / screen window
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# sets the game window's left hand upper corner caption
pygame.display.set_caption('terabit ver. 0.0.6a')
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


class player:
    def __init__(self, velocity, maxJumpRange):
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange
        pygame.display.update()

    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        self.jumpCounter = 0
        self.falling = True
        pygame.display.update()

    def keys(self):
        k = pygame.key.get_pressed()

        if k[pygame.K_LEFT]:
            self.xVelocity = -self.velocity
        elif k[pygame.K_RIGHT]:
            self.xVelocity = self.velocity
        else:
            self.xVelocity = 0

        if k[pygame.K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0
        pygame.display.update()

    def move(self):
        self.x += self.xVelocity
        # check x boundries

        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:
            if self.y <= SCREEN_HEIGHT - 10 and self.y + self.velocity >= SCREEN_HEIGHT - 10:
                self.y = SCREEN_HEIGHT - 10
                self.falling = False
            else:
                self.y += self.velocity
        pygame.display.update()

    def draw(self):
        image = pygame.image.load('friendly creature.png')
        
        width = 0
        
        pygame.get_rect()
        pygame.draw.rect(self, game_display, WHITE, width)
        
        timer.tick(frames_per_second)
        pygame.display.update()
    
    def do(self):
        self.keys()
        self.move()
        self.draw()
        pygame.display.update()

P = player(3, 50)
P.setLocation(HEIGHT_WIDTH, 0)


def main():
    print("Hello")
    game_display.fill(BLUE)
    for f in range(math.floor(gettopcorner()[0]), math.floor(gettopcorner()[0]) * -1):
        terrainforelement = terrainnoise.noise2d(x = f / frequency, y = 0)
        for g in range(0, math.floor((terrainforelement + 1) * 10)):
            drawsquare(-f, -g + 58, GREEN)
    pygame.display.update()

    
    
# main loop
    running = True
    while running:
        timer.tick(frames_per_second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                quit()
                
           P.do()
        
    screen.fill(BLUE)
    screen.blit((131, 177, 255))
    playersprites.clear(game_display)
    playersprites.update()
    playersprites.draw(game_display)
    pygame.display.update()

if __name__ == "__main__":
    main()
    
