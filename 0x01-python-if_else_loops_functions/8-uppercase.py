#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_code = ord(c)
        if ord('a') <= ascii_code <= ord('z'):
            # If the character is lowercase, convert it to uppercase
            ascii_code -= (ord('a') - ord('A'))
        print(chr(ascii_code), end='')
    print()  # Add a newline at the end

