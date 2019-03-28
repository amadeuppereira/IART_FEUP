import math
from game import Game
from node import Node
from queue import PriorityQueue
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
    # TODO: Ver os casos em que as peças ficam bloqueadas
    totalDistance = 0
    for i in range(len(piecesCoords)):
        j = i+1
        while j < len(piecesCoords) :
            distance = distance_between_points(piecesCoords[i][0], piecesCoords[i][1], piecesCoords[j][0], piecesCoords[j][1])
            # Se a distancia for 1 quer dizer que os pontos são adjacentes por isso podemos ignorar a sua distancia
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


def dfs(game):
    visited = []
    path = []
    leafs = PriorityQueue()
    leafs.put((0, game, path, visited))

    while not leafs.empty():
        _, current_game, path, visited = leafs.get()

        if current_game.finished:
            return path

        visited = visited + [current_game]

        # If not goal, get its child nodes
        child_nodes = {}

        # 4. Add child nodes to the leafs if they haven't been visited yet
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
                # The priority queue prioritises lower values over higher ones (i.e. 1 is prioritised higher than 10)
                # Since we are using depth of node as our prioritisation measure we need to pass in negative priorities
                # To ensure that nodes with greater depth get explored before shallower ones
                leafs.put((-depth_of_node, node, path + [node], visited + [node]))

    return path

def get_game_moves(game):
    temp = deepcopy(game)
    ret = []
    i = 0

    for block in game.blocks:
        if temp.move(block, "up"):
            ret.append(("{} u".format(i), temp))
            temp = deepcopy(game)
        if temp.move(block, "down"):
            ret.append(("{} d".format(i), temp))
            temp = deepcopy(game)
        if temp.move(block, "left"):
            ret.append(("{} l".format(i), temp))
            temp = deepcopy(game)
        if temp.move(block, "right"):
            ret.append(("{} r".format(i), temp))
            temp = deepcopy(game)

        i += 1

    return ret




# To test:
board = [[1,0,0,1],
        [3,1,1,3],
        [0,3,3,0],
        [4,0,0,4]]
# print(heuristic(board))

g = Game(board, 1)
print(g.blocks)
print(get_game_moves(g))

# for m, g in get_game_moves(g):
#     print(g)