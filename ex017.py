
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
程序源代码：
"""

import string
from sys import stdout

s = input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    stdout.write("("+c+")")
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char=%d, space=%d, digit=%d, others=%d' % (letters,space,digit,others))

end = input('\n end:\n')
