import os
from logic import hill_climbing_1, hill_climbing_2, simulated_annealing, genetic_algorithm


def start():
    print("-------------------------------")
    print("-    Timetabling Generator    -")
    print("-------------------------------")

    print("\n-> Select algorithm:")
    print("1. Hill-Climbing Basic")
    print("2. Hill-Climbing Steepest ascent")
    print("3. Simulated Annealing")
    print("4. Genetic Algorithm")
    print("\nInsert option: ", end='')
    option = int(input())

    if option == 1:
        result = hill_climbing_1()
    elif option == 2:
        result = hill_climbing_2()
    elif option == 3:
        result = simulated_annealing()
    elif option == 4:
        result = genetic_algorithm()
    else:
        print("Wrong option!")
        return

    result.writeToFile()


start()
