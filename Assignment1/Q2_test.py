"""Tests for question 2 - kth from last element (node) of the list."""

import unittest

import Q2


class Q2Test(unittest.TestCase):

  def testEmptyCase(self):
    list = Q2.SinglyLinkedList()
    with self.assertRaises(IndexError):
        list.get_from_last(1)
    with self.assertRaises(IndexError):
        list.get_from_last(0)

  def testKnownCases(self):
    # Create a list with elements from 1 to 4 with 4 as head of the list
    list = Q2.SinglyLinkedList()
    for i in range(1,5):
        list.insert_first(i)
    self.assertEquals(1, list.get_from_last(0).get_data())
    self.assertEquals(2, list.get_from_last(1).get_data())
    self.assertEquals(3, list.get_from_last(2).get_data())
    self.assertEquals(4, list.get_from_last(3).get_data())


  def testErrorCases(self):
    # Create a list with elements from 1 to 4 with 4 as head of the list
    list = Q2.SinglyLinkedList()
    for i in range(1, 5):
        list.insert_first(i)
    with self.assertRaises(ValueError):
        list.get_from_last(4)
    with self.assertRaises(ValueError):
        list.get_from_last(5)



if __name__ == '__main__':
  unittest.main()
