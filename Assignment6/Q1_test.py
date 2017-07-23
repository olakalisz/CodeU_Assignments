"""Tests for question 1 - rearranging cars."""

from itertools import permutations
from random import randint
import unittest
import logging

from Q1 import rearrange_cars

_NUMBER_OF_GENERATED_TESTS = 100
_NUMBER_OF_CARS_TO_PERMUTE = 5


def _apply_moves(current_positions, moves):
    """
    The method applies a sequence of moves to the given cars' layout on the parking and returns the resulting layout.

        Args:
            current_positions:  an array of integers, indicates the current locations (layout) of cars on the parking
            moves:              an array of Move objects, indicates how the cars are supposed to be moved.

        Returns:
            a list of integers, indicates the resulting cars' layout after the sequence of moves is applied.
    """
    for move in moves:
        # Swap 'start' and 'end' of the move to perform the move
        current_positions[move.get_start()], current_positions[move.get_end()] = current_positions[move.get_end()], \
                                                                                 current_positions[move.get_start()]
    return current_positions


def _test_result(start_positions, desired_positions):
    """
    The method verifies the correctness of the move sequence to rearrange cars and checks the number of moves.

        Args:
            start_positions:    a list of integers, indicates the initial locations (layout) of cars on the parking
            desired_positions:  a list of integers, indicates the desired locations (layout) of cars on the parking

        Returns:
            a boolean,  indicates whether the generated rearrangement is valid (leads to desired cars' positions)
            an integer, the number of moves performed
    """
    move_sequence = rearrange_cars(start_positions, desired_positions)
    positions_after_rearranging = _apply_moves(start_positions, move_sequence)
    if desired_positions == positions_after_rearranging:
        return True, len(move_sequence)
    else:
        return False, len(move_sequence)


class Q1Test(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)

    def testNoMoveCases(self):
        """Tests examples where no moves are expected."""
        start_positions = [1, 2, 0, 3]
        end_positions = [1, 2, 0, 3]
        verify_result, number_of_moves = _test_result(start_positions, end_positions)
        self.assertTrue(verify_result and number_of_moves == 0)

        logger = logging.getLogger(__name__)
        logger.info(
            'Test with no moves expected: start positions = %s, end positions = %s, number of moves performed = %s',
            start_positions, end_positions, number_of_moves)

        start_positions = []
        end_positions = []
        verify_result, number_of_moves = _test_result(start_positions, end_positions)
        self.assertTrue(verify_result and number_of_moves == 0)

        logger = logging.getLogger(__name__)
        logger.info(
            'Test with no moves expected: start positions = %s, end positions = %s, number of moves performed = %s',
            start_positions, end_positions, number_of_moves)

    def testGivenCases(self):
        """Tests the given example cases."""
        start_positions = [1, 2, 0, 3]
        end_positions = [3, 1, 2, 0]
        verify_result, number_of_moves = _test_result(start_positions, end_positions)
        self.assertTrue(verify_result)

        logger = logging.getLogger(__name__)
        logger.info('Testing given example: start positions = %s, end positions = %s, number of moves performed = %s',
                    start_positions, end_positions, number_of_moves)

    def testGeneratedExamples(self):
        """Generate all possible permutations of 5 cars' layouts on the parking and randomly choose 100 pairs
           from the pairs of of those permutations. Use the pairs of permutations as paris of start and end
           positions of cars."""
        # Generate all permutations of 5 cars on the parking.
        permutations_of_5 = list(permutations(range(_NUMBER_OF_CARS_TO_PERMUTE)))
        number_of_permutations = len(permutations_of_5)

        for i in range(_NUMBER_OF_GENERATED_TESTS):
            # Randomly choose a pair of those permutations.
            start_positions = list(permutations_of_5[randint(0, number_of_permutations - 1)])
            end_positions = list(permutations_of_5[randint(0, number_of_permutations - 1)])

            verify_result, number_of_moves = _test_result(start_positions, end_positions)
            self.assertTrue(verify_result)

            logger = logging.getLogger(__name__)
            logger.info('Generated test: start positions = %s, end positions = %s, number of moves performed = %s',
                        start_positions, end_positions, number_of_moves)


if __name__ == '__main__':
    unittest.main()
