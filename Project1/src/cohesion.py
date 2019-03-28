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
pygame.display.set_caption('Cohesion')
clock = pygame.time.Clock()
run = True
game = Game(levels[str(LEVEL)], str(LEVEL))

def quitgame() :
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def game_intro():
    global LEVEL
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(BLACK)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("COHESION", largeText)
        TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/3))
        screen.blit(TextSurf, TextRect)

        button("Player",120,350,100,50,DARK_GREEN,BRIGHT_GREEN,player_game_loop)
        button("Computer",380,350,100,50,DARK_GREEN,BRIGHT_GREEN,computer_game_loop)
        button("Exit",250,450,100,50,DARK_RED,BRIGHT_RED,quitgame)

        pygame.display.update()
        clock.tick(15)

def player_game_loop() :
    global LEVEL
    global run
    global game
    block = None
    
    screen.fill(BLACK)

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
                game = Game(levels[str(LEVEL)], str(LEVEL))
                
        # limit to 60 frames per second
        clock.tick(60)

        pygame.display.flip()

def computer_game_loop():
    global LEVEL
    global run
    global game
    global block

    game.init_computer_game()
    
    screen.fill(BLACK)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Computer Move Function Call
        game.computer_move()

        for i in range(len(game.board)):
            for j in range(len(game.board[0])):
                color = colors[game.board[i][j]]
                # #highlight
                # if block and [i,j] in block.coords:
                #     (r,g,b) = color
                #     color = (r*0.5, g*0.5, b*0.5)

                pygame.draw.rect(screen, color, \
                [(MARGIN + WIDTH) * j + MARGIN, \
                (MARGIN + HEIGHT) * i + MARGIN, \
                WIDTH, HEIGHT])

        if game.finished:
            LEVEL += 1
            if(LEVEL > len(levels)):
                run = False
            else:
                game = Game(levels[str(LEVEL)], str(LEVEL))
                
        # limit to 60 frames per second
        clock.tick(60)

        pygame.display.flip()

game_intro()
pygame.quit()
quit()