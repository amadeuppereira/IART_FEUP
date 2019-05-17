from input import *
from schedule import *

import random
import math

class Chromosome:

    def __init__(self, gene):
        self.gene = gene

    def mutate(self, probM):
        mutatedG = self.gene

        for i in len(mutatedG):
            if random.uniform(0,1) < probM:
                randomIndex = math.floor(random.uniform(0,1) * range(mutatedG))
                temp = mutatedG[randomIndex]
                #swap
                mutatedG[randomIndex] = mutatedG[i]
                mutatedG[i] = temp

        return Chromosome(mutatedG)

    def getValue(self):
        return value(self.gene)