#!/usr/bin/env python3

# Խնդրի արդյունքը ճիշտ է, բայց լուծված չի պահանջված եղանակով
# Խնդիրը պետք է լուծել այնպես, որ ֆունկցիային փոխանցված արգումենտը 
# լինի n, իսկ ֆունկցիան հաշվի 1 + 2 + ... + n-1 գումարը
# Ինչպես նաև պետք է հաշվի առնել, 
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
    print(count(num - 5))
    save('output.txt', count(num - 5))

def main():
    datas()

if __name__ == '__main__': 
    main()