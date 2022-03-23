#!/usr/bin/env python3

num = int(input('Your number ?: '))
if num >= 3 and num <= 7:
    print(1)
elif num % 2 == 0:
    print(2)
elif num != 3 and num != 7 and num > 7 or num < 3:
    print(0)
