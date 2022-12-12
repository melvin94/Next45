from argparse import ArgumentParser
from lib.rover import Rover
from pathlib import Path

ap = ArgumentParser()
ap.add_argument(
    '-i',
    '--input-path',
    required=True,
    help='The path to the input instructions text file.'
)


if __name__ == "__main__":
    args = ap.parse_args()
    input_path = Path(args.input_path)

    mars_rover = Rover(input_path)
    rover_position = mars_rover.process_instructions()
    print('The rover is located at:', rover_position)
