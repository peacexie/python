#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from io import StringIO
from io import BytesIO


with open('io_f1.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('io_f1.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('io_f1.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)



# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())



# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())



