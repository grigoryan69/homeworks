#!/usr/bin/env python3
import math

try:
    x = int(input('input your number: '))

except:
    print('You have to write a number')
else:
    a = input('Enter your option: ')
    if a == 'sqrt':
        print(math.sqrt(x))
    else:                       
        try:
            y = int(input('input your second number: '))
        except:
            print('You have to write number') 
        else:
            match a:
                case '+':
                    print(x + y)
                case '-':
                    print(x - y)
                case '/':
                    print(x // y)
                case '*':
                    print(x * y)
                case _:
                    print('You can choose only + - * /')