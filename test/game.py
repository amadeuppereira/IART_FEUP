from block import Block

class Game:

    def __init__(self, board):
        self.board = board
        self.generateBlocks()
        self.finished = False

    def generateBlocks(self):
        self.blocks = []

        for j in range(len(self.board)):
            for i in range(len(self.board[0])):
                new = Block(i, j, self.board[i][j])
                if new.color == 0:
                    continue
                    
                flag = False
                for block in self.blocks:
                    if block.check_block_adjacent(new):
                        flag = True

                if not flag:
                    self.blocks.append(new)
            
    def update_board(self):
        for j in range(len(self.board)):
            for i in range(len(self.board[0])):
                self.board[i][j] = 0

        for block in self.blocks:
            for [x,y] in block.coords:
                self.board[x][y] = block.color

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

    def update_blocks(self):
        for block1 in reversed(self.blocks):
            for block2 in reversed(self.blocks):
                if block1 != block2:
                    if block1.check_block_adjacent(block2):
                        self.blocks.remove(block2)
                
        if self.is_finished():
            self.finished = True
                    
    def move(self, block, move):
        if move == "up" and self.is_possible_up(block):
                block.up()
                self.update_board()
                self.update_blocks()
                return True
        elif move == "down" and self.is_possible_down(block):
                block.down()
                self.update_board()
                self.update_blocks()
                return True
        elif move == "left" and self.is_possible_left(block):
                block.left()
                self.update_board()
                self.update_blocks()
                return True
        elif move == "right" and self.is_possible_right(block):
                block.right()
                self.update_board()
                self.update_blocks()
                return True

        return False