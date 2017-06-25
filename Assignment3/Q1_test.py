"""Tests for question 1 - word search."""

import unittest

import Q1


def _grid(string):
    """Creates a 2D array of characters from a string.
       The string represents the grid by having the characters in each row separated by a '|'.

        Args:
            string: a string, representation of the grid as a single string.

        Returns:
            a 2-D array of characters corresponding to the grid given.
    """
    grid = []
    for row in string.split('|'):
        grid.append([ch for ch in row])
        # Make sure each row has the same length.
        if len(grid[0]) != len(grid[-1]):
            raise ValueError("not all rows have the same length")
    return grid


def _dictionary(words):
    """Create a dictionary with the given words.

        Args:
            words: a list of strings, the words to be added to the dictionary.

        Returns:
            an instance of Q1.Dictionary containing the given words.
    """
    return Q1.Dictionary(words)


class Q1Test(unittest.TestCase):
    def testEmptyCases(self):
        """Tests all cases where at least one of the arguments is empty."""
        self.assertEqual(set(), Q1.word_search(_grid(""), _dictionary([])))
        self.assertEqual(set(), Q1.word_search(_grid(""), _dictionary(["LODY", "ldyo", "oydl"])))
        self.assertEqual(set(), Q1.word_search(_grid("lo|yd"), _dictionary([])))

    def testKnownCases(self):
        """Tests some known cases."""
        # Test the given example
        self.assertEqual({"CAR", "CARD", "CAT"},
                         Q1.word_search(_grid("AAR|TCD"), _dictionary(["CAR", "CARD", "CART", "CAT"])))

        # Check if the insensitivity works and if two words starting from the same letter are find with different word
        self.assertEqual({"LODY", "LDYO", "OYDL"},
                         Q1.word_search(_grid("lo|yd"), _dictionary(["LODY", "ldyo", "oydl"])))

        # Check if the word formed from all letters in a grid is found
        self.assertEqual({"VERYLONGWORD", "WOOL", "VOW"},
                         Q1.word_search(_grid("very|rool|dwgn"), _dictionary(["verylongword", "wool", "vow", "wrong"])))

        # Test for duplicates with different combinations of upper-case lower-case characters.
        self.assertEqual({"CAR", "CARD", "CAT"},
                         Q1.word_search(_grid("AaR|TcD"), _dictionary(["CAR", "CARD", "CART", "CAT", "caT"])))


if __name__ == '__main__':
    unittest.main()
