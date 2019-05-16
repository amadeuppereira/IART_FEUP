import math
import random
from schedule import getRandomSolution, value, getBestNeighbour, getRandomNeighbour

MAX_ATTEMPS = 100000

# algoritmos Subida da Colina / hill-climbing
# algoritmo de arrefecimento simulado / Simulated Annealing
# algoritmos genéticos / Genetic Algorithms


# - Escolher um estado aleatoriamente do espaço de estados
# – Considerar todos os vizinhos desse estado
# – Escolher o melhor vizinho
# – Repetir o processo até não existirem vizinhos melhores
# – O estado corrente é a solução


def hill_climbing():
    current = getRandomSolution()
    for i in range(1, MAX_ATTEMPS):
        neighbor = getBestNeighbour(current)
        if value(neighbor) <= value(current):
            return current
        current = neighbor
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


hill_climbing()
