#!/usr/bin/env python3
import re

"""Գրել ծրագիր որը կգտնի 'Python exercises, PHP exercises, C++ exercises' string-ի միջի exercises’ substring- : ը
 re module-Օգտագործել ը։"""

def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

string = 'Python exercises, PHP exercises, C++ exercises'
substring = 'exercises'
new = []
for match in re.findall(substring, string):
        print('we find "%s"' % match)
        new.append(match)
            
x = ', '.join(new)
save('real_output.txt', x)