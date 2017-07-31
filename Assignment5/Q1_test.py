"""Tests for question 1 - unknown language characters' ordering."""

import unittest

import Q1


class Q1Test(unittest.TestCase):
    def testEmptyCase(self):
        empty_dictionary = []
        with self.assertRaises(ValueError):
            Q1.find_ordered_alphabet(empty_dictionary)

    def testKnownCases(self):
        """Tests some known cases."""
        # Test the given example
        given_dictionary = ["ART", "RAT", "CAT", "CAR"]
        self.assertTrue(Q1.find_ordered_alphabet(given_dictionary) in [['T', 'A', 'R', 'C'], ['A', 'T', 'R', 'C']])
        test_dictionary1 = ["baa", "abcd", "abca", "cab", "cad"]
        self.assertTrue(Q1.find_ordered_alphabet(test_dictionary1) in [['b', 'd', 'a', 'c'], ['d', 'b', 'a', 'c']])
        test_dictionary2 = ["ab", "bd", "c", "d"]
        self.assertEquals(Q1.find_ordered_alphabet(test_dictionary2), ['a', 'b', 'c', 'd'])

    def testWrongOrderCase(self):
        """Tests a case with wrong order of words in a dictionary."""
        # Test the given example
        wrong_dictionary = ["ART", "RAT", "CRT", "CAR"]
        with self.assertRaises(ValueError):
            Q1.find_ordered_alphabet(wrong_dictionary)


if __name__ == '__main__':
    unittest.main()
