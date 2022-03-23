#!/usr/bin/env python3

def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def iphone():
    iset = {*range(1, 20)}
    imin = 1
    imax = 1 
    for i in iset:
        if i > imax:
            imax = i
        elif i < imin:
            imin = i
    print(imax,imin)
    result = f'{imax}, {imin}'
    save('real_output.txt', result)

def main():
    iphone()


if __name__ == '__main__':
    main()