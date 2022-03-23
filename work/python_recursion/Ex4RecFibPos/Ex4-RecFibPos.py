#!/usr/bin/env python3

# Խնդիրը ճիշտ է լուծված, բայց պետք է հաշվի առնել, 
# որ օգտատերը կարող է ներմուծել ոչ թվային արժեք; Օր․՝ "Hi4"
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

x = int(input('Input yor number: '))

print(fib(x))
save('output.txt', fib(x))
