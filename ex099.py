
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
"""

import string
fp = open('ex099_f1.txt')
a = fp.read()
fp.close()
print(a)

fp = open('ex099_f2.txt')
b = fp.read()
fp.close()
print(b)

fp = open('ex099_f3.txt','w')
l = list(a + b)
l.sort()

s = ''
s = 'join:\n' + s.join(l)
fp.write(s)
fp.close()
print(s)

end = input('\n end:\n')
