#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
"""

for n in range(100,1000):
    i = int(n / 100)
    j = int(n / 10 % 10)
    k = int(n % 10)
    #print('i: %d, j: %d, k: %d' %i %j %k)
    '''
    print('n: %d' % n)
    print('  --- i : %d' % (i))
    print('  --- j : %d' % (j))
    print('  --- k : %d' % (k))
    print('  -:--- a : %d' % (i * i * i))
    print('  -:--- b : %d' % (j ** 3))
    print('  -:--- c : %d' % (k ** 3))
    print('  === : %d' % (i** 3 + j ** 3 + k ** 3))
    '''
    if n == i** 3 + j ** 3 + k ** 3 :
        print (n)
        
end = input('\n end:\n')
