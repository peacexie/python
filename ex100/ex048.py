
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：数字比较。
程序分析：无
"""

from sys import stdout

if __name__ == '__main__':
    i = 10
    j = 20
    if i > j:
        print ('%d 大于 %d' % (i,j))
    elif i == j:
        print ('%d 等于 %d' % (i,j))
    elif i < j:
        print ('%d 小于 %d' % (i,j))
    else:
        print ('未知')

end = input('\n end:\n')
