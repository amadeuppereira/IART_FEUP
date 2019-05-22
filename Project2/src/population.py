from input import * 
from chromosome import *
from schedule import *

import random
import math
import operator
#fisher yates shuffle algorithm

def shuffle(sequence, swapFunc):
    index = len(sequence)
    while index != 0:
        index -= 1
        swapFunc(sequence, index)
    return sequence

def fisherYatesSwap(sequence, index):
    rand = math.floor(random.uniform(0,1) * (index + 1))
    tmp = sequence[index]
    sequence[index] = sequence[rand]
    sequence[rand] = tmp

def rotateFromIndex(array, index):
    return array[index+1:] + array[:index+1]

class Poputalion: 
 
    def __init__(self, size, seed, probC, probM): 
        self.probC = probC 
        self.probM = probM 
        self.currentGroup = self.generate(size, seed)
        self.currentValues = list(map(lambda x: x.fitness(), self.currentGroup))

    def generate(self, size, seed):
        ret = [Chromosome(shuffle(seed, fisherYatesSwap)) for x in range(size)]
        return ret

    def getFittest(self):
        index, value = max(enumerate(self.currentValues), key=operator.itemgetter(1))
        return self.currentGroup[index]

    def crossover(self, mom, dad):
        cut_mom = random.randint(1, len(mom.gene)-1)
        cut_dad = random.randint(1, len(dad.gene)-1)

        start = min(cut_mom, cut_dad)
        end = max(cut_mom, cut_dad)

        child1part1 = mom.gene[0:start]
        child1part2 = mom.gene[end+1:]

        child2part1 = dad.gene[0:start]
        child2part2 = dad.gene[end+1:]

        child1 = child1part1 + dad.gene[start:end+1] + child1part2
        child2 = child2part1 + mom.gene[start:end+1] + child2part2


        return [Chromosome(child1),Chromosome(child2)]

p = Poputalion(1, getRandomSolution() , 0.3, 0.4)
g = Chromosome(getRandomSolution())
g1 = Chromosome(getRandomSolution())
children = p.crossover(g,g1)

print(isSolutionFeasible(children[0].gene))
print(isSolutionFeasible(children[1].gene))

print('parents:')
print(g.fitness())
print(g1.fitness())