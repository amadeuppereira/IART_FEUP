import pygame
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GREEN = pygame.Color(  0, 100,   0, 255)
DARK_RED = pygame.Color(139,   0,   0, 255)
BRIGHT_GREEN = pygame.Color(144, 238, 144, 255)
BRIGHT_RED = pygame.Color(250, 128, 114, 255)

colors = {
    0: WHITE,
    1: RED,
    2: GREEN,
    3: BLUE,
    4: YELLOW
}

# Margin between cells
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
MARGIN = 5

# Cell dimensions
NUMBER_OF_CELLS = 4
WIDTH = (DISPLAY_WIDTH - MARGIN * (NUMBER_OF_CELLS+1)) / NUMBER_OF_CELLS
HEIGHT = (DISPLAY_HEIGHT - MARGIN * (NUMBER_OF_CELLS+1)) / NUMBER_OF_CELLS

# COHESION
GAMEMODE = "easy"
LEVEL = 1