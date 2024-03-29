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

    #Checks whether the the blocks are adjacent or not, if true joins the coordinates of both blocks
    def check_block_adjacent(self, block):
        if self.color != block.color:
            return False

        for [x,y] in block.coords:
            if [x,y-1] in self.coords or \
               [x,y+1] in self.coords or \
               [x-1,y] in self.coords or \
               [x+1,y] in self.coords:

                self.coords += block.coords

                # remove duplicates
                seen = set()
                newlist = []
                for coord in self.coords:
                    t = tuple(coord)
                    if t not in seen:
                        newlist.append(coord)
                        seen.add(t)
                self.coords = newlist

                return True
            
        return False

    # subtracts 1 to y coordinate
    def up(self):
        for c in self.coords:
            c[0] = c[0] - 1

    # adds 1 to y coordinate
    def down(self):
        for c in self.coords:
            c[0] = c[0] + 1

    # subtracts 1 to x coordinate
    def left(self):
        for c in self.coords:
            c[1] = c[1] - 1

    # adds 1 to x coordinate
    def right(self):
        for c in self.coords:
            c[1] = c[1] + 1