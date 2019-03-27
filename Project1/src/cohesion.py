"""
Cohesion.py
Basic structure for game cohesion(can be found in the play store)
"""
import pygame
import json
from game import Game
from settings import *

levels = []

with open('levels.json') as json_file:  
    levels = json.load(json_file)[GAMEMODE]

pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Cohesion IART')

run = True
clock = pygame.time.Clock()

game = Game(levels[str(LEVEL)])

block = None

# Main Loop
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # click mouse and get position
            [x,y] = pygame.mouse.get_pos()    
            block = game.get_block(y // (HEIGHT + MARGIN), x // (WIDTH + MARGIN))

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

    
    for i in range(len(game.board)):
        for j in range(len(game.board[0])):
            color = colors[game.board[i][j]]
            #highlight
            if block and [i,j] in block.coords:
                (r,g,b) = color
                color = (r*0.5, g*0.5, b*0.5)

            pygame.draw.rect(screen, color, \
            [(MARGIN + WIDTH) * j + MARGIN, \
             (MARGIN + HEIGHT) * i + MARGIN, \
             WIDTH, HEIGHT])

    if game.finished:
        LEVEL += 1
        if(LEVEL > len(levels)):
            run = False
        else:
            game = Game(levels[str(LEVEL)])
            
    # limit to 60 frames per second
    clock.tick(60)

    pygame.display.flip()