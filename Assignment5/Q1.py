# coding=utf-8
"""The solution presented below takes θ(N+M) runtime where N is the number of characters in dictionary words (sum of
them) and M is the number of dictionary words. There are two main steps performed in the given solution. First is to
create a graph corresponding to the partial (lexicographical) order of characters in dictionary words. Second step
creates a total order of characters (i. e. the lexicographical order or in other words ordered alphabet) which are
stored at first in a singly linked list and then copied to the list of characters, This step uses a topological sort
algorithm."""

import SinglyLinkedList

_WHITE = 0
_GREY = 1
_BLACK = 2


def get_index_of_first_differing_char(word1, word2):
    """The method returns an index of the first character which is different in two given words.

        Args:
            word1: a string, the first word to perform comparison on
            word2: a string, the second word to perform comparison on

        Returns:
            an integer, the index of first character which is different in two words; if the words
            are the same or one word is a prefix of another, it returns -1.
    """
    # Set length to the length of shorter word.
    length = min(len(word1), len(word2))
    index = -1

    # Loop over words, after loop is executed index will point to last character that is the same in two words.
    for i in range(length):
        if word1[i] != word2[i]:
            index = i
            break

    return index


def create_corresponding_partial_order(dictionary):
    """Computes a partial order from a list of sorted words.

       The partial order of character returned by this function is determined based on the order of words in the given
       dictionary.

       To represent the partial order, we use graph, where nodes are characters and where a directed edge from a node
       (a character) to another signifies that the first should come before the second one in the alphabet.

        Args:
            dictionary: an array of strings, list of language words in lexicographical order, the character partial
                        ordering is created based on it

        Returns:
            graph: a dictionary of sets, corresponds to graph data structure, where characters from dictionary are
                   'vertices' and 'edges' indicate characters' partial ordering.
    """
    graph = {}

    # Instantiate the graph data structure.
    for word in dictionary:
        for char in word:
            if char not in graph:
                graph[char] = set()

    # Set the orderings of characters based on the order of words in given dictionary.
    # (NOTE: it is enough to compare only adjacent words).
    for i in range(len(dictionary) - 1):
        adjacent_word1 = dictionary[i]
        adjacent_word2 = dictionary[i + 1]
        index = get_index_of_first_differing_char(adjacent_word1, adjacent_word2)
        if index != -1:
            graph[adjacent_word1[index]].add(adjacent_word2[index])

    return graph


def initialize_state_dictionary(dictionary) :
    """This method initializes the state of each character (graph vertex) to "white".

       There are only three states: "white", "grey" and "black".

        Args:
            dictionary: an array of strings, list of language words in lexicographical order

        Returns:
            a dictionary with character keys and integer values corresponding to colours initialized to _WHITE.
            Colour of state means accordingly:
            _WHITE - the character ("vertex") has not been visited by the search yet
            _GREY - the character ("vertex") is being visited, recursive call on it is not finished yet
            _BLACK - the character ("vertex") has already been visited
       """
    state = {}

    # Instantiate states to _WHITE for all characters.
    for word in dictionary:
        for char in word:
            if char not in state:
                state[char] = _WHITE

    return state


def find_total_order_from_char(partial_order, state, char, total_order):
    """This method is the recursive part of topological sort (Similar to DFS from vertex).

        Args:
            partial_order: a dictionary of sets, graph data structure corresponding to characters partial order
            state: a dictionary of character keys and integer values, where integers indicate state of the
                   character ("vertex")
            char: a character, from which the search is performed
            total_order: a singly linked list of characters, the total order (lexicographical order) "accumulated
                         so far" the new character is always added at the front of the list.
    """
    # The character is in search now.
    state[char] = _GREY

    # Check all characters that are "next" in the partial ordering.
    for following_char in partial_order[char]:
        # Perform a search from this character if it has not been visited yet.
        if state[following_char] == _WHITE:
            find_total_order_from_char(partial_order, state, following_char, total_order)
        # If any searched characters are found here, we found a cycle in the order, i.e. it is not a correct ordering.
        elif state[following_char] == _GREY:
            raise ValueError("The given dictionary is not sorted in lexicographical order!")

    # The search from this character is finished.
    state[char] = _BLACK

    # Update the total order (alphabet).
    total_order.insert_first(char)


def find_ordered_alphabet(dictionary):
    """This method finds one of the possible lexicographic orders of dictionary characters given an ordered dictionary
       words.

        Args:
            dictionary: an array of strings, list of language words in lexicographical order

        Returns:
            a list of characters, one the the possible lexicographical orderings of dictionary characters.

        Throws:
            ValueError: if the passed dictionary is empty or the word order in it is not valid.
    """
    # Empty dictionary.
    if len(dictionary) == 0:
        raise ValueError("The given dictionary is empty!")

    # Create the partial ordering of dictionary characters.
    partial_order = create_corresponding_partial_order(dictionary)

    # Instantiate states to _WHITE for all characters
    state = initialize_state_dictionary(dictionary)

    # Initialize the singly linked list. It will contain the total order of characters "accumulated so far".
    total_order = SinglyLinkedList.SinglyLinkedList()

    # Perform a topological sort.
    for char in partial_order:
        if state[char] == _WHITE:
            find_total_order_from_char(partial_order, state, char, total_order)

    # Copy values from singly linked list to array of characters in order.
    ordered_alphabet = []
    current_char_node = total_order.get_head()
    while current_char_node is not None:
        ordered_alphabet.append(current_char_node.get_data())
        current_char_node = current_char_node.get_next_node()

    return ordered_alphabet
