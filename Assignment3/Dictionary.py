# coding=utf-8
class Dictionary:
    """Dummy implementation of the Dictionary class for testing purposes.
       In the real problem the methods isWord(string) and isPrefix(string) are assumed to have
       θ(n) running time where n is the number of characters in the string."""

    def __init__(self, word_list, prefix_list):
        # In this approach we are case insensitive, thus we change all the given words and prefixes to uppercase.
        for i in range(len(word_list)):
            word_list[i] = word_list[i].upper()
        for i in range(len(prefix_list)):
            prefix_list[i] = prefix_list[i].upper()

        self.__word_list = word_list
        self.__prefix_list = prefix_list

    def isWord(self, word):
        return word in self.__word_list

    def isPrefix(self, prefix):
        return prefix in self.__prefix_list
