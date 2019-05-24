from allocation import Allocation, generateRandomAllocation, getRandomNeighbour, getBestNeighbour
from population import Population
import math
import random

MAX_ATTEMPS = 10000

def hill_climbing():
    print("Hill Climbing\n")
    current = generateRandomAllocation()
    while(1):
        current_value = current.value()
        neighbour, neighbour_value = getBestNeighbour(current)
        print("Current: ", current_value)
        print("Neighbour: ", neighbour_value)
        if neighbour_value >= current_value:
            return current
        current = neighbour

def simulated_annealing():
    print("Simulated Annealing\n")
    current = generateRandomAllocation()
    T = 30
    for i in range(1, MAX_ATTEMPS):
        if T < 0:
            return current
        neighbour, neighbour_value = getRandomNeighbour(current)
        current_value = current.value()
        diff = neighbour_value - current_value
        probability = math.exp(-diff/T)
        print("Current Value", current_value, "----- Temperature", T, "----- Probability", probability)
        if diff < 0:
            current = neighbour
        elif probability > random.uniform(0, 1):
            current = neighbour
        T = T - ((1/math.log(1+i))*0.1)
    return current

# result = hill_climbing()
# result = simulated_annealing()
# result.writeToFile()

SIZE = 50
MUTATION_RATE = 0.1
ELITISM = 5

def genetic_algorithm():
    population = Population(SIZE, generateRandomAllocation(), MUTATION_RATE, ELITISM)
    for p in population:
        print(p.value())
    
    print(population.currentValues)

genetic_algorithm()