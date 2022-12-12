class Compass:
	def __init__(self, orientations):
		self.__compassOrientations = orientations
		self.__index = 0

	def setOrientation(self, orientation):
		self.__index = self.__compassOrientations.index(orientation)

	def getOrientation(self):
		return self.__compassOrientations[self.__index]

	def turnRight(self):
		self.__index += 1
		if self.__index >= len(self.__compassOrientations):
			self.__index = 0
		self.__index
		return self.getOrientation()

	def turnLeft(self):
		self.__index -= 1
		if self.__index < 0:
			self.__index = len(self.__compassOrientations) - 1
		return self.getOrientation()