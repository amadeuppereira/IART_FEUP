import time
from logic import *
from game import Game

# Board from an easy level
easy_board = [[1,0,0,1],
              [3,1,1,3],
              [0,3,3,0],
              [4,0,0,4]]

# Board from a medium level
medium_board = [[1,1,2,0],
                [0,2,1,1],
                [1,1,2,0],
                [0,0,1,1]]

# Board from an hard level
hard_board = [[1,2,0,0],
              [2,0,0,3],
              [0,4,4,2],
              [3,2,1,0]]

g = Game(easy_board, 1)
# g = Game(medium_board, 1)
# g = Game(hard_board, 1)

# ----------------------------------------------------------------------------------
#                                BREADTH-FIRST SEARCH
# ----------------------------------------------------------------------------------

print("-------- BREADTH-FIRST SEARCH --------", "\n")

# Easy
print("-> Easy")
g = Game(easy_board, 1)
start_time = time.time()
path = bfs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium
print("-> Medium")
g = Game(medium_board, 1)
start_time = time.time()
path = bfs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard
print("-> Hard")
g = Game(hard_board, 1)
start_time = time.time()
path = bfs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")



# ----------------------------------------------------------------------------------
#                                DEPTH-FIRST SEARCH
# ----------------------------------------------------------------------------------

print("-------- DEPTH-FIRST SEARCH --------", "\n")

# Easy
print("-> Easy")
g = Game(easy_board, 1)
start_time = time.time()
path = dfs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium
print("-> Medium")
g = Game(medium_board, 1)
start_time = time.time()
path = dfs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard
print("-> Hard")
g = Game(hard_board, 1)
start_time = time.time()
path = dfs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")



# ----------------------------------------------------------------------------------
#                                A* ALGORITHM SEARCH
# ----------------------------------------------------------------------------------

print("-------- A* ALGORITHM SEARCH --------")

# Easy (heuristic_1)
print("-> Easy (heuristic_1)")
g = Game(easy_board, 1)
start_time = time.time()
path = astar(g, heuristic_1)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Easy (heuristic_2)
print("-> Easy (heuristic_2)")
g = Game(easy_board, 1)
start_time = time.time()
path = astar(g, heuristic_2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Easy (heuristic_3)
print("-> Easy (heuristic_3)")
g = Game(easy_board, 1)
start_time = time.time()
path = astar(g, heuristic_3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")


# Medium (heuristic_1)
print("-> Medium (heuristic_1)")
g = Game(medium_board, 1)
start_time = time.time()
path = astar(g, heuristic_1)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium (heuristic_2)
print("-> Medium (heuristic_2)")
g = Game(medium_board, 1)
start_time = time.time()
path = astar(g, heuristic_2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium (heuristic_3)
print("-> Medium (heuristic_3)")
g = Game(medium_board, 1)
start_time = time.time()
path = astar(g, heuristic_3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")


# Hard (heuristic_1)
print("-> Hard (heuristic_1)")
g = Game(hard_board, 1)
start_time = time.time()
path = astar(g, heuristic_1)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard (heuristic_2)
print("-> Hard (heuristic_2)")
g = Game(hard_board, 1)
start_time = time.time()
path = astar(g, heuristic_2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard (heuristic_3)
print("-> Hard (heuristic_3)")
g = Game(hard_board, 1)
start_time = time.time()
path = astar(g, heuristic_3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")



# ----------------------------------------------------------------------------------
#                                GREEDY ALGORITHM SEARCH
# ----------------------------------------------------------------------------------

print("-------- GREEDY ALGORITHM SEARCH --------")

# Easy (heuristic_1)
print("-> Easy (heuristic_1)")
g = Game(easy_board, 1)
start_time = time.time()
path = greedy(g, heuristic_1)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Easy (heuristic_2)
print("-> Easy (heuristic_2)")
g = Game(easy_board, 1)
start_time = time.time()
path = greedy(g, heuristic_2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Easy (heuristic_3)
print("-> Easy (heuristic_3)")
g = Game(easy_board, 1)
start_time = time.time()
path = greedy(g, heuristic_3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")


# Medium (heuristic_1)
print("-> Medium (heuristic_1)")
g = Game(medium_board, 1)
start_time = time.time()
path = greedy(g, heuristic_1)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium (heuristic_2)
print("-> Medium (heuristic_2)")
g = Game(medium_board, 1)
start_time = time.time()
path = greedy(g, heuristic_2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium (heuristic_3)
print("-> Medium (heuristic_3)")
g = Game(medium_board, 1)
start_time = time.time()
path = greedy(g, heuristic_3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")


# Hard (heuristic_1)
print("-> Hard (heuristic_1)")
g = Game(hard_board, 1)
start_time = time.time()
path = greedy(g, heuristic_1)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard (heuristic_2)
print("-> Hard (heuristic_2)")
g = Game(hard_board, 1)
start_time = time.time()
path = greedy(g, heuristic_2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard (heuristic_3)
print("-> Hard (heuristic_3)")
g = Game(hard_board, 1)
start_time = time.time()
path = greedy(g, heuristic_3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")



# ----------------------------------------------------------------------------------
#                                UNIFORM COST SEARCH
# ----------------------------------------------------------------------------------

print("-------- UNIFORM COST SEARCH --------", "\n")

# Easy
print("-> Easy")
g = Game(easy_board, 1)
start_time = time.time()
path = ucs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium
print("-> Medium")
g = Game(medium_board, 1)
start_time = time.time()
path = ucs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard
print("-> Hard")
g = Game(hard_board, 1)
start_time = time.time()
path = ucs(g)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")



# ----------------------------------------------------------------------------------
#                               ITERATIVE DEPTH SEARCH
# ----------------------------------------------------------------------------------

print("-------- ITERATIVE DEPTH SEARCH --------", "\n")

# Easy (limit = 2)
print("-> Easy (limit = 2)")
g = Game(easy_board, 1)
start_time = time.time()
path = iterative_depth(g, 2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Easy (limit = 3)
print("-> Easy (limit = 3)")
g = Game(easy_board, 1)
start_time = time.time()
path = iterative_depth(g, 3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Easy (limit = 4)
print("-> Easy (limit = 4)")
g = Game(easy_board, 1)
start_time = time.time()
path = iterative_depth(g, 4)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")


# Medium (limit = 2)
print("-> Medium (limit = 2)")
g = Game(medium_board, 1)
start_time = time.time()
path = iterative_depth(g, 2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium (limit = 3)
print("-> Medium (limit = 3)")
g = Game(medium_board, 1)
start_time = time.time()
path = iterative_depth(g, 3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Medium (limit = 4)
print("-> Medium (limit = 4)")
g = Game(medium_board, 1)
start_time = time.time()
path = iterative_depth(g, 3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")


# Hard (limit = 2)
print("-> Hard (limit = 2)")
g = Game(hard_board, 1)
start_time = time.time()
path = iterative_depth(g, 2)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard (limit = 3)
print("-> Hard (limit = 3)")
g = Game(hard_board, 1)
start_time = time.time()
path = iterative_depth(g, 3)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# Hard (limit = 4)
print("-> Hard (limit = 4)")
g = Game(hard_board, 1)
start_time = time.time()
path = iterative_depth(g, 4)
elapsed_time = time.time() - start_time
print("MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")
