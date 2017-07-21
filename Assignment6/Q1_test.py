"""Tests for question 1 - rearranging cars."""

import itertools
import random
import unittest
import logging

import Q1

_NUMBER_OF_GENERATED_TESTS = 100
_NUMBER_OF_PERMUTATIONS = 120


def _apply_moves(current_positions, moves):
    """The method applies a sequence of moves to the given cars' layout on the parking and returns the resulting layout.

        Args:
            current_positions: an array of integers, indicates the current locations (layout) of cars on the parking
            moves: an array of Move objects, indicates how the cars are supposed to be moved.

        Returns:
            an array of integers, indicates the resulting cars' layout after the sequence of moves is applied."""
    for move in moves:
        temp = current_positions[move.get_end()]
        current_positions[move.get_end()] = current_positions[move.get_start()]
        current_positions[move.get_start()] = temp
    return current_positions


class Q1Test(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)

    def testGivenCases(self):
        """Tests the given example cases."""
        start_positions = [1, 2, 0, 3]
        end_positions = [3, 1, 2, 0]
        print_sequence = False

        logger = logging.getLogger(__name__)
        logger.info('Test with parameters: start positions = %s, end positions = %s', start_positions, end_positions)
        move_sequence = Q1.find_moves_sequence(start_positions, end_positions, print_sequence)
        self.assertEquals(_apply_moves(start_positions, move_sequence), end_positions)

    def testGeneratedExamples(self):
        """Generate all possible permutations of 5 cars' layouts on the parking and randomly choose 100 pairs
           from the pairs of of those permutations. Use the pairs of permutations as paris of start and end
           positions of cars."""
        # Generate all permutations of 5 cars on the parking.
        permutations = list(itertools.permutations(range(5)))
        
        for i in range(_NUMBER_OF_GENERATED_TESTS):
            # Randomly choose a pair of those permutations.
            start_positions = list(permutations[int(round(random.random() * (_NUMBER_OF_PERMUTATIONS - 1)))])
            end_positions = list(permutations[int(round(random.random() * (_NUMBER_OF_PERMUTATIONS - 1)))])
            print_sequence = False

            logger = logging.getLogger(__name__)
            logger.info('Test with parameters: start positions = %s, end positions = %s', start_positions,
                        end_positions)
            move_sequence = Q1.find_moves_sequence(start_positions, end_positions, print_sequence)
            self.assertEquals(_apply_moves(start_positions, move_sequence), end_positions)


if __name__ == '__main__':
    unittest.main()
