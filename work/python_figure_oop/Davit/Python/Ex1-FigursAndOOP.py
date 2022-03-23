#!/usr/bin/python3

'''
Գրել ծրագիր, որը երկրաչափական օբյեկտները կնկարագրի class֊երի միջոցով,
հնարավորություն կտա հաշվել նրա մակերեսը, փոփոխել նրա attribute֊ները։
Ծրագրի իրագործման ժամանակ
օգտագործել մեր կողմից քննարկված OOP֊ի concept֊ները։
    Պետք է առկա լինեն հետևյալ երկրաչափական տարրերը․
    
    Եռանկյուն
    Ուղղանյուն
    Քառակուսի
    Շրջանագիծ
    Էլիպս
'''

from math import pi
from math import sqrt

class NegativeValueError(ValueError):
    pass
class UnbelievableTriangle(ValueError):
    pass
class Figure():

	def __init__(self, a):

		if 0 < a:
			self._a = a
		else:
			raise NegativeValueError(f'Are you realy think that {a} is an possitive number?')
		
	def __doc__(self):

		return 'These classes were crated for counting areas.\
		\nCall your needed founction to get more information'	

class GoSquare(Figure):
	def __init__(self, a):
		if 0 < a:
			super().__init__(a)
		else:
			raise NegativeValueError(f'Are you realy think that {a} is an possitive number?')
	def area(self):
		return self._a * self._a

	def __doc__(self):
		return '''Hi i'm square, i was crated to count my areas.\nTo call my areas use area method and give them 2 arguments'''		

class GoRectangle(Figure):

	def __init__(self, a, b):
		if 0 < a and 0 < b:
			super().__init__(a)
			self._b = b
		else:
			raise NegativeValueError(f'Are you realy think that {b} is an possitive number?')

	def area(self):
		return self._a * self._b

	def __doc__(self):
		return '''Hi i'm rectangle, i was crated to count my areas.\nTo call my areas use area method and give them 2 arguments'''	


class GoTriangle(Figure):

	def __init__(self, a, b, c):

		if 0 < a and 0 < b and 0 < c:
			if a + b > c and b + c > a and a + c > b:   
				super().__init__(a)
				self._b = b
				self.__c = c
			else:
				raise UnbelievableTriangle('Your triangle is not real')
		else:
			raise NegativeValueError(f'Are you realy think that {c} is an possitive number?')
	
	def area(self):

		P = (self._a + self._b + self.__c)/2
		S = sqrt(P*(P-self._a)*(P-self._b)*(P-self.__c))
		return S
	
	def __doc__(self):
		return f'''Hi i'm triangle, i was crated to count my areas.\nTo call my areas use area method and give them 3 arguments'''	

class GoCircle(Figure):

	def __init__(self, a):
		if 0 < a:
			super().__init__(a)
		else:
			raise NegativeValueError(f'Are you realy think that {a} is an possitive number?')	
	def area(self):
		return pi*self._a*self._a
	
	def __doc__(self):
		return '''Hi i'm circle, i was crated to count my areas.\nTo call my areas use area method and give them 2 arguments'''	

# Էլիպսը երկու շառավիղ ունի, ներքևում շրջանագիծ ա նկարագրված
class GoEllipse(Figure):
	def __init__(self, a, b):
		if 0 < a and 0 < b:
			super().__init__(a)
			self._b = b
		else:
			raise NegativeValueError(f'Are you realy think that {a} is an possitive number?')
	def area(self):
		return self._a * pi * self._b

	def __doc__(self):
		return '''Hi i'm elips, i was crated to count my areas.\nTo call my areas use area method and give them 2 arguments'''	

go_triangle = GoTriangle(12,9,8)
print('The are of your GoTriangle is:', go_triangle.area())

go_rectangle = GoRectangle(5,9)
print('The are of your rectangle is:', go_rectangle.area())

go_square = GoSquare(5)
print('The are of your square is:', go_square.area())

go_GoCircle = GoCircle(61)
print('The are of your GoCircle is:', go_GoCircle.area())

go_elips = GoEllipse(56, 5)
print('The are of your elips is:', go_elips.area())
print(Figure(5).__doc__())