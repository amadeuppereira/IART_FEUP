from allocation import Allocation, generateRandomAllocation, getRandomNeighbour
import math
import random

MAX_ATTEMPS = 10000

# - Escolher um estado aleatoriamente do espaço de estados
# – Considerar todos os vizinhos desse estado
# – Escolher o melhor vizinho
# – Repetir o processo até não existirem vizinhos melhores
# – O estado corrente é a solução


def hill_climbing():
    print("Hill Climbing\n")
    current = generateRandomAllocation()
    while(1):
        current_value = current.value()
        neighbour, neighbour_value = current.getBestNeighbour()
        print("Current: ", current_value)
        print("Neighbour: ", neighbour_value)
        if neighbour_value >= current_value:
            return current
        current = neighbour


# – Semelhante ao Hill-Climbing Search mas admite explorar vizinhos piores
# – Temperatura que vai sendo sucessivamente reduzida define a probabilidade de aceitar soluções piores

def simulated_annealing():
    print("Simulated Annealing\n")
    current = generateRandomAllocation()
    print(current.value())
    T = 30
    for i in range(1, MAX_ATTEMPS):
        if T < 0:
            return current
        # neighbour, neighbour_value = current.getRandomNeighbour()
        neighbour, neighbour_value = getRandomNeighbour(current)
        current_value = current.value()
        diff = neighbour_value - current_value
        print("Current Value", current_value, "----- Temperature",
              T, "----- Probability", math.exp(-diff/T))
        if diff < 0:
            current = neighbour
        elif math.exp(-diff/T) > random.uniform(0, 1):
            current = neighbour
        T = T - ((1/math.log(1+i))*0.1)
    return current


# result = hill_climbing()
result = simulated_annealing()

result.writeToFile()
