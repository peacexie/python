
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：八进制转换为十进制
程序分析：无。
"""

from sys import stdout

a = 809
for i in range(10,100):
    b = i * a + 1
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print (b,'/',i,' = 809 * ',i,' + ', b % i)

end = input('\n end:\n')