"""Tests for question 1 - word search."""

import unittest

import Q1


class Q1Test(unittest.TestCase):
    def setUp(self):
        # Creating test grid - 2 dimensional array examples
        self._empty_grid = [[]]
        self._given_grid = [['A', 'A', 'R'], ['T', 'C', 'D']]
        self._test_grid_1 = [['l', 'o'], ['y', 'd']]
        self._test_grid_2 = [['v', 'e', 'r', 'y'], ['r', 'o', 'o', 'l'], ['d', 'w', 'g', 'n']]

        # Creating dictionary examples, using dummy implementation of Dictionary class
        self._empty_dictionary = Q1.Dictionary([], [])
        self._given_dictionary = Q1.Dictionary(["CAR", "CARD", "CART", "CAT"],
                                               ["C", "CA", "CAR", "CARD", "CART", "CAT"])
        self._test_dictionary_1 = Q1.Dictionary(["LODY", "ldyo", "oydl"],
                                                ["l", "lo", "lod", "lody", "ld", "ldy", "ldyo", "o", "oy", "oyd",
                                                 "oydl"])
        self._test_dictionary_2 = Q1.Dictionary(["verylongword", "wool", "vow", "wrong"],
                                                ["v", "ve", "ver", "very", "veryl", "verylo", "verylon",
                                                 "verylong", "verylongw", "verylongwo", "verylongwor",
                                                 "verylongword", "vo", "vow",
                                                 "w", "wo", "woo", "wool", "wr", "wro", "wron", "wrong"])

    def testEmptyCases(self):
        """Tests all cases where at least one of the arguments is empty."""
        self.assertEqual(set(), Q1.word_search(0, 0, self._empty_grid, self._empty_dictionary))
        self.assertEqual(set(), Q1.word_search(0, 0, self._empty_grid, self._test_dictionary_1))
        self.assertEqual(set(), Q1.word_search(2, 2, self._test_grid_1, self._empty_dictionary))

    def testKnownCases(self):
        """Tests some known cases."""
        # Test the given example
        self.assertEqual({"CAR", "CARD", "CAT"}, Q1.word_search(2, 3, self._given_grid, self._given_dictionary))

        # Check if the insensitivity works and if two words starting from the same letter are find with different word
        self.assertEqual({"LODY", "LDYO", "OYDL"}, Q1.word_search(2, 2, self._test_grid_1, self._test_dictionary_1))

        # Check if the word formed from all letters in a grid is found
        self.assertEqual({"VERYLONGWORD", "WOOL", "VOW"},
                         Q1.word_search(3, 4, self._test_grid_2, self._test_dictionary_2))


if __name__ == '__main__':
    unittest.main()
