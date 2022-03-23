#!/usr/bin/env python3
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def checker():
    num = input('Enter something: ')
    try:
        int(num)
        print('This is number: ')
        save('intTester.txt', 'This is number')
    except:
        print('This is not number: ')
        save('strTester.txt', 'This is not number')
def main():
    checker()

if __name__ == '__main__':
    main()