#!/usr/bin/env python3
i = 0
while i <= 10:
    j = 0
    row = f"Table de {i}:"
    while j <= 10:
        row += f" {i * j}"
        j += 1
    print(row)
    i += 1
