from input import *
from chromosome import *
from allocation import *

import random
import math
import operator


class Population:

	def __init__(self, size, seed, probM, elitism):
		self.elitism = elitism
		self.probM = probM
		self.currentGroup = self.generate(size, seed)
		self.currentValues = list(map(lambda x: x.fitness(), self.currentGroup))

	def generate(self, size, seed):
		ret = [getRandomNeighbour(seed) for x in range(size)]
		return ret

	def getFittest(self):
		index, value = max(enumerate(self.currentValues), key=operator.itemgetter(1))
		return self.currentGroup[index]

	def crossover(self, mom, dad):  # TODO : this crossing will not work , just for testing purpose, !!!CHANGE!!!
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

	#using roulette selection
	def select(self):
		p = random.uniform(0, sum(self.currentValues))
		for i, f in enumerate(self.currentValues):
			if p <= 0:
				break
			p -= f
		return self.currentGroup[i]

	def generateChildren(self):
		mom = self.select()
		dad = self.select()

		toCross = True if random.uniform(0,1) < self.probC else False
		if toCross:
			children = self.crossover(mom, dad)
		else:
			children = [mom, dad]

		mutatedChildren = list(map(lambda x: x.mutate(self.probM), children))

		return mutatedChildren

	def improveGeneration(self):
		nextGeneration = []

		while len(nextGeneration) < len(self.currentGroup):
			nextGeneration = nextGeneration + self.generateChildren()

		if len(nextGeneration) > len(self.currentGroup):
			nextGeneration = nextGeneration[:-1]

		self.currentGroup = nextGeneration
		self.currentValues = list(map(lambda x: x.fitness(), nextGeneration))

		return self


