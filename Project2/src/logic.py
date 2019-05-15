import math
import random

MAX_ATTEMPS = 100000

# algoritmos Subida da Colina / hill-climbing
# algoritmo de arrefecimento simulado / Simulated Annealing
# algoritmos genéticos / Genetic Algorithms

# TODO:
# Gets random solution for timetable
def getRandomNode() :
    print("Get random node")
    node = "idk"
    return node

# TODO:
# Gets the best neighbor from current node
def getBestNeighbor(current) :
    print("Best neighbor")
    node = "idk"
    return node

# TODO:
# Gets a random neighbor from current node
def getRandomNeighbor(current) :
    print("Random neighbor")
    node = "idk"
    return node

# TODO:
# Evaluates numerically a node
def value(node) :
    print("Evaluate node")
    ret = 0
    return ret

# - Escolher um estado aleatoriamente do espaço de estados 
# – Considerar todos os vizinhos desse estado 
# – Escolher o melhor vizinho 
# – Repetir o processo até não existirem vizinhos melhores 
# – O estado corrente é a solução
def hill_climbing() :
    current = getRandomNode()
    for i in range (1, MAX_ATTEMPS) :
        neighbor = getBestNeighbor(current)
        if value(neighbor) <= value(current) :
            return current
        current = neighbor
    return current

# – Semelhante ao Hill-Climbing Search mas admite explorar vizinhos piores 
# – Temperatura que vai sendo sucessivamente reduzida define a probabilidade de aceitar soluções piores
def simulated_annealing() :
    current = getRandomNode()
    T = 100
    for i in range (1, MAX_ATTEMPS) :
        if T < 0 : return current
        next = getRandomNeighbor(current)
        ap = math.exp((value(next)-value(current))/T)
        if ap > random.uniform(0, 1) :
            current = next
        T = T - (1/math.log(1+i))
    return current

simulated_annealing()
