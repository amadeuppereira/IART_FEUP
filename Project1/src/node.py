class Node:
    def __init__(self, current, path):
        self.current = current
        self.path = path
        self.children = []

    def get_current(self):
        return self.current

    def get_children(self):
        return self.children

    def get_path(self):
    	return self.path

    def add_child(self, child):
        self.children.append(child)