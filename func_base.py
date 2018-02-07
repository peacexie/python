#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = abs(-4)
print(a)

abs = 2
print(abs)

def abs(n=10):
    return n+1, n*1234

b = abs(20)
print(b)

print(abs)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

a = calc(1, 2)
print(a)

a = calc(1, 2, 3)
print(a)

a = calc(1, 3, 5, 7, 9)
print(a)

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

a = person('Michael', 30)
print(a)
a = person('Bob', 35, city='Beijing')
print(a)
a = person('Adam', 45, gender='M', job='Engineer')
print(a)

extra = {'city': 'Beijing', 'job': 'Engineer'}
a = person('Jack', 24, **extra)
print(a)

def person(name, age, *, city, job):
    print(name, age, city, job)

a = person('Jack', 24, city='Beijing', job='Engineer')
print(a)

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

a = person('Jack', 24, city='Beijing', job='Engineer')
print(a)

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

a = person('Jack', 24, job='Engineer')
print(a)


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

a = f1(1, 2)
a = f1(1, 2, c=3)
a = f1(1, 2, 3, 'a', 'b')
a = f1(1, 2, 3, 'a', 'b', x=99)
a = f2(1, 2, d=99, ext=None)
print(a)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
b = f1(*args, **kw)
print(b)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
b = f2(*args, **kw)
print(b)
