class shape:
	def _init_(self):
		self.__areaValue = 0
		self.__perimeterValue = 0
		
	def area(self):
		print("Area ", self.__areaValue)
		
	def perimeter(self):
		print("Perimeter ", self.__perimeterValue)
		
class rectangle(shape):
	def __init__(self, length, width):
		shape.__init__(self)
		self.__length = length
		self.__width = width
		
	def area(self):
		self.__areaValue = self.__length * self.__width
		print("Rectangle Area ", self.__areaValue)
		
class circle(shape):
	def __init__(self, radius):
		shape.__init__(self)
		self.__radius = radius

	def area(self):
		self.__areaValue = self.__radius * self.__radius * 3.142
		print("Circle Area ", self.__areaValue)
		
myCircle = circle(int(input("Enter the radius of the circle: ")))
myCircle.area()
myRectangle = rectangle(int(input("Enter the length of the rectangle: ")), int(input("Enter the width of the rectangle: ")))
myRectangle.area()
