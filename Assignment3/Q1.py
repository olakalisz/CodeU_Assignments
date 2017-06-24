# coding=utf-8
"""The approach taken in this solution is based on a DFS-like search. The worst case running time
   is θ((NXM)^2) (where N is the number of rows and M number of columns in the given gird)but because of the optimization
   used with isPrefix(string) method the average running time should be a lot better.
   The solution given below performs the DFS-like search on the given grid (using words_search_recursive method)
   but it searches ALL possible paths from each entry in a grid (corresponding to a letter).
   This is similar to creating a big search tree with all possible words. Using isPrefix(string) method
   it 'cuts off' early all the branches of the search tree which is being created that cannot form words."""

from Dictionary import Dictionary


def is_not_visited(i, j, rows, columns, visited):
    """A method checks if an entry with coordinates (i,j) is contained in a grid and weather it is still not visited.

        Args:
            i: an integer, first coordinate of an entry
            j: an integer, second coordinate of an entry
            rows: an integer, number of rows in a grid
            columns: an integer, number of columns in a grid
            visited: 2d boolean array, indicates which entries in a grid has already been visited (they are set to True)

        Returns:
            a boolean, True if an entry is in a grid and has not been visited yet, False otherwise."""
    return 0 <= i < rows and 0 <= j < columns and not visited[i][j]


def word_search(grid, dictionary):
    """A method performs a word search on a character grid and returns a list of words (no duplicates) that can
       be formed from grid's characters and are in a dictionary. Word search is case insensitive.

        Args:
            grid: a 2D array of characters, we are searching for words from dictionary in a grid
            dictionary: a Dictionary object, contains the words to search for in a grid

        Returns:
            a list of words (all uppercase), complete list of words that can be formed from grid's characters and
            are in a dictionary, there are no duplicated words in a list.
    """
    # Calculate the number of rows and columns in a grid.
    rows = len(grid)
    columns = len(grid[0])

    # Instantiate a list of words.
    word_list = []

    # For each entry in a grid perform a search from this grid entry to find all the words starting with the
    # corresponding character in a grid.
    for row in range(rows):
        for column in range(columns):
            # Instantiate 2d boolean array visited, with all entries set to False. It keeps track of visited entries,
            # which will be set to True. (Size of the visited array is corresponding to the size of the grid).
            visited = [[False for i in range(columns)] for j in range(rows)]

            # Instantiate a pair of integers corresponding to coordinates of the grid entry from which the search
            # will be performed.
            start = (row, column)

            # Call a recursive-DFS-like function from the entry
            word_search_recursive(dictionary, grid, visited, start, word_list)

    # For consistency we always return uppercase words (makes testing easier)
    for i in range(len(word_list)):
        word_list[i] = word_list[i].upper()

    # Return a set of words found in a grid and contained in a dictionary.
    return word_list


def word_search_recursive(dictionary, grid, visited, start, word_list, prefix=""):
    """This method works similar to DFS from vertex on a graph but here our grid is a 'graph', 'vertices' are the grid
       entries and 'edges' are between every two adjacent grid entries. The search checks ALL paths from the 'vertex'
       to find all the words that can be formed from a grid and are contained in a dictionary.

        Args:
            dictionary: a Dictionary object, contains the words to search for in a grid
            grid: 2D array of characters, we are searching for words from dictionary in a grid
            visited: 2D boolean array, its size is corresponding to the grid, if the grid entry has been already
                     visited by the search the corresponding 'visited entry' is set to True and otherwise it is set to
                     False
            start: a pair of integers, the entry ('vertex') we start our search from
            word_list: a list of strings, list of words that can be formulated from a character grid and are
                       in a dictionary
            prefix: a string, contains a word 'accumulated' so far, in a recursive call prefix is modify in order
                    to perform a DFS search, we terminate early if isPrefix(string) on a current prefix returns False

        Returns:
            it is a void function, no value is returned but the function modifies its word_list argument which
            accumulates the words found in a grid.
    """
    # Get coordinates of the starting entry in a search.
    (i, j) = start

    # Add a corresponding character to the prefix 'accumulated' so far.
    prefix = prefix + grid[i][j]

    # Indicate that the entry has been visited by search.
    visited[i][j] = True

    # Early terminate - cut off the search tree branch if the prefix so far is not a prefix in a dictionary.
    if dictionary.isPrefix(prefix):
        # Add a word to word list if it is a word in a dictionary.
        if dictionary.isWord(prefix):
            # Do not allow duplicates in a list of words.
            if prefix not in word_list:
                word_list += [prefix]

        # Get rows and columns of a grid.
        rows = len(grid)
        columns = len(grid[0])

        # Two arrays to keep track of adjacent entries.
        rows_adjacent = [-1, -1, -1, 0, 0, 1, 1, 1]
        columns_adjacent = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Recursive call, DFS-like search but searches ALL paths from an entry
        # Iterating through the two arrays above and using 'is_not_visited' method all
        # adjacent entries are found.
        for k in range(8):
            adjacent = (i+rows_adjacent[k], j+columns_adjacent[k])
            if is_not_visited(adjacent[0], adjacent[1], rows, columns, visited):
                word_search_recursive(dictionary, grid, visited, adjacent, word_list, prefix)

    # When a single search is finished reset an visited entry back to False.
    visited[i][j] = False
