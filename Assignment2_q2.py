# coding=utf-8
"""Finds the lowest common ancestor of two nodes in the given tree. Uses two methods:
   first one to 'get_ancestors_recursive' to find the ancestors of each of two nodes and
   second 'lowest_common_ancestor' to compare the ancestors of two nodes and find the lowest
   common one.
   Given solution takes θ(n) time, where n is the number of nodes in the tree."""


from BinaryTree import TreeNode
from Assignment2_q1 import get_ancestors_recursive


def lowest_common_ancestor(tree, key1, key2):
    """Finds the lowest common ancestor of two given nodes in the binary tree.

        Args:
            tree: a binary tree, tree to check for the lowest common ancestor of the two nodes
                  tree contains no duplicated keys
            key1: a key type in the given tree, first node to check for the lowest common ancestor
            key2: a key type in the given tree, second node to check for the lowest common ancestor

        Returns:
            a key type in the given tree, the lowest common ancestor of two nodes in the tree

        Raises:
            ValueError: if the given tree is empty
            KeyError: if any of two nodes given by key is not contained in a tree
    """
    # Raise an error if the tree is empty
    if tree is None:
        raise ValueError("Empty tree!")

    # Raise an error if the first node given by key is not contained in a tree
    node1_ancestors = get_ancestors_recursive(tree, key1)
    if not node1_ancestors:
        raise KeyError("The first key given is not in the tree!")

    # Raise an error if the second node given by key is not contained in a tree
    node2_ancestors = get_ancestors_recursive(tree, key2)
    if not node2_ancestors:
        raise KeyError("The second key given is not in the tree!")

    # Find the lowest common ancestor given two lists of ancestors.
    # Set an index pointer to the first element of the list of ancestors of two nodes.
    i = 0

    # Find the longer ans shorter node list and difference in their length
    if len(node1_ancestors) > len(node2_ancestors):
        longer_ancestors = node1_ancestors
        shorter_ancestors = node2_ancestors
    else:
        longer_ancestors = node2_ancestors
        shorter_ancestors = node1_ancestors
    len_diff = len(longer_ancestors) - len(shorter_ancestors)

    # Loop through the lists until the first element in common is found.
    # (The first node - root should always be the same)
    while i < len(shorter_ancestors):
        if shorter_ancestors[i] == longer_ancestors[i+len_diff]:
            break
        i += 1

    # Return the last key value of the node that was the same in two ancestor lists.
    return shorter_ancestors[i]
