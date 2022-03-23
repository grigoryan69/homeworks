#!/usr/bin/env python3
import math

AB = float(input('Enter length of 1 Figure: '))
AC = float(input('Enter length of 2 Figure: '))

BC = math.sqrt(AB ** 2 + AC ** 2)
S = (AB * AC) / 2
print('Area of the triangle: ' + str(S))
