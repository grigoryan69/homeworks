#!/usr/bin/env python3

list1 = ['I', 'two', 'love', 'for', 'to']
list2 = ['two', 'watch', '365', 'anime', 'bedmobile']
list3 = []
for i in list1:
    a = list1.index(i)
    if a % 2 == 0:
        list3 = list3 + [i]

for b in list2:
    s = list2.index(b)
    if s % 2 != 0:
        list3 = list3 + [b]
print(list3)
