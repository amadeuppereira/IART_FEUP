import time
from solver import *

prob1 = [[1,2,3],
         [5,0,6],
         [4,7,8]]

prob2 = [[1,3,6],
         [5,2,0],
         [4,7,8]]

prob3 = [[1,6,2],
         [5,7,3],
         [0,4,8]]

prob4 = [[5,1,3,4],
         [2,0,7,8],
         [10,6,11,12],
         [9,13,14,15]]

# ----------------------------------------------------------------------------------
#                                BREADTH-FIRST SEARCH
# ----------------------------------------------------------------------------------

print("-------- BREADTH-FIRST SEARCH --------", "\n")

# prob1
print("-> prob1")
start_time = time.time()
path = bfs(str(prob1))
# print_puzzle_moves(str(prob1), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob2
print("-> prob2")
start_time = time.time()
path = bfs(str(prob2))
# print_puzzle_moves(str(prob2), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob3
print("-> prob3")
start_time = time.time()
path = bfs(str(prob3))
# print_puzzle_moves(str(prob3), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob4
print("-> prob4")
start_time = time.time()
path = bfs(str(prob4))
# print_puzzle_moves(str(prob4), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# ----------------------------------------------------------------------------------
#                                A* ALGORITHM SEARCH
# ----------------------------------------------------------------------------------

print("-------- A* ALGORITHM SEARCH --------","\n")

# prob1 (heuristic_1)
print("-> prob1 (heuristic_1)")
start_time = time.time()
path = astar(str(prob1), heuristic_1)
# print_puzzle_moves(str(prob1), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob1 (heuristic_2)
print("-> prob1 (heuristic_2)")
start_time = time.time()
path = astar(str(prob1), heuristic_2)
# print_puzzle_moves(str(prob1), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob2 (heuristic_1)
print("-> prob2 (heuristic_1)")
start_time = time.time()
path = astar(str(prob2), heuristic_1)
# print_puzzle_moves(str(prob2), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob2 (heuristic_2)
print("-> prob2 (heuristic_2)")
start_time = time.time()
path = astar(str(prob2), heuristic_2)
# print_puzzle_moves(str(prob2), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob3 (heuristic_1)
print("-> prob3 (heuristic_1)")
start_time = time.time()
path = astar(str(prob3), heuristic_1)
# print_puzzle_moves(str(prob3), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob3 (heuristic_2)
print("-> prob3 (heuristic_2)")
start_time = time.time()
path = astar(str(prob3), heuristic_2)
# print_puzzle_moves(str(prob3), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob4 (heuristic_1)
print("-> prob4 (heuristic_1)")
start_time = time.time()
path = astar(str(prob4), heuristic_1)
# print_puzzle_moves(str(prob4), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob4 (heuristic_2)
print("-> prob4 (heuristic_2)")
start_time = time.time()
path = astar(str(prob4), heuristic_2)
# print_puzzle_moves(str(prob4), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")



# ----------------------------------------------------------------------------------
#                                GREEDY ALGORITHM SEARCH
# ----------------------------------------------------------------------------------

print("-------- GREEDY ALGORITHM SEARCH --------")

# prob1 (heuristic_1)
print("-> prob1 (heuristic_1)")
start_time = time.time()
path = greedy(str(prob1), heuristic_1)
# print_puzzle_moves(str(prob1), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob1 (heuristic_2)
print("-> prob1 (heuristic_2)")
start_time = time.time()
path = greedy(str(prob1), heuristic_2)
# print_puzzle_moves(str(prob1), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob2 (heuristic_1)
print("-> prob2 (heuristic_1)")
start_time = time.time()
path = greedy(str(prob2), heuristic_1)
# print_puzzle_moves(str(prob2), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob2 (heuristic_2)
print("-> prob2 (heuristic_2)")
start_time = time.time()
path = greedy(str(prob2), heuristic_2)
# print_puzzle_moves(str(prob2), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob3 (heuristic_1)
print("-> prob3 (heuristic_1)")
start_time = time.time()
path = greedy(str(prob3), heuristic_1)
# print_puzzle_moves(str(prob3), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob3 (heuristic_2)
print("-> prob3 (heuristic_2)")
start_time = time.time()
path = greedy(str(prob3), heuristic_2)
# print_puzzle_moves(str(prob3), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob4 (heuristic_1)
print("-> prob4 (heuristic_1)")
start_time = time.time()
path = greedy(str(prob4), heuristic_1)
# print_puzzle_moves(str(prob4), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")

# prob4 (heuristic_2)
print("-> prob4 (heuristic_2)")
start_time = time.time()
path = greedy(str(prob4), heuristic_2)
# print_puzzle_moves(str(prob4), path[0])
elapsed_time = time.time() - start_time
print("MOVES: ", path[0], "\nNUMBER OF MOVES: ", len(path[0]), "\nMEMORY: ", path[1], "\nTIME: ","{0:.4f}".format(elapsed_time), "\n")
