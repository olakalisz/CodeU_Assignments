class TreeNode(object):
    """My implementation of Binary Tree. TreeNode is a unit which is used in
       my implementation of Binary Tree and each TreeNode is a tree itself.
       There is no insert() method as I assumed that tree will be created in
       a bottom-up fashion. The 'top' node is the root. None corresponds
       to empty tree."""
    def __init__(self, value=None, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    def get_value(self):
        return self.__value

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_left(self, child):
        self.__left = child

    def set_right(self, child):
        self.__right = child
