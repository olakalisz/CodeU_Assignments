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

    def get_from_last(self, k):
        """Get kth to the last node of the list - assignment question
        (The idea is to have two pointers, both set to head at the start
        we move the first pointer k times - and thus it has len(list) - k
        elements till the end of the list - and then start moving both pointers
        until the first pointer reaches the end of the list, then return the second pointer)."""
        main_pointer = self.get_head()
        helper_pointer = self.get_head()

        if self.get_head() is None:
            raise IndexError("Empty list!")

        # Move first (helper) pointer k times
        for i in range(k):
            if helper_pointer.get_next_node() is None:
                raise ValueError("k is out of the list range")
            helper_pointer = helper_pointer.get_next_node()

        # Move both pointers until first (helper) pointer reaches the end of the list
        while helper_pointer.get_next_node():
            helper_pointer = helper_pointer.get_next_node()
            main_pointer = main_pointer.get_next_node()

        return main_pointer

    # For testing I only needed the insert_first() function of SinglyLinkedList and I omitted the
    # implementation of the other list functions