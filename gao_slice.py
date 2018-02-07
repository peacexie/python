#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

a = L[1:3]
print(a)

a = L[:3]
print(a)

L = list(range(100))
a = L[:10:2]
print(a)

a = L[::5]
print(a)

a = 'ABCDEFG'[:3]
print(a)

a = 'ABCDEFG'[::2]
print(a)

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)