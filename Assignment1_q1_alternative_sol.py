from collections import Counter

# Returns true if strings 's1' and 's2' are permutations of the other, false otherwise
def is_permutation(s1, s2):

    # We are case-insensitive
    s1 = s1.lower()
    s2 = s2.lower()

    # Character count in both strings needs to be the same for them to be permutations
    return Counter(s1) == Counter(s2)

# Test examples
print(is_permutation("Listen", "Silent"))
print(is_permutation("Triangle", "Integral"))
print(is_permutation("Apple", "Pabble"))