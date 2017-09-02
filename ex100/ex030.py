
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
程序分析：无。
"""

from sys import stdout

def huiwen(x):
    x = str(x)
    flag = True
    m = int(len(x)/2)
    for i in range(m):
        if x[i] != x[-i - 1]:
            flag = False
            break
    return flag

fp = open('ex030_huiwen.txt','w') # a/w
n = 0;
for i in range(70000,89999):
    if(huiwen(i)):
        n = n+1;
        istr = ("%3d : %5d " % (n,i))
        fp.write('\n'+istr)
        print (istr)
fp.close()

a = int(input("请输入一个数字:\n"))
flag = huiwen(a)
if flag:
    print ("%d 是一个回文数!" % a)
else:
    print ("%d 不是一个回文数!" % a)

end = input('\n end:\n')
