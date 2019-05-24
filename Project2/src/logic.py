from allocation import Allocation, generateRandomAllocation, getRandomNeighbour, getBestNeighbour, getBetterNeighbour
from population import Population
import math
import random

MAX_ATTEMPS = 10000


def hill_climbing_1():
    print("Hill Climbing\n")
    current = generateRandomAllocation()
    current_value = current.value()
    while(1):
        neighbour, neighbour_value = getBetterNeighbour(current)
        print("Current: ", current_value, "Neighbour: ", neighbour_value, end='\r')
        if neighbour_value >= current_value:
            return current
        current = neighbour
        current_value = neighbour_value


def hill_climbing_2():
    print("Hill Climbing\n")
    current = generateRandomAllocation()
    current_value = current.value()
    while(1):
        neighbour, neighbour_value = getBestNeighbour(current)
        print("Current: ", current_value, "Neighbour: ", neighbour_value, end='\r')
        if neighbour_value >= current_value:
            return current
        current = neighbour
        current_value = neighbour_value


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
        print("Current Value", current_value, "----- Temperature", T, "----- Probability", probability, end='\r')
        if diff < 0:
            current = neighbour
        elif probability > random.uniform(0, 1):
            current = neighbour
        T = T - ((1/math.log(1+i))*0.1)
    return current


SIZE = 20
MUTATION_RATE = 0.1
ELITISM = 5


def genetic_algorithm():
    population = Population(
        SIZE, generateRandomAllocation(), MUTATION_RATE, ELITISM)
    for i in range(20):
        print("\t{}/{}".format(i, 20), end='\r')
        population.nextGeneration()

    return population.currentGroup[0][0]
