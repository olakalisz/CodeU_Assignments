# coding=utf-8
"""The approach taken in this solution is based on a DFS-like search. The worst case running time
   is θ((NXM)^2) (where N is the number of rows and M number of columns in the given gird)but because of the optimization
   used with isPrefix(string) method the average running time should be a lot better.
   The solution given below performs the DFS-like search on the given grid (using words_search_recursive method)
   but it searches ALL possible paths from each entry in a grid (corresponding to a letter).
   This is similar to creating a big search tree with all possible words. Using isPrefix(string) method
   it 'cuts off' early all the branches of the search tree which is being created that cannot form words."""

from Dictionary import Dictionary

# An array to keep track of adjacent entries in a grid.
_ADJACENT_DELTAS = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def is_not_visited(i, j, rows, columns, visited):
    """A method checks if an entry with coordinates (i,j) is contained in a grid and whether it is not yet visited.

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
            a set of strings (all uppercase), complete set of words that can be formed from grid's characters and
            are in a dictionary, there are no duplicated words in a set.
    """
    # Calculate the number of rows and columns in a grid.
    rows = len(grid)
    columns = len(grid[0])

    # Instantiate a set of words.
    found_words = set()

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
            word_search_recursive(dictionary, grid, visited, start, found_words)

    # Return a set of words found in a grid and contained in a dictionary.
    return set(found_words)


def word_search_recursive(dictionary, grid, visited, start, found_words, prefix=""):
    """This method works similar to DFS from vertex on a graph but here our grid is a 'graph', 'vertices' are the grid
       entries and 'edges' are between every two adjacent grid entries. The search checks ALL paths from the 'start
       vertex' to find all the words that can be formed from a grid and are contained in a dictionary.

        Args:
            dictionary: a Dictionary object, contains the words to search for in a grid
            grid: 2D array of characters, we are searching for words from dictionary in a grid
            visited: 2D boolean array, its size is corresponding to the grid, if the grid entry has been already
                     visited by the search the corresponding 'visited entry' is set to True and otherwise it is set to
                     False
            start: a pair of integers, the entry ('vertex') we start our search from
            found_words: a set of strings, at the start found_words contains all the words that have been found
                         so far in a grid, the method adds to found_words any words it finds in search
            prefix: a string, contains a word 'accumulated' so far, in a recursive call prefix is modify in order
                    to perform a DFS search, we terminate early if isPrefix(string) on a current prefix returns False
    """
    # Get coordinates of the starting entry in a search.
    (i, j) = start

    # Add a corresponding character to the prefix 'accumulated' so far.
    prefix = prefix + grid[i][j]

    # Indicate that the entry has been visited by search.
    visited[i][j] = True

    # Add a word to word list if it is a word in a dictionary. Do not allow duplicates in a list of words.
    # Make each word uppercase fo consistency.
    if dictionary.isWord(prefix) and prefix not in found_words:
        found_words.add(prefix.upper())

    # Early terminate - cut off the search tree branch if the prefix so far is not a prefix in a dictionary.
    if dictionary.isPrefix(prefix):

        # Get rows and columns of a grid.
        rows = len(grid)
        columns = len(grid[0])

        # Recursive call, DFS-like search but searches ALL paths from an entry
        # Iterating through the two arrays above and using 'is_not_visited' method all
        # adjacent entries are found.
        for (row_delta, column_delta) in _ADJACENT_DELTAS:
            adjacent = (i + row_delta, j + column_delta)
            if is_not_visited(adjacent[0], adjacent[1], rows, columns, visited):
                word_search_recursive(dictionary, grid, visited, adjacent, found_words, prefix=prefix)

    # When a single search is finished reset an visited entry back to False.
    visited[i][j] = False
