"""The approach taken in this solution is based on a DFS-like search. The worst case running time
   is exponential but because of the optimization used with isPrefix(string) method the average
   running time should be a lot better.
   The solution given below uses create_corresponding_graph(rows, columns) method to create a graph corresponding
   to the grid - 2 dimensional array given. It uses a adjacency list representation of a graph
   (Python dictionary) with an edge between every corresponding two adjacent entries in a given grid.
   Then using both the given grid and a corresponding graph the DFS-like search is performed on a graph
   (using words_search_recursive method) but it searches ALL possible paths from each vertex (corresponding
   to a letter) similar to creating a big search tree with all possible words. Using isPrefix(string) method
   it 'cuts off' early all the branches of the search tree which is being created that cannot form words."""

from Dictionary import Dictionary


def create_corresponding_graph(rows, columns):
    """Method takes two arguments and returns a adjacency list representation of the corresponding grid with given
       number of rows and columns.

        Args:
            rows: integer, number of rows in the grid
            columns: integer, number of columns in the grid

        Returns:
            a dictionary, adjacency list representation of the graph corresponding to the character grid given in
            the problem. A vertex in a graph is an integer tuple which indicates the coordinates of an entry in
            the grid.
    """
    # Using a dictionary data structure for the adjacency list representation of the graph.
    graph = {}
    for i in range(rows):
        for j in range(columns):
            # Add an entry (tuple of coordinates) for each cell in a grid.
            graph[(i, j)] = []

            # Create arrays of possible adjacent entries.
            adjacent_horizontal = [i - 1, i, i + 1]
            adjacent_vertical = [j - 1, j, j + 1]

            # Populate each entry in a graph adjacency list representation.
            for h in adjacent_horizontal:
                for v in adjacent_vertical:
                    # There are eight adjacent cells to each cell in a grid
                    # Apart from edge cases, here we take care of edge cases.
                    if 0 <= h < rows and 0 <= v < columns and not (h == i and v == j):
                        graph[(i, j)] = graph[(i, j)] + [(h, v)]

    # Return an adjacency list representation of a graph corresponding to a grid.
    return graph


def word_search(rows, columns, grid, dictionary):
    """A method performs a word search on a character grid and returns a set of words (no duplicates) that can be formed
       from grid's characters and are in a dictionary. Word search is case insensitive.

        Args:
            rows: an integer, number of rows in a grid
            columns: an integer, number of columns in a grid
            grid: a 2D array of characters, we are searching for words from dictionary in a grid
            dictionary: a Dictionary object, contains the words to search for in a grid

        Returns:
            a set of words, complete list of words that can be formed from grid's characters and are in a dictionary,
            there are no duplicated words in a set.
    """
    # Instantiate a list of words.
    word_list = []

    # Create a graph corresponding to the given grid.
    graph = create_corresponding_graph(rows, columns)

    # For each vertex in a graph perform a search from vertex to find all the words starting with corresponding
    # character in a grid.
    for key in graph:
        words = word_search_recursive(dictionary, grid, graph, key)
        word_list = word_list + words

    # Remove duplicates from the word list.
    word_list = set(word_list)

    # Return a set of words found in a grid and contained in a dictionary.
    return word_list


def word_search_recursive(dictionary, grid, graph, start, prefix="", words=[], path=[]):
    """This method works similar to DFS from vertex on a graph but here it takes ALL paths from the vertex
       to find all the words that can be formed from a grid and are contained in a dictionary.

        Args:
            dictionary: a Dictionary object, contains the words to search for in a grid
            grid: 2D array of characters, we are searching for words from dictionary in a grid
            graph: a adjacency list (using Python dictionary) representation of a graph corresponding
                   to the given grid. Each vertes in a graph is a tuple of coordinates of a cell in a grid
            start: an integer tuple, the vertex we start our search from
            prefix: a string, contains a word 'accumulated' so far, in a recursive call prefix is modify in order
                    to perform a DFS search, we terminate early if isPrefix(string) on a current prefix returns False
            words: a list of strings, list of words that can be formulated from a character grid and are
                   in a dictionary
            path: list of integer tuples (similar to path in DFS search) we keep here an information about the vertices
                  visited so far in a search, it prevents visiting the same cell in a grid twice in a single word search

        Returns:
            a list of strings, list of words that can be form using characters in a grid, stating from start vertex
            (corresponding to some character in a grid) that are in a dictionary.
    """
    # Get coordinates of the starting vertex in a search.
    (i, j) = start

    # Add a corresponding character to the prefix 'accumulated' so far.
    # NOTE: We are case insensitive in this solution
    prefix = prefix + grid[i][j].upper()

    # Add a vertex to a path to prevent using the same grid cell twice in a search for single word.
    path = path + [start]

    # Early terminate - cut off the search tree branch if the prefix so far is not a prefix in a dictionary.
    if not dictionary.isPrefix(prefix):
        return words

    # Add a word to word list if it is a word in a dictionary.
    if dictionary.isWord(prefix):
        words = words + [prefix]

    # Recursive call, DFS-like search but searches ALL paths from a vertex
    for edge in graph[start]:
        if edge not in path:
            words = word_search_recursive(dictionary, grid, graph, edge, prefix, words, path)
    return words

