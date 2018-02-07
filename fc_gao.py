#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(x, y, f):
    return f(x) + f(y)

a = add(-5, 6, abs)
print(a)

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
a = list(r)
print(a)

a = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 90]))
print(a)


from functools import reduce
def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

a = reduce(fn, map(char2num, '13579'))
print(a)


a = sorted([36, 5, -12, 9, -21])
print(a)

a = sorted([36, 5, -12, 9, -21], key=abs)
print(a)

a = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(a)

a = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(a)

a = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(a)


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

"""
for n in primes():
    if n > 300 and n < 500:
        print(':::'+n)
    else:
        break
print()
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
"""




"""

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

"""

