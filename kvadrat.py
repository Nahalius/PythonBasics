#!/usr/bin/env python3.5

n = int(input())
g = n-2
a = '*'

print(n * a)
for i in range(0, n-2):
    print(a + g * " " + a)
print(n * a)

#Prints square with asterics
