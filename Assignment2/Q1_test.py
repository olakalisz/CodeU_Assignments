"""Tests for question 1 - print ancestors."""

import unittest

import Q1


class Q1Test(unittest.TestCase):

    def setUp(self):
        # Create given tree example
        node_1 = Q1.TreeNode(1)
        node_5 = Q1.TreeNode(5)
        node_3 = Q1.TreeNode(3, node_1, node_5)
        node_14 = Q1.TreeNode(14)
        node_9 = Q1.TreeNode(9, node_3, node_14)
        node_19 = Q1.TreeNode(19)
        node_18 = Q1.TreeNode(18, None, node_19)
        node_16 = Q1.TreeNode(16, node_9, node_18)
        self._tree = node_16

    def testEmptyCase(self):
        empty_tree = None
        with self.assertRaises(ValueError):
            Q1.print_ancestors(empty_tree, 0)

    def testKnownCases(self):
        self.assertEquals([5,3,9,16], Q1.print_ancestors(self._tree, 5))
        self.assertEquals([1,3,9,16], Q1.print_ancestors(self._tree, 1))
        self.assertEquals([3,9,16], Q1.print_ancestors(self._tree, 3))
        self.assertEquals([14,9,16], Q1.print_ancestors(self._tree, 14))
        self.assertEquals([19,18,16], Q1.print_ancestors(self._tree, 19))
        self.assertEquals([9,16], Q1.print_ancestors(self._tree, 9))
        self.assertEquals([18,16], Q1.print_ancestors(self._tree, 18))
        self.assertEquals([16], Q1.print_ancestors(self._tree, 16))

    def testErrorCases(self):
        with self.assertRaises(KeyError):
            Q1.print_ancestors(self._tree, 0)
        with self.assertRaises(KeyError):
            Q1.print_ancestors(self._tree, 4)

if __name__ == '__main__':
    unittest.main()