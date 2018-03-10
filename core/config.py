
import os, sys, platform
import configparser

def init():
    cfgs = {}
    cfgs['envs'] = envs()
    bcfg = ucfg(cfgs['envs'])
    for key in bcfg: # app, dir, path, db, blog ... 
        cfgs[key] = bcfg[key]
    sys.path.append(cfgs['dir']['cpdir'])
    #sys.path.append(cfgs['dir']['import'])
    sys.path.append(cfgs['dir']['views'])
    return cfgs

def envs():
    envs = {}
    envs['arc'] = platform.architecture()
    envs['sys'] = platform.system()
    envs['ver'] = platform.version()
    return envs

def ucfg(envs):
    conf = configparser.ConfigParser()
    conf.read("./data/appcfg.ini", encoding="utf-8-sig")
    secs = conf.sections()
    ucfg = {}
    for key in secs:
        ucfg[key] = dict(conf.items(key))
    return ucfg

