class Node(object):
    """Node is a unit which is used in my implementation of Singly Linked List."""
    def __init__(self, data = None, next_node = None):
        # Node is storing some data and a pointer to the next node
        self.__data = data
        self.__next_node = next_node

    def get_data(self):
        return self.__data

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, node):
        self.__next_node = node


class SinglyLinkedList(object):
    """My implementation of Singly Linked List."""

    def __init__(self, head = None):
        self.__head = head

    def get_head(self):
        return self.__head

    def insert_first(self, data):
        """Inserting elements to the front of the list."""
        new_node = Node(data)
        new_node.set_next_node(self.__head)
        self.__head = new_node