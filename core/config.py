
import sys, os, platform
import configparser
from core import argv

# 初始化配置
def init():
    cfgs = {}
    cfgs['envs'] = envs()
    bcfg = ucfg(cfgs['envs'])
    for key in bcfg: # app, dir, path, db, blog ... 
        cfgs[key] = bcfg[key]
    sys.path.append(cfgs['dir']['cpdir'])
    #sys.path.append(cfgs['dir']['import'])
    sys.path.append(cfgs['dir']['views'])
    argv.cfgs = cfgs
    return cfgs

# 运行环境信息
def envs():
    envs = {}
    envs['arc'] = platform.architecture()
    envs['sys'] = platform.system()
    envs['ver'] = platform.version()
    return envs

# 读取应用配置
def ucfg(envs):
    conf = configparser.ConfigParser()
    conf.read("./data/appcfg.ini", encoding="utf-8-sig")
    secs = conf.sections()
    ucfg = {}
    for key in secs:
        ucfg[key] = dict(conf.items(key))
    return ucfg

