# Returns true if strings 's1' and 's2' are permutations of the other, false otherwise
def is_permutation(s1, s2):

    # We are case-insensitive
    s1 = s1.lower()
    s2 = s2.lower()

    # If strings lengths are not equal they cannot be permutations of the other
    if len(s1) != len(s2):
        return False

    # Initialise two dictionaries 'lc1' and 'lc2' to count occurrences of letters in 's1' and 's2'
    lc1 = {}    # Letter count for 's1' (character count)
    lc2 = {}    # Letter count for 's2' (character count)

    # Populate dictionaries 'lc1' and 'lc2'
    for i in range (len(s1)):
        l1 = s1[i]
        l2 = s2[i]

        if l1 in lc1:
            lc1[l1] += 1
        else:
            lc1[l1] = 1

        if l2 in lc2:
            lc2[l2] += 1
        else:
            lc2[l2] = 1

    # Check whether 's1' and 's2' contain the same set of letters and if the number of occurrences of each
    # letter in both strings is the same
    for character in lc1:
        if character not in lc2:
            return False

        if lc1[character] != lc2[character]:
            return False

    return True

# Test examples
print(is_permutation("Listen", "Silent"))
print(is_permutation("Triangle", "Integral"))
print(is_permutation("Apple", "Pabble"))