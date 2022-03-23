#!/usr/bin/env python3

def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def lists():
    list_=[1, 1, 2, 3, 4, 4, 5, 1]
    print(list_)
    list_.insert(2,12)
    print(list_)
    values = ', '.join(str(v) for v in list_)
    save('real_output.txt', values)

def main():
    lists()

if __name__ == '__main__':
    main()