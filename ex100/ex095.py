
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：字符串日期转换为易读的日期格式。
程序分析：无。
"""

from sys import stdout
from dateutil import parser
# ImportError: No module named 'dateutil'

dt = parser.parse("Aug 28 2015 12:00AM")
print (dt)

end = input('\n end:\n')