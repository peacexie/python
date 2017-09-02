#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)

# 匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x

a = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)

fx = lambda x: x * x
print(fx)
print(fx(5))

def build(x, y):
    return lambda: x * x + y * y

a = build(3, 2)
print(a())
