"""Tests for question 1 - counting islands."""

import unittest

import Q1


class Q1Test(unittest.TestCase):
    def setUp(self):
        # Creating some map grid testing examples
        self._empty_map = [[]]
        self._no_islands_map = [[False for i in range(5)] for j in range(7)]
        self._all_land_map = [[True for i in range(10)] for j in range(4)]
        self._given_map = [[False, True, False, True],
                           [True, True, False, False],
                           [False, False, True, False],
                           [False, False, True, False]]
        self._test_map_1 = [[False, True, False, False, False],
                            [False, True, True, True, True],
                            [True, True, False, False, False],
                            [False, False, True, True, False]]
        self._test_map_2 = [[True, True, True, True, True],
                           [True, False, False, False, True],
                           [True, False, True, False, True],
                           [True, False, False, False, True],
                           [True, True, True, True, True]]

    def testEmptyCase(self):
        """Tests the case when map argument is empty."""
        self.assertEquals(0, Q1.counting_islands(self._empty_map))

    def testNoIslandsCase(self):
        """Tests the case when there are no islands in a map grid"""
        self.assertEquals(0, Q1.counting_islands(self._no_islands_map))

    def testAllLandCase(self):
        """Tests the case when all map tiles are land"""
        self.assertEquals(1, Q1.counting_islands(self._all_land_map))

    def testKnownCases(self):
        """Tests some known cases."""
        # Test the given example
        self.assertEquals(3, Q1.counting_islands(self._given_map))
        # Test other map example
        self.assertEquals(2, Q1.counting_islands(self._test_map_1))
        # Test other map example - ring island
        self.assertEquals(2, Q1.counting_islands(self._test_map_2))


if __name__ == '__main__':
    unittest.main()
