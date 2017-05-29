# coding=utf-8
from BinaryTree import TreeNode, BinaryTree

"""Finds the lowest common ancestor of two nodes in the given tree. Uses two methods:
   first one to 'get_ancestors_recursive' to find the ancestors of each of two nodes and
   second 'lowest_common_ancestor' to compare the ancestors of two nodes and find the lowest
   common one.
   Given solution takes θ(n) time, where n is the number of nodes in the tree."""


def get_ancestors_recursive(tree, key, ancestors):
    """Finds all the ancestors of the key in the given binary tree. Ancestors are ordered: first
       in the list (and first printed) is the key itself then it 'crawls up' the tree up until the root.
       Ancestors contain the key itself. Method used recursively, adds one ancestors at a time.

        Args:
            tree: a binary tree, tree to check for ancestors, no duplicated keys allowed
            key: a key type in a given tree, a key for the ancestors to be printed
            ancestors: a list of key type, list of ancestors 'so far'

        Returns:
            a list of key type, list of the ancestors of the key and prints ancestors,
            if a list is empty then the given key is not in the tree
    """
    root = tree.get_root()
    # Base case
    if root is None:
        return []

    # Get left and right subtree from the node for the recursive call.
    left_subtree = BinaryTree(root.get_left())
    right_subtree = BinaryTree(root.get_right())

    # If the key is in the root, add it to ancestor list
    if root.get_value() == key:
        ancestors.append(root.get_value())
        return ancestors

    # If the key is in either left of right subtree of the node, add the node
    # to the ancestor list. Recursive call, works similar to dfs.
    if (get_ancestors_recursive(left_subtree, key, ancestors) != []
            or get_ancestors_recursive(right_subtree, key, ancestors) != []):
        ancestors.append(root.get_value())
        return ancestors

    # Otherwise return empty list
    return []


def lowest_common_ancestor(tree, node1, node2):
    """Finds the lowest common ancestor of two given nodes in the binary tree.

        Args:
            tree: a binary tree, tree to check for the lowest common ancestor of the two nodes
                  tree contains no duplicated keys
            node1: a key type in the given tree, first node to check for the lowest common ancestor
            node2: a key type in the given tree, second node to check for the lowest common ancestor

        Returns:
            a key type in the given tree, the lowest common ancestor of two nodes in the tree

        Throws:
            IndexError: if the given tree is empty
            ValueError: if any of two nodes given by key is not contained in a tree
    """
    # Throw an error if the tree is empty
    if tree.get_root() is None:
        raise IndexError("Empty tree!")

    # Throw an error if the first node given by key is not contained in a tree
    node1_ancestors = get_ancestors_recursive(tree, node1, [])
    if not node1_ancestors:
        raise ValueError("The first key given is not in the tree!")

    # Throw an error if the second node given by key is not contained ina tree
    node2_ancestors = get_ancestors_recursive(tree, node2, [])
    if not node2_ancestors:
        raise ValueError("The second key given is not in the tree!")

    # Find the lowest common ancestor given two lists of ancestors.
    # Set two index pointers to the last element of the lists of ancestors of two nodes.
    i = len(node1_ancestors) - 1
    j = len(node2_ancestors) - 1

    # Loop from the end of two lists until the first node with different key values
    # in the lists is found. (The first node - root should always be the same)
    while i >= 0 and j >= 0:
        if node1_ancestors[i] != node2_ancestors[j]:
            break
        i -= 1
        j -= 1

    # Return the last key value of the node that was the same in two ancestor lists.
    return node1_ancestors[i+1]
