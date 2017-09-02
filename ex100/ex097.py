
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：从键盘输入一些字符，逐个把它们送到磁盘上去，直到输入一个#为止。
程序分析：无。
"""

from sys import stdout

if __name__ == '__main__':
    from sys import stdout
    #filename = input('input a file name:\n')
    fp = open('ex097_f1.txt',"w")
    ch = input('input string:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('')
    fp.close()

end = input('\n end:\n')