"""
Cohesion.py
Basic structure for game cohesion(can be found in the play store)

"""
import pygame
import copy

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

def takeY(elem):
	return elem[1]

def takeX(elem):
	return elem[0]

def handleRight(grid, x, y):
	color = grid[x][y]
	blocks[str(color)].sort(key = takeY ,reverse=True)
	if possibleMove(grid, x, y, 'up'):
		for cell in blocks[str(color)]:
			grid = moveRightCell(grid , cell[0], cell[1])
			cell[1] += 1
	return grid

def moveRightCell(grid, x, y):
	if grid[x][y+1] == 0 or grid[x][y+1] == grid[x][y]:
		grid[x][y+1] = grid[x][y]
		grid[x][y] = 0
	return grid

def handleUp(grid, x, y):
	color = grid[x][y]
	blocks[str(color)].sort(key = takeX)
	if possibleMove(grid, x, y, 'up'):
		for cell in blocks[str(color)]:
			grid = moveUpCell(grid , cell[0], cell[1])
			cell[0] -= 1
	return grid

def moveUpCell(grid, x, y):
	if grid[x-1][y] == 0:
		grid[x-1][y] = grid[x][y]
		grid[x][y] = 0
	return grid


def handleLeft(grid, x, y):
    color = grid[x][y]
    blocks[str(color)].sort(key = takeY)
    if possibleMove(grid, x, y, 'left'):
    	for cell in blocks[str(color)]:
    		grid = moveLeftCell(grid , cell[0], cell[1])
    		cell[1] -= 1
    return grid

def moveLeftCell(grid, x, y):
	if grid[x][y-1] == 0:
		grid[x][y-1] = grid[x][y]
		grid[x][y] = 0
	return grid

def handleDown(grid, x, y):
	color = grid[x][y]
	blocks[str(color)].sort(key = takeX, reverse=True)
	if possibleMove(grid, x, y, 'down'):
		for cell in blocks[str(color)]:
			grid = moveDownCell(grid , cell[0], cell[1])
			cell[0] += 1
	return grid

    

def moveDownCell(grid, x, y):
	if grid[x+1][y] == 0 or grid[x+1][y] == grid[x][y]:
		grid[x+1][y] = grid[x][y]
		grid[x][y] = 0
	return grid

def possibleMove(grid, x, y, move):
	color = grid[x][y]

	if move == 'down':
		for cell in blocks[str(color)]:
			if grid[cell[0] + 1][cell[1]] != 0 and grid[cell[0] +1][cell[1]] != grid[cell[0]][cell[1]]:
				return False
	elif move == 'up':
		for cell in blocks[str(color)]:
			if grid[cell[0] - 1][cell[1]] != 0 and grid[cell[0] - 1][cell[1]] != grid[cell[0]][cell[1]]:
				return False
	elif move == 'right':
		for cell in blocks[str(color)]:
			if grid[cell[0]][cell[1] + 1] != 0 and grid[cell[0]][cell[1] + 1] != grid[cell[0]][cell[1]]:
				return False
	elif move == 'left':
		for cell in blocks[str(color)]:
			if grid[cell[0]][cell[1] - 1] != 0 and grid[cell[0]][cell[1] - 1] != grid[cell[0]][cell[1]]:
				return False
	return True



pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cohesion IART')

run = True
clock = pygame.time.Clock()

currentSelected = []
blocks = {}

#block for green
blocks["1"] = [[0,0],[0,1]]

#block for red
blocks["2"] = [[2,1]]

def fillMatrix(blocks):
	for colorBlock in blocks:
		for i in range(len(blocks[colorBlock])):
			matrix[blocks[colorBlock][i][0]][blocks[colorBlock][i][1]] = int(colorBlock)


fillMatrix(blocks)
print(matrix)

# Give some cells colors just for testing
# matrix[0][0] = 1
# matrix[2][1] = 1

# Main Loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # click mouse and get position
            pos = pygame.mouse.get_pos()
            currentSelected.clear()
            currentSelected.append(pos[1] // (WIDTH + MARGIN))
            currentSelected.append(pos[0] // (WIDTH + MARGIN))

    keys = pygame.key.get_pressed()

    if len(currentSelected) == 2:

        if keys[pygame.K_RIGHT]:
            if currentSelected[1]+1 < 4:
                matrix = handleRight(matrix, currentSelected[0], currentSelected[1])
                print(blocks)
            currentSelected = []
        elif keys[pygame.K_UP]:
            if currentSelected[0]-1 > -1:
                matrix = handleUp(matrix, currentSelected[0], currentSelected[1])
            currentSelected = []
        elif keys[pygame.K_LEFT]:
            if currentSelected[1]-1 > -1:
                matrix = handleLeft(matrix, currentSelected[0], currentSelected[1])
            currentSelected = []
        elif keys[pygame.K_DOWN]:
            if currentSelected[0]+1 < 4:
                matrix = handleDown(matrix, currentSelected[0], currentSelected[1])
                print(blocks)
            currentSelected = []

    for row in range(4):
        for column in range(4):
            color = WHITE
            if matrix[row][column] == 1:
                color = GREEN
            elif matrix[row][column] == 2:
                color = RED
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    
    # limit to 60 frames per second
    clock.tick(60)

    pygame.display.flip()