from Assignment1_q2_Node import *

# My implementation of Singly Linked List
class SinglyLinkedList(object):

    def __init__(self, head = None):
        self.head = head

    # Inserting elements to the front of the list
    def insert_first(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    # Get kth to the last element of the list - assignment question
    # (The idea is to have two pointers, both set to head at the start
    # we move the first pointer k times - and thus it has len(list) - k
    # elements till the end of the list - and then start moving both pointers
    # until the first pointer reaches the end of the list, then return the second pointer)
    def get_from_last(self, k):
        main_pointer = self.head
        helper_pointer = self.head

        if self.head is None:
            raise ValueError("Empty list!")

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


# Testing
s = SinglyLinkedList()
s.insert_first(1)
s.insert_first(2)
s.insert_first(3)
s.insert_first(4)
print s.get_from_last(1).get_data() # returns 2
# print s.get_from_last(4).get_data() # error, k out of range

# Empty list error expected
p = SinglyLinkedList()
print p.get_from_last(0).get_data()


