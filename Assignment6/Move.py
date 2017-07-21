class Move:
    """
    Implementation of Move class. Move is an object with two integer attributes:
        start_spot: space where the move starts
        end_spot: space where the move ends.
    """
    def __init__(self, start_spot, end_spot):
        self.__start_spot = start_spot
        self.__end_spot = end_spot

    def get_start(self):
        return self.__start_spot

    def get_end(self):
        return self.__end_spot

    def pretty_print(self):
        print "move from {} to {}".format(self.get_start(), self.get_end())
