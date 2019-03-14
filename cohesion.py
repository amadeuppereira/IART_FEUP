"""
Cohesion.py
Basic structure for game cohesion(can be found in the play store)

"""
import pygame

"""
class Cohesion:


	#FIELD DIMENSIONS
	ROWS = 4
	COLUMNS = 4

	DIRECTIONS = {
		"UP": (0, 1),
		"RIGHT": (1, 0),
		"LEFT": (-1, 0),
		"DOWN": (0, -1),
	}

"""

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Cell dimensions
WIDTH = 100
HEIGHT = 100

#Margin between cells
MARGIN = 40

matrix = []
for row in range(4):
	matrix.append([])
	for column in range(4):
		matrix[row].append(0)

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cohesion')

run = True
clock = pygame.time.Clock()

#Main Loop
while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for row in range(4):
		for column in range(4):
			color = WHITE
			pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    #limit to 60 frames per second
	clock.tick(60)

	pygame.display.flip()