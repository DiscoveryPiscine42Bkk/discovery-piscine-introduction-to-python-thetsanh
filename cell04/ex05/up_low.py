#!/usr/bin/env python3
string = input("Enter a word: ")
result = ""
for char in string:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
        result += char
print(result)
