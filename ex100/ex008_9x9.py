
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：输出9*9乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""

print ('')
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print ('%d * %d = % -2d' % (i,j,result))
    print ('')

print ('')
for i in range(1,10):
    line = ''
    for j in range(1,i+1):
        result = i * j
        line = line + ('%d*%d=%-2d ' % (j,i,result))
    print (line)

end = input('\n end:\n')
