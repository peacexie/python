#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

"""
http://blog.csdn.net/rao356/article/details/48975617
windows系统下，django1.8+python3.5使用pymysql链接 mysql数据库
"""

import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='',port=3306,charset='utf8')
cur = conn.cursor()
cur.execute("USE txmao_main")

cur.execute("select version()")
for i in cur:
    print(i)
    
cur.execute('select uname,pptmod from users_uppt_ys where uname LIKE %s', ('%%tand%%',))
values = cur.fetchall()
for i in values:
    print(i)

#cur.execute('select kid,title from base_model_ys where pid=%s', ('groups',))
cur.execute("select kid,title from base_model_ys where pid='groups'")
values = cur.fetchall()
for i in values:
    print(i)

cur.close()
conn.close()

