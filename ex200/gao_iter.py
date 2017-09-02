#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}
print(d)

for key in d:
    print(key)
for value in d.values():
    print(value)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, '=', value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)