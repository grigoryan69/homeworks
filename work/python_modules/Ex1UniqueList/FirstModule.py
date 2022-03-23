#!/usr/bin/env python3

'''Գրել module, որը կունենա հետևյալը՝
Ֆունկցիա, որը որպես արգումենտ կստանա list, կհաշվի դրա էլեմենտների գումարը, կլցնի list-ը set-ի մեջ, ապա կհաշվի set-ի էլելմենտների գումարը և կտպի “list have unique elements”, եթե առաջինի գումարը հավասար լինի երկրորդի գումարին և հակառակը։
Ունենալ երկու python ֆայլեր, որոնցից մեկի մեջ import անել վերոնշյալ module-ը, ապա երկրորդ ֆայլի մեջ import անել առաջին ֆայլը և օգտագործել առաջինում ներմուծված module-ի ֆունցիան։ Արդյունքը մեկնաբանել։'''

def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def ulistsum(num_list):
    count = 0
    count2 = 0
    new_set = set(num_list)
    for i in num_list: 
        count += i
    for x in new_set:
        count2 += x
    if count == count2:
        save('counter.txt', count2)
        values = ', '.join(str(v) for v in new_set)
        save('elements.txt', values)
        save('mode.txt', 'unique')
        return ('List have unique elements: {0}\nSum of your uniqu list is {1}'.format(new_set, count2))
    else:
        save('counter.txt', count)
        values = ', '.join(str(v) for v in num_list)
        save('elements.txt', values)
        save('mode.txt', 'not special')
        return ('List have not special elements: {1}\n\
Sum of your not uniqu list is {0}'.format(count, num_list))            
    
     

