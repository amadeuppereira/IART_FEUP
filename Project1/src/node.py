class Node:
    def __init__(self, game, path = []):
        self.game = game
        self.path = path

    # def get_current(self):
    #     return self.game

    # def get_path(self):
    # 	return self.path

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.game == other.game
        else:
            return False