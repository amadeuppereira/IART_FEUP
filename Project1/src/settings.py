colors = {
    0: ["white", "white"],
    1: ["red", "darkRed"],
    2: ["green2", "darkGreen"],
    3: ["blue", "darkBlue"],
    4: ["yellow", "orange"]
}

# Margin between cells
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

FPS = 10

# Side menu
SIDE_MENU_WIDTH = 200

# Cell dimensions
NUMBER_OF_CELLS = 4
MARGIN = 5
CELL_WIDTH = (DISPLAY_WIDTH - SIDE_MENU_WIDTH - MARGIN * (NUMBER_OF_CELLS+1)) / NUMBER_OF_CELLS
CELL_HEIGHT = (DISPLAY_HEIGHT - MARGIN * (NUMBER_OF_CELLS+1)) / NUMBER_OF_CELLS

# COHESION
GAMEMODE = "easy"
LEVEL = 1
HEURISTIC = "heuristic_1"

HINT_ALG = "a*"
HINT_HEURISTIC = "heuristic_1"