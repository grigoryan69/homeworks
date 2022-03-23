#!/usr/bin/env python3

def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def fib(n, fiblist, boolian):
	if n < 0:
		return f'your number {str(n)} is not possitive'
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	count = fib(n - 1, fiblist, boolian) + fib(n - 2, fiblist, False)
	if boolian:
		fiblist.append(count)
	return count

fiblist = [0, 1]
try:
    n = int(input('Enter a number to find fib: '))
except ValueError:
    print('Enter a number no string')
else:
    fib(n - 1, fiblist, True)
    print(fiblist)
    values = ', '.join(str(v) for v in fiblist)
    save('output.txt', values)
