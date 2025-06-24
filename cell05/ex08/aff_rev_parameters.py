#!/usr/bin/env python3

import sys
n = len(sys.argv)
if n <= 3:
    print("none")
else:
    for i in range(n - 1, 0 , -1):
        print(sys.argv[i])