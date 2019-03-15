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

def handleRight(grid, x, y):
    grid[x][y + 1] = grid[x][y]
    grid[x][y] = 0
    return grid

def handleUp(grid, x, y):
    grid[x-1][y] = grid[x][y]
    grid[x][y] = 0
    return grid

def handleLeft(grid, x, y):
    grid[x][y-1] = grid[x][y]
    grid[x][y] = 0
    return grid

def handleDown(grid, x, y):
    grid[x+1][y] = grid[x][y]
    grid[x][y] = 0
    return grid

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cohesion')

run = True
clock = pygame.time.Clock()

currentSelected = []
matrix[0][0] = 1
matrix[2][2] = 2

#Main Loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #click mouse and get position
            pos = pygame.mouse.get_pos()
            currentSelected.clear()
            currentSelected.append(pos[1] // (WIDTH + MARGIN))
            currentSelected.append(pos[0] // (WIDTH + MARGIN))

    keys = pygame.key.get_pressed()

    if len(currentSelected) == 2:

        if keys[pygame.K_RIGHT]:
            matrix = handleRight(matrix, currentSelected[0], currentSelected[1])
            currentSelected = []
        elif keys[pygame.K_UP]:
            matrix = handleUp(matrix, currentSelected[0], currentSelected[1])
            currentSelected = []
        elif keys[pygame.K_LEFT]:
            matrix = handleLeft(matrix, currentSelected[0], currentSelected[1])
            currentSelected = []
        elif keys[pygame.K_DOWN]:
            matrix = handleDown(matrix, currentSelected[0], currentSelected[1])
            currentSelected = []

    for row in range(4):
        for column in range(4):
            color = WHITE
            if matrix[row][column] == 1:
                color = GREEN
            elif matrix[row][column] == 2:
                color = RED
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    
    #limit to 60 frames per second
    clock.tick(60)

    pygame.display.flip()