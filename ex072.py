
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：创建一个链表。
程序分析：无。
"""

from sys import stdout

if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print (ptr)

end = input('\n end:\n')

