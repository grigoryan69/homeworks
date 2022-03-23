#!/usr/bin/env python3

def tabell():
    n = int(input('enter your number:'))
    for i in range(1, 10):
        print(f'{n} * {i} = {n*i}')


tabell()
