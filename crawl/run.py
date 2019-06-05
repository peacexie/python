#coding=UTF-8

import sys, time
sys.path.append("./")
sys.path.append("../")
from libs import cj360, tools

'''
    运行参数
    run.py <city|id> <link|cont|0|auto> [test]
    argv[0] : 运行文件
    argv[1] : 城市(eg.dg)或规则id(eg.1024)或数据id(eg.5678)或不限(eg.0)
    argv[2] : link:采集网址, cont:采集详情, 0:link+cont, auto:备用
    argv[3] : 可选, 不为空即当成`test`模式
    eg: 
        - run.py 1025 link test --- 测试-规则id=1025 的列表规则
        - run.py dg   link      --- 采集-所有dg规则 的网址
        - run.py 1024 link      --- 采集-规则id=1024 的网址
        - run.py 5678 cont test --- 测试-数据id=5678 的详情规则
        - run.py dg   cont      --- 采集-所有dg规则 的详情
        - run.py 5678 cont      --- 采集-数据id=5678 的详情
        - run.py 0    0         --- 采集所有 - 网址和详情
'''

argvs = sys.argv
part = argvs[1] if len(argvs)>=2 else '0'
act = argvs[2] if len(argvs)>=3 else 'link'
istest = 'test' if len(argvs)>=4 else '' # 测试规则,不保存到数据库

cj = cj360.main()
rules = cj.getRules(part, act, istest)
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

# 爬连接
if act=='link' or act=='0':
    for rule in rules:
        res = cj.pyUrls(rule, istest)
        if istest or rule['debug']==1:
            debug['link'][rule['id']] = res
        #print(res,rule['debug'])

# 爬内容
if act=='cont' or act=='0':
    # 按下标整理规则字典
    rdic = {}
    for rule in rules:
        rdic[rule['id']] = rule
    # 取出未采集详情的列表
    lists = cj.getDList(part, istest)
    for itm in lists:
        rule = rdic[itm['ruleid']];
        res = cj.saveDetail(rule, itm, istest)
        if istest or rule['debug']==1:
            debug['cont'][itm['id']] = res
        #print("\n", res)
    
# 爬图片?

# debug-end
debug = tools.debug(debug)
print("\n", debug)

'''
    remark
'''

print("\n")
print(part, act, cj)
sys.exit()
