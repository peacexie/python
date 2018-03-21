
import sys, os, platform, configparser
from flask import request as freq

global cfgs

# ---------------------------------------------- 

# 初始化配置
def init():
    global cfgs
    cfgs = {}
    cfgs['envs'] = envs()
    bcfg = ucfg()
    for key in bcfg: # app, dir, path, db, blog ... 
        cfgs[key] = bcfg[key]
    sys.path.append(cfgs['dir']['cpdir'])
    #sys.path.append(cfgs['dir']['import'])
    sys.path.append(cfgs['dir']['views'])
    #argv.cfgs = cfgs
    return cfgs

# 运行环境信息
def envs():
    envs = {}
    envs['arc'] = platform.architecture()
    envs['sys'] = platform.system()
    envs['ver'] = platform.version()
    return envs

# 读取应用配置
def ucfg():
    conf = configparser.ConfigParser()
    conf.read("./data/appcfg.ini", encoding="utf-8-sig")
    secs = conf.sections()
    ucfg = {}
    for key in secs:
        ucfg[key] = dict(conf.items(key))
    return ucfg

# ---------------------------------------------- 

# 得到命令行参数, no=1,2,3
def cmd(no, d=''):
    args = sys.argv
    val = args[no] if len(args)>no else d
    return val

# 得到Url参数, d:默认值
def get(key, d=''):
    val = freq.args.get(key)
    if not val or len(val)==0:
        val = d
    return val

# cfgs:运行时参数:取值/赋值
def cfg(key, val=None):
    global cfgs
    if val is None:
        return cfgs[key] if hasattr(cfgs, key) else None
        pass #get
    else:
        cfgs[key] = val
        pass #get

# ---------------------------------------------- 

# 计算批次,给多进程使用
def range(pcnt, no, cmax, cmin):
    cbat = int(cmax / pcnt)
    n1 = (no*cbat) + cmin
    n2 = cmax if pcnt==no+1 else ((no*cbat)+cbat)
    if n2>cmax:
        n2 = cmax
    res = {'n1':n1, 'n2':n2}
    #print(res)
    return res
def limit(pcnt, no, recs):
    cbat = int(recs / pcnt)
    if not no:
        lmts = "LIMIT " + str(cbat)
    elif pcnt==no+1:
        lmts = "LIMIT " + str(no*cbat) + ',' + str(cbat+pcnt)
    else:
        lmts = "LIMIT " + str(no*cbat) + ',' + str(cbat)
    #print(lmts)
    return lmts

