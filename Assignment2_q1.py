# coding=utf-8
"""Prints all the ancestors of the key in the given binary tree. Uses two methods:
   first method 'print_ancestors' takes a tree and a key and calls the second helper
   recursive method 'get_ancestors_recursive' which also takes tree and a key but it
   also passes a list of ancestors so far as an argument.
   Given solution takes θ(n) time, where n is the number of nodes in the tree."""


from BinaryTree import TreeNode


def print_ancestors(tree, key):
    """Prints all the ancestors of the key in the given binary tree and returns a list of them.
       Ancestors contain the key itself. Ancestors are ordered: first in the list (and first printed)
       is the key itself then it 'crawls up' the tree up until the root.

        Args:
            tree: a binary tree, tree to check for ancestors, no duplicated keys allowed
            key: a key type in a given tree, a key for the ancestors to be printed

        Returns:
            a list of key type, list of the ancestors of the key and prints ancestors

        Raises:
            ValueError: if the given tree is empty
            KeyError: if the given tree does not contain the key
    """
    # Throw an error if the tree is empty
    if tree is None:
        raise ValueError("Empty tree!")

    # Call the helper recursive method and pass an empty list of ancestors as last argument.
    # (Empty list - base case)
    ancestors = get_ancestors_recursive(tree, key)

    # If the list returned by recursive method is empty it implies the tree does not contain
    # the given key. (Otherwise it contains at least the key itself)
    if not ancestors:
        raise KeyError("Given key is not in the tree!")

    # Print ancestors.
    for a in ancestors:
        print a

    # Return the result from the recursive call - list of ancestors.
    return ancestors


def get_ancestors_recursive(tree, key):
    """Returns a list of all the ancestors of the key in the given binary tree.
       Ancestors contain the key itself. Method used recursively, adds one ancestor at a time.

        Args:
            tree: a binary tree, tree to check for ancestors, no duplicated keys allowed
            key: a key type in a given tree, a key for the ancestors to be printed

        Returns:
            a list of key type, list of the ancestors of the key and prints ancestors
    """
    # Base case
    if tree is None:
        return []

    # Get left and right subtree from the node for the recursive call.
    left_subtree = tree.get_left()
    right_subtree = tree.get_right()

    # If the key is in the root, print the root and add it to ancestor list
    if tree.get_value() == key:
        return [tree.get_value()]

    # If the key is in either left of right subtree of the node, print the node
    # and add it to the ancestor list. Recursive call, works similar to dfs.
    if (get_ancestors_recursive(left_subtree, key)
            or get_ancestors_recursive(right_subtree, key)):
        left_ancestors = get_ancestors_recursive(left_subtree, key)
        if left_ancestors:
            return left_ancestors + [tree.get_value()]
        else:
            right_ancestors = get_ancestors_recursive(right_subtree, key)
            return right_ancestors + [tree.get_value()]

    # Otherwise return empty list
    return []
