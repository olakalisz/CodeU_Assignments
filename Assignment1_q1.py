"""Checks if two strings are permutations of each other."""

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

    # If strings lengths are not equal they cannot be permutations of the other
    if len(s1) != len(s2):
        return False

    # Initialise two dictionaries 'character_counts1' and 'character_counts2'
    # to count occurrences of characters in 's1' and 's2'
    character_counts1 = {}
    character_counts2 = {}

    # Populate dictionaries 'character_counts1' and 'character_counts2'

    for i in range(len(s1)):
        l1 = s1[i]
        l2 = s2[i]

        if l1 in character_counts1:
            character_counts1[l1] += 1
        else:
            character_counts1[l1] = 1

        if l2 in character_counts2:
            character_counts2[l2] += 1
        else:
            character_counts2[l2] = 1

    # Check whether 's1' and 's2' contain the same set of characters and if the number of occurrences of each
    # character in both strings is the same
    return character_counts1 == character_counts2