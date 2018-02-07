#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print('2015-3-25')

now()

print()
print(now.__name__)
print()

def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('mymsg(Peace)')
def now2():
    print('2016-10-25')

now2()


"""
print(now)
print(now())
print(now.__name__)

f = now
print(f)
print(f())
"""

