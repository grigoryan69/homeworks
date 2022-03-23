#!/usr/bin/env python3

# Ֆակտորիալի խնդիրը ճիշտ է լուծված, բայց ամբողջական խնդիրը
# պահանջում էր հաշվել օգտատիրոջ կոմից ներմուծված թվի ֆակտորիալը
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n

x = int(input('Enter some number: '))
sum = factorial(x) 
print(sum)  
save('output.txt', sum)