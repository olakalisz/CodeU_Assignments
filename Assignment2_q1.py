# coding=utf-8
from BinaryTree import TreeNode, BinaryTree

"""Prints all the ancestors of the key in the given binary tree. Uses two methods:
   first method 'print_ancestors' takes a tree and a key and calls the second helper
   recursive method 'print_ancestors_recursive' which also takes tree and a key but it
   also passes a list of ancestors so far as an argument.
   Given solution takes θ(n) time, where n is the number of nodes in the tree."""


def print_ancestors(tree, key):
    """Prints all the ancestors of the key in the given binary tree and returns a list of them.
       Ancestors contain the key itself. Ancestors are ordered: first in the list (and first printed)
       is the key itself then it 'crawls up' the tree up until the root.

        Args:
            tree: a binary tree, tree to check for ancestors, no duplicated keys allowed
            key: a key type in a given tree, a key for the ancestors to be printed

        Returns:
            a list of key type, list of the ancestors of the key and prints ancestors

        Throws:
            IndexError: if the given tree is empty
            ValueError: if the given tree does not contain the key
    """
    # Throw an error if the tree is empty
    if tree.get_root() is None:
        raise IndexError("Empty tree!")

    # Call the helper recursive method and pass an empty list of ancestors as last argument.
    # (Empty list - base case)
    ancestors = print_ancestors_recursive(tree, key, [])

    # If the list returned by recursive method is empty it implies the tree does not contain
    # the given key. (Otherwise it contains at least the key itself)
    if not ancestors:
        raise ValueError("Given key is not in the tree!")

    # Return the result from the recursive call - list of ancestors.
    return ancestors


def print_ancestors_recursive(tree, key, ancestors):
    """Prints all the ancestors of the key in the given binary tree and returns a list of them.
       Ancestors contain the key itself. Method used recursively, adds one ancestors at a time.

        Args:
            tree: a binary tree, tree to check for ancestors, no duplicated keys allowed
            key: a key type in a given tree, a key for the ancestors to be printed
            ancestors: a list of key type, list of ancestors 'so far'

        Returns:
            a list of key type, list of the ancestors of the key and prints ancestors
    """
    root = tree.get_root()
    # Base case
    if root is None:
        return []

    # Get left and right subtree from the node for the recursive call.
    left_subtree = BinaryTree(root.get_left())
    right_subtree = BinaryTree(root.get_right())

    # If the key is in the root, print the root and add it to ancestor list
    if root.get_value() == key:
        ancestors.append(root.get_value())
        print root.get_value()
        return ancestors

    # If the key is in either left of right subtree of the node, print the node
    # and add it to the ancestor list. Recursive call, works similar to dfs.
    if (print_ancestors_recursive(left_subtree, key, ancestors) != []
            or print_ancestors_recursive(right_subtree, key, ancestors) != []):
        ancestors.append(root.get_value())
        print root.get_value()
        return ancestors

    # Otherwise return empty list
    return []
