import unittest
import os

# The class to be tested
import rover


class TestRover(unittest.TestCase):
	"""
	Inherit unittest.TestCase
	"""
	testRover = rover.Rover()		# Create a Rover object
	inputDirectory = "./inputs/"	# input directory for all test input cases

	# test case: sample result
	def test_0_sample(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input0.txt"))
		self.assertEqual(result, "3 3 S")

	# test case: moving only in horizontal direction
	def test_1_horizontal_movement(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input1.txt"))
		self.assertEqual(result, "1 0 E")

	# test case: moving only in vertical direction
	def test_2_vertical_movement(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input2.txt"))
		self.assertEqual(result, "0 1 N")

	# test case: rotate left
	def test_3_rotation_left(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input3.txt"))
		self.assertEqual(result, "0 0 W")

	# test case: rotate right
	def test_4_rotation_right(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input4.txt"))
		self.assertEqual(result, "0 0 E")

	# test case: out of bounds; before (0,0) in horizontal direction
	def test_5_out_of_bounds_before_00_horizontal(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input5.txt"))
		self.assertEqual(result, "0 0 W")

	# test case: out of bounds; before (0,0) in vertical direction
	def test_6_out_of_bounds_before_00_vertical(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input6.txt"))
		self.assertEqual(result, "0 0 S")

	# test case: out of bounds; beyond horizontal boundary
	def test_7_out_of_bounds_horizontal_boundary(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input7.txt"))
		self.assertEqual(result, "9 4 E")

	# test case: out of bounds; beyond vertical boundary
	def test_8_out_of_bounds_vertical_boundary(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input8.txt"))
		self.assertEqual(result, "9 4 N")

	# test case: out of bounds before final coordinate
	def test_9_out_of_bounds_vertical_boundary(self):
		result = self.testRover.readInput(os.path.join(self.inputDirectory,"input9.txt"))
		self.assertEqual(result, "9 4 N")

if __name__ == "__main__":
	unittest.main()