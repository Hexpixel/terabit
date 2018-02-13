"""

terabit v0.0.2

includes:
>>MIT License

description:
A two-dimensional terrain and sandbox based game written by Terapixel (Hexpixel) and TheGreatRambler.

"""

# imports

import pygame
import pymunk
import math
from opensimplex import OpenSimplex
import random

# stores some colors in different variables allowing easier access to colors.

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
# infoObject = pygame.display.Info()

# SCREEN_WIDTH = infoObject.current_w
# SCREEN_HEIGHT = infoObject.current_h

# terrain block dimensions

BLOCK_WIDTH = 5
BLOCK_HEIGHT = 5

# this command sets a game clock

timer = pygame.time.Clock()

# sets the width and height of the screen display / screen window

game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# sets the game window's left hand upper corner caption

pygame.display.set_caption('terabit v0.0.2')

# frames per second - increase this value to have smoother game play... note to TheGreatRambler: wouldn't advise this for Windows Vista users kek :P

frames_per_second = 500

# player x and y

playerx = 0
playery = 0

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
    dataforsquare = (
    (x - topcornerdata[0]) * BLOCK_WIDTH, (y - topcornerdata[1]) * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
    width = 0
    pygame.draw.rect(game_display, texture, dataforsquare, width)


def draw():
    pygame.display.flip()
    timer.tick(frames_per_second)
    game_display.fill(BLUE)



# add a collision handler

#def add_collision_handler(collision_type_a, collision_type_b):

# detects if there is a collision

#def detectCollisions():


class player(pygame.sprite.Sprite):
    def __init__(self, velocity, maxJumpRange):
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange

    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        # Stores if player is jumping or not.
        self.jumpCounter = 0
        # Allows the player to fall.
        self.falling = True
        self.onGround = False



    # player controls:

    def do_quit(self):
        qk = pygame.key.get_pressed()
        if qk[pygame.K_q]:
            pygame.quit()
            quit()

    def go_up(self):
        uk = pygame.key.get_pressed()
        if uk[pygame.K_SPACE]:
            self.jumping = True
            self.jumpCounter = 0

    def go_down(self):
        dk = pygame.key.get_pressed()
        self.y = 0
        if dk[pygame.K_s]:
            self.y += 10

    def go_right(self):
        rk = pygame.key.get_pressed()
        if rk[pygame.K_d]:
            self.xVelocity = self.velocity

    def go_left(self):
        lk = pygame.key.get_pressed()
        if lk[pygame.K_a]:
            self.xVelocity = -self.velocity

    #def stop_moving(self):
        # Called when the user lets off the keyboard.
        #self.change_x = 0
        #self.change_y = 0

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

    def draw(self):
        self.size = (50, 50)
        rect = pygame.Rect((self.x, self.y), self.size)
        pygame.draw.rect(game_display, WHITE, rect)

    def do(self):
        self.go_up()
        self.go_right()
        self.go_left()
        self.move()
        self.draw()


P = player(3, 50)
P.setLocation(HEIGHT_WIDTH, 0)



def main():
    """ Main Program """

    done = False
    while not done:

        pygame.display.flip()
        timer.tick(frames_per_second)
        game_display.fill(BLUE)

        for f in range(math.floor(gettopcorner()[0]), math.floor(gettopcorner()[0]) * -1):
            terrainforelement = terrainnoise.noise2d(x=f / frequency, y=0)
            for g in range(0, math.floor((terrainforelement + 1) * 10)):
                drawsquare(-f, -g + 58, GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    P.do_quit()
                if event.key == pygame.K_SPACE:
                    P.go_up()
                if event.key == pygame.K_s:
                    P.go_down()
                if event.key == pygame.K_d:
                    P.go_right()
                if event.key == pygame.K_a:
                    P.go_left()

            #if event.type == pygame.KEYUP:
                #if event.key == pygame.K_a:
                    #P.stop_moving()
                #if event.key == pygame.K_d:
                    #P.stop_moving()

        pygame.display.flip()
        timer.tick(frames_per_second)
        P.do()


if __name__ == "__main__":
    main()
    
