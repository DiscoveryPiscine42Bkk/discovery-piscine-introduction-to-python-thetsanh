#!/usr/bin/env python3

import sys
n = len(sys.argv)
if n != 2:
    print("none")
else:
    inp = input("What was the parameter? ")
    if inp == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")