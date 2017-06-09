"""Tests for question 1 - permutation, alternative solution."""

import unittest

import Q1_alternative_sol


class Q1Test(unittest.TestCase):

  def testEdgeCases(self):
    self.assertEquals(True, Q1_alternative_sol.is_permutation("", ""))
    self.assertEquals(False, Q1_alternative_sol.is_permutation("a", ""))
    self.assertEquals(False, Q1_alternative_sol.is_permutation("", "a"))

  def testKnownCases(self):
    self.assertEquals(True, Q1_alternative_sol.is_permutation("Listen", "Silent"))
    self.assertEquals(True, Q1_alternative_sol.is_permutation("Triangle", "Integral"))
    self.assertEquals(False, Q1_alternative_sol.is_permutation("Apple", "Pabble"))


if __name__ == '__main__':
  unittest.main()
