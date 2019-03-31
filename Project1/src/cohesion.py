"""
Cohesion.py
Basic structure for game cohesion(can be found in the play store)
"""

import tkinter as tk
import json
from game import Game
from settings import *
from logic import get_computer_path
from copy import deepcopy
import time

levels = []
with open('levels.json') as json_file:  
    levels = json.load(json_file)[GAMEMODE]

run = False
block = None
game = Game(deepcopy(levels[str(LEVEL)]), LEVEL)

root = tk.Tk()
root.geometry(str(DISPLAY_WIDTH) + "x" + str(DISPLAY_HEIGHT))
root.title("COHESION")
root.resizable(0,0)



def handle_click(event): 
    global run
    global block 
    if not run: return
    block = game.get_block(
        event.y // (CELL_HEIGHT + MARGIN),
        event.x // (CELL_WIDTH + MARGIN))
    display_game()

def handle_key_press(event): 
    global run
    global block
    global LEVEL
    global run
    global game
    global next_level

    if not run: return

    if block:
        if event.keysym == "Up":
            if game.move(block, "up"):
                block = None
        elif event.keysym == "Down":
            if game.move(block, "down"):
                block = None
        elif event.keysym == "Left":
            if game.move(block, "left"):
                block = None
        elif event.keysym == "Right":
            if game.move(block, "right"):
                block = None

    display_game()

    if game.finished:
        next_level.config(state="normal")

def display_game():
    canvas.delete(tk.ALL)
    for i in range(len(game.board)):
        for j in range(len(game.board[0])):
            color = colors[game.board[i][j]][0]
            #highlight
            if block and [i,j] in block.coords:
                color = colors[game.board[i][j]][1]

            canvas.create_rectangle(
                (MARGIN + CELL_WIDTH) * j + MARGIN,
                (MARGIN + CELL_HEIGHT) * i + MARGIN,
                (MARGIN + CELL_WIDTH) * j + MARGIN + CELL_WIDTH,
                (MARGIN + CELL_HEIGHT) * i + MARGIN + CELL_HEIGHT,
                fill=color)

canvas = tk.Canvas(root, 
    width=DISPLAY_WIDTH-SIDE_MENU_WIDTH,
    height=DISPLAY_HEIGHT,
    highlightthickness=0,
    bg="black",)
canvas.bind("<Button-1>", handle_click)
canvas.bind("<Key>", handle_key_press)
canvas.pack(side=tk.RIGHT)
display_game()


level_text = tk.StringVar()
level_text.set('LEVEL')
level_label = tk.Label(root,
    textvariable=level_text,
    pady=10,
    wraplength=SIDE_MENU_WIDTH,
    font=("Helvetica", 20))
level_label.pack()
level_label.place(relx=0.02)


levels_box = tk.Spinbox(root, from_=0, to = len(levels))
levels_box.pack()
levels_box.place(height = 25, width = 50, rely = 0.034, relx = 0.15)



difficulty_text = tk.StringVar()
difficulty_text.set("EASY")
difficulty_label = tk.Label(root,
    textvariable=difficulty_text,
    wraplength=SIDE_MENU_WIDTH,
    font=("Helvetica", 12))
difficulty_label.pack()
difficulty_label.place(relx = 0.13, rely = 0.1, width = 80, height = 40)

var = tk.StringVar()
def select_mode():
    select = var.get()
    global difficulty_text
    difficulty_text.set(select.upper())

easy_mode = tk.Radiobutton(root, text="EASY", variable=var, value="easy" , indicatoron = 0, command = select_mode)
easy_mode.pack(anchor = "w")
easy_mode.place(rely = 0.09, width = 56)

medium_mode = tk.Radiobutton(root, text="MEDIUM", variable=var, value="medium", indicatoron = 0, command = select_mode)
medium_mode.pack(anchor = "w")
medium_mode.place(rely = 0.125)

hard_mode = tk.Radiobutton(root, text="HARD", variable=var, value="hard", indicatoron = 0, command = select_mode)
hard_mode.pack(anchor = "w")
hard_mode.place(rely = 0.16, width = 56)





def next_level_handler():
    global LEVEL
    global run
    global game
    global next_level

    LEVEL += 1
    if(LEVEL > len(levels)):
        run = False
        level_text.set('No more levels in this difficulty')
    else:
        game = Game(deepcopy(levels[str(LEVEL)]), LEVEL)
        level_text.set('Level: ' + str(LEVEL))
        display_game()

    next_level.config(state="normal")




next_level = tk.Button(root,
    text="Next Level",
    state="disabled",
    command=next_level_handler)
next_level.pack()
next_level.place(rely = 0.9 , relx = 0.04, height = 35, width = 140)


def start_player():
    global run
    global game
    global next_level

    game = Game(deepcopy(levels[str(LEVEL)]), LEVEL)
    display_game()
    canvas.focus_set()
    next_level.config(state="disabled")
    run = True

player_button = tk.Button(root,
    text="Play",
    command= start_player)
player_button.pack()
player_button.place(rely = 0.45, relx = 0.02, height = 55, width = 170)

def alg_updated(event):
    global depth_input

    if algorithm.get() == "iterative depth":
        depth_input.config(state="normal")
    else:
        depth_input.config(state="disabled")


algorithms = [
    "bfs",
    "dfs",
    "a*",
    "greedy",
    "ucs",
    "iterative depth"
]
algorithm = tk.StringVar(root)
algorithm.set(algorithms[0])

algorithm_op = tk.OptionMenu(root, algorithm, *algorithms, command=alg_updated)
algorithm_op.config(width=SIDE_MENU_WIDTH)
algorithm_op.pack()
algorithm_op.place(rely = 0.6 , relx = 0.02, width = 170)

max_depth = tk.StringVar(root)
max_depth.set("Max Depth")

depth_input = tk.Entry(root, textvariable=max_depth)
depth_input.config(state="disabled")
depth_input.pack()
depth_input.place(rely = 0.7 , relx = 0.02, height = 45)

def start_ai():
    global algorithm_op
    global run
    global game
    global ai_info
    global block
    global next_level

    run = False
    algorithm_op.config(state="disabled")
    player_button.config(state="disabled")
    next_level.config(state="disabled")

    game = Game(deepcopy(levels[str(LEVEL)]), LEVEL)
    display_game()

    depth = 3
    if str.isdigit(max_depth.get()):
        depth = int(max_depth.get())

    path, stats = get_computer_path(game, algorithm.get(), depth)

    if len(path) == 0:
        ai_info.set("Time: %.5f s\nMemory: %d\nNo solution found!" % (stats[0], stats[1]))
    else:
        ai_info.set("Time: %.5f s\nMemory: %d\nCost: %d" % (stats[0], stats[1], len(path)))
        for n in range(len(path)):
            time.sleep(1)
            index = path[n][0]
            move = path[n][1]
            block = game.blocks[index]
            game.move(block, move)
            display_game()
            root.update()
    
    algorithm_op.config(state="normal")
    player_button.config(state="normal")

    if game.finished:
        next_level.config(state="normal")
    
    block = None
    display_game()

solve_button = tk.Button(root,
    text="Solve",
    padx=50,
    command= start_ai)
solve_button.pack()
solve_button.place(rely = 0.8 , relx = 0.04, height = 45)

ai_info = tk.StringVar()
ai_info.set('STATS')
ai_info_label = tk.Label(root,
    textvariable=ai_info,
    wraplength=SIDE_MENU_WIDTH,
    font=("Helvetica", 20),
    bg = "black",
    fg = "green")
ai_info_label.pack()
ai_info_label.place(rely = 0.2, relx = 0.005, width = 193)


root.mainloop()