
import os, sys, platform
import configparser

def app(app, _cfgs):
    for key in _cfgs['app']:
        app.config[key.upper()] = _cfgs['app'][key]
'''
    app.config['SECRET_KEY'] = '123456'  
    app.secret_key = '123456' 
'''

def init():
    _cfgs = {}
    _cfgs['envs'] = envs()
    bcfg = ucfg(_cfgs['envs'])
    for key in bcfg: # app, dir, path, db, blog ... 
        _cfgs[key] = bcfg[key]
    sys.path.append(_cfgs['dir']['cpdir'])
    return _cfgs

def envs():
    envs = {}
    envs['arc'] = platform.architecture()
    envs['sys'] = platform.system()
    envs['ver'] = platform.version()
    return envs

def ucfg(envs):
    conf = configparser.ConfigParser()
    conf.read("./data/config.ini", encoding="utf-8-sig")
    secs = conf.sections()
    ucfg = {}
    for key in secs:
        ucfg[key] = dict(conf.items(key))
    return ucfg

