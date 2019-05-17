import math
import random
from schedule import getRandomSolution, value, getBestNeighbour, getRandomNeighbour, getBetterRandomNeighbour
from output import *
from input import num_events

MAX_ATTEMPS = 1000


# - Escolher um estado aleatoriamente do espaço de estados
# – Considerar todos os vizinhos desse estado
# – Escolher o melhor vizinho
# – Repetir o processo até não existirem vizinhos melhores
# – O estado corrente é a solução


def hill_climbing():
    print("Hill Climbing")
    current = getRandomSolution()
    for i in range(1, MAX_ATTEMPS):
        current_value = value(current)
        neighbour, neighbour_value = getBestNeighbour(current)
        print("Current: ", current_value)
        print("Neighbour: ", neighbour_value)
        if neighbour_value > current_value:
            return current
        current = neighbour
    return current


MAX_ATTEMPS_RANDOM = 900


def hill_climbing_improved():
    print("Hill Climbing")
    current = getRandomSolution()
    print(value(current))
    flag = False
    for i in range(1, MAX_ATTEMPS):
        current_value = value(current)
        if flag:
            neighbour, neighbour_value = getBestNeighbour(current)
        else:
            neighbour, neighbour_value = getBetterRandomNeighbour(
                current, current_value, MAX_ATTEMPS_RANDOM)
        print("Current: ", current_value)
        print("Neighbour: ", neighbour_value)
        if neighbour_value > current_value:
            return current
        elif neighbour == current:
            return current
        elif neighbour_value == current_value:
            flag = True
        current = neighbour
    return current


# – Semelhante ao Hill-Climbing Search mas admite explorar vizinhos piores
# – Temperatura que vai sendo sucessivamente reduzida define a probabilidade de aceitar soluções piores


def simulated_annealing():
    current = getRandomSolution()
    T = 100
    for i in range(1, MAX_ATTEMPS):
        if T < 0:
            return current
        next = getRandomNeighbour(current)
        ap = math.exp((value(next)-value(current))/T)
        if ap > random.uniform(0, 1):
            current = next
        T = T - (1/math.log(1+i))
    return current


solution = hill_climbing_improved()

for x in solution:
    print(x.id, x.event_room)
# write_to_file(solution, num_events)
