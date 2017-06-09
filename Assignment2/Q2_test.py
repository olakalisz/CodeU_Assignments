"""Tests for question 1 - print ancestors."""

import unittest

import Q2


class Q2Test(unittest.TestCase):

    def setUp(self):
        # Create given tree example
        node_1 = Q2.TreeNode(1)
        node_5 = Q2.TreeNode(5)
        node_3 = Q2.TreeNode(3, node_1, node_5)
        node_14 = Q2.TreeNode(14)
        node_9 = Q2.TreeNode(9, node_3, node_14)
        node_19 = Q2.TreeNode(19)
        node_18 = Q2.TreeNode(18, None, node_19)
        node_16 = Q2.TreeNode(16, node_9, node_18)
        self._tree = node_16

    def testEmptyCase(self):
        empty_tree = None
        with self.assertRaises(ValueError):
            Q2.lowest_common_ancestor(empty_tree, 0, 0)

    def testKnownCases(self):
        self.assertEquals(9, Q2.lowest_common_ancestor(self._tree, 5, 14))
        self.assertEquals(16, Q2.lowest_common_ancestor(self._tree, 5, 19))
        self.assertEquals(3, Q2.lowest_common_ancestor(self._tree, 1, 3))
        self.assertEquals(18, Q2.lowest_common_ancestor(self._tree, 18, 18))
        self.assertEquals(16, Q2.lowest_common_ancestor(self._tree, 16, 16))

    def testErrorCases(self):
        with self.assertRaises(KeyError):
            Q2.lowest_common_ancestor(self._tree, 0, 5)
        with self.assertRaises(KeyError):
            Q2.lowest_common_ancestor(self._tree, 5, 0)

if __name__ == '__main__':
    unittest.main()