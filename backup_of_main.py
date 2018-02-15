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

# sets the width and height of the screen display / screen window
game_display = pygame.display.set_mode((display_width, display_height))
# sets the game window's left hand upper corner caption
pygame.display.set_caption('game ver. 1.00')
frames_per_second = 60


# defines the display surface:

# this commented code below this line is already assigned above somewhere.
# display_width = 800
# display_height = 600
height_width = display_width / 2
height_height = display_width = display_height / 2
display_area = display_width * display_height

small_font = pygame.font.SysFont(None, 25)
med_font = pygame.font.SysFont(None, 50)
large_font = pygame.font.SysFont(None, 80)



# this function code closes the game.

def events():
    for event in pygame.event.get():
    #if the event type is equal to QUIT command (which quits the game)
    #or is equal to the event types KEYDOWN and is equal to KEY_ESCPAPE, quit the game and exit sys.

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

def text_objects(text, color, size, textSurface):
    if size == 'small':
        textSurface = small_font.render(text, True, color)
    elif size == 'medium':
        textSurface = med_font.render(text, True, color)
    elif size == 'large':
        textSurface = large_font.redner(text, True, color)


    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    game_display.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            #if the event type is equal to QUIT command (which quits the game)
            #or is equal to the event types KEYDOWN and is equal to KEY_ESCPAPE, quit the game and exit sys.

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        game_display.fill(BLACK)

        message_to_screen = ("terraingame by Terapixel", GREEN, -100, "large")

        message_to_screen = ("Press 'c' to start or press 'q' to quit.", WHITE, -30)

        pygame.display.flip()
        timer.tick(frames_per_second)


# wait for video/game intro to start up
# pause()



# this is the main loop.

while True:

    timer.tick(frames_per_second)
    game_display.fill(BLUE)
    # while loop that falls on events,
    events()
    # updates the display as well.
    pygame.display.update()
    game_intro()
    
