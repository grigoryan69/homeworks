class Rectangle():
    def __init__(self, rec, tungle):
        self.rec = rec
        self.tungle = tungle

    def area(self):
    	return self.rec * self.tungle

while True:
	try:
		a = float(input('Firts number: '))
	except ValueError:
		print('Enter a number')	
	else:
		try:
			b = float(input('Second number: '))
		except ValueError:
			print('Enter a number')		
		else:
			if a >= 0 or b >= 0:
				print('Incorect input')		
			else:
				x = Rectangle(a, b)
				print(x.area())