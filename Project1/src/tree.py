from node import Node

class Tree:

    def __init__(self):
        self.nodes = {}

    def get_nodes(self):
        return self.nodes

    def add_node(self, new_node_identifier, parent=None):
        new_node = Node(new_node_identifier)
        self[new_node_identifier] = new_node

        if parent is not None:
            self[parent].add_child(new_node_identifier)

        return new_node

    def __getitem__(self, key):
        return self.nodes[key]

    def __setitem__(self, key, item):
        self.nodes[key] = item

# TODO: tree
# tree = Tree()
# tree.add_node(root)  # root node
# # tree.add_node(new_child, parent)