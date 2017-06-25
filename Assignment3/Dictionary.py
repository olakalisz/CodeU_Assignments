# coding=utf-8
class Dictionary:
    """Dummy implementation of the Dictionary class for testing purposes.
       In the real problem the methods isWord(string) and isPrefix(string) are assumed to have
       θ(n) running time where n is the number of characters in the string."""

    def __init__(self, word_list):
        # In this approach we are case insensitive, thus we change all the given words and prefixes to uppercase.
        for i in range(len(word_list)):
            word_list[i] = word_list[i].upper()
        # Initialise dictionary's word list
        self.__word_list = set(word_list)

        # Populate dictionary's prefix list based on the given word list
        self.__prefix_list = set()
        for word in self.__word_list:
            for i in range(1, len(word)):
                prefix = word[:i]
                if prefix not in self.__prefix_list:
                    self.__prefix_list.add(prefix)

    def isWord(self, word):
        word = word.upper()
        return word in self.__word_list

    def isPrefix(self, prefix):
        prefix = prefix.upper()
        return prefix in self.__prefix_list
