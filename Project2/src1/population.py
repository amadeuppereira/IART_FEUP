from input import *
from chromosome import *
from allocation import *
from settings import *

import random
import math
import operator
import numpy as np


class Population:

	def __init__(self, size, seed, probM, elitism):
		self.elitism = elitism
		self.probM = probM
		self.currentGroup = self.generate(size, seed)

	def generate(self, size, seed):
		ret = [getRandomNeighbour(seed) for x in range(size)]
		ret.sort(key = lambda x : x[1])
		return ret

	#using roulette selection
	def select(self):
		p = random.uniform(0, sum(x[1] for x in self.currentGroup))
		for i, a in enumerate(self.currentGroup):
			_, f = a
			if p <= 0:
				break
			p -= f
		return self.currentGroup[i]

	def generateChildren(self):
		mom = self.select()
		dad = self.select()

		children = self.crossover(mom[0], dad[0])

		return children, children.value()

	def crossover(self, mom, dad): 
		unassignedEvents = []
		child = Allocation(TIMESLOTS)
		for e in EVENTS:
    			
			# Mutate
			if random.uniform(0, 1) < self.probM:
				slots = getPossibleSlots(e, child.slots)
				if len(slots) != 0:
					s, rooms = random.choice(slots)
					r = random.choice(rooms)
					child.allocate(s, e.id, r)
					continue


			s1 = None
			s2 = None
			r1 = None
			r2 = None
			is_compatible_mom = False
			is_compatible_dad = False
		
			try:
				s1, r1 = mom.event_data[e.id]
				is_compatible_mom = all(helper.isCompatible(e.id, e1) for e1 in child.slots[s1].distribution.keys())\
					and r1 not in child.slots[s1].distribution.values()
			except KeyError:
				pass

			try:
				s2, r2 = dad.event_data[e.id]
				is_compatible_dad = all(helper.isCompatible(e.id, e1) for e1 in child.slots[s2].distribution.keys())\
					and r2 not in child.slots[s2].distribution.values()
			except KeyError:
				pass
			
			if s1 and s2:
				if random.randint(0, 1) and is_compatible_mom:
					child.allocate(s1, e.id, r1)
				elif is_compatible_dad:
					child.allocate(s2, e.id, r2)
				else:
					unassignedEvents.append(e.id)
			elif not s1 and is_compatible_dad:
				child.allocate(s2, e.id, r2)
			elif not s2 and is_compatible_mom:
				child.allocate(s1, e.id, r1)
			else:
				unassignedEvents.append(e.id)

		for e in unassignedEvents.copy():
			if tryPlaceEvent(e, child.slots):
				unassignedEvents.remove(e)

		return child
				
	def nextGeneration(self):
		nextGeneration = self.currentGroup[:self.elitism]

		while len(nextGeneration) < len(self.currentGroup):
			nextGeneration.append(self.generateChildren())

		nextGeneration.sort(key = lambda x : x[1])
		self.currentGroup = nextGeneration