
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：按逗号分隔列表。
"""

from sys import stdout

L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print (s1)

end = input('\n end:\n')
