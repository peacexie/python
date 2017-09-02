
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
程序分析：无
"""

from sys import stdout

TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print ('如果输入的数字小于 50，程序将停止运行。')
again = 1
while again:
    num = int(input('Please input number'))
    print ('运算结果为 %d' % (SQ(num)))
    if num >= 50:
        again = TRUE
    else:
        again = FALSE

end = input('\n end:\n')
