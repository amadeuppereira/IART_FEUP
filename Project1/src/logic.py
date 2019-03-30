import math
from game import Game
from node import Node
import queue as Q
from copy import deepcopy

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
    for key, value in pieces.items():
        totalDistances = totalDistances + distance_equal_pieces(value)
    return totalDistances

# Returns all the available moves for the game passed by parameter
# [ ([coords from one piece of a block, movement direction], [new board generated]), ... ]
def get_game_moves(game):
    temp_game = deepcopy(game)
    ret = []

    for block in game.blocks:
        temp_game = deepcopy(game)
        temp_block = temp_game.get_block(block.coords[0][0], block.coords[0][1])
        temp_coords = temp_block.coords[0][:]

        if temp_game.move(temp_block, "up"):
            ret.append(([temp_coords, "up"], temp_game))
            temp_game = deepcopy(game)
            temp_block = temp_game.get_block(block.coords[0][0], block.coords[0][1])

        if temp_game.move(temp_block, "down"):
            ret.append(([temp_coords, "down"], temp_game))
            temp_game = deepcopy(game)
            temp_block = temp_game.get_block(block.coords[0][0], block.coords[0][1])

        if temp_game.move(temp_block, "left"):
            ret.append(([temp_coords, "left"], temp_game))
            temp_game = deepcopy(game)
            temp_block = temp_game.get_block(block.coords[0][0], block.coords[0][1])

        if temp_game.move(temp_block, "right"):
            ret.append(([temp_coords, "right"], temp_game))
            temp_game = deepcopy(game)
            temp_block = temp_game.get_block(block.coords[0][0], block.coords[0][1])

    return ret


# ----------------------------------------------------------------------------------
#                                ALGORITHMS
# ----------------------------------------------------------------------------------
# all return path
# path = [ [coords from one piece of a block, movement direction], ... ]

"""
Breadth-First Search
"""
def bfs(game) :
    path = []
    queue = [[game, path]]
    visited = []
    
    while len(queue) != 0:
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

    while len(queue) != 0:
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


# TODO:
"""
Greedy Search
"""
def greedy(game):
    print('greedy')

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

    while len(queue) != 0:
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


def get_computer_path(game) :
    # return bfs(game)
    a = astar(game)
    print(a)
    return a
    # return dfs(game)
    # return iterative_depth(game, 3)




# To test:
import time
# board = [[1,0,0,0],
#         [0,1,1,0],
#         [0,3,3,0],
#         [4,4,0,0]]
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
print(ucs(g))
print(time.time() - start_time)





# queue = Q.PriorityQueue()
# a = Node("node1")
# b = Node("node2")
# c = Node("node3")
# d = Node("node4")
# e = Node("node5")
# f = Node("node6")
# g = Node("node7")
# h = Node("node8")

# queue.put((0, 1))
# queue.put((0, 0))
# queue.put((0, a)) #1
# queue.put((0, c)) #3
# queue.put((1, d)) #4
# queue.put((1, h)) #8
# queue.put((0, g)) #7
# queue.put((1, e)) #5
# queue.put((0, b)) #2
# queue.put((0, f)) #6


# while not queue.empty():
#     print(queue.get())



# pesquisa em largura, pesquisa em profundidade, aprofundamento progressivo, pesquisa de custo
# uniforme, pesquisa gulosa e algoritmo A*, com configurações diversas (diferentes modos de
# representação do problema e diferentes heurísticas)