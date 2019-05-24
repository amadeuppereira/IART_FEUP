from input import *
from helper import *
from allocation import *
from input import *

import random
import math

class Chromosome:

    def __init__(self, gene):
        self.gene = gene
    
    def mutate(self, probM):
        new_gene = self.gene
        #TODO : transformation 
        return new_gene

        
    
    def fitness(self):
        return # 1 / value(self.gene)


