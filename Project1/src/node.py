class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.children = []

    def get_identifier(self):
        return self.identifier

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)