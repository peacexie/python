
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：暂停一秒输出。
程序分析：无。
"""

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print (key, value)
    time.sleep(0.2) # 暂停 1 秒

s1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print (s1)

# 暂停一秒
time.sleep(0.2)

s1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print (s1)

end = input('\n end:\n')
