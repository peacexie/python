
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：循环输出列表
程序分析：无。
"""

from sys import stdout

if __name__ == '__main__':
    s = ["man","woman","girl","boy","sister"]
    for i in range(len(s)):
        print (s[i])

end = input('\n end:\n')