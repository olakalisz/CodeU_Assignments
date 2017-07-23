"""The solution presented here goes through all parking spaces and 'places' on each of them the desired car (car which
   on the particular space in the desired positions layout - second array). Because dictionary structure is used to
   keep track of current cars' positions the runtime of the given solution is O(N) where N is the number of car and the
   space used is also O(N)."""

from Move import Move

_NO_CAR = 0


def rearrange_cars(start_positions, desired_positions, print_sequence=False):
    """
    The method finds a move sequence that will change cars' layout on the parking from start positions to desired
       positions.

        Args:
            start_positions:    a list of integers, indicates the initial locations (layout) of cars on the parking
            desired_positions:  a list of integers, indicates the desired locations (layout) of cars on the parking
            print_sequence:     a boolean, indicates whether the move sequence should should be formatted and printed
                                (useful to disable it for testing)

        Returns:
            a list of Move objects, indicates the sequence of moves that will move the cars on the parking
            from initial layout to the desired one.
    """
    moves = []
    # Copy start_position array so that we do not change it in place. (Makes testing easier)
    current_positions = list(start_positions)
    position_map = create_position_map(current_positions)

    # Set the right car on each parking space.
    for spot in range(len(current_positions)):
        if desired_positions[spot] != 0:
            set_single_spot(spot=spot, current_positions=current_positions, position_map=position_map,
                            desired_positions=desired_positions, moves=moves)

    if print_sequence:
        for move in moves:
            print move

    return moves


def create_position_map(current_positions):
    """
    The method creates a dictionary which assigns each car its current position.

        Args:
            current_positions: a list of integers, indicates the current locations (layout) of cars on the parking

        Returns:
            A list of integers. Indicates the mapping of cars to their positions. List index is corresponding to a car
            and the value is car's position.
    """
    position_map = [0] * len(current_positions)
    for i in range(len(current_positions)):
        car = current_positions[i]
        position_map[car] = i
    return position_map


def set_single_spot(spot, current_positions, position_map, desired_positions, moves):
    """
    The method sets a 'desired car' on the spot passed as an argument.
       It uses the maximum of two moves to set the car.

        Args:
            spot:               an integer, the parking space we want to set the car on
            current_positions:  a list of integers, indicates the current locations (layout) of cars on the parking
            position_map:       a dictionary mapping integers to integers, cars' numbers are keys and cars' position on the
                                parking are values
            desired_positions:  a list of integers, indicates the desired locations (layout) of cars on the parking
            moves:              a list of Move objects, sequence of the moves 'done so far'
    """
    current_car = current_positions[spot]
    desired_car = desired_positions[spot]

    # There is no need to set a spot if the right car is already there.
    if current_car == desired_car:
        return
    else:
        # The first move is to empty the spot. There is no need to empty the spot if it is already empty (not occupied).
        if current_car != _NO_CAR:
            empty_spot = position_map[_NO_CAR]
            make_move(car=current_car, start_spot=spot, end_spot=empty_spot, current_positions=current_positions,
                      position_map=position_map, moves=moves)

        # The second move sets to right car to now empty parking space.
        desired_car_spot = position_map[desired_car]
        make_move(car=desired_car, start_spot=desired_car_spot, end_spot=spot, current_positions=current_positions,
                  position_map=position_map, moves=moves)


def make_move(car, start_spot, end_spot, current_positions, position_map, moves):
    """
    The method 'performs' a move, i.e. adds move to the move list and updates all position data structures.

        Args:
            car:                an integer, indicates a car on a parking
            start_spot:         an integer, the space where the move 'begins'
            end_spot:           an integer, the space where the move 'ends'
            current_positions:  a list of integers, indicates the current locations (layout) of cars on the parking
            position_map:       a list of integers, indicates the mapping of cars to their positions. List index is
                                corresponding to a car and the value is car's position
            moves:              a list of Move objects, sequence of the moves 'done so far'
    """
    moves.append(Move(start_spot, end_spot))
    position_map[_NO_CAR] = start_spot
    position_map[car] = end_spot
    current_positions[start_spot] = _NO_CAR
    current_positions[end_spot] = car
