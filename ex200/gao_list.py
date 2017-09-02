#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = list(range(1, 11))
print(a)

a = [x * x for x in range(1, 11)]
print(a)

a = [x * x for x in range(1, 11) if x % 2 == 0]
print(a)

a = [m + n for m in 'ABC' for n in 'XYZ']
print(a)

a = [m + n + k for m in 'AB' for n in 'XY' for k in '12']
print(a)

import os # 导入os模块，模块的概念后面讲到
a = [d for d in os.listdir('.')] # +"\n"
print(a)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
a = [k + '=' + v for k, v in d.items()]
print(a)

L = ['Hello', 'World', 'IBM', 'Apple']
a = [s.lower() for s in L]
print(a)

Lx = ['Hello', 'World', 18, 'Apple', None]
a = [s.lower() for s in Lx if isinstance(s, str)]
print(a)