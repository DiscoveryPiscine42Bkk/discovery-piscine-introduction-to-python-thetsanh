#!/usr/bin/env python3
def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error")
    else:
        print(f"Hello, {name}.")

greetings() 
greetings("Alice")  
greetings(123) 