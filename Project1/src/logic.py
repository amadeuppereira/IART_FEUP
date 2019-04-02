import math
from game import Game
from copy import deepcopy
import time
import queue as Q

# Returns all the pieces positions ordered by their color
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

# Returns the distance between two points by their coordinates
def distance_between_points(x1,y1,x2,y2) :
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2)

def manhattan_distance_between_points(x1,y1,x2,y2) :
    return abs(x1 - x2) + abs(y1 - y2)

# Return the sum of all the distances between pieces of the same color
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

def manhattan_distance_equal_pieces(piecesCoords) :
    totalDistance = 0
    for i in range(len(piecesCoords)):
        j = i+1
        while j < len(piecesCoords) :
            distance = manhattan_distance_between_points(piecesCoords[i][0], piecesCoords[i][1], piecesCoords[j][0], piecesCoords[j][1])
            # If the distance between two points is 1 then it means they are adjacent so we ignore their distance
            if distance > 1 :
                totalDistance = totalDistance + distance
            j = j+1
    return totalDistance


# ----------------------------------------------------------------------------------
#                                HEURISTICS
# ----------------------------------------------------------------------------------

# Returns the sum of all distances between pieces of the same color
def heuristic_1(game) :
    board = game.board
    pieces = getPiecesPositionsByColor(board)
    totalDistances = 0
    for _, value in pieces.items():
        totalDistances = totalDistances + distance_equal_pieces(value)
    return totalDistances

# Returns the sum of all the manhattan distances between pieces of the same color
def heuristic_2(game) :
    board = game.board
    pieces = getPiecesPositionsByColor(board)
    totalDistances = 0
    for _, value in pieces.items():
        totalDistances = totalDistances + manhattan_distance_equal_pieces(value)
    return totalDistances

# Returns an estimated number of movements remaining to group all the blocks with the same color
def heuristic_3(game) :
    board = game.board
    pieces = getPiecesPositionsByColor(board)
    n_colors = len(pieces.items())

    return (len(game.blocks) - n_colors) * 3



# ----------------------------------------------------------------------------------
#                                GAME MOVES
# ----------------------------------------------------------------------------------

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
# All return [path, mem]
# path = [ [block index, movement direction], ... ]
# mem = number of nodes saved in memory

"""
Breadth-First Search
"""
def bfs(game) :
    path = []
    queue = [[game, path]]
    visited = []
    mem = 1

    while queue:
        new_queue = []

        for queue_item in queue :
            game = queue_item[0]
            path = queue_item[1]

            if game.is_finished():
                return (path, mem)

            new_moves = get_game_moves(game)

            for move, new_game in new_moves:
                if new_game not in visited:
                    new_path = path + [move]
                    new_queue.append([new_game, new_path])
                    mem += 1

            visited.append(game)

        queue = new_queue

    return ([], mem)

"""
Depth-First Search
"""
def dfs(game):
    visited = []
    path = []
    queue = [[game, path]]
    mem = 1

    while queue:
        child_nodes = []

        queue_item = queue[0]
        game = queue_item[0]
        path = queue_item[1]

        if game.is_finished():
            return (path, mem)

        new_moves = get_game_moves(game)

        for move, new_game in new_moves:
            if new_game not in visited:
                new_path = path + [move]
                child_nodes.append([new_game, new_path])
                mem += 1

        visited.append(game)

        # Appending new nodes to the start of the list
        queue = child_nodes + queue[1:]

    return ([], mem)

"""
A* Algorithm
"""
def astar(game, heuristic):
    path = []
    queue = [[heuristic(game), game, path]]

    visited = []
    mem = 1

    while queue:
        i = 0
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j

        game = queue[i][1]
        path = queue[i][2]

        queue = queue[:i] + queue[i+1:]

        if game.is_finished():
            return (path, mem)
        if game in visited: continue
        for move, new_game in get_game_moves(game):
            if new_game in visited: continue
            new_path = path + [move]
            new_node = [heuristic(new_game) + len(new_path), new_game, new_path]
            queue.append(new_node)
            mem += 1

        visited.append(game)

    return ([], mem)

"""
Greedy Search
"""
def greedy(game, heuristic):
    path = []
    queue = [[heuristic(game), game, path]]

    visited = []
    mem = 1

    while queue:
        i = 0
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j

        game = queue[i][1]
        path = queue[i][2]

        queue = queue[:i] + queue[i+1:]

        if game.is_finished():
            return (path, mem)
        if game in visited: continue
        for move, new_game in get_game_moves(game):
            if new_game in visited: continue
            new_path = path + [move]
            new_node = [heuristic(new_game), new_game, new_path]
            queue.append(new_node)
            mem += 1

        visited.append(game)

    return ([], mem)


"""
Uniform Cost Search
"""
def ucs(game):
    path = []
    queue = [[0, game, path]]
    visited = []
    mem = 1

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
            return (path, mem)
        if game in visited: continue
        for move, new_game in get_game_moves(game):
            if new_game in visited: continue
            new_path = path + [move]
            # Only add 1 to cost because each move only costs 1
            new_node = [cost + 1, new_game, new_path]
            queue.append(new_node)
            mem += 1

        visited.append(game)

    return ([], mem)

"""
Depth-First Search with limit
"""
def dfs_limit(game, limit):
    visited = [[0, game]]
    path = []
    queue = [[0, game, path]]
    mem = 1

    while queue:
        child_nodes = []

        queue_item = queue[0]
        depth = queue_item[0]
        game = queue_item[1]
        path = queue_item[2]

        if game.is_finished():
            return (path, mem)

        new_depth = depth + 1
        if depth < limit :
            new_moves = get_game_moves(game)
            for move, new_game in new_moves:
                repeated = False
                for node_visited in visited:
                    if node_visited[1] == new_game:
                        if new_depth >= node_visited[0]:
                            repeated = True

                if not repeated:
                    new_path = path + [move]
                    child_nodes.append([new_depth, new_game, new_path])
                    mem += 1

            visited.append([depth, game])
            queue = child_nodes + queue[1:]
        else:
            queue = queue[1:]

    return ([], mem)

"""
Iterative Depth Search
"""
def iterative_depth(game, max_depth):
    mem = 0
    for i in range(0, max_depth):
        ret = dfs_limit(game, i)
        mem += ret[1]
        if ret[0]:
            return (ret[0], mem)

    return ([], mem)




# COMPUTER MOVE: calls algorithms and returns path
def get_computer_path(game, alg, heuristic , max_depth = 20) :

    if heuristic == "heuristic_1": heuristic = heuristic_1
    elif heuristic == "heuristic_2": heuristic = heuristic_2
    elif heuristic == "heuristic_3": heuristic = heuristic_3

    start_time = time.time()

    if alg == "bfs":
        path, mem = bfs(game)
        return (path, [time.time() - start_time, mem])
    elif alg == "dfs":
        path, mem = dfs(game)
        return (path, [time.time() - start_time, mem])
    elif alg == "a*":
        path, mem = astar(game, heuristic)
        return (path, [time.time() - start_time, mem])
    elif alg == "greedy":
        path, mem = greedy(game, heuristic)
        return (path, [time.time() - start_time, mem])
    elif alg == "ucs":
        path, mem = ucs(game)
        return (path, [time.time() - start_time, mem])
    elif alg == "iterative depth":
        path, mem = iterative_depth(game, max_depth)
        return (path, [time.time() - start_time, mem])
