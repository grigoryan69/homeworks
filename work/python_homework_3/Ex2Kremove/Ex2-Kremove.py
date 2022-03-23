#!/usr/bin/env python3

def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def RmNum(inlist):
    x = 2
    for i in inlist:
        if i == x:
            inlist.remove(x)
    return inlist        

def lists():
    list1 = [1,1,2,3,4,4,5,1]
    print(RmNum(list1))
    values = ', '.join(str(v) for v in list1)
    save('real_output.txt', values)

def main():
    lists()

if __name__ == '__main__':
    main()