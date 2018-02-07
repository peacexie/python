from math import pi

class cls1(object):

    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

class cls2(object):

    def area(a, b):
        return a*b

    def around(r):
        return pi * r * r

class cls3(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
