#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
h = input('h: ')
w = input('w: ')
h = float(h)
w = float(w)
"""

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

li = list(range(101))
sum = 0
for x in li:
    sum = sum + x
print(sum)

def ft1(n=4):
    print(n)
    return range(n+1);

li = ft1(100)
sum = 0
for x in ft1():
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)