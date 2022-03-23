class Pow:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def power(self=0):
		x = int(input('Enter your first number: '))
		y = int(input('Enter your second number: '))
		return pow(x, y)

print(Pow.power())