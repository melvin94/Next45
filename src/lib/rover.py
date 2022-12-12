from dataclasses import dataclass
from lib.compass import Compass
from pathlib import Path


# The default orientation scheme of the rover.
_ORIENTATION_NESW = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


@dataclass
class _RoverData:
    """Construct. A dataclass that contains the rover data.

    :param __input_path: The path to the instructions text file.
    """

    __input_path: Path

    def __post_init__(self):
        """Post-construct. Loads the input file and initializes the rover data
        accordingly."""

        with open(self.__input_path, 'r') as f:
            rover_input = f.read().split('\n')

        x_boundary = int(rover_input[0][0])
        y_boundary = int(rover_input[0][1])
        self.boundary = (x_boundary, y_boundary)

        x_coord = int(rover_input[1][0])
        y_coord = int(rover_input[1][1])
        self.position = [x_coord, y_coord]

        self.orientation = rover_input[1][3]

        self.instructions = rover_input[2]


class Rover:
    """A class that simulates a Mars Rover."""

    def __init__(self, input_path: Path) -> None:
        """Construct.

        :param input_path: The input path to the rover instructions text file.
        """

        self.__rover_data = self.__read_instructions(input_path)
        self.__rover_compass = Compass(_ORIENTATION_NESW)

    def __read_instructions(self, input_path: Path) -> _RoverData:
        """Initializes the rover dataclass with the given input file path."""

        return _RoverData(input_path)

    def __is_in_safe_zone(self, position: tuple[int, int]) -> bool:
        """Determines if the anticipated location of the rover is within the
        bounds of the `safe zone`."""

        if position[0] < 0:
            return False
        if position[1] < 0:
            return False
        if position[0] > self.__rover_data.boundary[0]:
            return False
        if position[1] > self.__rover_data.boundary[1]:
            return False

        return True

    def __move(self,
               position: tuple[int, int],
               orientation: str) -> tuple[int, int]:
        """Gets the position of the rover if it moves in the direction it were
        facing.

        :param position: The current position of the rover.
        :param orientation: The current facing direction of the rover.
        :returns: The calculated new position of the rover if it moves.
        """

        if orientation == 'N':
            position[1] += 1

        if orientation == 'E':
            position[0] += 1

        if orientation == 'S':
            position[1] -= 1

        if orientation == 'W':
            position[0] -= 1

        return position

    def __rotate(self, instruction: str) -> str:
        """Turns the rover orientation.

        :param instruction: The instruction containing whether to turn left or
                            right.
        :returns: The new rover orientation.
        """

        if instruction == 'L':
            self.__rover_compass.turn_left()
        if instruction == 'R':
            self.__rover_compass.turn_right()

        return self.__rover_compass.get_orientation()

    def __is_safe_to_navigate(self) -> bool:
        """Map out the rover path from the instructions to determine if it is
        save to navigate.

        :returns: True/False, depending on if the path is safe or not.
        """

        pos = self.__rover_data.position.copy()
        orientation = self.__rover_data.orientation
        self.__rover_compass.calibrate_compass(orientation)

        for instruction in self.__rover_data.instructions:
            if instruction == 'M':
                pos = self.__move(pos, orientation)
                if not self.__is_in_safe_zone(pos):
                    return False
            else:
                orientation = self.__rotate(instruction)

        return True

    def __navigate(self) -> None:
        """Performs the navigation of the rover."""

        self.__rover_compass.calibrate_compass(self.__rover_data.orientation)
        for instruction in self.__rover_data.instructions:
            if instruction == 'M':
                self.__rover_data.position = self.__move(
                    self.__rover_data.position,
                    self.__rover_data.orientation
                )
            else:
                self.__rover_data.orientation = self.__rotate(instruction)

    def process_instructions(self) -> str:
        """Processes the set of instructions available in the input file.

        :returns: The final position and orientation of the rover as a string.
        """

        if not self.__is_safe_to_navigate():
            x, y = self.__rover_data.position
            orientation = self.__rover_data.orientation

        else:
            self.__navigate()
            x, y = self.__rover_data.position
            orientation = self.__rover_data.orientation

        return f'{x}{y} {orientation}'
