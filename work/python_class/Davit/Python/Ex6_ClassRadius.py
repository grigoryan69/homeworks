from math import pi
class Round():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
    	result = self.radius ** 2 * pi
    	return 'The area of your circle is: {0}'.format(result)

    def perimeter(self):
    	result = 2 * self.radius * pi
    	return ('The perimeter of your circle is: {0}'.format(result))

while True:
	try:
		x = int(input('Enter your number: '))
	except ValueError:
		print('Input a number')
	else:
		Round_object = Round(x)
		print(Round_object.area())
		print(Round_object.perimeter())