
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
程序分析：无。
"""

from sys import stdout

if __name__ == '__main__':
    nmax = 50
    n = int(input('please input the total of numbers:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0 : 
            k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 0
        i += 1
        if i == n : 
            i = 0

    i = 0
    while num[i] == 0:
        i += 1
    print (num[i])

end = input('\n end:\n')
