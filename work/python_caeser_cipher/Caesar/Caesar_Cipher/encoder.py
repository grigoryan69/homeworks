#!/usr/bin/env python3

def encod(encoder, knownkey):
    y=0
    encoder = encoder.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    encoded = ''
    for letter in encoder:
        real_position = alphabet.find(letter)
        keyd_position = int(real_position) - int(knownkey)
        if letter in alphabet:
            encoded += alphabet[keyd_position]
        else:
            encoded += letter
    return encoded.capitalize()
