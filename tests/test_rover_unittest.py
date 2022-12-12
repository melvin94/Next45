from os.path import join
from src.lib.rover import Rover


import unittest


class TestRover(unittest.TestCase):
    """
    Inherit unittest.TestCase
    """

    input_directory = 'data/inputs/'  # input directory for all input tests

    # test case: sample result
    def test_0_sample(self):
        test_rover = Rover(join(self.input_directory, 'input0.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '33 S')

    # test case: moving only in horizontal direction
    def test_1_horizontal_movement(self):
        test_rover = Rover(join(self.input_directory, 'input1.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '10 E')

    # test case: moving only in vertical direction
    def test_2_vertical_movement(self):
        test_rover = Rover(join(self.input_directory, 'input2.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '01 N')

    # test case: rotate left
    def test_3_rotation_left(self):
        test_rover = Rover(join(self.input_directory, 'input3.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '00 W')

    # test case: rotate right
    def test_4_rotation_right(self):
        test_rover = Rover(join(self.input_directory, 'input4.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '00 E')

    # test case: out of bounds; before (0,0) in horizontal direction
    def test_5_out_of_bounds_before_00_horizontal(self):
        test_rover = Rover(join(self.input_directory, 'input5.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '00 W')

    # test case: out of bounds; before (0,0) in vertical direction
    def test_6_out_of_bounds_before_00_vertical(self):
        test_rover = Rover(join(self.input_directory, 'input6.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '00 S')

    # test case: out of bounds; beyond horizontal boundary
    def test_7_out_of_bounds_horizontal_boundary(self):
        test_rover = Rover(join(self.input_directory, 'input7.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '94 E')

    # test case: out of bounds; beyond vertical boundary
    def test_8_out_of_bounds_vertical_boundary(self):
        test_rover = Rover(join(self.input_directory, 'input8.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '94 N')

    # test case: out of bounds before final coordinate
    def test_9_out_of_bounds_vertical_boundary(self):
        test_rover = Rover(join(self.input_directory, 'input9.txt'))
        result = test_rover.process_instructions()
        self.assertEqual(result, '94 N')
