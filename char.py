"""
this is the character class.
sprites are not included in this script.
"""

# imports
import pygame
import main
import testdata

WHITE = (255, 255, 255),
BLACK = (0, 0, 0),
RED = (255, 0, 0),
GREEN = (63, 163, 47),
BLUE = (131, 177, 255)

class Block(pygame.sprite.Sprite):
    def __init__(self, sprite_color=WHITE, width=64, height=64):
        super(Block, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

class Char():
    # two parameters we need are MaxJumpRange and velocity.
    def __init__(self, velocity, MaxJumpRange):
        # velocity is a positive velocity which defines the number of pixels that can move left or right or up or down.
        # ex. if you press the left key you will move 3 pixels to the left and if you press the right key you will move 3 pixels to the right.
        self.velocity = velocity
        # ex. if maximum jump range is 10 pixels and velocity is 3 pixels, you will jump 30 pixels upwards from the ground.
        self.MaxJumpRange = MaxJumpRange

    # sets the coordinates for the x and y's amd initializes some of the other variables in this class.
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        # what self.xVelocity does is if we press the right key,
        self.xVelocity = 0
        self.jumping = False
        # keeps track of our progress while we're jumping.
        self.jumpCounter = 0
        self.falling = True

    def keys(self):
        # REMEMBER: this is a local variable to this function and this class. DOES NOT affect its twin variable.
        key_arrow_pressed = pygame.key.get_pressed()
        # this makes the player look like its moving left
        if key_arrow_pressed[pygame.K_LEFT]:
            self.xVelocity = -self.velocity
        elif key_arrow_pressed[pygame.K_RIGHT]:
            self.xVelocity = self.velocity
        else:
            self.xVelocity = 0

        # checks if the values up above are True
        if key_arrow_pressed[pygame.K_UP] and not self.falling:
            self.jumping = True
            self.jumpCounter = 0

    def move(self):
        # checks the x boundaries
        self.x += self.xVelocity

        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            if self.jumpCounter == self.MaxJumpRange:
                self.jumping = False
                self.falling = True
            elif self.falling:
                if self.y <= H - 10 and self.y + self.velocity >= H - 10:
                    self.y = H - 10
                    self.falling = False
                else:
                    self.y += self.velocity

    def draw(self):
        display = pygame.display.get_surface()
        pygame.draw.circle(display, main.WHITE, (self.x, self.y - 25), 25, 0)

    def do(self):
        self.keys()
        self.move()
        self.draw()


P = Char(3, 50)
P.setLocation(testdata.SCREEN_WIDTH, 0)

# main loop

while True:
    P.do()
    
