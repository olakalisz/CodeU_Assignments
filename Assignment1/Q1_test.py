"""Tests for question 1 - permutation."""

import unittest

import Q1


class Q1Test(unittest.TestCase):

  def testEdgeCases(self):
    self.assertEquals(True, Q1.is_permutation("", ""))
    self.assertEquals(False, Q1.is_permutation("a", ""))
    self.assertEquals(False, Q1.is_permutation("", "a"))

  def testKnownCases(self):
    self.assertEquals(True, Q1.is_permutation("Listen", "Silent"))
    self.assertEquals(True, Q1.is_permutation("Triangle", "Integral"))
    self.assertEquals(False, Q1.is_permutation("Apple", "Pabble"))


if __name__ == '__main__':
  unittest.main()
