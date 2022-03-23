#!/usr/bin/env python3

# Խնդիրը ճիշտ է լուծված, բայց պետք է հաշվի առնել, 
# որ օգտատերը կարող է ներմուծել ոչ թվային արժեք; Օր․՝ "Hi4"

def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

def count(n):
    if n == 1:
        return 1
    else:
        return n + count(n - 1)
def datas():
    num = int(input('Input your number: '))
    print(count(num))
    save('output.txt', count(num))

def main():
    datas()

if __name__ == '__main__': 
    main()