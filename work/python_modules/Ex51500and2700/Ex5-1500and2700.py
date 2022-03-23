#!/usr/bin/env python3
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))
'''
Գրել ծրագիր, որը կգտնի այն թվերը, որոնք առանց մնացորդի բաժանվում են  7-ի և 5-ի, գտնվում են 1500 ֊ 2700 թվերի միջակայքում (երկուսն էլ ներառյալ), արդյունքը լցնել list-ի մեջ և բաժանել ստորակետերով։
'''
thelist = []
for i in range(1500, 2701):
    if (i % 5 == 0) and (i % 7 == 0):
        thelist.append(str(i))

print(','.join(thelist))
save('real_output.txt', ','.join(thelist))