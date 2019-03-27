class Block:

    def __init__(self, x, y, color):
        self.coords = []
        self.coords.append([x,y])
        self.color = color

    def __repr__(self):
        return "{} : {}".format(self.color, str(self.coords))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.coords == other.coords
        else:
            return False

    def check_block_adjacent(self, block):
        if self.color != block.color:
            return False

        for [x,y] in block.coords:
            if [x,y-1] in self.coords or \
               [x,y+1] in self.coords or \
               [x-1,y] in self.coords or \
               [x+1,y] in self.coords:

              self.coords += block.coords
              return True
            
        return False

    def up(self):
        for c in self.coords:
            c[0] = c[0] - 1

    def down(self):
        for c in self.coords:
            c[0] = c[0] + 1

    def left(self):
        for c in self.coords:
            c[1] = c[1] - 1

    def right(self):
        for c in self.coords:
            c[1] = c[1] + 1