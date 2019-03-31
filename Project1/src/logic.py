import math
from game import Game
import queue as Q
from copy import deepcopy
import time

def getPiecesPositionsByColor(board):
    pieces = {}
    for j in range(len(board)):
        for i in range(len(board[0])):
            if board[i][j] != 0 :
                if board[i][j] in pieces.keys():
                    pieces[board[i][j]].append([i, j])
                else:
                    pieces[board[i][j]] = [[i, j]]
    return pieces

def distance_between_points(x1,y1,x2,y2) :
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2)

def distance_equal_pieces(piecesCoords) :
    totalDistance = 0
    for i in range(len(piecesCoords)):
        j = i+1
        while j < len(piecesCoords) :
            distance = distance_between_points(piecesCoords[i][0], piecesCoords[i][1], piecesCoords[j][0], piecesCoords[j][1])
            # If the distance between two points is 1 then it means they are adjacent so we ignore their distance
            if distance > 1 :
                totalDistance = totalDistance + distance
            j = j+1
    return totalDistance

# Returns the sum of all distances between pieces of the same color
def heuristic(board) :
    pieces = getPiecesPositionsByColor(board)
    totalDistances = 0
    for _, value in pieces.items():
        totalDistances = totalDistances + distance_equal_pieces(value)
    return totalDistances

# Takes in account the pieces distance, the number of available moves
# and the blocks/colors ratio
def heuristic1(game) :
    board = game.board
    pieces = getPiecesPositionsByColor(board)
    totalDistances = 0
    n_colors = 0
    for _, value in pieces.items():
        n_colors += 1
        totalDistances = totalDistances + distance_equal_pieces(value)
    
    blocks_color_ratio = len(game.blocks) / n_colors

    n_moves = 0
    for block in game.blocks:
        if game.is_possible_up(block): n_moves += 1
        if game.is_possible_down(block): n_moves += 1
        if game.is_possible_left(block): n_moves += 1
        if game.is_possible_right(block): n_moves += 1
            
    return totalDistances*0.3 + blocks_color_ratio*0.3 + n_moves*0.3
    

    

# Returns all the available moves for the game passed by parameter
# [ ([block index, movement direction], new game), ... ]
def get_game_moves(game):
    temp_game = deepcopy(game)
    ret = []

    for i in range(len(game.blocks)):
        if temp_game.move(temp_game.blocks[i], "up"):
            ret.append(([i, "up"], temp_game))
            temp_game = deepcopy(game)

        if temp_game.move(temp_game.blocks[i], "down"):
            ret.append(([i, "down"], temp_game))
            temp_game = deepcopy(game)
        
        if temp_game.move(temp_game.blocks[i], "left"):
            ret.append(([i, "left"], temp_game))
            temp_game = deepcopy(game)
        
        if temp_game.move(temp_game.blocks[i], "right"):
            ret.append(([i, "right"], temp_game))
            temp_game = deepcopy(game)

    return ret


# ----------------------------------------------------------------------------------
#                                ALGORITHMS
# ----------------------------------------------------------------------------------
# all return path
# path = [ [block index, movement direction], ... ]

"""
Breadth-First Search
"""
def bfs(game) :
    path = []
    queue = [[game, path]]
    visited = []
    
    while queue:
        new_queue = []

        for queue_item in queue :
            game = queue_item[0]
            path = queue_item[1]

            if game.is_finished():
                return path

            new_moves = get_game_moves(game)
            
            for move, new_game in new_moves:
                if new_game not in visited:
                    new_path = path + [move]
                    new_queue.append([new_game, new_path])
                    visited.append(game)
        
        queue = new_queue

    print('No solutions found')
    return []

"""
Depth-First Search
"""
def dfs(game):
    visited = []
    path = []
    queue = [[game, path]]

    while queue:
        child_nodes = []

        queue_item = queue[0]
        game = queue_item[0]
        path = queue_item[1]

        if game.is_finished():
            return path

        new_moves = get_game_moves(game)
        
        for move, new_game in new_moves:
            if new_game not in visited:
                new_path = path + [move]
                child_nodes.append([new_game, new_path])
                visited.append(game)
        
        # Appending new nodes to the start of the list
        queue = child_nodes + queue[1:]
    
    print('No solutions found')
    return []

