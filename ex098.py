
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
程序分析：无。
"""

from sys import stdout

if __name__ == '__main__':
    fp = open('ex098_f1.txt','w')
    string = input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('ex098_f1.txt','r')
    print (fp.read())
    fp.close()

end = input('\n end:\n')