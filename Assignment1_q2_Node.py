# Node is a unit which is used in my implementation of Singly Linked List
class Node(object):

    def __init__(self, data = None, next_node = None):
        # Node is storing some data and a pointer to the next node
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node