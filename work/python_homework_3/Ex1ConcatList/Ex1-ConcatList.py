#!/usr/bin/env python3
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(data)

def list_():
    a = ['p', 'q']
    num = 1 
    b = []
    while num  < 6:
        x = (str(num))
        s = x + str(a[0])
        d = x + str(a[1])
        b.append(s) 
        b.append(d)
        num += 1
    print(b)
    x = ", ".join(b)
    save('real_output.txt', x)

def main():
    list_()

if __name__ == '__main__':
    main()