from block import Block
import time

class Game:

    def __init__(self, board, level = 1):
        self.board = board
        self.generateBlocks()
        self.finished = False
        self.number_moves = 0
        self.start_time = time.time()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.board == other.board
        else:
            return False

    def __repr__(self):
        return str(self.board)

    def __lt__(self, othe):
        return False

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
        return True

    def is_possible_up(self, block):
        for [x,y] in block.coords:
            x1 = x - 1
            if x1 < 0 or (self.board[x1][y] != 0 and self.board[x1][y] != block.color):
                return False
        return True

    def is_possible_down(self, block):
        for [x,y] in block.coords:
            x1 = x + 1
            if x1 > 3 or (self.board[x1][y] != 0 and self.board[x1][y] != block.color):
                return False
        return True

    def is_possible_left(self, block):
        for [x,y] in block.coords:
            y1 = y - 1
            if y1 < 0 or (self.board[x][y1] != 0 and self.board[x][y1] != block.color):
                return False
        return True

    def is_possible_right(self, block):
        for [x,y] in block.coords:
            y1 = y + 1
            if y1 > 3 or (self.board[x][y1] != 0 and self.board[x][y1] != block.color):
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
                self.update_blocks()
                self.update_board()
                return True
        elif move == "down" and self.is_possible_down(block):
                self.number_moves = self.number_moves + 1
                block.down()
                self.update_blocks()
                self.update_board()
                return True
        elif move == "left" and self.is_possible_left(block):
                self.number_moves = self.number_moves + 1
                block.left()
                self.update_blocks()
                self.update_board()
                return True
        elif move == "right" and self.is_possible_right(block):
                self.number_moves = self.number_moves + 1
                block.right()
                self.update_blocks()
                self.update_board()
                return True

        return False