"""
A* Algorithm
"""
def astar(game):
    path = []
    queue = [[heuristic(game.board), game, path]]
    visited = []
    while queue:
        i = 0
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j
        
        previous_heuristic = queue[i][0]
        game = queue[i][1]
        path = queue[i][2]
        queue = queue[:i] + queue[i+1:]

        if game.is_finished():
            break
        if game in visited: continue
        for move, new_game in get_game_moves(game):
            if new_game in visited: continue
            new_path = path + [move]
            new_node = [previous_heuristic + heuristic(new_game.board) - heuristic(game.board), new_game, new_path]
            queue.append(new_node)
            visited.append(game)

    return path  

"""
Greedy Search
"""
def greedy(game):
    path = []
    queue = [heuristic(game.board), game, path]
    visited = []
    while queue:
        game = queue[1]
        path = queue[2]
        
        best_child = []

        if game.is_finished():
            return path

        if game in visited: continue
        for move, new_game in get_game_moves(game):
            if new_game in visited: continue
            new_path = path + [move]
            new_node = [heuristic(new_game.board), new_game, new_path]
            visited.append(game)
            if best_child:
                if best_child[0] > new_node[0]:
                    best_child = new_node
            else:
                best_child = new_node

        queue = best_child

    print('No solutions found')
    return []

"""
Uniform Cost Search
"""
def ucs(game):
    path = []
    queue = [[0, game, path]]
    visited = []
    while queue:
        i = 0
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j
        
        cost = queue[i][0]
        game = queue[i][1]
        path = queue[i][2]
        queue = queue[:i] + queue[i+1:]

        if game.is_finished():
            break
        if game in visited: continue
        for move, new_game in get_game_moves(game):
            if new_game in visited: continue
            new_path = path + [move]
            # Only add 1 to cost because each move only costs 1 
            new_node = [cost + 1, new_game, new_path]
            queue.append(new_node)
            visited.append(game)

    return path 

"""
Iterative Depth Search
"""
def iterative_depth(game, limit):
    visited = []
    path = []
    queue = [[0, game, path]]

    while queue:
        child_nodes = []
        
        queue_item = queue[0]
        depth = queue_item[0]
        game = queue_item[1]
        path = queue_item[2]

        if game.is_finished():
            return path

        new_moves = get_game_moves(game)
        new_depth = depth + 1
        for move, new_game in new_moves:
            if new_game not in visited:
                new_path = path + [move]
                child_nodes.append([new_depth, new_game, new_path])
                visited.append(game)
        
        if new_depth % limit == 0:
            queue = queue[1:] + child_nodes
        else:
            queue = child_nodes + queue[1:]
    
    print('No solutions found')
    return []


# COMPUTER MOVE: call algorithms and return path
def get_computer_path(game) :
    # return bfs(game)
    return astar(game)
    # return dfs(game)
    # return iterative_depth(game, 3)
    # return ucs(game)
    # return greedy(game)

 
def greedy1(game):
    path = []
    queue = [heuristic1(game), game, path]
    visited = []
    while queue:
        game = queue[1]
        path = queue[2]
        
        best_child = []

        if game.is_finished():
            return path

        if game in visited: continue
        for move, new_game in get_game_moves(game):
            if new_game in visited: continue
            new_path = path + [move]
            new_node = [heuristic1(new_game), new_game, new_path]
            visited.append(game)
            if best_child:
                if best_child[0] > new_node[0]:
                    best_child = new_node
            else:
                best_child = new_node

        queue = best_child

    print('No solutions found')
    return []

# To test:
# import time
# board = [[1,0,0,0],
#          [0,1,1,0],
#          [0,3,3,0],
#          [4,4,0,0]]
# board = [[1,0,0,1],
#         [3,1,1,3],
#         [0,3,3,0],
#         [4,0,0,4]]
# board = [[1,1,2,0],
#         [0,2,1,1],
#         [1,1,2,0],
#         [0,0,1,1]]
board = [[1,1,0,2],
        [3,3,3,0],
        [3,3,3,1],
        [0,2,1,0]]
g = Game(board, 1)
start_time = time.time()
greedy(g)
print(time.time() - start_time)
start_time = time.time()
greedy1(g)
print(time.time() - start_time)