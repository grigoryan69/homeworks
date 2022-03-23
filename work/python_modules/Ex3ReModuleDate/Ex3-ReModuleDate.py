#!/usr/bin/env python3
import re

"""
Գրել ծրագիր, որը հետևյալ url-ից 
կգտնի և կտպի տարեթիվը, ամիսը և օրը։ Օգտագործել re module-ը։
"""
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

string = 'https://www.washingtonpost.com/news/football-insider/wp/2021/08/08/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/'
x = string.split('/')
day = x[8]
month = x[7]
year = x[6]

now = []
for years in re.findall(year, string):

    print('Year "%s"' % years)
    now.append(years)
    break

for months in re.findall(month, string):

    print('month "%s"' % months)
    now.append(months)
    break

for days in re.findall(day, string):

    print('Day "%s"' % days)
    now.append(days)
    break

x = ', '.join(now)
save('real_output.txt', x)