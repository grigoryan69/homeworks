#!/usr/bin/env python3
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

Set1 = {1,2,3,4,5}
Set2 = set(input('Input your set: '))
Set3 = [] 
print('First set before:')
print(Set1)
for i in Set2:
    s = int(i)
    Set3.append(s)
    Set1.remove(s)
print('Second set: ')
Set3 = set(Set3)
print(Set3)
print('Frist set after: ')
print(Set1)
values = ', '.join(str(v) for v in Set1)
save('real_output.txt', values)