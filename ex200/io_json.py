#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import json



d = dict(name='Bob测试0', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)



d = dict(name='Bob测试1', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob测试2', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)



