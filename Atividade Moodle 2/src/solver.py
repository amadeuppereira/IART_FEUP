# Install for puzzle prints:
# pip3 install numpy
import numpy as np


# ----------------------------------------------------------------------------------
#                                GAME MOVES
# ----------------------------------------------------------------------------------

"""
Returns a list of all possible moves
[ (movement direction, new board), ...]
"""
def get_moves(board): 
    new_boards = []  

    m = eval(board)
    puzzle_size = len(m) -1
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); # blank space (zero)

    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]  # move up
      new_boards.append(('up',str(m)))
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]
      
    if i < puzzle_size:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      new_boards.append(('down',str(m)))
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      new_boards.append(('left',str(m)))
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < puzzle_size:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      new_boards.append(('right',str(m)))
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

    return new_boards


"""
Returns objective puzzle given its size
"""
def get_objective_puzzle(puzzle_size) :
    ret = []
    number = 1
    for i in range(puzzle_size):
        line = []
        for j in range(puzzle_size):
            line.append(number)
            number += 1
        ret.append(line)
    ret[puzzle_size-1][puzzle_size-1] = 0
    return str(ret)


    
# ----------------------------------------------------------------------------------
#                                HEURISTICS
# ----------------------------------------------------------------------------------

"""
Counts the number of misplaced tiles
""" 
def heuristic_1(puzzle):
    misplaced = 0
    compare = 1
    p = eval(puzzle)
    puzzle_size = len(p)
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            if i == puzzle_size-1 and j == puzzle_size-1:
                if p[i][j] != 0:
                    misplaced += 1
            elif p[i][j] != compare:
                misplaced += 1
            compare += 1
    return misplaced

"""
Manhattan distance between misplaced tiles and their correct position
"""  
def heuristic_2(puzzle):
    distance = 0
    p = eval(puzzle)
    puzzle_size = len(p)       
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            if p[i][j] == 0:
                distance += abs(i - (puzzle_size-1)) + abs(j - (puzzle_size-1))
            else:
                distance += abs(i - int(float(p[i][j]-1)/puzzle_size)) + abs(j -  int(float(p[i][j]-1)%puzzle_size))
    return distance



# ----------------------------------------------------------------------------------
#                                ALGORITHMS
# ----------------------------------------------------------------------------------

"""
Breadth-First Search
"""
def bfs(start) :
    path = []
    queue = [[start, path]]
    visited = []
    mem = 1
    end = get_objective_puzzle(len(eval(start)))

    while queue:
        new_queue = []

        for queue_item in queue :
            puzzle = queue_item[0]
            path = queue_item[1]

            if puzzle == end:
                return (path, mem)

            new_moves = get_moves(puzzle)

            for move, new_game in new_moves:
                if new_game not in visited:
                    new_path = path + [move]
                    new_queue.append([new_game, new_path])
                    mem += 1

            visited.append(puzzle)

        queue = new_queue

    return ([], mem)


"""
A* Algorithm
"""
def astar(start, heuristic):
    path = []
    queue = [[heuristic(start), start, path]]
    end = get_objective_puzzle(len(eval(start)))
    visited = []
    mem = 1

    while queue:
        i = 0
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j

        puzzle = queue[i][1]
        path = queue[i][2]

        queue = queue[:i] + queue[i+1:]

        if puzzle == end:
            return (path, mem)

        if puzzle in visited: continue
        for move, new_game in get_moves(puzzle):
            if new_game in visited: continue
            new_path = path + [move]
            new_node = [heuristic(new_game) + len(new_path), new_game, new_path]
            queue.append(new_node)
            mem += 1

        visited.append(puzzle)

    return ([], mem)


"""
Greedy Search
"""
def greedy(start, heuristic):
    path = []
    queue = [[heuristic(start), start, path]]
    end = get_objective_puzzle(len(eval(start)))
    visited = []
    mem = 1

    while queue:
        i = 0
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j

        puzzle = queue[i][1]
        path = queue[i][2]

        queue = queue[:i] + queue[i+1:]

        if puzzle == end:
            return (path, mem)

        if puzzle in visited: continue
        for move, new_game in get_moves(puzzle):
            if new_game in visited: continue
            new_path = path + [move]
            new_node = [heuristic(new_game), new_game, new_path]
            queue.append(new_node)
            mem += 1

        visited.append(puzzle)

    return ([], mem)



# ----------------------------------------------------------------------------------
#                                PUZZLE PRINTS
# ----------------------------------------------------------------------------------

"""
Returns new puzzle after move
"""
def make_move(board, move) :
    m = eval(board)
    puzzle_size = len(m) -1
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); # blank space (zero)

    if move == 'up':
        m[i][j], m[i-1][j] = m[i-1][j], m[i][j]
        return str(m)
    elif move == 'down':
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
        return str(m)
    elif move == 'right' :
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
        return str(m)
    elif move == 'left' :
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
        return str(m)
    else :
        return ''

def print_puzzle(puzzle) :
    print(np.matrix(eval(puzzle)))
    print('----------------')

def print_puzzle_moves(board, moves):
    print_puzzle(board)
    for i in range(len(moves)):
        board = make_move(board, moves[i])
        print_puzzle(board)