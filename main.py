import pygame
import sys
from pygame.locals import *
import char



# Global constants

# defines some colors from color library

WHITE = (255, 255, 255),
BLACK = (0, 0, 0),
RED = (255, 0, 0),
GREEN = (0, 255, 0),
BLUE = (28, 134, 238)

# initializes the game
pygame.init()

#sets a game clock
timer = pygame.time.Clock()
display_width = 800
display_height = 600

# sets the witdth and height of the screen display / screen window
game_display = pygame.display.set_mode((display_width, display_height))
# sets the game window's left hand upper corner caption
pygame.display.set_caption('ver. 1.00')
frames_per_second = 500


# defines the display surface:

# this commented code below this line is already assigned above somewhere.
# display_width = 800
# display_height = 600
height_width = display_width / 2
height_height = display_width = display_height / 2
display_area = display_width * display_height



# this function code closes the game.

def events():
    for event in pygame.event.get():
        """ if the event type is equal to QUIT command (which quits the game)
        or is equal to the event types KEYDOWN and is equal to KEY_ESCPAPE, quit the game and exit sys. """

        if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
            pygame.quit()
            sys.exit()

# this function code pauses the game before it starts and waits for user input
# / waits for the user to hit a certain key on the keyboard.

def pause():
    while True:
        events()
        key_arrow_pressed = pygame.key.get_pressed()
        # this breaks the pause function allowing the game to start as long as the 'ENTER' key is pressed.
        if key_arrow_pressed[K_ESCAPE]:
            break

# wait for video/game intro to start up
pause()



# this is the main loop.
while True:
    # while loop that falls on events,
    events()

    # updates the display as well.
    pygame.display.update()
    timer.tick(frames_per_second)
    game_display.fill(BLACK)
