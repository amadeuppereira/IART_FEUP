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
level_text.set('Level: ' + str(LEVEL))
level_label = tk.Label(root,
    textvariable=level_text,
    pady=10,
    wraplength=SIDE_MENU_WIDTH,
    font=("Helvetica", 20))
level_label.pack()

difficulty_text = tk.StringVar()
difficulty_text.set('Difficulty: ' + GAMEMODE.upper())
difficulty_label = tk.Label(root,
    textvariable=difficulty_text,
    wraplength=SIDE_MENU_WIDTH,
    font=("Helvetica", 20))
difficulty_label.pack()

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

max_depth = tk.StringVar(root)
max_depth.set("Max Depth")

depth_input = tk.Entry(root, textvariable=max_depth)
depth_input.config(state="disabled")
depth_input.pack()

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

ai_info = tk.StringVar()
ai_info.set('')
ai_info_label = tk.Label(root,
    textvariable=ai_info,
    wraplength=SIDE_MENU_WIDTH,
    font=("Helvetica", 20))
ai_info_label.pack()


root.mainloop()