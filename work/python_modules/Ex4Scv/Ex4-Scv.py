#!/usr/bin/env python3
import csv
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))
'''
Գրել ծրագիր, որը csv ֆայլում կգրի list-երի list-ը։ Գրելուց հետո կարդալ տվյալֆայլը և տպել բովանդակությունը։
'''
inlist = [
    ['Apple', 'Dont have'],
    ['Bananas', 'Have'],
    ['Kiwi', 'Dont have'], 
    ['Plum', 'Dont have'], 
    ['Melon', 'Have'],
]

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(inlist)

with open('data.csv', 'r') as f:
    print(f.read())
