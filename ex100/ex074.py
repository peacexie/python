
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：放松一下，算一道简单的题目。
程序分析：无。
"""

from sys import stdout

if __name__ == '__main__':
    arr1 = (3,12,8,9,11)
    ptr = list(arr1)
    print (ptr)
    ptr.sort()
    print (ptr)

end = input('\n end:\n')