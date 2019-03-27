"""
Cohesion.py
Basic structure for game cohesion(can be found in the play store)
"""
import pygame
from game import Game

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

colors = {
    0: WHITE,
    1: RED,
    2: GREEN,
    3: BLUE,
    4: YELLOW
}


#Cell dimensions
WIDTH = 138
HEIGHT = 138

#Margin between cells
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
MARGIN = 10

pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Cohesion IART')

run = True
clock = pygame.time.Clock()

game = Game([[0,0,0,0],
             [0,1,0,1],
             [2,2,1,2],
             [3,3,3,3]])

block = None

# Main Loop
while run:
    run = not game.finished

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # click mouse and get position
            [x,y] = pygame.mouse.get_pos()
            block = game.get_block(y // (WIDTH + MARGIN), x // (WIDTH + MARGIN))

    keys = pygame.key.get_pressed()

    if block:

        if keys[pygame.K_UP]:
            if game.move(block, "up"):
                block = None
        elif keys[pygame.K_DOWN]:
            if game.move(block, "down"):
                block = None
        elif keys[pygame.K_LEFT]:
            if game.move(block, "left"):
                block = None
        elif keys[pygame.K_RIGHT]:
            if game.move(block, "right"):
                block = None

    for row in range(4):
        for column in range(4):
            color = colors[game.board[row][column]]
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    
    # limit to 60 frames per second
    clock.tick(60)

    pygame.display.flip()