#coding=UTF-8

import sys, time
sys.path.append("./")
sys.path.append("../")
#from urllib import parse
#from pyquery import PyQuery as pyq
#from core import argv, dbop, files, urlpy
from libs import cj360, tools

# file.py, city|tid, url|save|0|auto
argvs = sys.argv
part = argvs[1] if len(argvs)>=2 else '0'
act = argvs[2] if len(argvs)>=3 else 'url'
#print(part,act)

cj = cj360.main()
rules = cj.getRules(part)
if not rules:
    sys.exit('Null Rules!')

'''
0-默认,
1-爬网址,2-已过滤,3/7-爬内容,4-爬图片,5-预留
7-爬内容/待入库
8-已入库,9-已删除
'''

# debug-start
debug = tools.debug()

# 爬网址
if act=='url' or act=='0':
    for rule in rules:
        res = cj.pyUrls(rule)
        if rule['debug']==1:
            debug['url'][rule['id']] = res
        #print(res,rule['debug'])

# 爬内容
if act=='save' or act=='0':
    # 按下标整理规则字典
    rdic = {}
    for rule in rules:
        rdic[rule['id']] = rule
    # 取出未采集详情的列表
    lists = cj.getDList(part)
    for itm in lists:
        rule = rdic[itm['ruleid']];
        res = cj.saveDetail(rule, itm)
        if rule['debug']==1:
            debug['save'][itm['id']] = res
        #print("\n", res)
    
# 爬图片?

# debug-end
debug = tools.debug(debug)
print("\n", debug)

'''
from core import urlpy
url = 'http://www.discuz.net/forum.php?mod=announcement&id=229'
url = 'http://xd.semtech.net.cn/index.asp'
url = 'http://www.cc10000.cn/0/7/3/5yx/'
res = urlpy.page(url)
print(res)

'''

print("\n")
print(part, act, cj)
sys.exit()
