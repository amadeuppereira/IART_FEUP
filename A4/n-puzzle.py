# Breadth-first search

import copy

initialState = [[1,3,6],[5,2,0],[4,7,8]]

objectiveState = [[1,2,3],[4,5,6],[7,8,0]]

def up(puzzle) :
    rowIndex = 0
    columnIndex = 0
    zeroRow = 0
    zeroColumn = 0

    for row in puzzle :
        for element in row :
            if element == 0 :
                zeroRow = rowIndex
                zeroColumn = columnIndex
                break
            columnIndex += 1
        rowIndex += 1
        columnIndex = 0

    newPuzzle = copy.deepcopy(puzzle)
    if zeroRow-1 >= 0 :
        newPuzzle[zeroRow][zeroColumn] = newPuzzle[zeroRow-1][zeroColumn]
        newPuzzle[zeroRow-1][zeroColumn] = 0
        
    return ['up', newPuzzle]

def down(puzzle) :
    rowIndex = 0
    columnIndex = 0
    zeroRow = 0
    zeroColumn = 0

    for row in puzzle :
        for element in row :
            if element == 0 :
                zeroRow = rowIndex
                zeroColumn = columnIndex
                break
            columnIndex += 1
        rowIndex += 1
        columnIndex = 0

    newPuzzle = copy.deepcopy(puzzle)
    if zeroRow+1 < len(puzzle) :
        newPuzzle[zeroRow][zeroColumn] = newPuzzle[zeroRow+1][zeroColumn]
        newPuzzle[zeroRow+1][zeroColumn] = 0
    
    return ['down', newPuzzle]

def left(puzzle) :
    rowIndex = 0
    columnIndex = 0
    zeroRow = 0
    zeroColumn = 0

    for row in puzzle :
        for element in row :
            if element == 0 :
                zeroRow = rowIndex
                zeroColumn = columnIndex
                break
            columnIndex += 1
        rowIndex += 1
        columnIndex = 0

    newPuzzle = copy.deepcopy(puzzle)
    if zeroColumn-1 >= 0 :
        newPuzzle[zeroRow][zeroColumn] = newPuzzle[zeroRow][zeroColumn-1]
        newPuzzle[zeroRow][zeroColumn-1] = 0
    
    return ['left', newPuzzle]

def right(puzzle) :
    rowIndex = 0
    columnIndex = 0
    zeroRow = 0
    zeroColumn = 0

    for row in puzzle :
        for element in row :
            if element == 0 :
                zeroRow = rowIndex
                zeroColumn = columnIndex
                break
            columnIndex += 1
        rowIndex += 1
        columnIndex = 0

    newPuzzle = copy.deepcopy(puzzle)
    if zeroColumn+1 < len(puzzle[0]) :
        newPuzzle[zeroRow][zeroColumn] = newPuzzle[zeroRow][zeroColumn+1]
        newPuzzle[zeroRow][zeroColumn+1] = 0
    
    return ['right', newPuzzle]

def getNewPuzzles(puzzle) :
    newPuzzles = [up(puzzle)]
    newPuzzles.append(down(puzzle))
    newPuzzles.append(left(puzzle))
    newPuzzles.append(right(puzzle))
    return newPuzzles

def loop(puzzles, history) :
    if not puzzles :
        print('No solution found!')
        return -1

    loopPuzzlesList = []
    loopHistory = []
    index = 0
    for puzzle in puzzles :
        newPuzzles = getNewPuzzles(puzzle[len(puzzle)-1])
        for newPuzzle in newPuzzles :
            historyPuzzlesList = puzzle[:]
            historyMoves = history[index][:]
            if newPuzzle[1] == objectiveState :
                print('Solution found:')
                history[index].append(newPuzzle[0])
                # puzzle.append(newPuzzle[1])
                print(history[index])
                # print(puzzle)
                return 1
            if newPuzzle[1] not in historyPuzzlesList :
                historyPuzzlesList.append(newPuzzle[1])
                historyMoves.append(newPuzzle[0])
                loopPuzzlesList.append(historyPuzzlesList)
                loopHistory.append(historyMoves)
        index += 1
    loop(loopPuzzlesList, loopHistory)

def solve() :
    currentState = [[initialState]]
    loop(currentState, [[]])

solve()