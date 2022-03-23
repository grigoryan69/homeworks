#!/usr/bin/env python3

def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

Set1 = {1,2,3,4,5}
Set2 = set(input('Input your set: '))
Set3 = [] 
for i in Set2:
    s = int(i)
    Set3.append(s)
print('Frist set: ')
print(Set1)
Set3 = set(Set3)
print('Second set: ')
print(Set3)
print('Difference between first set and second set: ')
print(Set1-Set3)
values = ', '.join(str(v) for v in Set1-Set3)
save('real_output.txt', values)