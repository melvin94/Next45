import compass

class Rover():
	def __init__(self):
		self.__horizontalBoundary = None
		self.__verticalBoundary = None

		self.__horizontalCoordinate = None
		self.__verticalCoordinate = None

		self.__orientation = None

		self.__roverCompass = compass.Compass(["N", "E", "S", "W"])

	def readInput(self, roverInputFile):

		inputFile = open(roverInputFile)
		roverInput = inputFile.read().split("\n")
		inputFile.close()

		self.__horizontalBoundary = int(roverInput[0][0])
		self.__verticalBoundary = int(roverInput[0][1])

		self.__horizontalCoordinate = int(roverInput[1][0])
		self.__verticalCoordinate = int(roverInput[1][1])

		self.__orientation = roverInput[1][3]

		self.__roverCompass.setOrientation(self.__orientation)

		self.moveRover(roverInput[2])

		print (self.__horizontalCoordinate, self.__verticalCoordinate, self.__orientation)
		return (str(self.__horizontalCoordinate) + " " + str(self.__verticalCoordinate) + " " + self.__orientation)

	def moveRover(self, roverInstructions):
		initialHorizontalCoordinate = self.__horizontalCoordinate
		initialVerticalCoordinate = self.__verticalCoordinate
		initialRoverOrientation = self.__orientation

		for roverInstruction in roverInstructions:
			if (roverInstruction == "M"):
				self.move()
			else:
				self.rotate(roverInstruction)

		if (self.__horizontalCoordinate < 0) \
			or (self.__horizontalCoordinate > self.__horizontalBoundary) \
			or (self.__verticalCoordinate < 0) \
			or (self.__verticalCoordinate > self.__verticalBoundary):
				print ("Rover will be placed out of bounds; not executing movement")
				self.__horizontalCoordinate = initialHorizontalCoordinate
				self.__verticalCoordinate = initialVerticalCoordinate
				self.__orientation = initialRoverOrientation


	def move(self):
		if (self.__orientation == "N"):
			self.__verticalCoordinate += 1

		if (self.__orientation == "E"):
			self.__horizontalCoordinate += 1

		if (self.__orientation == "S"):
			self.__verticalCoordinate -= 1

		if (self.__orientation == "W"):
			self.__horizontalCoordinate -= 1

	def rotate(self, direction):
		if (direction == "L"):
			self.__orientation = self.__roverCompass.turnLeft()

		if (direction == "R"):
			self.__orientation = self.__roverCompass.turnRight()