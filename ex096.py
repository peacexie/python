
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：计算字符串中子串出现的次数。
程序分析：无。
"""

from sys import stdout

if __name__ == '__main__':
    str1 = input('input a string:\n')
    str2 = input('input a sub string:\n')
    ncount = str1.count(str2)
    print (ncount)

end = input('\n end:\n')