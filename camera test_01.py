import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

def text(font, string, x, y, xJustify = None, yJustify = None, surface = None):
	global WHITE, BLACK
	if not surface: surface = pygame.display.get_surface()
	textSurface = font.render(string, 1, WHITE, BLACK)
	textRect = textSurface.get_rect()
	if xJustify == 1:
		x -= textRect.width
	elif xJustify == 2:
		x -= textRect.center[0]
	if yJustify == 1:
		y -= textRect.height
	elif yJustify == 2:
		y -= textRect.center[1]
	surface.blit(textSurface, (x, y))		
	
# define display surface			
screen_width, screen_height = 800, 600
height_width, height_height = screen_width / 2, screen_height / 2
area = screen_width * screen_height

# initialise display
pygame.init()
timer = pygame.time.Clock()
game_display = pygame.display.set_mode((W, H))
pygame.display.set_caption("Scrolling background test 01")
frames_per_second = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE  = (0, 0, 255, 255)

circleRadius = 25

stageX = 50
stageY = HH - 200
stageHeight = 400
stageWidth = W - 100

dw = 712
dhw = dw / 2

# main loop
while True:
	events()

	mx, my = pygame.mouse.get_pos()
	
	if mx < stageX + circleRadius: mx = stageX + circleRadius
	if mx > stageX + stageWidth - circleRadius: mx = stageX + stageWidth - circleRadius
	
	if mx < stageX + dhw: dx = stageX + dhw
	elif mx > stageX + stageWidth - dhw: dx = stageX + stageWidth - dhw
	else:
		dx = mx
	
	pygame.draw.rect(game_display, WHITE, (stageX, stageY, stageWidth, stageHeight), 2)
	pygame.draw.rect(game_display, BLUE, (dx - dhw, stageY, dw, stageHeight), 2)
	pygame.draw.circle(game_display, WHITE, (mx, HH + 100), circleRadius, 0)
	
	pygame.display.update()
	timer.tick(frames_per_second)
	game_display.fill(BLUE)
