#!/usr/bin/python
# -*- coding: UTF-8 -*-

h = input('h: ')
w = input('w: ')
h = float(h)
w = float(w)

bmi = w / h / h

print(bmi)
if bmi<=18.5:
    print('低于18.5：过轻')
elif bmi>18.5 and bmi<=25:
    print('正常')
elif bmi>25 and bmi<=28:
    print('过重')
elif bmi>28 and bmi<=32:
    print('肥胖')
else:
    print('高于32：严重肥胖')

"""
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""


age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')