from block import Block
from logic import heuristic
import time
from tree import Tree

class Game:

    def __init__(self, board, level):
        print("----- LEVEL NOº " + level + " -----")
        self.board = board
        self.generateBlocks()
        self.finished = False
        self.number_moves = 0
        self.start_time = time.time()

    def generateBlocks(self):
        self.blocks = []

        for j in range(len(self.board)):
            for i in range(len(self.board[0])):
                new = Block(i, j, self.board[i][j])
                if new.color != 0:
                    self.blocks.append(new)

        self.update_blocks()
        self.update_blocks()
            
    def update_board(self):
        for j in range(len(self.board)):
            for i in range(len(self.board[0])):
                self.board[i][j] = 0

        for block in self.blocks:
            for [x,y] in block.coords:
                self.board[x][y] = block.color

    def update_blocks(self):
        for block1 in self.blocks:
            for block2 in reversed(self.blocks):
                if block1 != block2:
                    if block1.check_block_adjacent(block2):
                        self.blocks.remove(block2)
                
        if self.is_finished():
            self.finished = True
        
    def is_finished(self):
        colors = []
        for block in self.blocks:
            if block.color in colors:
                return False
            else:
                colors.append(block.color)
        print("Finished with " + str(self.number_moves) + " moves")
        elapsed_time = time.time() - self.start_time
        print("You took " + str("{0:.2f}".format(elapsed_time)) + " seconds")
        return True

    def is_possible_up(self, block):
        for [x,y] in block.coords:
            x = x - 1
            if x < 0 or (self.board[x][y] != 0 and self.board[x][y] != block.color):
                return False
        return True

    def is_possible_down(self, block):
        for [x,y] in block.coords:
            x = x + 1
            if x > 3 or (self.board[x][y] != 0 and self.board[x][y] != block.color):
                return False
        return True

    def is_possible_left(self, block):
        for [x,y] in block.coords:
            y = y - 1
            if y < 0 or (self.board[x][y] != 0 and self.board[x][y] != block.color):
                return False
        return True

    def is_possible_right(self, block):
        for [x,y] in block.coords:
            y = y + 1
            if y > 3 or (self.board[x][y] != 0 and self.board[x][y] != block.color):
                return False
        return True

    def get_block(self, x, y):
        for block in self.blocks:
            for [x1,y1] in block.coords:
                if x1==x and y1==y:
                    return block

        return False
                
    def move(self, block, move):
        if move == "up" and self.is_possible_up(block):
                self.number_moves = self.number_moves + 1
                block.up()
                self.update_board()
                self.update_blocks()
                return True
        elif move == "down" and self.is_possible_down(block):
                self.number_moves = self.number_moves + 1
                block.down()
                self.update_board()
                self.update_blocks()
                return True
        elif move == "left" and self.is_possible_left(block):
                self.number_moves = self.number_moves + 1
                block.left()
                self.update_board()
                self.update_blocks()
                return True
        elif move == "right" and self.is_possible_right(block):
                self.number_moves = self.number_moves + 1
                block.right()
                self.update_board()
                self.update_blocks()
                return True

        return False                