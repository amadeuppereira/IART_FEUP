from block import Block

class Board:

    def __init__(self, board):
        self.board = board
        self.generateBlocks()

    def generateBlocks(self):

        self.blocks = {}

        for j in range(len(self.board)):
            for i in range(len(self.board[0])):
                color = self.board[i][j]
                if color == 0:
                    continue
                if color not in self.blocks:
                    self.blocks[color] = []
                    
                flag = False
                for block in self.blocks[color]:
                    if block.add_piece(i, j):
                        flag = True

                if not flag:
                    self.blocks[color].append(Block(i, j))

        print(self.blocks)
    


Board([[1,1,1,1],
       [2,2,2,2],
       [3,3,3,3],
       [4,4,4,4]])