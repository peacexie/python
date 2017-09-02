#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = [x * x for x in range(10)]
print(a)

g = (x * x for x in range(10))
for n in g:
    print(n)
#print(a)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(13))

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib2(10)
print('fib(10):', f)
for x in f:
    print(x)

g = fib2(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break