"""Checks if two strings are permutations of each other."""

from collections import Counter

def is_permutation(s1, s2):
    """Checks if 's1' and 's2' are permutations of each other.

    Args:
        s1: a string, first string to compare
        s2: a string, second string to compare

    Returns:
        a boolean, true if strings are permutations of each other, false otherwise
    """
    # We are case-insensitive
    s1 = s1.lower()
    s2 = s2.lower()

    # Character count in both strings needs to be the same for them to be permutations
    return Counter(s1) == Counter(s2)