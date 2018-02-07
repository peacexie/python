#!/usr/bin/python
# -*- coding: UTF-8 -*-

ct = ['Michael', 'Bob', 'Tracy']
print(ct)
print(len(ct))
print(ct[1])
print(ct[-2])
#print(ct[-6])
ct.append('Adam')
print(ct)
ct.insert(1, 'Jack')
print(ct)
ct.pop()
print(ct)
ct.pop(1)
print(ct)

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][1])

ct2 = ('Michael', 'Bob', 'Tracy')
print(ct2)
t = (1,)
print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)