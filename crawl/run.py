#coding=UTF-8

import sys, time
sys.path.append("./")
sys.path.append("../")
from libs import cj360, tools

# 运行参数 见 `_wm.cmd` 注释

argvs = sys.argv
part = argvs[1] if len(argvs)>=2 else '0'
act = argvs[2] if len(argvs)>=3 else 'link'
istest = 'test' if len(argvs)>=4 else ''

cj = cj360.main()
rules = cj.getRules(part, act, istest)
if not rules:
    sys.exit('Null Rules!')

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
print("\n")
print(part, act, cj)
sys.exit()
'''
