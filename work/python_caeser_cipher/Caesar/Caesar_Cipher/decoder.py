#!/usr/bin/env python3

def decod(letters, key):
    y=0
    letters = letters.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    decoded = ''
    for letter in letters:
        real_position = alphabet.find(letter)
        keyd_position = int(real_position) + int(key)
        if letter in alphabet:
            decoded += alphabet[keyd_position]

        else:
            decoded += letter
    return decoded.capitalize()
