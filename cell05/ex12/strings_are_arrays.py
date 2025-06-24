#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    z_count = sys.argv[1].count("z")
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)
