import math
class Choose:
	def __init__(self):
		pass
		
	def sqrt(self, sqr):
		self.sqr = math.sqrt(sqr)
		return self.sqr
	def last_two(self, lasts):
		self.lasts = lasts[-2:] 
		return self.lasts	

while True:
	try:
		x = int(input('Type: '))
		y = input('Type: ')
	except ValueError:
		print('You have to enter a number')
	else:
		if x == 1:
			try:
				int(y)
			except ValueError:
				a = Choose()
				print(a.last_two(str(y)))
			else:
				a = Choose()
				print(a.sqrt(int(y)))			
		else:
			print('Incorect operation')