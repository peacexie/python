
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
程序源代码：
"""

import datetime
 
if __name__ == '__main__':
 
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%Y-%m-%d'))
 
    # 创建日期对象
    mybDate = datetime.date(1941, 1, 5)
 
    print(mybDate.strftime('%Y-%m-%d'))
 
    # 日期算术运算
    mynDate = mybDate + datetime.timedelta(days=1)
 
    print(mynDate.strftime('%Y-%m-%d'))
 
    # 日期替换
    myfbDate = mybDate.replace(year=mybDate.year + 1)
 
    print(myfbDate.strftime('%Y-%m-%d'))
    
end = input('\n end:\n')
