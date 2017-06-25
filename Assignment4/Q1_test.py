"""Tests for question 1 - counting islands."""

import unittest

import Q1


def _map_grid(string):
    """Creates a 2D array of characters from a string. The string represents the grid by having the T/F
       characters corresponding to boolean True/False in each row separated by a '|'.

        Args:
            string: a string, representation of the grid as a single string T for True, F for False, no other
            characters allowed (If any other characters are used they will be converted to False).

        Returns:
            a 2-D array of booleans corresponding to the map grid given.
    """
    map_grid = []
    for row in string.split('|'):
        map_grid.append([True if ch == 'T' else False for ch in row])
        # Make sure each row has the same length.
        if len(map_grid[0]) != len(map_grid[-1]):
            raise ValueError("not all rows have the same length")
    return map_grid


class Q1Test(unittest.TestCase):
    def testEmptyCase(self):
        """Tests the case when map argument is empty."""
        self.assertEquals(0, Q1.counting_islands(_map_grid("")))

    def testNoIslandsCase(self):
        """Tests the case when there are no islands in a map grid"""
        no_islands_map = [[False for i in range(5)] for j in range(7)]
        self.assertEquals(0, Q1.counting_islands(no_islands_map))

    def testAllLandCase(self):
        """Tests the case when all map tiles are land"""
        all_land_map = [[True for i in range(10)] for j in range(4)]
        self.assertEquals(1, Q1.counting_islands(all_land_map))

    def testKnownCases(self):
        """Tests some known cases."""
        # Test the given example
        self.assertEquals(3, Q1.counting_islands(_map_grid("FTFT|TTFF|FFTF|FFTF")))
        # Test other map example
        self.assertEquals(2, Q1.counting_islands(_map_grid("FTFFF|FTTTT|TTFFF|FFTTF")))
        # Test other map example - ring island
        self.assertEquals(2, Q1.counting_islands(_map_grid("TTTTT|TFFFT|TFTFT|TFFFT|TTTTT")))


if __name__ == '__main__':
    unittest.main()
