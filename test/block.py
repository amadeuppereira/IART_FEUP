class Block:

    def __init__(self, x, y):
        self.coords = []
        self.coords.append([x,y])

    def __repr__(self):
        return str(self.coords)

    def add_piece(self, x, y):
        for [x1, y1] in self.coords:
            if (abs(x1 - x) == 1 and y1 - y == 0) \
                or (x1 - x == 0 and abs(y1 - y) == 1):

                self.coords.append([x,y])
                return True
            
        return False