from input import * 
import random
import math

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



class Poputalion: 
 
    def __init__(self, size, probC, probM): 
        self.probC = probC 
        self.probM = probM 

    


print(shuffle([1,2,3,4], fisherYatesSwap))

    

