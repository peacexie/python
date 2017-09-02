
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。
"""

from sys import stdout

if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a) 
    print (a)
    tmp = int(len(a) / 2)
    for i in range(tmp):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print (a)

end = input('\n end:\n')
