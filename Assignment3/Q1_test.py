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
        self._empty_dictionary = Q1.Dictionary([])
        self._given_dictionary = Q1.Dictionary(["CAR", "CARD", "CART", "CAT"])
        self._test_dictionary_1 = Q1.Dictionary(["LODY", "ldyo", "oydl"])
        self._test_dictionary_2 = Q1.Dictionary(["verylongword", "wool", "vow", "wrong"])

        # Creating lists of desired outputs:
        self._given_desired_output = ["CAR", "CARD", "CAT"]
        self._test_desired_output_1 = ["LODY", "LDYO", "OYDL"]
        self._test_desired_output_2 = ["VERYLONGWORD", "WOOL", "VOW"]

    def testEmptyCases(self):
        """Tests all cases where at least one of the arguments is empty."""
        self.assertEqual([], Q1.word_search(self._empty_grid, self._empty_dictionary))
        self.assertEqual([], Q1.word_search(self._empty_grid, self._test_dictionary_1))
        self.assertEqual([], Q1.word_search(self._test_grid_1, self._empty_dictionary))

    def testKnownCases(self):
        """Tests some known cases."""
        # Test the given example
        for word in self._given_desired_output:
            self.assertTrue(word in Q1.word_search(self._given_grid, self._given_dictionary))

        # Check if the insensitivity works and if two words starting from the same letter are find with different word
        for word in self._test_desired_output_1:
            self.assertTrue(word in Q1.word_search(self._test_grid_1, self._test_dictionary_1))

        # Check if the word formed from all letters in a grid is found
        for word in self._test_desired_output_2:
            self.assertTrue(word in Q1.word_search(self._test_grid_2, self._test_dictionary_2))


if __name__ == '__main__':
    unittest.main()
