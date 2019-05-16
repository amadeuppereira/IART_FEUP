from input import *
from schedule import *

import random
import math

class Gene:

    def __init__(self, chromosome):
        self.chromosome = chromosome

    def mutate(self, probM):
        mutatedC = self.chromosome

        for i in range(mutatedC):
            if random.uniform(0,1) < probM:
                randomIndex = math.floor(random.uniform(0,1) * range(mutatedC))
                temp = mutatedC[randomIndex]
                #swap
                mutatedC[randomIndex] = mutatedC[i]
                mutatedC[i] = temp

        return Gene(mutatedC)

    def getValue(self):
        return value(self.chromosome)

        