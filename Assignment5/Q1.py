# coding=utf-8
"""The solution presented below takes θ(N+M) runtime where N is the number of characters in dictionary words (sum of
them) and M is the number of dictionary words. There are two main steps performed in the given solution. First is to
create a graph corresponding to the partial (lexicographical) order of characters in dictionary words. Second step
creates a total order of characters (i. e. the lexicographical order or in other words ordered alphabet) which are
stored at first in a singly linked list and then copied to the list of characters, This step uses a topological sort
algorithm."""

import SinglyLinkedList


def get_index_of_first_differing_char(word1, word2):
    """The method returns an index of the first character which is different in two given words.

        Args:
            word1: a string, the first word to perform comparison on
            word2: a string, the second word to perform comparison on

        Returns:
            an integer, the index of first character which is different in two words, if the words
            are the same or the beginning of longer word is the same as the whole shorter word, it
            returns -1.
    """
    # Set length to the length of shorter word.
    length = len(word1) if len(word1) < len(word2) else len(word2)
    index = -1

    # Loop over words, after loop is executed index will point to last character that is the same in two words.
    for i in range(length):
        if word1[i] == word2[i]:
            index += 1
        else:
            break

    # Point index to the first differing character in two words.
    index += 1

    # Reset index to -1 if the words are the same or beginning of longer word is the same as the whole shorter word.
    if index == length:
        index = -1

    return index


def create_corresponding_partial_order(dictionary):
    """The method returns a partial order of characters from dictionary, based on the order of words in a dictionary,
       in the graph form.

        Args:
            dictionary: an array of strings, list of language words in lexicographical order, the character partial
                        ordering is created based on it

        Returns:
            graph: a dictionary of sets, corresponds to graph data structure, where characters from dictionary are
                   'vertices' and 'edges' indicate characters' partial ordering
            state: a dictionary of strings, where each string is either "white", "grey" or "black". It indicates the
                   state that the "vertex" (character) is in while topological search is performed. In this method
                   only initialize state dictionary to all "white".
    """
    graph = {}
    state = {}

    # Instantiate the graph data structure and set state to "white" for all characters/,
    for word in dictionary:
        for char in word:
            if char not in graph:
                graph[char] = set()
                state[char] = "white"

    # Set the orderings of characters based on the order of words in given dictionary.
    # (NOTE: it is enough to compare only adjacent words).
    for i in range(len(dictionary) - 1):
        adjacent_word1 = dictionary[i]
        adjacent_word2 = dictionary[i + 1]
        index = get_index_of_first_differing_char(adjacent_word1, adjacent_word2)
        if index != -1:
            graph[adjacent_word1[index]].add(adjacent_word2[index])

    return graph, state


def find_total_order_from_char(partial_order, state, char, total_order):
    """This method is the recursive part of topological sort (Similar to DFS from vertex).

        Args:
            partial_order: a dictionary of sets, graph data structure corresponding to characters partial order
            state: a dictionary of strings, where strings indicate state of the character ("vertex")
                   white - the character ("vertex") has not been visited by the search yet
                   grey - the character ("vertex") is being visited, recursive call on it is not finished yet
                   black - the character ("vertex") has already been visited
            char: a character, from which the search is performed
            total_order: a singly linked list of characters, the total order (lexicographical order) "accumulated
                         so far" the new character is always added at the front of the list.
    """
    # The character is in search now.
    state[char] = "grey"

    # Check all characters that are "next" in the partial ordering.
    for following_char in partial_order[char]:
        # Perform a search from this character if it has not been visited yet.
        if state[following_char] == "white":
            find_total_order_from_char(partial_order, state, following_char, total_order)
        # If any searched characters are found here, we found a cycle in the order, i.e. it is not a correct ordering.
        elif state[following_char] == "grey":
            raise ValueError("The given dictionary is not sorted in lexicographical order!")
        break

    # The search from this character is finished.
    state[char] = "black"

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
    (partial_order, state) = create_corresponding_partial_order(dictionary)

    # Initialize the singly linked list. It will contain the total order of characters "accumulated so far".
    total_order = SinglyLinkedList.SinglyLinkedList()

    # Perform a topological sort.
    for char in partial_order:
        if state[char] == "white":
            find_total_order_from_char(partial_order, state, char, total_order)

    # Copy values from singly linked list to array of characters in order.
    ordered_alphabet = []
    current_char_node = total_order.get_head()
    while current_char_node is not None:
        ordered_alphabet.append(current_char_node.get_data())
        current_char_node = current_char_node.get_next_node()

    return ordered_alphabet
