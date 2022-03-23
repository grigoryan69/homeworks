#!/usr/bin/env python3


def factorial():
    fac_num = int(input("Enter your number: "))
    a = 1
    for i in range(2, fac_num+1):
        a *= i
    print(a)


def main():
    factorial()


if __name__ == '__main__':
    main()
